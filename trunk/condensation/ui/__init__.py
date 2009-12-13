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

__all__ = []


from baseformwidget import BaseFormWidget
from booleanformwidget import BooleanFormWidget
from coloredframe import ColoredFrame
from condensationviewmanager import CondensationViewManager
from conobjectview import CONObjectView
from formwidgetfactory import FormWidgetFactory
from integerlistformwidget import IntegerListFormWidget
from integerlistwidget import IntegerListWidget
from mainwindow import MainWindow
from navigationhistory import NavigationHistory
from resources import Resources
from serverconfigview import ServerConfigView
from serverviewmanager import ServerViewManager
from splashscreen import SplashScreen
from stringformwidget import StringFormWidget
from stringlistformwidget import StringListFormWidget
from stringlistwidget import StringListWidget
from textentrydialog import TextEntryDialog
from treemenu import TreeMenu
from vhostconfigview import VHostConfigView
from vhostviewmanager import VHostViewManager
from viewmanager import ViewManager

# load icons
Resources.load_pixbuf('vhost-enabled', 'images/icons/vhost-enabled.svg')
Resources.load_pixbuf('vhost-disabled', 'images/icons/vhost-disabled.svg')
Resources.load_pixbuf('server-connected', 'images/icons/server-connected.svg')
Resources.load_pixbuf('server-disconnected', 'images/icons/server-disconnected.svg')
Resources.load_pixbuf('configuration-icon', 'images/icons/configuration.svg')

# register viewmanagers
ViewManager.register_viewmanager('Main', CondensationViewManager)
ViewManager.register_viewmanager("Server", ServerViewManager)
ViewManager.register_viewmanager("VHost", VHostViewManager)

# register views
ViewManager.register_view('Server', ServerConfigView)
ViewManager.register_view('VHost', VHostConfigView)

# register form-widgets
FormWidgetFactory.register_widget(BooleanFormWidget)
FormWidgetFactory.register_widget(IntegerListFormWidget)
FormWidgetFactory.register_widget(StringFormWidget)
FormWidgetFactory.register_widget(StringListFormWidget)

