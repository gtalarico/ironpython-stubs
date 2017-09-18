class AggregateException(Exception,ISerializable,_Exception):
 """
 Represents one or more errors that occur during application execution.

 

 AggregateException()

 AggregateException(message: str)

 AggregateException(message: str,innerException: Exception)

 AggregateException(innerExceptions: IEnumerable[Exception])

 AggregateException(*innerExceptions: Array[Exception])

 AggregateException(message: str,innerExceptions: IEnumerable[Exception])

 AggregateException(message: str,*innerExceptions: Array[Exception])
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def Flatten(self):
  """
  Flatten(self: AggregateException) -> AggregateException

  

   Flattens an System.AggregateException instances into a single,new instance.

   Returns: A new,flattened System.AggregateException.
  """
  pass
 def GetBaseException(self):
  """
  GetBaseException(self: AggregateException) -> Exception

  

   Returns the System.AggregateException that is the root cause of this exception.

   Returns: Returns the System.AggregateException that is the root cause of this exception.
  """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: AggregateException,info: SerializationInfo,context: StreamingContext)

   Initializes a new instance of the System.AggregateException class with serialized data.

  

   info: The object that holds the serialized object data.

   context: The contextual information about the source or destination.
  """
  pass
 def Handle(self,predicate):
  """ Handle(self: AggregateException,predicate: Func[Exception,bool]) """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def ToString(self):
  """
  ToString(self: AggregateException) -> str

  

   Creates and returns a string representation of the current System.AggregateException.

   Returns: A string representation of the current exception.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,message: str)

  __new__(cls: type,message: str,innerException: Exception)

  __new__(cls: type,innerExceptions: IEnumerable[Exception])

  __new__(cls: type,*innerExceptions: Array[Exception])

  __new__(cls: type,message: str,innerExceptions: IEnumerable[Exception])

  __new__(cls: type,message: str,*innerExceptions: Array[Exception])

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 InnerExceptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a read-only collection of the System.Exception instances that caused the current exception.



Get: InnerExceptions(self: AggregateException) -> ReadOnlyCollection[Exception]



"""


