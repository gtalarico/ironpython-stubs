class InitializationEventAttribute(Attribute,_Attribute):
 """
 Specifies which event is raised on initialization. This class cannot be inherited.

 

 InitializationEventAttribute(eventName: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,eventName):
  """ __new__(cls: type,eventName: str) """
  pass
 EventName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the initialization event.



Get: EventName(self: InitializationEventAttribute) -> str



"""


