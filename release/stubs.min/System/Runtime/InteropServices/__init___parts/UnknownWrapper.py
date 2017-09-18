class UnknownWrapper(object):
 """
 Wraps objects the marshaler should marshal as a VT_UNKNOWN.

 

 UnknownWrapper(obj: object)
 """
 @staticmethod
 def __new__(self,obj):
  """ __new__(cls: type,obj: object) """
  pass
 WrappedObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object contained by this wrapper.



Get: WrappedObject(self: UnknownWrapper) -> object



"""


