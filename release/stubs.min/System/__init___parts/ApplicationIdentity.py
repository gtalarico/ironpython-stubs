class ApplicationIdentity(object):
 """
 Provides the ability to uniquely identify a manifest-activated application. This class cannot be inherited.
 
 ApplicationIdentity(applicationIdentityFullName: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ApplicationIdentity()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ToString(self):
  """
  ToString(self: ApplicationIdentity) -> str
  
   Returns the full name of the manifest-activated application.
   Returns: The full name of the manifest-activated application.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,applicationIdentityFullName):
  """ __new__(cls: type,applicationIdentityFullName: str) """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 CodeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location of the deployment manifest as a URL.

Get: CodeBase(self: ApplicationIdentity) -> str

"""

 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the full name of the application.

Get: FullName(self: ApplicationIdentity) -> str

"""


