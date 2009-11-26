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

.PHONY: clean stats docs


clean:
	@find . -regextype posix-extended -type f -iregex ".*(~|\.pyc)" -delete
	@rm cachegrind.out


stats:
	@echo "Statistics:"
	@echo -n "Lines in .py files without empty lines: "
	@find . -iname "*.py" | xargs cat -s | wc -l


docs:
	@epydoc --check --config scripts/epydoc.config


cachegrind:
	@python scripts/pyprof2calltree.py -i profile.out -o cachegrind.out