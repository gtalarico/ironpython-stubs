class TypeLibFuncAttribute(Attribute,_Attribute):
 """
 Contains the System.Runtime.InteropServices.FUNCFLAGS that were originally imported for this method from the COM type library.

 

 TypeLibFuncAttribute(flags: TypeLibFuncFlags)

 TypeLibFuncAttribute(flags: Int16)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,flags):
  """
  __new__(cls: type,flags: TypeLibFuncFlags)

  __new__(cls: type,flags: Int16)
  """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Runtime.InteropServices.TypeLibFuncFlags value for this method.



Get: Value(self: TypeLibFuncAttribute) -> TypeLibFuncFlags



"""


