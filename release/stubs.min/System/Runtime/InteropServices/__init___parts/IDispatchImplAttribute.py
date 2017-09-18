class IDispatchImplAttribute(Attribute,_Attribute):
 """
 Indicates which IDispatch implementation the common language runtime uses when exposing dual interfaces and dispinterfaces to COM.

 

 IDispatchImplAttribute(implType: IDispatchImplType)

 IDispatchImplAttribute(implType: Int16)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,implType):
  """
  __new__(cls: type,implType: IDispatchImplType)

  __new__(cls: type,implType: Int16)
  """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Runtime.InteropServices.IDispatchImplType value used by the class.



Get: Value(self: IDispatchImplAttribute) -> IDispatchImplType



"""


