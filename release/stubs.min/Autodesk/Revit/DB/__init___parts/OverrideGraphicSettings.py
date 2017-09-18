class OverrideGraphicSettings(object,IDisposable):
 """
 Settings to override display of elements in a view.

 

 OverrideGraphicSettings(overrideGraphicSettings: OverrideGraphicSettings)

 OverrideGraphicSettings()
 """
 def Dispose(self):
  """ Dispose(self: OverrideGraphicSettings) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: OverrideGraphicSettings,disposing: bool) """
  pass
 def SetCutFillColor(self,color):
  """
  SetCutFillColor(self: OverrideGraphicSettings,color: Color) -> OverrideGraphicSettings

  

   Sets the cut surface fill color.

  

   color: Cut surface fill color for the override (invalidColorValue means no override is 

    set).

  

   Returns: Reference to the changed object.
  """
  pass
 def SetCutFillPatternId(self,fillPatternId):
  """
  SetCutFillPatternId(self: OverrideGraphicSettings,fillPatternId: ElementId) -> OverrideGraphicSettings

  

   Sets the ElementId of the cut surface fill pattern.

  

   fillPatternId: ElementId of the cut surface fill pattern for the override. InvalidElementId 

    means no override is set. The pattern must be a drafting pattern.

  

   Returns: Reference to the changed object.
  """
  pass
 def SetCutFillPatternVisible(self,cutFillPatternVisible):
  """
  SetCutFillPatternVisible(self: OverrideGraphicSettings,cutFillPatternVisible: bool) -> OverrideGraphicSettings

  

   Sets the visibility of the cut surface fill pattern.

  

   cutFillPatternVisible: Value of the visibility of the cut surface fill pattern.

   Returns: Reference to the changed object.
  """
  pass
 def SetCutLineColor(self,color):
  """
  SetCutLineColor(self: OverrideGraphicSettings,color: Color) -> OverrideGraphicSettings

  

   Sets the cut surface line color.

  

   color: Value of the cut surface line color for the override. InvalidColorValue means 

    no override is set.

  

   Returns: Reference to the changed object.
  """
  pass
 def SetCutLinePatternId(self,linePatternId):
  """
  SetCutLinePatternId(self: OverrideGraphicSettings,linePatternId: ElementId) -> OverrideGraphicSettings

  

   Sets the ElementId of the cut surface line pattern.

  

   linePatternId: ElementId of the cut surface line pattern for the override. InvalidElementId 

    means no override is set.

  

   Returns: Reference to the changed object.
  """
  pass
 def SetCutLineWeight(self,lineWeight):
  """
  SetCutLineWeight(self: OverrideGraphicSettings,lineWeight: int) -> OverrideGraphicSettings

  

   Sets the cut surface line weight.

  

   lineWeight: Value of the cut surface line weight for the override. InvalidPenNumber means 

    no override is set.

  

   Returns: Reference to the changed object.
  """
  pass
 def SetDetailLevel(self,detailLevel):
  """
  SetDetailLevel(self: OverrideGraphicSettings,detailLevel: ViewDetailLevel) -> OverrideGraphicSettings

  

   Sets the detail level.

  

   detailLevel: Value of the detail level. ViewDetailLevel.Undefined means no override is set.

   Returns: Reference to the changed object.
  """
  pass
 def SetHalftone(self,halftone):
  """
  SetHalftone(self: OverrideGraphicSettings,halftone: bool) -> OverrideGraphicSettings

  

   Sets the halftone value.

  

   halftone: True if the override displays in halftone,false otherwise.

   Returns: Reference to the changed object.
  """
  pass
 def SetProjectionFillColor(self,color):
  """
  SetProjectionFillColor(self: OverrideGraphicSettings,color: Color) -> OverrideGraphicSettings

  

   Sets the projection surface fill color.

  

   color: Value of the projection surface fill color for the override. InvalidColorValue 

    means no override is set.

  

   Returns: Reference to the changed object.
  """
  pass
 def SetProjectionFillPatternId(self,fillPatternId):
  """
  SetProjectionFillPatternId(self: OverrideGraphicSettings,fillPatternId: ElementId) -> OverrideGraphicSettings

  

   Sets the projection surface fill pattern.

  

   fillPatternId: ElementId of the projection surface fill pattern for the override. 

    InvalidElementId means no override is set. The pattern must be a drafting 

    pattern.

  

   Returns: Reference to the changed object.
  """
  pass
 def SetProjectionFillPatternVisible(self,projectFillPatternVisible):
  """
  SetProjectionFillPatternVisible(self: OverrideGraphicSettings,projectFillPatternVisible: bool) -> OverrideGraphicSettings

  

   Sets the visibility of the projection surface fill pattern.

  

   projectFillPatternVisible: Value of the visibility of the projection surface fill pattern.

   Returns: Reference to the changed object.
  """
  pass
 def SetProjectionLineColor(self,color):
  """
  SetProjectionLineColor(self: OverrideGraphicSettings,color: Color) -> OverrideGraphicSettings

  

   Sets the projection surface line color.

  

   color: Value of the projection surface line color for the override. InvalidColorValue 

    means no override is set.

  

   Returns: Reference to the changed object.
  """
  pass
 def SetProjectionLinePatternId(self,linePatternId):
  """
  SetProjectionLinePatternId(self: OverrideGraphicSettings,linePatternId: ElementId) -> OverrideGraphicSettings

  

   Sets the ElementId of the projection surface line pattern.

  

   linePatternId: ElementId of the projection surface line pattern for the override. 

    InvalidElementId means no override is set.

  

   Returns: Reference to the changed object.
  """
  pass
 def SetProjectionLineWeight(self,lineWeight):
  """
  SetProjectionLineWeight(self: OverrideGraphicSettings,lineWeight: int) -> OverrideGraphicSettings

  

   Sets the projection surface line weight.

  

   lineWeight: Value of the projection surface line weight for the override. InvalidPenNumber 

    means no override is set.

  

   Returns: Reference to the changed object.
  """
  pass
 def SetSurfaceTransparency(self,transparency):
  """
  SetSurfaceTransparency(self: OverrideGraphicSettings,transparency: int) -> OverrideGraphicSettings

  

   Sets the projection surface transparency.

  

   transparency: Value of the transparency of the projection surface (0=opaque,100=fully 

    transparent).

  

   Returns: Reference to the changed object.
  """
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
 def __new__(self,overrideGraphicSettings=None):
  """
  __new__(cls: type,overrideGraphicSettings: OverrideGraphicSettings)

  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CutFillColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Cut surface fill color.



Get: CutFillColor(self: OverrideGraphicSettings) -> Color



"""

 CutFillPatternId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """ElementId of the cut surface fill pattern.



Get: CutFillPatternId(self: OverrideGraphicSettings) -> ElementId



"""

 CutLineColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Cut surface line color.



Get: CutLineColor(self: OverrideGraphicSettings) -> Color



"""

 CutLinePatternId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """ElementId of the cut surface line pattern.



Get: CutLinePatternId(self: OverrideGraphicSettings) -> ElementId



"""

 CutLineWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Cut surface line weight.



Get: CutLineWeight(self: OverrideGraphicSettings) -> int



"""

 DetailLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Detail Level.



Get: DetailLevel(self: OverrideGraphicSettings) -> ViewDetailLevel



"""

 Halftone=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Value of the halftone override.



Get: Halftone(self: OverrideGraphicSettings) -> bool



"""

 IsCutFillPatternVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Visibility of the cut surface fill pattern.



Get: IsCutFillPatternVisible(self: OverrideGraphicSettings) -> bool



"""

 IsProjectionFillPatternVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The visibility of the projection surface fill pattern.



Get: IsProjectionFillPatternVisible(self: OverrideGraphicSettings) -> bool



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: OverrideGraphicSettings) -> bool



"""

 ProjectionFillColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Projection surface fill color.



Get: ProjectionFillColor(self: OverrideGraphicSettings) -> Color



"""

 ProjectionFillPatternId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """ElementId of the projection surface fill pattern.



Get: ProjectionFillPatternId(self: OverrideGraphicSettings) -> ElementId



"""

 ProjectionLineColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Projection surface line color.



Get: ProjectionLineColor(self: OverrideGraphicSettings) -> Color



"""

 ProjectionLinePatternId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the projection surface line pattern.



Get: ProjectionLinePatternId(self: OverrideGraphicSettings) -> ElementId



"""

 ProjectionLineWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The projection surface line weight.



Get: ProjectionLineWeight(self: OverrideGraphicSettings) -> int



"""

 Transparency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Transparency of surfaces.



Get: Transparency(self: OverrideGraphicSettings) -> int



"""


 InvalidPenNumber=-1

