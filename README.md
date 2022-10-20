# notes

## My notes, articles, papers, etc.

### Computer Science at AGH UST

* 🚧 **algebra.tex** ([pdf](pdf/algebra.pdf)) – *Algebra, dr hab. Jakub Przybyło*

### Miscellaneous

* **filtr.tex** ([pdf](pdf/filtr.pdf)) – *Funkcje tworzące i filtracja pierwiastkami jedności*

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
