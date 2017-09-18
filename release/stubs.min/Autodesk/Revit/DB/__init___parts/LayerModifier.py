class LayerModifier(object,IDisposable):
 """
 A modifier used to designate extra strings to appear in the exported layer name.
 
 LayerModifier(modifierType: ModifierType,separator: str)
 LayerModifier()
 """
 def Dispose(self):
  """ Dispose(self: LayerModifier) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: LayerModifier,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,modifierType=None,separator=None):
  """
  __new__(cls: type,modifierType: ModifierType,separator: str)
  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LayerModifier) -> bool

"""

 ModifierType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The modifier type.

Get: ModifierType(self: LayerModifier) -> ModifierType

Set: ModifierType(self: LayerModifier)=value
"""

 Separator=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The separator string that will follow this modifier in the export layer name.

Get: Separator(self: LayerModifier) -> str

Set: Separator(self: LayerModifier)=value
"""


