class TypeLibTypeAttribute(Attribute,_Attribute):
 """
 Contains the System.Runtime.InteropServices.TYPEFLAGS that were originally imported for this type from the COM type library.

 

 TypeLibTypeAttribute(flags: TypeLibTypeFlags)

 TypeLibTypeAttribute(flags: Int16)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,flags):
  """
  __new__(cls: type,flags: TypeLibTypeFlags)

  __new__(cls: type,flags: Int16)
  """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Runtime.InteropServices.TypeLibTypeFlags value for this type.



Get: Value(self: TypeLibTypeAttribute) -> TypeLibTypeFlags



"""


