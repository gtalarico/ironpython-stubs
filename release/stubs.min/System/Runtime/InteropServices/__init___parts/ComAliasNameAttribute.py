class ComAliasNameAttribute:
 """
 Indicates the COM alias for a parameter or field type.
 
 ComAliasNameAttribute(alias: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ComAliasNameAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,alias):
  """ __new__(cls: type,alias: str) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the alias for the field or parameter as found in the type library when it was imported.

Get: Value(self: ComAliasNameAttribute) -> str

"""


