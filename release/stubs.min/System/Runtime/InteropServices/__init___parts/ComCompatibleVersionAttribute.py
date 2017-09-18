class ComCompatibleVersionAttribute(Attribute,_Attribute):
 """
 Indicates to a COM client that all classes in the current version of an assembly are compatible with classes in an earlier version of the assembly.

 

 ComCompatibleVersionAttribute(major: int,minor: int,build: int,revision: int)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,major,minor,build,revision):
  """ __new__(cls: type,major: int,minor: int,build: int,revision: int) """
  pass
 BuildNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the build number of the assembly.



Get: BuildNumber(self: ComCompatibleVersionAttribute) -> int



"""

 MajorVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the major version number of the assembly.



Get: MajorVersion(self: ComCompatibleVersionAttribute) -> int



"""

 MinorVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minor version number of the assembly.



Get: MinorVersion(self: ComCompatibleVersionAttribute) -> int



"""

 RevisionNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the revision number of the assembly.



Get: RevisionNumber(self: ComCompatibleVersionAttribute) -> int



"""


