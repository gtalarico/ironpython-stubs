class HandledEventArgs(EventArgs):
 """
 Provides data for events that can be handled completely in an event handler.
 
 HandledEventArgs()
 HandledEventArgs(defaultHandledValue: bool)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HandledEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,defaultHandledValue=None):
  """
  __new__(cls: type)
  __new__(cls: type,defaultHandledValue: bool)
  """
  pass
 Handled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the event handler has completely handled the event or whether the system should continue its own processing.

Get: Handled(self: HandledEventArgs) -> bool

Set: Handled(self: HandledEventArgs)=value
"""


