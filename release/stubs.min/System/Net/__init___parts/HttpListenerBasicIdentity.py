class HttpListenerBasicIdentity(GenericIdentity):
 """
 Holds the user name and password from a basic authentication request.
 
 HttpListenerBasicIdentity(username: str,password: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HttpListenerBasicIdentity()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def CreateClaim(self,*args):
  """ CreateClaim(self: ClaimsIdentity,reader: BinaryReader) -> Claim """
  pass
 def GetObjectData(self,*args):
  """ GetObjectData(self: ClaimsIdentity,info: SerializationInfo,context: StreamingContext) """
  pass
 def WriteTo(self,writer):
  """ WriteTo(self: ClaimsIdentity,writer: BinaryWriter,userData: Array[Byte]) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,username,password):
  """ __new__(cls: type,username: str,password: str) """
  pass
 CustomSerializationData=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Password=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates the password from a basic authentication attempt.

Get: Password(self: HttpListenerBasicIdentity) -> str

"""


