class InterfaceTypeAttribute(Attribute,_Attribute):
 """
 Indicates whether a managed interface is dual,dispatch-only,or IUnknown -only when exposed to COM.

 

 InterfaceTypeAttribute(interfaceType: ComInterfaceType)

 InterfaceTypeAttribute(interfaceType: Int16)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,interfaceType):
  """
  __new__(cls: type,interfaceType: ComInterfaceType)

  __new__(cls: type,interfaceType: Int16)
  """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Runtime.InteropServices.ComInterfaceType value that describes how the interface should be exposed to COM.



Get: Value(self: InterfaceTypeAttribute) -> ComInterfaceType



"""


