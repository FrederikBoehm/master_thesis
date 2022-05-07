%
% Informatik 9 -  LaTeX Style for Thesis
%
% Heavily based on the University of Waterloo 1991 thesis style with
% 1995 extensions by Anil Goel and Andrej Brodnik.
%
% Adopted for the Informatik 9 by  Wolfgang Heidrich
%
% History (in Erlangen):
% ======================
%
% Initial Version:              Wolfgang Heidrich       Jan. 16, 1996
%
%                       Removed all additional features like
%                       the "prepage environment" that is required
%                       only in Waterloo.
%                       Fixed the rediculously large line spacing.
%


% export a new document class
% (based on the standard "report" class)
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{studdipl}[1996/01/16]
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions

\typeout{studdipl: Studien/Diplomarbeiten am Lehrstuhl fuer Graphische
Datenverarbeitung, Informatik 9}

\LoadClass{report}

%%%%
%
% Layout of the page:
%--------------------

                       % HORIZONTAL DIMENSIONS

   %----------------------------------------------------------------
   % NOTE: change only ``\textwidth'' and ``\evensidemargin'' (which
   %       is also outer margin - 1inch). The other margins are
   %       computed automatically.
   %----------------------------------------------------------------

   % Width of text:
\setlength{\textwidth}{6.5in}
   % Margins:
\setlength{\hoffset}{0pt}               % No horizontal offset, so the
                                        % margin is 1 inch already.
     % even side in two sided document:
\setlength{\evensidemargin}{0in}     % has to be added another 0.15in
     % odd sided in two sided document and outer in one sided docment:
\setlength{\oddsidemargin}{\paperwidth}        %    paperwidth
\addtolength{\oddsidemargin}{-1in}             %  - (1 in +    \
                                               %                = outer margin
\addtolength{\oddsidemargin}{-\evensidemargin} %     even side)/
\addtolength{\oddsidemargin}{-\textwidth}      %  - text width
\addtolength{\oddsidemargin}{-1in}             %  - 1 in       = default margin

   % Marginal notes:
\setlength{\marginparwidth}{0.90in}     % Width of marginal notes.
\setlength{\marginparsep}{0.10in}       % space between outer margin and
                                        % marginal note

                        % VERTICAL DIMENSIONS

   % Height of text:
\setlength{\textheight}{8in}  % including footnotes and figures,
                                % excluding running head and foot.
   % Margins:
\setlength{\topmargin}{0pt}     % just default 1inch on the top
\addtolength{\headheight}{12pt}
\setlength{\headsep}{20pt}


% allow figures to fill a large percentage of the page without
% creating a separate figure page.
\renewcommand{\topfraction}{0.999}
\renewcommand{\textfraction}{0.001}
\setcounter{topnumber}{10}
\setcounter{dbltopnumber}{10}
\setcounter{totalnumber}{10}
\renewcommand{\dbltopfraction}{0.999}
\renewcommand{\dblfloatpagefraction}{0.999}


% increase line spacing to make things more readable
\renewcommand{\baselinestretch}{1.1}


% for draft versions we add a heading with the date
\RequirePackage{fancyhdr}
% \headrulewidth0pt
\newcommand\draft{
  \rhead[{Draft version (\today)}]{}
  \lhead[{}]{Draft version (\today)}
}
\pagestyle{fancyplain}


% \prepages and \mainbody
% (prepages have roman page numbering)

\def\prepages{\normalfont\pagenumbering{roman}}
\def\mainbody{\pagenumbering{arabic}}


%
% Additional information for the title page + defaults
%
\newcommand\thesistype[1]{\gdef\@thesistype{#1}}
\newcommand\birthday[1]{\gdef\@birthday{#1}}
\newcommand\birthplace[1]{\gdef\@birthplace{#1}}
\newcommand\supervisor[1]{\gdef\@supervisor{#1}}
\newcommand\bdate[1]{\gdef\@bdate{#1}}
\newcommand\edate[1]{\gdef\@edate{#1}}

\gdef\@thesistype{$<$TYPE OF THESIS$>$}
\gdef\@title{$<$TITLE$>$}
\gdef\@author{$<$AUTHOR$>$}
\gdef\@birthday{$<$BIRTHDAY$>$}
\gdef\@birthplace{$<$BIRTHPLACE$>$}
\gdef\@supervisor{$<$SUPERVISOR$>$}
\gdef\@bdate{$<$BEGINNING OF THESIS$>$}
\gdef\@edate{$<$END OF THESIS$>$}

                             % TITLE PAGE

\renewcommand{\maketitle}{%
\begin{titlepage} \setlength{\parindent}{0pt}
\thispagestyle{empty}
\begin{center}
{\LARGE\bf\@title}
\vspace{1.50cm}

{\large \@thesistype\ im Fach Informatik}
\vspace{1.50cm}

{\small vorgelegt von}\bigskip

{\bf\@author}\bigskip

geb.\ am \@birthday\ in \@birthplace\bigskip
\vspace{1.5cm}

{\small angefertigt am}\bigskip

{\bf Department Informatik\\
Lehrstuhl Graphische Datenverarbeitung\\
Friedrich-Alexander-Universit\"at Erlangen-N\"urnberg}
\vfill

Betreuer: \@supervisor\\
\bigskip
Betreuender Hochschullehrer: Prof. Dr. Marc Stamminger
\vfill
\vfill

Beginn der Arbeit:\ \@bdate\bigskip

Abgabe der Arbeit:\ \@edate
\vfill

\end{center}
\newpage
\end{titlepage}
}% \maketitle


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% BIBLIOGRAPHY
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Redefine bibliography from report.cls to add a table of
% contents entry
\def\thebibliography#1{\chapter*{\bibname\@mkboth
  {\bibname}{\bibname}}\addcontentsline{toc}{chapter}{\bibname}\list
  {[\arabic{enumi}]}{\settowidth\labelwidth{[#1]}\leftmargin\labelwidth
    \advance\leftmargin\labelsep
    \usecounter{enumi}}
    \def\newblock{\hskip .11em plus .33em minus .07em}
    \sloppy\clubpenalty4000\widowpenalty4000
    \sfcode`\.=1000\relax}

\let\endthebibliography=\endlist


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% DECLARATION
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\declaration#1{
\parindent0pt
\chapter*{Erkl\"arung}
\bigskip

Ich versichere, dass ich die Arbeit ohne fremde Hilfe und ohne Benutzung
anderer als der angegebenen Quellen angefertigt habe und dass die Arbeit in
gleicher oder \"ahnlicher Form noch keiner anderen Pr\"ufungsbeh\"orde
vorgelegen hat und von dieser als Teil einer Pr\"ufungsleistung angenommen
wurde. Alle Ausf\"uhrungen, die w\"ortlich oder sinngem\"a\ss\ \"ubernommen
wurden, sind als solche gekennzeichnet.

\bigskip
Ich bin damit einverstanden, dass die Arbeit ver\"offentlicht wird und
dass in wissenschaftlichen Ver\-\"offent\-lich\-ungen auf sie Bezug genommen wird.

\def\test{#1}
\def\tmp{copyright}
\ifx\test\tmp
\typeout{Ausschliessliches Nutzungsrecht fuer die Universitaet}
\bigskip
Das ausschlie\ss liche Nutzungsrecht an dieser Arbeit, sowie an den, im
Zusammenhang mit ihr erstellten Programmen, liegt bei der Universit\"at
Erlangen-N\"urnberg, vertreten durch den Lehrstuhl f\"ur Graphische
Datenverarbeitung.
\fi

\def\tmp{nutzung}
\ifx\test\tmp
\typeout{Nutzungsrecht fuer die Universitaet}
\bigskip
Der Universit\"at Erlangen-N\"urnberg, vertreten durch den Lehrstuhl f\"ur
Graphische Datenverarbeitung, wird ein (nicht ausschlie\ss liches)
Nutzungsrecht an dieser Arbeit sowie an den im Zusammenhang mit ihr
erstellten Programmen einger\"aumt.
\fi

\vskip3cm
Erlangen, den \@edate\hfill

\hfill{\vbox{\hrule{\hbox{\strut$\qquad$\small(\@author)$\qquad$}}}}
\thispagestyle{empty}
}


% LocalWords:  LaTeX studdipl report pt topnumber dbltopnumber totalnumber toc
% LocalWords:  fancyheadings Draft version fancyplain roman arabic birthday em
% LocalWords:  birthplace supervisor bdate edate title author empty Universit
% LocalWords:  mkboth chapter enumi minus Erkl Pr Ausf sinngem ver copyright
% LocalWords:  fuer Universitaet ausschlie liche nutzung liches einger
