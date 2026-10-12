\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesPackage{TesiDiaUniroma3}[2008/02/13 v1.0 Tesi - DIA-Uniroma3]

\LoadClass[a4paper,11pt,oneside,italian]{memoir}

% Si utilizza la sillabazione italiana
\RequirePackage[italian]{babel}
% Load graphicx
\RequirePackage{graphicx}
% Line spacing
\RequirePackage{setspace}
% pacchetti AGGIUNTIVI
\usepackage{listings}
\usepackage{csvsimple}
% pacchetti per i font
\usepackage[T1]{fontenc}
% interlinea
\linespread{1.8}
% margini (la dimensione del blocco di testo viene regolata di conseguenza)
\setlrmarginsandblock{3.5cm}{2.5cm}{*}
% profondità dell'indice (settato per stampare fino alle sottosezioni)
\setcounter{tocdepth}{2}
% numera parti, capitoli, sezioni, sottosezioni e sotto-sottosezioni
\maxsecnumdepth{subsubsection}
\setsecnumdepth{subsubsection}

% header personalizzati
\let\footruleskip\relax % for compatibility of memoir and fancyhdr
\let\rm\rmfamily        % for compatibility of memoir and blindtext (demo only)
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\addtolength{\headheight}{14pt}
\fancyhead[R]{\textbf{\thepage}}
\fancyhead[L]{\textbf{\leftmark}}

% AnnoAccademico (Anno/Anno+1)
\newcommand{\@annoAccademico}{2019/2020}
\newcommand{\annoAccademico}[1]{\renewcommand{\@annoAccademico}{#1}}
% Autore 
\newcommand{\@autore}{Cognome Nome}
\newcommand{\autore}[1]{\renewcommand{\@autore}{#1}}
% Titolo
\newcommand{\@titolo}{Titolo della tesi}
\newcommand{\titolo}[1]{\renewcommand{\@titolo}{#1}}
% Matricola 
\newcommand{\@matricola}{000000}
\newcommand{\matricola}[1]{\renewcommand{\@matricola}{#1}}
% Relatore (Titolo Nome Cognome, es: Prof. Pippo Caruso)
\newcommand{\@relatore}{Prof. Nome Cognome}
\newcommand{\relatore}[1]{\renewcommand{\@relatore}{#1}}
% correlatori (Titolo Nome Cognome, es: Dott. Pippo Caruso)
\newcommand{\@correlatori}{Ing. Nome Cognome}
\newcommand{\correlatori}[1]{\renewcommand{\@correlatori}{#1}}
% correlatori (Titolo Nome Cognome, es: Dott. Pippo Caruso)
\newcommand{\@correlatore}{Ing. Nome Cognome}
\newcommand{\correlatore}[1]{\renewcommand{\@correlatore}{#1}}


% Dedica
\newcommand{\@dedica}{}
\newcommand{\dedica}[1]{\renewcommand{\@dedica}{#1}}

% Generazione del FRONTESPIZIO
\newcommand{\generaFrontespizio}{
   \thispagestyle{empty}
   \begin{center}
      \vspace{5mm}
      {\includegraphics[width=0.75 \linewidth]{figure/logoRomaTRE.png}} \\
      \vspace{5mm}
      {\Large UNIVERSIT\`A DEGLI STUDI ROMA TRE} \\
      \vspace{5mm}
      {\LARGE Dipartimento di Ingegneria Civile, Informatica e delle Tecnologie Aeronautiche} \\
      {\Large Corso di Laurea Triennale in Ingegneria Informatica} \\
      \vspace{7mm}
      {\LARGE Tesi di Laurea Triennale} \\
      \vspace{7mm}
      {\textsc{\huge \@titolo}} \\
      \vspace{7mm}
      \vspace{10mm}
\vspace{10mm}
\noindent
\begin{minipage}[t]{0.45\textwidth}
\centering
\textbf{Laureando} \\
\@autore \\
Matricola \@matricola
\end{minipage}
\hfill
\begin{minipage}[t]{0.45\textwidth}
\centering
\textbf{Relatore} \\
\@relatore \\[3mm]
\textbf{Correlatrice} \\
\@correlatore
\end{minipage}

      \vspace{5mm}


      \vfill
      {\large Anno Accademico \@annoAccademico} \\
   \end{center}
   \newpage 
}

% Comandi riguardanti l'inserimento di capitoli
\newcommand{\ringraziamenti}[1]{\newpage \chapter*{Ringraziamenti} \input{#1}}
\newcommand{\introduzione}[1]{\newpage \chapter{Introduzione} \input{#1}}
\newcommand{\conclusioni}[1]{\newpage \chapter{Conclusioni} \markboth{CONCLUSIONI}{CONCLUSIONI} \input{#1}}
\newcommand{\capitolo}[2]{\newpage \chapter{#1}\label{cap:#2}\input{#2}}

% Comandi riguardanti la generazione di indici
\newcommand{\generaIndice}{
	%\fancyhead[L]{\textbf{\rightmark}}
	\newpage
	\tableofcontents
	\clearpage
	%\fancyhead[L]{\textbf{\leftmark}}
}
\newcommand{\generaIndiceTabelle}{\newpage \listoftables}
\newcommand{\generaIndiceFigure}{\newpage \listoffigures}

% Bibliografia in ordine alfabetico
\let \OldBib \bibliography
\renewcommand{\bibliography}[1]{\newpage \markboth{Bibliografia}{Bibliografia} \OldBib{#1}}
\bibliographystyle{unsrt} %acm for numerical order