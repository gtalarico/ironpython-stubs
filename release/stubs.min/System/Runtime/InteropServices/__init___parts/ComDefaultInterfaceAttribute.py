class ComDefaultInterfaceAttribute(Attribute,_Attribute):
 """
 Specifies a default interface to expose to COM. This class cannot be inherited.

 

 ComDefaultInterfaceAttribute(defaultInterface: Type)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,defaultInterface):
  """ __new__(cls: type,defaultInterface: Type) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Type object that specifies the default interface to expose to COM.



Get: Value(self: ComDefaultInterfaceAttribute) -> Type



"""


