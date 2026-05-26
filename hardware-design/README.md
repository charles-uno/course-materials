# Hardware Design (CSCI 241)

Course materials by Charles Fyfe. Adapted in part from materials by Melissa Lynn

Course listing [here](https://catalog.stolaf.edu/academic-programs/computer-science)

## Just The PDFs Please!

PDFs are built automatically using GitHub Actions. Check out the `Actions` tab up top. 

## Repo Summary

- `syllabus` - The syllabus. Information about curriculum, grading, policies, etc
- `chapters` - This holds most of the actual content! Each chapter contains slides, homework, and a quiz
- `project` - Document explaining the final project for the course
- `final` - The final exam. Also some tooling to generate personalized exams for each student based on what they've already demonstrated
- `build` - Templates and scripts for building our Markdown source files into PDFs via LaTeX

## Building Locally

Typesetting is done via LaTeX. Source code for LaTeX is pretty ugly, so much of the content is written in Markdown and converted over at build time. If you want to run that process locally, you'll need:

- MikTex, MacTex, or similar. The big install
- Python 3, plus the packages in `build/requirements.txt`
- Make

These requirements are for Mac OS. Linux is probably pretty much the same. If you need it to run on Windows, I'll bet an AI bot can figure it out

Circuit diagrams created using [this tool](https://www.circuit2tikz.tf.fau.de/designer/)

# TODO - Curriculum

Add dedicated DISCUSSION slides. not just a question in the middle of a list

Add BOARD WORK slides. Ideally one per section. Dedicated group work

TODO: add stretch goals to the homework? Stuff that is hard! many students will not be able to do it! we don't expect everyone to get it right. not worth that many points. it's like giving your tiger a frozen pumpkin full of hamburger meat. enrichment

Switch from `word` to `long`? Some weirdness around 64-bit comparisons on 32-bit values

circuitverse - clarify that the button is a different type of input
add screenshots to help with testbench setup

# TODO - Repo

md2tex pending updates:
- handle block quotes

Handle repo-level `header.yaml`. Same pattern as the directory-level one. Just author and course title I guess

Figure out how to create tagged PDFs for accessibility


