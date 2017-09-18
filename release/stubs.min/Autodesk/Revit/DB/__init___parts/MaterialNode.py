class MaterialNode(RenderNode,IDisposable):
 """ This class represents a change of material during a model-exporting process. """
 def Dispose(self):
  """ Dispose(self: RenderNode,A_0: bool) """
  pass
 def GetAppearance(self):
  """
  GetAppearance(self: MaterialNode) -> Asset

  

   Appearance properties associated with the material.

   Returns: An instance of a rendering material asset
  """
  pass
 def GetAppearanceOverride(self):
  """
  GetAppearanceOverride(self: MaterialNode) -> Asset

  

   Returns appearance properties that override the preset appearance of the 

    material.

  

   Returns: An instance of a rendering material asset,of null if there is no override.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RenderNode,disposing: bool) """
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
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color the material is being rendered at



Get: Color(self: MaterialNode) -> Color



"""

 Glossiness=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The level of glossiness of the material



Get: Glossiness(self: MaterialNode) -> int



"""

 HasOverriddenAppearance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the default rendering appearance the material has is being overridden.



Get: HasOverriddenAppearance(self: MaterialNode) -> bool



"""

 MaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the element assocated with this material in the model.



Get: MaterialId(self: MaterialNode) -> ElementId



"""

 Smoothness=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The level of smoothness of the material.



Get: Smoothness(self: MaterialNode) -> int



"""

 ThumbnailFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The path if a file that contains a thumbnail image of the material.



Get: ThumbnailFile(self: MaterialNode) -> str



"""

 Transparency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The value of transparency the material is being rendered with



Get: Transparency(self: MaterialNode) -> float



"""


