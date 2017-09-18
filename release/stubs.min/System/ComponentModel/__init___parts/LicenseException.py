class LicenseException(SystemException,ISerializable,_Exception):
 """
 Represents the exception thrown when a component cannot be granted a license.

 

 LicenseException(type: Type)

 LicenseException(type: Type,instance: object)

 LicenseException(type: Type,instance: object,message: str)

 LicenseException(type: Type,instance: object,message: str,innerException: Exception)
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: LicenseException,info: SerializationInfo,context: StreamingContext)

   Sets the System.Runtime.Serialization.SerializationInfo with information about the exception.

  

   info: The System.Runtime.Serialization.SerializationInfo to be used for deserialization.

   context: The destination to be used for deserialization.
  """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,type,instance=None,message=None,innerException=None):
  """
  __new__(cls: type,type: Type)

  __new__(cls: type,type: Type,instance: object)

  __new__(cls: type,type: Type,instance: object,message: str)

  __new__(cls: type,type: Type,instance: object,message: str,innerException: Exception)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 LicensedType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the component that was not granted a license.



Get: LicensedType(self: LicenseException) -> Type



"""


