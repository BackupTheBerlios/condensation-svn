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


import logging

import condensation.core


class LogSink(logging.Handler, condensation.core.SignalSource):

    _records = []
    _records_text = []
    _global_callbacks = {
        'new-record': list(),
    }


    def __init__(self):
        logging.Handler.__init__(self)
        condensation.core.SignalSource.__init__(self)
        self._callbacks = self._global_callbacks



    def emit(self, record):
        #print record.__dict__
        new_index = len(self._records)
        self._records.append(record)
        self._records_text.append(self.format(record))
        self.raise_signal('new-record', new_index)



    def get_text(self):
        return "\n".join(self._records_text)



    def get_record_list(self):
        return self._records



    def get_record_text(self, index):
        return self._records_text[index]



    def get_record(self, index):
        return self._records[index]

