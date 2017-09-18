class DBNull(object,ISerializable,IConvertible):
 """ Represents a nonexistent value. This class cannot be inherited. """
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: DBNull,info: SerializationInfo,context: StreamingContext)

   Implements the System.Runtime.Serialization.ISerializable interface and returns the data needed 

    to serialize the System.DBNull object.

  

  

   info: A System.Runtime.Serialization.SerializationInfo object containing information required to 

    serialize the System.DBNull object.

  

   context: A System.Runtime.Serialization.StreamingContext object containing the source and destination of 

    the serialized stream associated with the System.DBNull object.
  """
  pass
 def GetTypeCode(self):
  """
  GetTypeCode(self: DBNull) -> TypeCode

  

   Gets the System.TypeCode value for System.DBNull.

   Returns: The System.TypeCode value for System.DBNull,which is System.TypeCode.DBNull.
  """
  pass
 def ToString(self,provider=None):
  """
  ToString(self: DBNull,provider: IFormatProvider) -> str

  

   Returns an empty string using the specified System.IFormatProvider.

  

   provider: The System.IFormatProvider to be used to format the return value.-or- null to obtain the format 

    information from the current locale setting of the operating system.

  

   Returns: An empty string (System.String.Empty).

  ToString(self: DBNull) -> str

  

   Returns an empty string (System.String.Empty).

   Returns: An empty string (System.String.Empty).
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __nonzero__(self,*args):
  """ __nonzero__(value: DBNull) -> bool """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Value=None

