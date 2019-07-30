class INestedSite:
 """ Provides the ability to retrieve the full nested name of a component. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return INestedSite()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the full name of the component in this site.

Get: FullName(self: INestedSite) -> str

"""


