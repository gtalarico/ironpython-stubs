# encoding: utf-8
# module Wms.EdiMessaging.EventArgs calls itself EventArgs
# from Wms.RemotingObjects, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class StatusChangedEventArgs:
    """ StatusChangedEventArgs(previousState: MessageStatus, newStatus: MessageStatus) """
    @staticmethod # known case of __new__
    def __new__(self, previousState, newStatus):
        """ __new__(cls: type, previousState: MessageStatus, newStatus: MessageStatus) """
        pass

    NewStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewStatus(self: StatusChangedEventArgs) -> MessageStatus

"""

    PreviousStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreviousStatus(self: StatusChangedEventArgs) -> MessageStatus

"""



