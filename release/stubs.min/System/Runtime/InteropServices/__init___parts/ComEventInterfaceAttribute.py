class ComEventInterfaceAttribute(Attribute,_Attribute):
 """
 Identifies the source interface and the class that implements the methods of the event interface that is generated when a coclass is imported from a COM type library.

 

 ComEventInterfaceAttribute(SourceInterface: Type,EventProvider: Type)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,SourceInterface,EventProvider):
  """ __new__(cls: type,SourceInterface: Type,EventProvider: Type) """
  pass
 EventProvider=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the class that implements the methods of the event interface.



Get: EventProvider(self: ComEventInterfaceAttribute) -> Type



"""

 SourceInterface=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the original source interface from the type library.



Get: SourceInterface(self: ComEventInterfaceAttribute) -> Type



"""


