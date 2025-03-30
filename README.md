# notes

[![GitHub Repo stars](https://img.shields.io/github/stars/mdbrnowski/notes?style=flat-square&logo=github&color=yellow)](https://github.com/mdbrnowski/notes/)

## My notes, articles, papers, etc.

### Computer Science at AGH University

* **algebra.tex** [[pdf](https://mdbrnowski.github.io/notes/pdf/algebra.pdf)] – *Algebra*
* **analiza.tex** [[pdf](https://mdbrnowski.github.io/notes/pdf/analiza.pdf)] – *Analiza II*
* **toizo.tex** [[pdf](https://mdbrnowski.github.io/notes/pdf/toizo.pdf)] – *Teoria obliczeń i złożoności obliczeniowej*

### Miscellaneous

* **filtr.tex** [[pdf](https://mdbrnowski.github.io/notes/pdf/filtr.pdf)] – *Funkcje tworzące i filtracja pierwiastkami jedności*
* **fft.tex** [[pdf](https://mdbrnowski.github.io/notes/pdf/fft.pdf)] – *Szybka transformacja Fouriera (FFT)*

## The mystd.sty package

This repository contains `mystd.sty` – my template for creating notes in LaTeX.

```latex
\documentclass[11pt]{scrartcl}
\usepackage[pretty,polish]{mystd}
\title{}
\author{}
\date{}

\begin{document}
    \maketitle
    \tableofcontents
    \newpage
\end{document}
```

To the package `mystd.sty` one can pass a few arguments:

* `thm`/`nothm` – colors and frames for theorems and similar environments
* `colorsec`/`nocolorsec` – prettier sections numeration
* `pretty` – passes `thm` and `colorsec`
* `polish` – Polish version (keywords and other)
* `monofont` – use JetBrainsMono font
* `answers` – use answer and hint environments
