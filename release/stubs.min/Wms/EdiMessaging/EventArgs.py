# encoding: utf-8
# module Wms.EdiMessaging.EventArgs calls itself EventArgs
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class StatusChangedEventArgs(EventArgs):
 """ StatusChangedEventArgs(previousState: MessageStatus,newStatus: MessageStatus) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StatusChangedEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,previousState,newStatus):
  """ __new__(cls: type,previousState: MessageStatus,newStatus: MessageStatus) """
  pass
 NewStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NewStatus(self: StatusChangedEventArgs) -> MessageStatus

"""

 PreviousStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreviousStatus(self: StatusChangedEventArgs) -> MessageStatus

"""



