class _Exception:
 """ Exposes the public members of the System.Exception class to unmanaged code. """
 def Equals(self,obj):
  """
  Equals(self: _Exception,obj: object) -> bool

  

   Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 

    method.

  

  

   obj: The System.Object to compare with the current System.Object.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def GetBaseException(self):
  """
  GetBaseException(self: _Exception) -> Exception

  

   Provides COM objects with version-independent access to the System.Exception.GetBaseException 

    method.

  

   Returns: The first exception thrown in a chain of exceptions. If the System.Exception.InnerException 

    property of the current exception is a null reference (Nothing in Visual Basic),this property 

    returns the current exception.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: _Exception) -> int

  

   Provides COM objects with version-independent access to the System.Object.GetHashCode method.

   Returns: The hash code for the current instance.
  """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: _Exception,info: SerializationInfo,context: StreamingContext)

   Provides COM objects with version-independent access to the 

    System.Exception.GetObjectData(System.Runtime.Serialization.SerializationInfo,System.Runtime.Seri

    alization.StreamingContext) method

  

  

   info: The System.Runtime.Serialization.SerializationInfo object that holds the serialized object data 

    about the exception being thrown.

  

   context: The System.Runtime.Serialization.StreamingContext structure that contains contextual information 

    about the source or destination.
  """
  pass
 def GetType(self):
  """
  GetType(self: _Exception) -> Type

  

   Provides COM objects with version-independent access to the System.Exception.GetType method.

   Returns: A System.Type object that represents the exact runtime type of the current instance.
  """
  pass
 def ToString(self):
  """
  ToString(self: _Exception) -> str

  

   Provides COM objects with version-independent access to the System.Exception.ToString method.

   Returns: A string that represents the current System.Exception object.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 HelpLink=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Exception.HelpLink property.



Get: HelpLink(self: _Exception) -> str



Set: HelpLink(self: _Exception)=value

"""

 InnerException=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Exception.InnerException property.



Get: InnerException(self: _Exception) -> Exception



"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Exception.Message property.



Get: Message(self: _Exception) -> str



"""

 Source=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Exception.Source property.



Get: Source(self: _Exception) -> str



Set: Source(self: _Exception)=value

"""

 StackTrace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Exception.StackTrace property.



Get: StackTrace(self: _Exception) -> str



"""

 TargetSite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Exception.TargetSite property.



Get: TargetSite(self: _Exception) -> MethodBase



"""


