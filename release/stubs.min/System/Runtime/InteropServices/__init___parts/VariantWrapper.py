class VariantWrapper(object):
 """
 Marshals data of type VT_VARIANT | VT_BYREF from managed to unmanaged code. This class cannot be inherited.
 
 VariantWrapper(obj: object)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return VariantWrapper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,obj):
  """ __new__(cls: type,obj: object) """
  pass
 WrappedObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object wrapped by the System.Runtime.InteropServices.VariantWrapper object.

Get: WrappedObject(self: VariantWrapper) -> object

"""


