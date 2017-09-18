class Lazy(object):
 """
 Lazy[T]()

 Lazy[T](valueFactory: Func[T])

 Lazy[T](isThreadSafe: bool)

 Lazy[T](mode: LazyThreadSafetyMode)

 Lazy[T](valueFactory: Func[T],isThreadSafe: bool)

 Lazy[T](valueFactory: Func[T],mode: LazyThreadSafetyMode)
 """
 def ToString(self):
  """
  ToString(self: Lazy[T]) -> str

  

   Creates and returns a string representation of the System.Lazy property for this instance.

   Returns: The result of calling the System.Object.ToString method on the System.Lazy property for this 

    instance,if the value has been created (that is,if the System.Lazy property returns true). 

    Otherwise,a string indicating that the value has not been created.
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,valueFactory: Func[T])

  __new__(cls: type,isThreadSafe: bool)

  __new__(cls: type,mode: LazyThreadSafetyMode)

  __new__(cls: type,valueFactory: Func[T],isThreadSafe: bool)

  __new__(cls: type,valueFactory: Func[T],mode: LazyThreadSafetyMode)
  """
  pass
 IsValueCreated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether a value has been created for this System.Lazy instance.



Get: IsValueCreated(self: Lazy[T]) -> bool



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the lazily initialized value of the current System.Lazy instance.



Get: Value(self: Lazy[T]) -> T



"""


