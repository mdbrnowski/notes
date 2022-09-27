# notes

## My notes, articles, papers, etc.

* **filt.tex** – *Funkcje tworzące i filtracja pierwiastkami jedności*

## The `mystd.sty` package

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

Do pakietu `mystd.sty` można podać kilka argumentów:

* `thm`/`nothm` – kolory i ramki (lub ich brak) dla twierdzień i podobnych
* `colorsec`/`nocolorsec` – ładniejsze numerowanie sekcji (lub jego brak)
* `pretty` – podaje `thm` oraz `colorsec`
* `polish` – polskie słowa kluczowe i tytuły sekcji

Pakiet `mystd.sty` oferuje wiele dodatkowych narzędzi:

* Environments
  * `theorem` (Theorem, Twierdzenie)
  * `lemma` (Lemma, Lemat)
  * `corollary` (Corollary, Wniosek)
  * `algorithm` (Algorithm, Algorytm)
  * `claim` (Claim, Stwierdzenie)
  * `example` (Example, Przykład)
  * `remark` (Remark, Uwaga)
  * `conjecture` (Conjecture, Przypuszczenie)
  * `definition` (Definition, Definicja)
  * `exercise` (Exercise, Ćwiczenie)
  * `fact` (Fact, Fakt)
  * `problem` (Problem, Problem)
  * `question` (Question, Pytanie)
