# encoding: utf-8
# module RevitServices.EventHandler calls itself EventHandler
# from RevitServices, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class EventHandlerProxy(object):
    """ EventHandlerProxy() """
    def OnApplicationDocumentClosed(self, sender, args):
        """ OnApplicationDocumentClosed(self: EventHandlerProxy, sender: object, args: DocumentClosedEventArgs) """
        pass

    def OnApplicationDocumentClosing(self, sender, args):
        """ OnApplicationDocumentClosing(self: EventHandlerProxy, sender: object, args: DocumentClosingEventArgs) """
        pass

    def OnApplicationDocumentOpened(self, sender, args):
        """ OnApplicationDocumentOpened(self: EventHandlerProxy, sender: object, args: DocumentOpenedEventArgs) """
        pass

    def OnApplicationViewActivated(self, sender, args):
        """ OnApplicationViewActivated(self: EventHandlerProxy, sender: object, args: ViewActivatedEventArgs) """
        pass

    def OnApplicationViewActivating(self, sender, args):
        """ OnApplicationViewActivating(self: EventHandlerProxy, sender: object, args: ViewActivatingEventArgs) """
        pass

    DocumentClosed = None
    DocumentClosing = None
    DocumentOpened = None
    ViewActivated = None
    ViewActivating = None


