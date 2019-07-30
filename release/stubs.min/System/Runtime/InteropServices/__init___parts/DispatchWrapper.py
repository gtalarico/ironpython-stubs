class DispatchWrapper(object):
 """
 Wraps objects the marshaler should marshal as a VT_DISPATCH.
 
 DispatchWrapper(obj: object)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DispatchWrapper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,obj):
  """ __new__(cls: type,obj: object) """
  pass
 WrappedObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object wrapped by the System.Runtime.InteropServices.DispatchWrapper.

Get: WrappedObject(self: DispatchWrapper) -> object

"""


