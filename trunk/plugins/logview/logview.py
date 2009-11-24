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
import logging
import pango

import condensation

class LogView(gtk.VBox):

    def __init__(self, main):
        gtk.VBox.__init__(self)

        scrolled_window =  gtk.ScrolledWindow()
        self.add(scrolled_window)
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        col_defs = [
            ('Time', self.record_time),
            ('Level', self.record_level),
            ('Name', self.record_name),
            ('Message', self.record_message),
        ]
        self.liststore = gtk.ListStore(object)
        self.treeview = gtk.TreeView(self.liststore)
        self.treeview.set_reorderable(False)

        for col_def in col_defs:
            cell = gtk.CellRendererText()
            col = gtk.TreeViewColumn(col_def[0], cell)
            col.set_cell_data_func(cell, col_def[1])
            self.treeview.append_column(col)

        for record in main._logsink.get_record_list():
            self.liststore.append([record])

        main._logsink.connect_signal('new-record', self.new_record)

        scrolled_window.add(self.treeview)
        scrolled_window.show_all()



    def get_icon(self):
        return condensation.ui.Resources.get_pixbuf('log-view-icon')



    def get_name(self):
        return "Log View"



    def record_time(self, column, cell, model, iter):
        record = model.get_value(iter, 0)
        cell.set_property('text', record.asctime)


    def record_level(self, column, cell, model, iter):
        record = model.get_value(iter, 0)
        cell.set_property('text', record.levelname)


    def record_name(self, column, cell, model, iter):
        record = model.get_value(iter, 0)
        cell.set_property('text', record.name)


    def record_message(self, column, cell, model, iter):
        record = model.get_value(iter, 0)
        cell.set_property('text', record.message)


    def new_record(self, logsink, new_index):
        self.liststore.append([logsink.get_record(new_index)])

