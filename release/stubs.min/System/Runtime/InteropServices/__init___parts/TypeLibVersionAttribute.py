class TypeLibVersionAttribute:
 """
 Specifies the version number of an exported type library.
 
 TypeLibVersionAttribute(major: int,minor: int)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TypeLibVersionAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,major,minor):
  """ __new__(cls: type,major: int,minor: int) """
  pass
 MajorVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the major version number of the type library.

Get: MajorVersion(self: TypeLibVersionAttribute) -> int

"""

 MinorVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minor version number of the type library.

Get: MinorVersion(self: TypeLibVersionAttribute) -> int

"""


