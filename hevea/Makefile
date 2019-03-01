# Hevea
# LaTeX Makefile.  This file has compilation rules to help you process
# this kind of documents.
#
# Author: José Lopes Oliveira Jr. <jilo.cc>
# Based on J. F. Mitre's Makefile.
#
# LICENSE
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# USAGE
# Symply copy this file to the root of your LaTeX project root and run
# ``make'' to create a PDF output.
#
# For further options, run ``make help''.
#
# NOTES
# LaTeX main file must have \begin{document} as the first command of a
# line.  Spaces before it ---indentation--- are allowed.  The same for 
# \bibliography and \makenomenclature ---nomencl package.
##


##
# GLOBAL VARIABLES
# DOC - determines the main file name.
# BIB - is empty if you're not using bibliography.
# NOM - work like BIB, but for nomenclature with nomencl package.
#
DOC = $(shell grep -l '^[ ]*\\begin{document}' *.tex | sed 's/.tex$$//')
BIB = $(shell grep -l '^[ ]*\\bibliography' $(DOC).tex 2> /dev/null)
NOM = $(shell grep -l '^[ ]*\\makenomenclature' $(DOC).tex 2> /dev/null)

ERR_MAIN_NOT_FOUND = HEVEA: Unable to find main file ---\\\begin{document}.


##
# RULES
#
.PHONY: clean mostlyclean

# pdflatex by default
all:
	@if [ -z $(DOC) ]; then echo "$(ERR_MAIN_NOT_FOUND)";\
		exit 1; fi
	@pdflatex $(DOC).tex
	@if [ ! -z $(BIB) ]; then bibtex $(DOC); fi
	@if [ ! -z $(NOM) ]; then makeindex $(DOC).nlo -s nomencl.ist \
		-o $(DOC).nls; fi
	@pdflatex $(DOC).tex
	@pdflatex $(DOC).tex
	
# dvi rule not tested
dvi:
	@if [ -z $(DOC) ]; then echo "$(ERR_MAIN_NOT_FOUND)";\
		exit 1; fi
	@latex $(DOC).tex
	@if [ ! -z $(BIB) ]; then bibtex $(DOC); fi
	@if [ ! -z $(NOM) ]; then makeindex $(DOC).nlo -s nomencl.ist \
		-o $(DOC).nls; fi
	@latex $(DOC).tex
	@latex $(DOC).tex
	@dvips $(DOC).dvi
	@ps2pdf $(DOC).ps

mostlyclean:
	@find .\
		  -type f\
		  -regex '.*\.\(aux\|log\|toc\|lot\|lof\|ttt\|fff\|bbl\|blg\|out\|ind\|ilg\|idx\|glo\|gls\|abx\|nlo\|nls\|syx\)$$'\
		  -delete

clean: mostlyclean
	@find .\
		  -type f\
		  -regex '.*\.\(dvi\|ps\|pdf\|bak\|~\|tar\|gz\)$$'\
		  -delete

tar:
	@if [ -z $(DOC) ]; then echo "$(ERR_MAIN_NOT_FOUND)";\
		exit 1; fi
	@if [ -f "$(DOC).tar.gz" ]; then echo "HEVEA: Tar file already exists.";\
		exit 1; fi
	@find .\
		  -type f\
		  ! -regex '.*\.\(aux\|log\|toc\|lot\|lof\|ttt\|fff\|bbl\|blg\|out\|ind\|ilg\|idx\|glo\|gls\|abx\|nlo\|nls\|syx\|dvi\|ps\|pdf\|bak\|~\)$$' |\
	 xargs tar -czvf $(DOC).tar.gz

help:
	@echo "\n\
HEVEA - Makefile\n\
================\n\
1. Make sure this file is in the root of your LaTeX project.\n\n\
2. LaTeX main file must have its \\\begin{document} in the\n\
   beggining of the line ---you can put spaces before it.\n\n\
3. If you're using \\\bibliography or \\makenomenclature,\n\
   use the previous rule for them.\n\n\
4. Run \`\`make'' to compile your project.\n\n\
5. pdflatex is the default compiler, but you can use\n\
   latex instead, by using \`\`make dvi'' ---it'll create\n\
   the DVI and PS files to yield PDF output.\n\n\
6. Run \`\`make clean'' to remove LaTeX control files.\n\n\
7. \`\`make tar'' will compress project files ---except\n\
  for the compiled files--- into a .tar.gz file.\n\n\
8. Have fun!  :)\n\
"
