#!/usr/bin/env python3

import sys
import yaml


def to_macro_name(key: str, singularize: bool = False) -> str:
    if singularize and key.endswith("s") and not key.endswith("ss"):
        key = key[:-1]
    return "".join(part.capitalize() for part in key.split("_") if part)


def render_vars(data: dict) -> str:
    lines = [
        "% Auto-generated from vars.yaml -- do not edit directly",
        r"\RequirePackage{xspace}",
        "",
    ]
    for key, val in data.items():
        if isinstance(val, list):
            macro = to_macro_name(key, singularize=True)
            lines.append(f"\\newcommand{{\\{macro}}}[1]{{%")
            lines.append("  \\ifcase#1\\relax")
            for item in val:
                lines.append(f"  \\or {item}\\xspace")
            lines.append(r"  \else \textcolor{red}{TBD}\xspace")
            lines.append("  \\fi")
            lines.append("}")
        elif val is not None:
            macro = to_macro_name(key)
            lines.append(f"\\newcommand{{\\{macro}}}{{{val}\\xspace}}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <vars.yaml> <output.gen.tex>", file=sys.stderr)
        return 1
    in_path, out_path = sys.argv[1], sys.argv[2]
    print(f"building {in_path} -> {out_path} ... ", end="", flush=True)
    with open(in_path, "r") as handle:
        data = yaml.safe_load(handle) or {}
    with open(out_path, "w") as handle:
        handle.write(render_vars(data))
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
