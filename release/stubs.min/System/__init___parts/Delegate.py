class Delegate(object,ICloneable,ISerializable):
 """ Represents a delegate,which is a data structure that refers to a static method or to a class instance and an instance method of that class. """
 def Call(self,*args):
  """ x.__call__(...) <==> x(...)x.__call__(...) <==> x(...) """
  pass
 def Clone(self):
  """
  Clone(self: Delegate) -> object

  

   Creates a shallow copy of the delegate.

   Returns: A shallow copy of the delegate.
  """
  pass
 @staticmethod
 def Combine(*__args):
  """
  Combine(*delegates: Array[Delegate]) -> Delegate

  

   Concatenates the invocation lists of an array of delegates.

  

   delegates: The array of delegates to combine.

   Returns: A new delegate with an invocation list that concatenates the invocation lists of the delegates 

    in the delegates array. Returns null if delegates is null,if delegates contains zero elements,

    or if every entry in delegates is null.

  

  Combine(a: Delegate,b: Delegate) -> Delegate

  

   Concatenates the invocation lists of two delegates.

  

   a: The delegate whose invocation list comes first.

   b: The delegate whose invocation list comes last.

   Returns: A new delegate with an invocation list that concatenates the invocation lists of a and b in that 

    order. Returns a if b is null,returns b if a is a null reference,and returns a null reference 

    if both a and b are null references.
  """
  pass
 def CombineImpl(self,*args):
  """
  CombineImpl(self: Delegate,d: Delegate) -> Delegate

  

   Concatenates the invocation lists of the specified multicast (combinable) delegate and the 

    current multicast (combinable) delegate.

  

  

   d: The multicast (combinable) delegate whose invocation list to append to the end of the invocation 

    list of the current multicast (combinable) delegate.

  

   Returns: A new multicast (combinable) delegate with an invocation list that concatenates the invocation 

    list of the current multicast (combinable) delegate and the invocation list of d,or the current 

    multicast (combinable) delegate if d is null.
  """
  pass
 @staticmethod
 def CreateDelegate(type,*__args):
  """
  CreateDelegate(type: Type,method: MethodInfo,throwOnBindFailure: bool) -> Delegate

  

   Creates a delegate of the specified type to represent the specified static method,with the 

    specified behavior on failure to bind.

  

  

   type: The System.Type of delegate to create.

   method: The System.Reflection.MethodInfo describing the static or instance method the delegate is to 

    represent.

  

   throwOnBindFailure: true to throw an exception if method cannot be bound; otherwise,false.

   Returns: A delegate of the specified type to represent the specified static method.

  CreateDelegate(type: Type,target: Type,method: str,ignoreCase: bool,throwOnBindFailure: bool) -> Delegate

  

   Creates a delegate of the specified type that represents the specified static method of the 

    specified class,with the specified case-sensitivity and the specified behavior on failure to 

    bind.

  

  

   type: The System.Type of delegate to create.

   target: The System.Type representing the class that implements method.

   method: The name of the static method that the delegate is to represent.

   ignoreCase: A Boolean indicating whether to ignore the case when comparing the name of the method.

   throwOnBindFailure: true to throw an exception if method cannot be bound; otherwise,false.

   Returns: A delegate of the specified type that represents the specified static method of the specified 

    class.

  

  CreateDelegate(type: Type,firstArgument: object,method: MethodInfo) -> Delegate

  

   Creates a delegate of the specified type that represents the specified static or instance 

    method,with the specified first argument.

  

  

   type: The System.Type of delegate to create.

   firstArgument: The object to which the delegate is bound,or null to treat method as static (Shared in Visual 

    Basic).

  

   method: The System.Reflection.MethodInfo describing the static or instance method the delegate is to 

    represent.

  

   Returns: A delegate of the specified type that represents the specified static or instance method.

  CreateDelegate(type: Type,method: MethodInfo) -> Delegate

  

   Creates a delegate of the specified type to represent the specified static method.

  

   type: The System.Type of delegate to create.

   method: The System.Reflection.MethodInfo describing the static or instance method the delegate is to 

    represent. Only static methods are supported in the .NET Framework version 1.0 and 1.1.

  

   Returns: A delegate of the specified type to represent the specified static method.

  CreateDelegate(type: Type,firstArgument: object,method: MethodInfo,throwOnBindFailure: bool) -> Delegate

  

   Creates a delegate of the specified type that represents the specified static or instance 

    method,with the specified first argument and the specified behavior on failure to bind.

  

  

   type: A System.Type representing the type of delegate to create.

   firstArgument: An System.Object that is the first argument of the method the delegate represents. For instance 

    methods,it must be compatible with the instance type.

  

   method: The System.Reflection.MethodInfo describing the static or instance method the delegate is to 

    represent.

  

   throwOnBindFailure: true to throw an exception if method cannot be bound; otherwise,false.

   Returns: A delegate of the specified type that represents the specified static or instance method,or 

    null if throwOnBindFailure is false and the delegate cannot be bound to method.

  

  CreateDelegate(type: Type,target: object,method: str,ignoreCase: bool) -> Delegate

  

   Creates a delegate of the specified type that represents the specified instance method to invoke 

    on the specified class instance with the specified case-sensitivity.

  

  

   type: The System.Type of delegate to create.

   target: The class instance on which method is invoked.

   method: The name of the instance method that the delegate is to represent.

   ignoreCase: A Boolean indicating whether to ignore the case when comparing the name of the method.

   Returns: A delegate of the specified type that represents the specified instance method to invoke on the 

    specified class instance.

  

  CreateDelegate(type: Type,target: object,method: str) -> Delegate

  

   Creates a delegate of the specified type that represents the specified instance method to invoke 

    on the specified class instance.

  

  

   type: The System.Type of delegate to create.

   target: The class instance on which method is invoked.

   method: The name of the instance method that the delegate is to represent.

   Returns: A delegate of the specified type that represents the specified instance method to invoke on the 

    specified class instance.

  

  CreateDelegate(type: Type,target: object,method: str,ignoreCase: bool,throwOnBindFailure: bool) -> Delegate

  

   Creates a delegate of the specified type that represents the specified instance method to invoke 

    on the specified class instance,with the specified case-sensitivity and the specified behavior 

    on failure to bind.

  

  

   type: The System.Type of delegate to create.

   target: The class instance on which method is invoked.

   method: The name of the instance method that the delegate is to represent.

   ignoreCase: A Boolean indicating whether to ignore the case when comparing the name of the method.

   throwOnBindFailure: true to throw an exception if method cannot be bound; otherwise,false.

   Returns: A delegate of the specified type that represents the specified instance method to invoke on the 

    specified class instance.

  

  CreateDelegate(type: Type,target: Type,method: str,ignoreCase: bool) -> Delegate

  

   Creates a delegate of the specified type that represents the specified static method of the 

    specified class,with the specified case-sensitivity.

  

  

   type: The System.Type of delegate to create.

   target: The System.Type representing the class that implements method.

   method: The name of the static method that the delegate is to represent.

   ignoreCase: A Boolean indicating whether to ignore the case when comparing the name of the method.

   Returns: A delegate of the specified type that represents the specified static method of the specified 

    class.

  

  CreateDelegate(type: Type,target: Type,method: str) -> Delegate

  

   Creates a delegate of the specified type that represents the specified static method of the 

    specified class.

  

  

   type: The System.Type of delegate to create.

   target: The System.Type representing the class that implements method.

   method: The name of the static method that the delegate is to represent.

   Returns: A delegate of the specified type that represents the specified static method of the specified 

    class.
  """
  pass
 def DynamicInvoke(self,args):
  """
  DynamicInvoke(self: Delegate,*args: Array[object]) -> object

  

   Dynamically invokes (late-bound) the method represented by the current delegate.

  

   args: An array of objects that are the arguments to pass to the method represented by the current 

    delegate.-or- null,if the method represented by the current delegate does not require 

    arguments.

  

   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def DynamicInvokeImpl(self,*args):
  """
  DynamicInvokeImpl(self: Delegate,args: Array[object]) -> object

  

   Dynamically invokes (late-bound) the method represented by the current delegate.

  

   args: An array of objects that are the arguments to pass to the method represented by the current 

    delegate.-or- null,if the method represented by the current delegate does not require 

    arguments.

  

   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Delegate,obj: object) -> bool

  

   Determines whether the specified object and the current delegate are of the same type and share 

    the same targets,methods,and invocation list.

  

  

   obj: The object to compare with the current delegate.

   Returns: true if obj and the current delegate have the same targets,methods,and invocation list; 

    otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Delegate) -> int

  

   Returns a hash code for the delegate.

   Returns: A hash code for the delegate.
  """
  pass
 def GetInvocationList(self):
  """
  GetInvocationList(self: Delegate) -> Array[Delegate]

  

   Returns the invocation list of the delegate.

   Returns: An array of delegates representing the invocation list of the current delegate.
  """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: Delegate) -> MethodInfo

  

   Gets the static method represented by the current delegate.

   Returns: A System.Reflection.MethodInfo describing the static method represented by the current delegate.
  """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: Delegate,info: SerializationInfo,context: StreamingContext)

   Not supported.

  

   info: Not supported.

   context: Not supported.
  """
  pass
 def InPlaceAdd(self,*args):
  """ InPlaceAdd(self: Delegate,other: Delegate) -> Delegate """
  pass
 def InPlaceSubtract(self,*args):
  """ InPlaceSubtract(self: Delegate,other: Delegate) -> Delegate """
  pass
 @staticmethod
 def Remove(source,value):
  """
  Remove(source: Delegate,value: Delegate) -> Delegate

  

   Removes the last occurrence of the invocation list of a delegate from the invocation list of 

    another delegate.

  

  

   source: The delegate from which to remove the invocation list of value.

   value: The delegate that supplies the invocation list to remove from the invocation list of source.

   Returns: A new delegate with an invocation list formed by taking the invocation list of source and 

    removing the last occurrence of the invocation list of value,if the invocation list of value is 

    found within the invocation list of source. Returns source if value is null or if the invocation 

    list of value is not found within the invocation list of source. Returns a null reference if the 

    invocation list of value is equal to the invocation list of source or if source is a null 

    reference.
  """
  pass
 @staticmethod
 def RemoveAll(source,value):
  """
  RemoveAll(source: Delegate,value: Delegate) -> Delegate

  

   Removes all occurrences of the invocation list of a delegate from the invocation list of another 

    delegate.

  

  

   source: The delegate from which to remove the invocation list of value.

   value: The delegate that supplies the invocation list to remove from the invocation list of source.

   Returns: A new delegate with an invocation list formed by taking the invocation list of source and 

    removing all occurrences of the invocation list of value,if the invocation list of value is 

    found within the invocation list of source. Returns source if value is null or if the invocation 

    list of value is not found within the invocation list of source. Returns a null reference if the 

    invocation list of value is equal to the invocation list of source,if source contains only a 

    series of invocation lists that are equal to the invocation list of value,or if source is a 

    null reference.
  """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: Delegate,d: Delegate) -> Delegate

  

   Removes the invocation list of a delegate from the invocation list of another delegate.

  

   d: The delegate that supplies the invocation list to remove from the invocation list of the current 

    delegate.

  

   Returns: A new delegate with an invocation list formed by taking the invocation list of the current 

    delegate and removing the invocation list of value,if the invocation list of value is found 

    within the current delegate's invocation list. Returns the current delegate if value is null or 

    if the invocation list of value is not found within the current delegate's invocation list. 

    Returns null if the invocation list of value is equal to the current delegate's invocation list.
  """
  pass
 def __call__(self,*args):
  """ x.__call__(...) <==> x(...)x.__call__(...) <==> x(...) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __iadd__(self,*args):
  """ __iadd__(self: Delegate,other: Delegate) -> Delegate """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __isub__(self,*args):
  """ __isub__(self: Delegate,other: Delegate) -> Delegate """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(type: type,function: object) -> object """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Method=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the method represented by the delegate.



Get: Method(self: Delegate) -> MethodInfo



"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the class instance on which the current delegate invokes the instance method.



Get: Target(self: Delegate) -> object



"""


