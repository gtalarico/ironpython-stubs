class MulticastDelegate(Delegate,ICloneable,ISerializable):
 """ Represents a multicast delegate; that is,a delegate that can have more than one element in its invocation list. """
 def CombineImpl(self,*args):
  """
  CombineImpl(self: MulticastDelegate,follow: Delegate) -> Delegate

  

   Combines this System.Delegate with the specified System.Delegate to form a new delegate.

  

   follow: The delegate to combine with this delegate.

   Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
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
  Equals(self: MulticastDelegate,obj: object) -> bool

  

   Determines whether this multicast delegate and the specified object are equal.

  

   obj: The object to compare with this instance.

   Returns: true if obj and this instance have the same invocation lists; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: MulticastDelegate) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def GetInvocationList(self):
  """
  GetInvocationList(self: MulticastDelegate) -> Array[Delegate]

  

   Returns the invocation list of this multicast delegate,in invocation order.

   Returns: An array of delegates whose invocation lists collectively match the invocation list of this 

    instance.
  """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo

  

   Returns a static method represented by the current System.MulticastDelegate.

   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: MulticastDelegate,info: SerializationInfo,context: StreamingContext)

   Populates a System.Runtime.Serialization.SerializationInfo object with all the data needed to 

    serialize this instance.

  

  

   info: An object that holds all the data needed to serialize or deserialize this instance.

   context: (Reserved) The location where serialized data is stored and retrieved.
  """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: MulticastDelegate,value: Delegate) -> Delegate

  

   Removes an element from the invocation list of this System.MulticastDelegate that is equal to 

    the specified delegate.

  

  

   value: The delegate to search for in the invocation list.

   Returns: If value is found in the invocation list for this instance,then a new System.Delegate without 

    value in its invocation list; otherwise,this instance with its original invocation list.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type,target: object,method: str)

  __new__(cls: type,target: Type,method: str)
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
