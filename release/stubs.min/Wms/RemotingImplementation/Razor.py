# encoding: utf-8
# module Wms.RemotingImplementation.Razor calls itself Razor
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BasePage:
 # no doc
 def ResolveLayout(self,*args):
  """
  ResolveLayout(self: TemplateBase[TModel],name: str) -> ITemplate
  
   Resolves the layout template.
  
   name: The name of the layout template.
   Returns: An instance of RazorEngine.Templating.ITemplate.
  """
  pass
 def T(self,key):
  """ T(self: BasePage[TModel],key: str) -> object """
  pass
 def Translate(self,key):
  """ Translate(self: BasePage[TModel],key: str) -> object """
  pass
 def TryTranslatePortal(self,key):
  """ TryTranslatePortal(self: BasePage[TModel],key: str) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 HasDynamicModel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines whether this template has a dynamic model.

"""


 _context=None


class ILocalizeable:
 # no doc
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 CultureInfo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CultureInfo(self: ILocalizeable) -> CultureInfo

Set: CultureInfo(self: ILocalizeable)=value
"""



