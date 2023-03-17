# notes

## My notes, articles, papers, etc.

### Computer Science at AGH UST

* 🚧 **analiza.tex** ([pdf](pdf/analiza.pdf)) – *Analiza II*
* 🚧 **algebra.tex** ([pdf](pdf/algebra.pdf)) – *Algebra*

### Miscellaneous

* **filtr.tex** ([pdf](pdf/filtr.pdf)) – *Funkcje tworzące i filtracja pierwiastkami jedności*
* **fft.tex** ([pdf](pdf/fft.pdf)) - *Szybka transformacja Fouriera (FFT)*

<br>

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
    \eject
\end{document}
```

To the package `mystd.sty` one can pass a few arguments:

* `thm`/`nothm` – colors and frames for theorems and similar environments
* `colorsec`/`nocolorsec` – prettier sections numeration
* `pretty` – passes `thm` and `colorsec`
* `polish` – polish version (keywords and other)

In `mystd.sty` I have also defined:

* Environments
  * `theorem` (Theorem, Twierdzenie)
  * `lemma` (Lemma, Lemat)
  * `corollary` (Corollary, Wniosek)
  * `example` (Example, Przykład)
  * `remark` (Remark, Uwaga)
  * `conjecture` (Conjecture, Przypuszczenie)
  * `definition` (Definition, Definicja)
  * `exercise` (Exercise, Ćwiczenie)
  * `fact` (Fact, Fakt)
  * `problem` (Problem, Problem)
  * `question` (Question, Pytanie)
* Math operators (`\cis`, `\lcm`, `\Arg`, ...)
* Commands (`\iff`, `\implies`, `\vocab`, ...)
* Symbols (`\sA` for `\mathcal A` and `\scA` for `\mathscr A`)
* And more (it's best to see it for yourself in the source file)

## A few words about the software environment

To use this repository on your computer you need to have [Task](https://taskfile.dev/) and [tectonic](https://github.com/tectonic-typesetting/tectonic) installed. In my opinion, it is the best choice when it comes to both small and large LaTeX projects.
