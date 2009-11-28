############################################################################
#    Copyright (C) 2009 by Thomas Hille                                    #
#    thomas.hille@nightsabers.org                                          #
#                                                                          #
#    This program is free software; you can redistribute it and#or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
############################################################################

.PHONY: cachegrind clean docs release stats tests

VERSION=0.0.1
#BUILDVERSION=$(VERSION)
BUILDVERSION=$(VERSION)-svn.$(shell svnversion | sed 's/M$$//')

# don't change the following
RELEASEDIR=condensation-$(BUILDVERSION)
RELEASEFILE=condensation-$(BUILDVERSION).tar.bz2
DOCRELEASEFILE=condensation-docs-$(BUILDVERSION).tar.bz2

cachegrind:
	@python scripts/pyprof2calltree.py -i profile.out -o cachegrind.out


clean:
	@echo -e "\n============================ CLEANING UP =================================\n"
	@rm -fr $(RELEASEDIR)
	@rm -f $(RELEASEFILE)
	@find . -regextype posix-extended -type f -iregex ".*(~|\.pyc)" -delete
	@rm -f cachegrind.out
	@rm -f .coverage


docs:
	@echo -e "\n========================= BUILDING API DOCS ==============================\n"
	@rm -fr docs
	@epydoc --check --config scripts/epydoc.config


release: docs clean
	@echo -e "\n====================== MAKING REALEASE v$(BUILDVERSION) ===========================\n"
	@mkdir $(RELEASEDIR)
	@cp -R condensation images plugins COPYING run-condensation.py $(RELEASEDIR)
	@tar --exclude=.svn -cjf $(RELEASEFILE) $(RELEASEDIR)
	@rm -fr $(RELEASEDIR)
	@tar -cjf $(DOCRELEASEFILE) docs
	

stats:
	@echo "Statistics:"
	@echo -n "Lines in .py files without empty lines: "
	@find . -iname "*.py" | xargs cat -s | wc -l


tests:
	@echo -e "\n=========================== RUNNING TESTS ================================\n"
	@python-coverage -x tests/run-tests.py
	@echo -e "\n=========================== CODE COVERAGE ================================\n"
	@python-coverage -r -o /usr

