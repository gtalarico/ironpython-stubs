from System import EventArgs
# encoding: utf-8
# module Wms.EdiMessaging.EventArgs calls itself EventArgs
# from Wms.RemotingObjects, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class StatusChangedEventArgs(EventArgs):
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


    Instance = StatusChangedEventArgs()
    """hardcoded/returns an instance of the class"""

