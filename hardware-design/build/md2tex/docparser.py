import pathlib
import yaml


class ParseFailure(Exception):
    pass


# ==========


class DocElement:

    _HTML_TAG = None

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance._params = {}
        instance._children = []
        return instance

    def contains_code(self) -> bool:
        # frames that contain code need to be marked [fragile]
        if isinstance(self, CodeBlock) or isinstance(self, InlineCode):
            return True
        return any(c.contains_code() for c in self._children)

    def to_tex(self) -> str:
        return self._children_to_tex()

    def _child_to_tex(self) -> str:
        assert len(self._children) == 1
        return self._children[0].to_tex()

    def _children_to_tex(self) -> str:
        return "\n".join(c.to_tex() for c in self._children)

    def to_html(self) -> str:
        return "\n".join(
            [self._html_open(), self.indent(self._children_to_html()), self._html_close()]
        )

    def _child_to_html(self) -> str:
        assert len(self._children) == 1
        return self._children[0].to_html()

    def _children_to_html(self) -> str:
        return "\n".join(c.to_html() for c in self._children)

    def _html_tag_name(self) -> str:
        return self._HTML_TAG or self.__class__.__name__

    def _html_open(self, include_params=True) -> str:
        if include_params and self._params:
            return f"<{self._html_tag_name()} {self.pretty_html_params()}>"
        return f"<{self._html_tag_name()}>"

    def _html_close(self) -> str:
        return f"</{self._html_tag_name()}>"

    def _html_solo(self) -> str:
        return f"<{self._html_tag_name()} \\>"

    def indent(self, text, depth=2) -> str:
        return "\n".join(" "*depth + l for l in text.splitlines())

    @classmethod
    def break_at_line_starting_without(cls, body: str, delim: list[str]) -> tuple[str, str]:
        leftover_lines = body.splitlines()
        # don't break on the first line. we are in a section and looking for the start of the next section
        lines = [leftover_lines.pop(0)]
        while leftover_lines:
            if not any(leftover_lines[0].startswith(d) for d in delim):
                break
            lines.append(leftover_lines.pop(0))
        return "\n".join(lines), "\n".join(leftover_lines)

    def pretty_html_params(self) -> str:
        pretty = []
        for key, val in self._params.items():
            assert isinstance(key, str)
            if val is None:
                continue
            elif isinstance(val, str):
                pretty.append(f'{key}="{val}"')
            elif isinstance(val, int) or isinstance(val, float):
                pretty.append(f'{key}={val}')
            else:
                raise ValueError(f"Unsupported HTML param: {val}")
        return " ".join(pretty)

    def get_children(self, raw: str, head: dict) -> list["DocElement"]:
        children = []
        while raw:
            next_elt, raw = self.get_next_and_leftovers(raw, head)
            children.append(next_elt)
        return children

    def get_next_and_leftovers(self, raw: str, head: dict) -> tuple["DocElement", str]:
        doc_element_types: list[DocElement] = [
            Section,
            Subsection,
            Subsubsection,
            CodeBlock,
            TexBlock,
            UnorderedList,
            OrderedList,
            Image,
            EmptyLine,
            # multicolumn block must come before table
            MulticolumnBlock,
            Table,
        ]
        for elt_type in doc_element_types:
            if elt_type.matches(raw):
                return elt_type.get_with_leftovers(raw, head)
        # Paragraph is the catchall for anything that doesn't match elsewhere
        return Paragraph.get_with_leftovers(raw, head)

    def split_md_table_row(self, row: str) -> list[str]:
        return [x.strip() for x in row.split("|")[1:-1]]


# ==========


class Document(DocElement):

    def __init__(self, md_path: str):
        head, body = self._get_head_and_body(md_path)
        self._children = self.get_children(body, head)
        self._params = head

    def _get_head_and_body(self, md_path: str) -> tuple[dict, str]:
        with open(md_path, "r") as handle:
            lines = [x.rstrip() for x in handle.readlines()]
        header_lines = []
        while lines:
            line = lines.pop(0)
            if line.startswith("---"):
                break
            header_lines.append(line)
        if lines:
            try:
                head = yaml.safe_load("\n".join(header_lines)) or {}
            except yaml.scanner.ScannerError:
                raise ParseFailure("failed to parse yaml header")
            body = "\n".join(lines)
        else:
            # no YAML header
            head = {}
            body = "\n".join(header_lines)
        return head, body

    def to_tex(self):
        contents = self._children_to_tex()
        return self.with_variables(self.with_template(contents))

    def with_template(self, content: str) -> str:
        template_name = self._params.get("template")
        if not template_name:
            return content
        # this script lives in build/md2tex
        # templates dir is build/templates
        build_path = pathlib.Path(__file__).resolve().parent.parent
        template_path = f"{build_path}/templates/{template_name}"
        try:
            with open(template_path, "r") as handle:
                template = handle.read()
        except FileNotFoundError:
            raise ParseFailure(f"template '{template_name}' not found")
        return template.replace("@@content@@", content)

    def with_variables(self, content: str) -> str:
        for key, val in self._params.items():
            if f"@@{key}@@" in content:
                if isinstance(val, str):
                    tex_val = Paragraph(val, {}).to_tex()
                elif isinstance(val, list):
                    md_val = "\n".join(f"- {x}" for x in val)
                    tex_val = UnorderedList(md_val, {}).to_tex()
                else:
                    raise ParseFailure(f"unable to insert value for '{key}'")
                content = content.replace(f"@@{key}@@", tex_val)
        return content


# ==========


class SectionBase(DocElement):

    _DEPTH = 0

    def __init__(self, raw, head):
        title, contents = self.get_title_and_contents(raw)
        self._params = {"title": title, "beamer": head.get("beamer", False)}
        self._children = self.get_children(contents, head)

    @property
    def _title(self):
        return self._params["title"]

    @property
    def _is_beamer(self):
        return self._params["beamer"]

    def get_title_and_contents(self, body: str) -> tuple[str, str]:
        if "\n" in body:
            title, contents = body.split("\n", 1)
        else:
            title, contents = body, ""
        return title.split(None, 1)[-1], contents

    @classmethod
    def matches(cls, raw: str) -> bool:
        return raw.startswith("#"*cls._DEPTH + " ")

    @classmethod
    def get_with_leftovers(cls, body: str, head: dict) -> tuple[DocElement, str]:
        current, leftovers = cls.get_contents_and_leftovers(body)
        return cls(current, head), leftovers

    @classmethod
    def get_contents_and_leftovers(cls, body: str) -> tuple[str, str]:
        # Section ends when we hit another section or end of file. Subsection
        # ends when we hit section, subsection, or EOF. etc
        delims = [i*"#" + " " for i in range(1, cls._DEPTH+1)]
        leftover_lines = body.splitlines()
        # don't break on the first line. we are in a section and looking for the start of the next section
        lines = [leftover_lines.pop(0)]
        while leftover_lines:
            if any(leftover_lines[0].startswith(d) for d in delims):
                break
            lines.append(leftover_lines.pop(0))
        return "\n".join(lines), "\n".join(leftover_lines)


class Section(SectionBase):

    _DEPTH = 1

    def to_tex(self) -> str:
        if self._is_beamer:
            return "\n\\Section{" + self._title + "}\n" + self._children_to_tex()
        else:
            return "\n\\section{" + self._title + "}\n" + self._children_to_tex()


class Subsection(SectionBase):

    _DEPTH = 2

    def to_tex(self) -> str:
        if self._is_beamer:
            return "\n\\Subsection{" + self._title + "}\n" + self._children_to_tex()
        else:
            return "\n\\subsection{" + self._title + "}\n" + self._children_to_tex()


class Subsubsection(SectionBase):

    _DEPTH = 3

    def to_tex(self) -> str:
        if self._is_beamer and self.contains_code():
            return "\\begin{frame}[fragile]{" + self._title + "}" + self._children_to_tex() + "\n\\end{frame}"
        elif self._is_beamer:
            return "\\begin{frame}{" + self._title + "}" + self._children_to_tex() + "\n\\end{frame}"
        else:
            return "\n\\subsubsection{" + self._title + "}\n" + self._children_to_tex()


# ==========


class UnorderedList(DocElement):

    _HTML_TAG = "ul"
    _MARKERS = ("- ", "* ")

    def __init__(self, raw, head):
        self._children = self._get_items(raw, head)

    def to_tex(self) -> str:
        return r"\begin{itemize}" + "\n" + self._children_to_tex() + "\n" + r"\end{itemize}"

    @classmethod
    def matches(cls, raw: str) -> bool:
        return any(raw.startswith(m) for m in cls._MARKERS)

    @classmethod
    def get_with_leftovers(cls, body: str, head: dict) -> tuple[DocElement, str]:
        # list continues as long as we see indented lines and lines starting with list markers
        # TODO: smarter indentation handling for nested lists
        current, leftovers = cls.break_at_line_starting_without(body, [" ", "- ", "* "])
        return cls(current, head), leftovers

    def _get_items(self, raw: str, head: dict) -> list[DocElement]:
        raw_items = []
        for line in raw.splitlines():
            if self.matches(line):
                raw_items.append(line)
            else:
                raw_items[-1] += "\n" + line
        return [ListItem(ri, head) for ri in raw_items]


class OrderedList(DocElement):

    _HTML_TAG = "ol"

    def __init__(self, raw, head):
        self._children = self._get_items(raw, head)

    def to_tex(self) -> str:
        return r"\begin{enumerate}" + "\n" + self._children_to_tex() + "\n" + r"\end{enumerate}"

    @classmethod
    def matches(cls, raw: str) -> bool:
        if not raw:
            return False
        # look only at the first line. do not absorb leading empty lines
        first_line = raw.split("\n", 1)[0]
        if not first_line.strip():
            return False
        first_word = first_line.split(None, 1)[0]
        if first_word.endswith(".") or first_word.endswith(")"):
            return first_word[:-1].isdigit()
        else:
            return False

    @classmethod
    def get_with_leftovers(cls, raw: str, head: dict) -> tuple[DocElement, str]:
        # list continues as long as we see indented lines and lines starting with list markers
        leftover_lines = raw.splitlines()
        lines = [leftover_lines.pop(0)]
        while leftover_lines:
            line = leftover_lines[0]
            if line.startswith(" ") or cls.matches(line):
                lines.append(leftover_lines.pop(0))
            else:
                break
        return cls("\n".join(lines), head), "\n".join(leftover_lines)

    def _get_items(self, raw: str, head: dict) -> list[DocElement]:
        raw_items = []
        for line in raw.splitlines():
            if self.matches(line) or not raw_items:
                raw_items.append(line)
            else:
                raw_items[-1] += "\n" + line
        return [ListItem(ri, head) for ri in raw_items]


class ListItem(DocElement):

    _HTML_TAG = "li"

    def __init__(self, raw, head):
        # chop off the list item delimiter
        raw = raw.split(None, 1)[-1]
        # if this is a multi-line item, following lines are indented. chop
        # that off so we can identify nested stuff
        if "\n" in raw:
            lines = raw.splitlines()
            depth = len(lines[1]) - len(lines[1].lstrip())
            lines = lines[:1] + [l[depth:] for l in lines[1:]]
            raw = "\n".join(lines)

        # list items are usually just a line of text. but in principle one list
        # item can have multiple lines of text, code blocks, etc.
        self._children = self.get_children(raw, head)

    def to_tex(self):
        return r"\item " + self._children_to_tex() + "\n"


# ==========


class FencedBlock(DocElement):

    _FENCE = None

    @classmethod
    def matches(cls, raw: str) -> bool:
        return raw.startswith(cls._FENCE) and "\n" + cls._FENCE in raw

    @classmethod
    def get_with_leftovers(cls, raw: str, head: dict) -> tuple[DocElement, str]:
        assert cls.matches(raw)
        raw = raw.lstrip(cls._FENCE)
        assert ("\n" + cls._FENCE) in raw
        body_and_leftovers = raw.split("\n" + cls._FENCE, 1)
        if len(body_and_leftovers) > 1:
            body, leftovers = body_and_leftovers
        else:
            body, leftovers = body_and_leftovers[0], ""
        return cls(body, head), leftovers


class CodeBlock(FencedBlock):

    _FENCE = "```"

    def __init__(self, body, head):
        first_line, content = body.split("\n", 1)
        if "," in first_line:
            language, flags = first_line.split(",", 1)
        else:
            language, flags = first_line, None
        self._params = {"language": language or "text", "flags": flags}
        self._children.append(Literal(content, head))

    def to_tex(self) -> str:
        language = self._params["language"]
        content = self._child_to_tex()
        flags = self._params["flags"]
        if flags:
            return r"\begin{minted}[" + flags + "]{" + language + "}\n" + content + "\n" + r"\end{minted}"
        else:
            return r"\begin{minted}{" + language + "}\n" + content + "\n" + r"\end{minted}"


class TexBlock(FencedBlock):

    _FENCE = "$$$"

    def __init__(self, raw, head):
        self._children.append(Literal(raw, head))

    def to_tex(self) -> str:
        return self._child_to_tex()


class MulticolumnBlock(FencedBlock):

    _FENCE = "|||"

    def __init__(self, raw, head):
        self._children = self.get_children(raw, head)

    def to_tex(self) -> str:
        return r"\bigskip\begin{multicols}{2}" + "\n" + self.indent(self._children_to_tex()) + "\n" + r"\end{multicols}\bigskip"


# ==========


class Table(DocElement):

    def __init__(self, raw, head):
        lines = raw.splitlines()
        self._children.append(TableRow(lines[0], head))
        self._params['align'] = self.get_alignment(lines[1])
        for line in lines[2:]:
            self._children.append(TableRow(line, head))

    def get_alignment(self, row) -> str:
        entries = self.split_md_table_row(row)
        alignments = []
        for entry in entries:
            if entry.startswith(":") and not entry.endswith(":"):
                alignments.append("l")
            elif not entry.startswith(":") and entry.endswith(":"):
                alignments.append("r")
            else:
                alignments.append("c")
        return " ".join(alignments)

    def to_tex(self) -> str:
        # horizontal line after the header
        open = r"\begin{tabular}{" + self._params["align"] + "}"
        content = "\n".join(
        [self._children[0].to_tex(), r"\hline"] + [child.to_tex() for child in self._children[1:]]
        )
        close = r"\end{tabular}"
        return open + "\n" + self.indent(content) + "\n" + close

    @classmethod
    def matches(cls, raw: str) -> bool:
        return raw.startswith("|")

    @classmethod
    def get_with_leftovers(cls, raw: str, head: dict) -> tuple[DocElement, str]:
        assert cls.matches(raw)
        lines = []
        leftover_lines = raw.splitlines()
        while leftover_lines and cls.matches(leftover_lines[0]):
            lines.append(leftover_lines.pop(0))
        return cls("\n".join(lines), head), "\n".join(leftover_lines)


class TableRow(DocElement):

    def __init__(self, raw, head):
        values = self.split_md_table_row(raw)
        self._children = [Paragraph(v, head) for v in values]

    def to_tex(self) -> str:
        children = [c.to_tex() for c in self._children]
        return " & ".join(children) + r" \\"


# ==========


class Paragraph(DocElement):

    _HTML_TAG = "p"

    def __init__(self, raw, head):
        self._children = self.get_inline_children(raw, head)

    def get_inline_children(self, raw, head):
        children = []
        while raw:
            child, raw = self.get_next_and_leftovers_inline(raw, head)
            children.append(child)
        return children

    def get_next_and_leftovers_inline(self, raw, head):
        for cls in [InlineCode, Bold, Italic, URL, Hyperlink, Comment]:
            if cls.matches(raw):
                try:
                    return cls.get_with_leftovers_inline(raw, head)
                except Exception:
                    print("UH OH")
                    print(cls, "choked on:", repr(raw))
                    raise
        # otherwise, we're grabbing plain text. Start by just taking one
        # character at a time. We can optimize this later by taking chunks with
        # no special characters
        return Literal(raw[:1], head), raw[1:]

    @classmethod
    def matches(cls, raw: str) -> bool:
        # this is the default that catches everything unmatched
        return True

    def to_tex(self):
        return "".join(c.to_tex() for c in self._children)

    def to_html(self):
        return "".join(c.to_html() for c in self._children)

    @classmethod
    def get_with_leftovers(cls, raw: str, head: dict) -> tuple[DocElement, str]:
        lines = raw.splitlines()
        return cls(lines[0], head), "\n".join(lines[1:])


class InlineBase(DocElement):

    _DELIM = ""

    # TODO: need to handle code within bold. italic within bold
    def __init__(self, raw, head):
        self._children.append(Literal(raw, head))

    @classmethod
    def get_with_leftovers_inline(cls, raw: str, head: dict) -> tuple[DocElement, str]:
        assert cls.matches(raw)
        content, leftovers = raw.lstrip(cls._DELIM).split(cls._DELIM, 1)
        return cls(content, head), leftovers

    @classmethod
    def matches(cls, raw) -> bool:
        # watch out for overlapping delimiters, such as italic (*) and bold (**)
        return raw.startswith(cls._DELIM) and not raw[1:].startswith(cls._DELIM)


class InlineCode(InlineBase):

    _DELIM = "`"

    def to_tex(self) -> str:
        return r"\verb|" + self._child_to_tex() + "|"

    def to_html(self) -> str:
        return "<code>" + self._child_to_html() + "</code>"
    

class Bold(InlineBase):

    _DELIM = "**"

    def to_tex(self) -> str:
        return r"\textbf{" + self._child_to_tex() + "}"

    def to_html(self) -> str:
        return "<b>" + self._child_to_html() + "</b>"


class Italic(InlineBase):

    _DELIM = "*"

    def to_tex(self) -> str:
        return r"\emph{" + self._child_to_tex() + "}"

    def to_html(self) -> str:
        return "<i>" + self._child_to_html() + "</i>"


class URL(InlineBase):

    @classmethod
    def matches(cls, raw):
        return raw.startswith("http://") or raw.startswith("https://")

    @classmethod
    def get_with_leftovers_inline(cls, raw: str, head: dict) -> tuple[DocElement, str]:
        assert cls.matches(raw)
        next_word = raw.split(None, 1)[0]
        leftovers = raw[len(next_word):]
        return cls(next_word, head), leftovers

    def to_tex(self) -> str:
        return r"\url{" + self._child_to_tex() + "}"


class Hyperlink(InlineBase):

    def __init__(self, text, url, head): 
        self._children = [Paragraph(text, {})]
        self._params = {"url": url}

    @classmethod
    def matches(cls, raw):
        return raw.startswith("[") and "](" in raw and ")" in raw.split("](")[1]

    @classmethod
    def get_with_leftovers_inline(cls, raw: str, head: dict) -> tuple[DocElement, str]:
        assert cls.matches(raw)
        text, leftovers = raw[1:].split("](", 1)
        url, leftovers = leftovers.split(")", 1)
        return cls(text, url, head), leftovers

    def to_tex(self) -> str:
        return r"\href{" + self._params["url"] + "}{" + self._child_to_tex() + "}"


class Comment(InlineBase):

    def __init__(self, body, head):
        self._children = [Literal(body, head)]

    def to_tex(self):
        return "%" + self._child_to_tex()
    
    @classmethod
    def matches(cls, raw: str) -> bool:
        return raw.lstrip().startswith("%")

    @classmethod
    def get_with_leftovers_inline(cls, raw: str, head: dict) -> tuple[InlineBase, str]:
        # Quote absorbs the whole remaining line
        return cls(raw.lstrip()[1:], head), ""


# ==========


class Image(DocElement):

    def __init__(self, alt_text, url):
        self._params = {"alt_text": alt_text, "url": url}
        self._children = []

    @classmethod
    def matches(cls, raw):
        return raw.startswith("![") and "](" in raw and ")" in raw.split("](", 1)[1]

    @classmethod
    def get_with_leftovers(cls, raw, head):
        assert cls.matches(raw)
        alt_text, leftovers = raw[2:].split("](")
        url, leftovers = leftovers.split(")", 1)
        return cls(alt_text, url), leftovers

    def to_tex(self):
        alt_text = self._params["alt_text"]
        url = self._params["url"]
        return r"\begin{center}\includegraphics[width=0.9\columnwidth, height=0.9\textheight, keepaspectratio]{" + url + r"}\end{center}"


class EmptyLine(DocElement):

    def __init__(self, body, head):
        pass

    def to_tex(self):
        return "\n"
    
    def to_html(self) -> str:
        return "<br \\>"
    
    @classmethod
    def matches(cls, raw: str) -> bool:
        return raw and not raw.splitlines()[0].strip()

    @classmethod
    def get_with_leftovers(cls, raw: str, head: dict) -> tuple[DocElement, str]:
        # if there are multiple empty lines in a row, absorb them all
        lines = raw.splitlines()
        while lines and not lines[0].strip():
            lines.pop(0)
        return cls("", head), "\n".join(lines)


class Literal(DocElement):

    def __init__(self, raw, head):
        self._params = {"text": raw}

    def to_tex(self):
        return self._params["text"]

    def to_html(self) -> str:
        return self._params["text"]
