class ArgIterator(object):
 """
 Represents a variable-length argument list; that is,the parameters of a function that takes a variable number of arguments.

 

 ArgIterator(arglist: RuntimeArgumentHandle)

 ArgIterator(arglist: RuntimeArgumentHandle,ptr: Void*)
 """
 def End(self):
  """
  End(self: ArgIterator)

   Concludes processing of the variable-length argument list represented by this instance.
  """
  pass
 def Equals(self,o):
  """
  Equals(self: ArgIterator,o: object) -> bool

  

   This method is not supported,and always throws System.NotSupportedException.

  

   o: An object to be compared to this instance.

   Returns: This comparison is not supported. No value is returned.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ArgIterator) -> int

  

   Returns the hash code of this object.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def GetNextArg(self,rth=None):
  """
  GetNextArg(self: ArgIterator,rth: RuntimeTypeHandle) -> TypedReference

  

   Returns the next argument in a variable-length argument list that has a specified type.

  

   rth: A runtime type handle that identifies the type of the argument to retrieve.

   Returns: The next argument as a System.TypedReference object.

  GetNextArg(self: ArgIterator) -> TypedReference

  

   Returns the next argument in a variable-length argument list.

   Returns: The next argument as a System.TypedReference object.
  """
  pass
 def GetNextArgType(self):
  """
  GetNextArgType(self: ArgIterator) -> RuntimeTypeHandle

  

   Returns the type of the next argument.

   Returns: The type of the next argument.
  """
  pass
 def GetRemainingCount(self):
  """
  GetRemainingCount(self: ArgIterator) -> int

  

   Returns the number of arguments remaining in the argument list.

   Returns: The number of remaining arguments.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,arglist,ptr=None):
  """
  __new__(cls: type,arglist: RuntimeArgumentHandle)

  __new__(cls: type,arglist: RuntimeArgumentHandle,ptr: Void*)
  """
  pass
 def __ne__(self,*args):
  pass
