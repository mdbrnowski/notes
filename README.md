# notes

> Too many authors to cite?
>
> No problem et al.

## My notes, articles, papers, etc.

### Computer Science at AGH University

* **analiza.tex** [[pdf](https://mdbrnowski.github.io/notes/pdf/analiza.pdf)] – *Analiza II*
* **algebra.tex** [[pdf](https://mdbrnowski.github.io/notes/pdf/algebra.pdf)] – *Algebra*

### Miscellaneous

* **filtr.tex** [[pdf](https://mdbrnowski.github.io/notes/pdf/filtr.pdf)] – *Funkcje tworzące i filtracja pierwiastkami jedności*
* **fft.tex** [[pdf](https://mdbrnowski.github.io/notes/pdf/fft.pdf)] - *Szybka transformacja Fouriera (FFT)*

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
* `polish` – Polish version (keywords and other)

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
* Math operators (`\cis`, `\lcm`, ...)
* Commands (`\iff`, `\implies`, `\vocab`, ...)
* Symbols (`\sA` for `\mathcal A` and `\scA` for `\mathscr A`)
* And more (it's best to see it for yourself in the source file)

## A few words about the software environment

To use this repository on your computer you need to have [Task](https://taskfile.dev/) and [tectonic](https://github.com/tectonic-typesetting/tectonic) installed. In my opinion, it is the best choice when it comes to both small and large LaTeX projects. Besides that, I recommend using [textidote](https://sylvainhalle.github.io/textidote/), which allows you to check your work for grammar and spelling.
