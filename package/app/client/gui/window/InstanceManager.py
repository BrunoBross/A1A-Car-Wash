from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk


class InstanceManager(metaclass=Singleton):
    def __init__(self):
        self.__instances = set()

    def __postUpdate(self):
        if not len(self.__instances):
            Gtk.main_quit()

    def addInstance(self, instance):
        self.__instances.add(instance)
        self.__postUpdate()

    def terminateInstance(self, instance):
        self.__instances.remove(instance)
        self.__postUpdate()
