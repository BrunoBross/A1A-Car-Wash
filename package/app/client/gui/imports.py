import gi

from package.Config import Config

gi.require_version("Gtk", Config.GTK_VERSION)
from gi.repository import Gtk
