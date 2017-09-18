class Exception(object,ISerializable,_Exception):
 """
 Represents errors that occur during application execution.

 

 Exception()

 Exception(message: str)

 Exception(message: str,innerException: Exception)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetBaseException(self):
  """
  GetBaseException(self: Exception) -> Exception

  

   When overridden in a derived class,returns the System.Exception that is the root cause of one 

    or more subsequent exceptions.

  

   Returns: The first exception thrown in a chain of exceptions. If the System.Exception.InnerException 

    property of the current exception is a null reference (Nothing in Visual Basic),this property 

    returns the current exception.
  """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: Exception,info: SerializationInfo,context: StreamingContext)

   When overridden in a derived class,sets the System.Runtime.Serialization.SerializationInfo with 

    information about the exception.

  

  

   info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about 

    the exception being thrown.

  

   context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the 

    source or destination.
  """
  pass
 def GetType(self):
  """
  GetType(self: Exception) -> Type

  

   Gets the runtime type of the current instance.

   Returns: A System.Type object that represents the exact runtime type of the current instance.
  """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def ToString(self):
  """
  ToString(self: Exception) -> str

  

   Creates and returns a string representation of the current exception.

   Returns: A string representation of the current exception.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,innerException=None):
  """
  __new__(cls: type)

  __new__(cls: type,message: str)

  __new__(cls: type,message: str,innerException: Exception)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Data=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of key/value pairs that provide additional user-defined information about the exception.



Get: Data(self: Exception) -> IDictionary



"""

 HelpLink=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a link to the help file associated with this exception.



Get: HelpLink(self: Exception) -> str



Set: HelpLink(self: Exception)=value

"""

 HResult=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets HRESULT,a coded numerical value that is assigned to a specific exception.



Get: HResult(self: Exception) -> int



"""

 InnerException=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Exception instance that caused the current exception.



Get: InnerException(self: Exception) -> Exception



"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a message that describes the current exception.



Get: Message(self: Exception) -> str



"""

 Source=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the application or the object that causes the error.



Get: Source(self: Exception) -> str



Set: Source(self: Exception)=value

"""

 StackTrace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a string representation of the immediate frames on the call stack.



Get: StackTrace(self: Exception) -> str



"""

 TargetSite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the method that throws the current exception.



Get: TargetSite(self: Exception) -> MethodBase



"""


