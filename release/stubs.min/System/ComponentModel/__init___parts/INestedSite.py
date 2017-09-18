class INestedSite(ISite,IServiceProvider):
 """ Provides the ability to retrieve the full nested name of a component. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the full name of the component in this site.



Get: FullName(self: INestedSite) -> str



"""


