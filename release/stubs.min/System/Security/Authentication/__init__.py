# encoding: utf-8
# module System.Security.Authentication calls itself Authentication
# from System,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AuthenticationException:
 """
 The exception that is thrown when authentication fails for an authentication stream.
 
 AuthenticationException()
 AuthenticationException(message: str)
 AuthenticationException(message: str,innerException: Exception)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,innerException=None):
  """
  __new__(cls: type)
  __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerException: Exception)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class CipherAlgorithmType:
 """
 Defines the possible cipher algorithms for the System.Net.Security.SslStream class.
 
 enum CipherAlgorithmType,values: Aes (26129),Aes128 (26126),Aes192 (26127),Aes256 (26128),Des (26113),None (0),Null (24576),Rc2 (26114),Rc4 (26625),TripleDes (26115)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Aes=None
 Aes128=None
 Aes192=None
 Aes256=None
 Des=None
 None_ =None
 Null=None
 Rc2=None
 Rc4=None
 TripleDes=None
 value__=None


class ExchangeAlgorithmType:
 """
 Specifies the algorithm used to create keys shared by the client and server.
 
 enum ExchangeAlgorithmType,values: DiffieHellman (43522),None (0),RsaKeyX (41984),RsaSign (9216)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 DiffieHellman=None
 None_ =None
 RsaKeyX=None
 RsaSign=None
 value__=None


class HashAlgorithmType:
 """
 Specifies the algorithm used for generating message authentication codes (MACs).
 
 enum HashAlgorithmType,values: Md5 (32771),None (0),Sha1 (32772),Sha256 (32780),Sha384 (32781),Sha512 (32782)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Md5=None
 None_ =None
 Sha1=None
 Sha256=None
 Sha384=None
 Sha512=None
 value__=None


class InvalidCredentialException:
 """
 The exception that is thrown when authentication fails for an authentication stream and cannot be retried.
 
 InvalidCredentialException()
 InvalidCredentialException(message: str)
 InvalidCredentialException(message: str,innerException: Exception)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,innerException=None):
  """
  __new__(cls: type)
  __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerException: Exception)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class SslProtocols:
 """
 Defines the possible versions of System.Security.Authentication.SslProtocols.
 
 enum (flags) SslProtocols,values: Default (240),None (0),Ssl2 (12),Ssl3 (48),Tls (192),Tls11 (768),Tls12 (3072)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Default=None
 None_ =None
 Ssl2=None
 Ssl3=None
 Tls=None
 Tls11=None
 Tls12=None
 value__=None


# variables with complex values

