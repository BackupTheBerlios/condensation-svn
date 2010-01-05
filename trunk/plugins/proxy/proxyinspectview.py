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

import gtk

from proxyrecordlistwidget import ProxyRecordListWidget
from proxyrecordwidget import ProxyRecordWidget


class ProxyInspectView(gtk.VBox):

    def __init__(self, view_object):
        self.view_object = view_object
        gtk.VBox.__init__(self)

        self.listwidget = ProxyRecordListWidget(self.view_object)
        self.pack_start(self.listwidget, True, True)
        self.listwidget.connect('selected-changed', self._selected_changed)

        self.recordwidget = ProxyRecordWidget()
        frame = gtk.Frame()
        frame.add(self.recordwidget)
        frame.set_shadow_type(gtk.SHADOW_NONE)
        frame.set_border_width(5)
        expander = gtk.Expander(_('Details'))
        expander.add(frame)
        self.pack_end(expander, False, True)
        expander.show_all()



    def get_icon(self):
        return 'condensation-inspect'



    def get_name(self):
        return _("Inspect")



    def _selected_changed(self, listwidget):
        record = self.listwidget.get_selected()
        if record:
            self.recordwidget.set_record(record)
        else:
            print "empty record!!" # TODO: shouldn't hapen, handle accordingly


