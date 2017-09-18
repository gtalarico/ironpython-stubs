class PrivilegeNotHeldException(UnauthorizedAccessException,ISerializable,_Exception):
 """
 The exception that is thrown when a method in the System.Security.AccessControl namespace attempts to enable a privilege that it does not have.

 

 PrivilegeNotHeldException()

 PrivilegeNotHeldException(privilege: str)

 PrivilegeNotHeldException(privilege: str,inner: Exception)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: PrivilegeNotHeldException,info: SerializationInfo,context: StreamingContext)

   Sets the info parameter with information about the exception.

  

   info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about 

    the exception being thrown.

  

   context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the 

    source or destination.
  """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,privilege=None,inner=None):
  """
  __new__(cls: type)

  __new__(cls: type,privilege: str)

  __new__(cls: type,privilege: str,inner: Exception)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 PrivilegeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the privilege that is not enabled.



Get: PrivilegeName(self: PrivilegeNotHeldException) -> str



"""


