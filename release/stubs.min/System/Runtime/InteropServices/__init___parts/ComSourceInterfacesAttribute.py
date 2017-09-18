class ComSourceInterfacesAttribute(Attribute,_Attribute):
 """
 Identifies a list of interfaces that are exposed as COM event sources for the attributed class.

 

 ComSourceInterfacesAttribute(sourceInterfaces: str)

 ComSourceInterfacesAttribute(sourceInterface: Type)

 ComSourceInterfacesAttribute(sourceInterface1: Type,sourceInterface2: Type)

 ComSourceInterfacesAttribute(sourceInterface1: Type,sourceInterface2: Type,sourceInterface3: Type)

 ComSourceInterfacesAttribute(sourceInterface1: Type,sourceInterface2: Type,sourceInterface3: Type,sourceInterface4: Type)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,sourceInterfaces: str)

  __new__(cls: type,sourceInterface: Type)

  __new__(cls: type,sourceInterface1: Type,sourceInterface2: Type)

  __new__(cls: type,sourceInterface1: Type,sourceInterface2: Type,sourceInterface3: Type)

  __new__(cls: type,sourceInterface1: Type,sourceInterface2: Type,sourceInterface3: Type,sourceInterface4: Type)
  """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the fully qualified name of the event source interface.



Get: Value(self: ComSourceInterfacesAttribute) -> str



"""


