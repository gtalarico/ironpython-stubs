class VariantWrapper(object):
 """
 Marshals data of type VT_VARIANT | VT_BYREF from managed to unmanaged code. This class cannot be inherited.

 

 VariantWrapper(obj: object)
 """
 @staticmethod
 def __new__(self,obj):
  """ __new__(cls: type,obj: object) """
  pass
 WrappedObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object wrapped by the System.Runtime.InteropServices.VariantWrapper object.



Get: WrappedObject(self: VariantWrapper) -> object



"""


