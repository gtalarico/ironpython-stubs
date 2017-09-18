class ApplicationId(object):
 """
 Contains information used to uniquely identify a manifest-based application. This class cannot be inherited.

 

 ApplicationId(publicKeyToken: Array[Byte],name: str,version: Version,processorArchitecture: str,culture: str)
 """
 def Copy(self):
  """
  Copy(self: ApplicationId) -> ApplicationId

  

   Creates and returns an identical copy of the current application identity.

   Returns: An System.ApplicationId object that represents an exact copy of the original.
  """
  pass
 def Equals(self,o):
  """
  Equals(self: ApplicationId,o: object) -> bool

  

   Determines whether the specified System.ApplicationId object is equivalent to the current 

    System.ApplicationId.

  

  

   o: The System.ApplicationId object to compare to the current System.ApplicationId.

   Returns: true if the specified System.ApplicationId object is equivalent to the current 

    System.ApplicationId; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ApplicationId) -> int

  

   Gets the hash code for the current application identity.

   Returns: The hash code for the current application identity.
  """
  pass
 def ToString(self):
  """
  ToString(self: ApplicationId) -> str

  

   Creates and returns a string representation of the application identity.

   Returns: A string representation of the application identity.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,publicKeyToken,name,version,processorArchitecture,culture):
  """ __new__(cls: type,publicKeyToken: Array[Byte],name: str,version: Version,processorArchitecture: str,culture: str) """
  pass
 def __ne__(self,*args):
  pass
 Culture=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a string representing the culture information for the application.



Get: Culture(self: ApplicationId) -> str



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the application.



Get: Name(self: ApplicationId) -> str



"""

 ProcessorArchitecture=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the target processor architecture for the application.



Get: ProcessorArchitecture(self: ApplicationId) -> str



"""

 PublicKeyToken=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the public key token for the application.



Get: PublicKeyToken(self: ApplicationId) -> Array[Byte]



"""

 Version=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the version of the application.



Get: Version(self: ApplicationId) -> Version



"""


