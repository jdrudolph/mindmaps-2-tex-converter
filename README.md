mindmaps-2-tex-converter
========================


This python code takes as input a mindmap and converts it either into a nice Latexed list or into beamer slides.

To create mindmaps I can recommend free mind : [project page and download](http://freemind.sourceforge.net/wiki/index.php/Main_Page)

On UNIX systems texcreator can be used as stand-alone.
Run once:

    chmod +x texcreator.py

Type `./texcreator.py --help` for usage information

Afterwards create pdf from latex file in command line as follows:

    rubber -d /path/to/latex_file.tex

`rubber` is a convenient wrapper for `pdflatex` which is the standard for
converting `.tex` to `.pdf`.

A more integrated workflow might look like:

    ./texcreator.py /path/to/MindMap.mm --to beamer | rubber-pipe -d > presentation.pdf


**Enjoy!**
