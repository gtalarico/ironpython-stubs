class HandleRef(object):
 """
 Wraps a managed object holding a handle to a resource that is passed to unmanaged code using platform invoke.
 
 HandleRef(wrapper: object,handle: IntPtr)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HandleRef()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def ToIntPtr(value):
  """
  ToIntPtr(value: HandleRef) -> IntPtr
  
   Returns the internal integer representation of a System.Runtime.InteropServices.HandleRef object.
  
   value: A System.Runtime.InteropServices.HandleRef object to retrieve an internal integer representation from.
   Returns: An System.IntPtr object that represents a System.Runtime.InteropServices.HandleRef object.
  """
  pass
 @staticmethod
 def __new__(self,wrapper,handle):
  """
  __new__[HandleRef]() -> HandleRef
  
  __new__(cls: type,wrapper: object,handle: IntPtr)
  """
  pass
 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the handle to a resource.

Get: Handle(self: HandleRef) -> IntPtr

"""

 Wrapper=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object holding the handle to a resource.

Get: Wrapper(self: HandleRef) -> object

"""


