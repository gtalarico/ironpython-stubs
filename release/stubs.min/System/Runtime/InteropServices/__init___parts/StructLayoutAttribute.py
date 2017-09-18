class StructLayoutAttribute(Attribute,_Attribute):
 """
 Lets you control the physical layout of the data fields of a class or structure.

 

 StructLayoutAttribute(layoutKind: LayoutKind)

 StructLayoutAttribute(layoutKind: Int16)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,layoutKind):
  """
  __new__(cls: type,layoutKind: LayoutKind)

  __new__(cls: type,layoutKind: Int16)
  """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Runtime.InteropServices.LayoutKind value that specifies how the class or structure is arranged.



Get: Value(self: StructLayoutAttribute) -> LayoutKind



"""


 CharSet=None
 Pack=None
 Size=None

