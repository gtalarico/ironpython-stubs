class AnalysisDisplayStyle(Element,IDisposable):
 """ Exposes API for manipulation of analysis display style. """
 @staticmethod
 def CreateAnalysisDisplayStyle(document,name,*__args):
  """
  CreateAnalysisDisplayStyle(document: Document,name: str,markersAndTextSettings: AnalysisDisplayMarkersAndTextSettings,colorSettings: AnalysisDisplayColorSettings,legendSettings: AnalysisDisplayLegendSettings) -> AnalysisDisplayStyle
  
   Factory method - creates analysis display style object of type Markers and Text 
    for the given document.
  
  
   document: Document for which analysis display style object is created.
   name: Name of the analysis display style within the %document%.
   markersAndTextSettings: Markers and text settings for the style.
   colorSettings: Color settings for the style.
   legendSettings: Legend settings for the style.
   Returns: New analysis display style object.
  CreateAnalysisDisplayStyle(document: Document,name: str,coloredSurfaceSettings: AnalysisDisplayColoredSurfaceSettings,colorSettings: AnalysisDisplayColorSettings,legendSettings: AnalysisDisplayLegendSettings) -> AnalysisDisplayStyle
  
   Factory method - creates analysis display style object of type Colored Surface 
    for the given document.
  
  
   document: Document for which analysis display style object is created.
   name: Name of the analysis display style within the %document%.
   coloredSurfaceSettings: Colored surface settings for the style.
   colorSettings: Color settings for the style.
   legendSettings: Legend settings for the style.
   Returns: New analysis display style object.
  CreateAnalysisDisplayStyle(document: Document,name: str,diagramSettings: AnalysisDisplayDiagramSettings,colorSettings: AnalysisDisplayColorSettings,legendSettings: AnalysisDisplayLegendSettings) -> AnalysisDisplayStyle
  
   Factory method - creates analysis display style object of type Diagram for the 
    given document.
  
  
   document: Document for which analysis display style object is created.
   name: Name of the analysis display style within the %document%.
   diagramSettings: Diagram settings for the style.
   colorSettings: Color settings for the style.
   legendSettings: Legend settings for the style.
   Returns: New analysis display style object.
  CreateAnalysisDisplayStyle(document: Document,name: str,deformedShapeSettings: AnalysisDisplayDeformedShapeSettings,colorSettings: AnalysisDisplayColorSettings,legendSettings: AnalysisDisplayLegendSettings) -> AnalysisDisplayStyle
  
   Factory method - creates analysis display style object of type Deformed Shape 
    for the given document.
  
  
   document: Document for which analysis display style object is created.
   name: Name of the analysis display style within the %document%.
   deformedShapeSettings: Deformed Shape settings for the style.
   colorSettings: Color settings for the style.
   legendSettings: Legend settings for the style.
   Returns: New analysis display style object.
  CreateAnalysisDisplayStyle(document: Document,name: str,vectorSettings: AnalysisDisplayVectorSettings,colorSettings: AnalysisDisplayColorSettings,legendSettings: AnalysisDisplayLegendSettings) -> AnalysisDisplayStyle
  
   Factory method - creates analysis display style object of type Vectors for the 
    given document.
  
  
   document: Document for which analysis display style object is created.
   name: Name of the analysis display style within the %document%.
   vectorSettings: Vector settings for the style.
   colorSettings: Color settings for the style.
   legendSettings: Legend settings for the style.
   Returns: New analysis display style object.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 @staticmethod
 def FindByName(document,name):
  """
  FindByName(document: Document,name: str) -> ElementId
  
   Finds analysis display style by name.
  
   document: Document in which to look for analysis display style element.
   name: Name of analysis display style to look for.
   Returns: Element id of the found analysis display style,invalidElementId if not found.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetColoredSurfaceSettings(self):
  """
  GetColoredSurfaceSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayColoredSurfaceSettings
  
   Get colored surface settings object from the style.
  """
  pass
 def GetColorSettings(self):
  """
  GetColorSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayColorSettings
  
   Get color settings object from the style.
  """
  pass
 def GetDeformedShapeSettings(self):
  """
  GetDeformedShapeSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayDeformedShapeSettings
  
   Get deformed shape settings object from the style.
  """
  pass
 def GetDiagramSettings(self):
  """
  GetDiagramSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayDiagramSettings
  
   Get diagram settings object from the style.
  """
  pass
 @staticmethod
 def GetElements(document):
  """
  GetElements(document: Document) -> ICollection[ElementId]
  
   Returns set of all analysis display styles elements in the given document.
  
   document: Document from which analysis display style elements are retrieved.
   Returns: All analysis display style elements existing in the document.
  """
  pass
 def GetLegendSettings(self):
  """
  GetLegendSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayLegendSettings
  
   Get legend settings object from the style.
  """
  pass
 def GetMarkersAndTextSettings(self):
  """
  GetMarkersAndTextSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayMarkersAndTextSettings
  
   Get markers and text settings object from the style.
  """
  pass
 def GetVectorSettings(self):
  """
  GetVectorSettings(self: AnalysisDisplayStyle) -> AnalysisDisplayVectorSettings
  
   Get vector settings object from the style.
  """
  pass
 def HasColoredSurfaceSettings(self):
  """
  HasColoredSurfaceSettings(self: AnalysisDisplayStyle) -> bool
  
   If true style has colored surface settings.
  """
  pass
 def HasDeformedShapeSettings(self):
  """
  HasDeformedShapeSettings(self: AnalysisDisplayStyle) -> bool
  
   If true style has deformed shape settings.
  """
  pass
 def HasDiagramSettings(self):
  """
  HasDiagramSettings(self: AnalysisDisplayStyle) -> bool
  
   If true style has diagram settings.
  """
  pass
 def HasMarkersAndTextSettings(self):
  """
  HasMarkersAndTextSettings(self: AnalysisDisplayStyle) -> bool
  
   If true style has markers and text settings.
  """
  pass
 def HasVectorSettings(self):
  """
  HasVectorSettings(self: AnalysisDisplayStyle) -> bool
  
   If true style has vector settings.
  """
  pass
 @staticmethod
 def IsNameUnique(document,name,excludedElement):
  """
  IsNameUnique(document: Document,name: str,excludedElement: AnalysisDisplayStyle) -> bool
  
   Verify the uniqueness of the name among all analysis display style elements of 
    the document.
  
  
   document: Document in which name uniqueness is verified.
   name: Name to verify uniqueness of.
   excludedElement: Element to be excluded from uniqueness verification (for renaming of an 
    existing element).
  
   Returns: True if name is unique,false otherwise.
  """
  pass
 @staticmethod
 def IsTextTypeIdValid(textTypeId,doc):
  """
  IsTextTypeIdValid(textTypeId: ElementId,doc: Document) -> bool
  
   Verify if text type id is valid.
  
   textTypeId: Text type id to be validated.
   doc: Document for which %textTypeId% is validated.
   Returns: True if text type id is valid,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetColoredSurfaceSettings(self,coloredSurfaceSettings):
  """
  SetColoredSurfaceSettings(self: AnalysisDisplayStyle,coloredSurfaceSettings: AnalysisDisplayColoredSurfaceSettings)
   Set colored surface settings object for the style.
  """
  pass
 def SetColorSettings(self,colorSettings):
  """
  SetColorSettings(self: AnalysisDisplayStyle,colorSettings: AnalysisDisplayColorSettings)
   Set color settings object for the style.
  """
  pass
 def SetDeformedShapeSettings(self,deformedShapeSettings):
  """
  SetDeformedShapeSettings(self: AnalysisDisplayStyle,deformedShapeSettings: AnalysisDisplayDeformedShapeSettings)
   Set deformed shape settings object for the style.
  """
  pass
 def SetDiagramSettings(self,diagramSettings):
  """
  SetDiagramSettings(self: AnalysisDisplayStyle,diagramSettings: AnalysisDisplayDiagramSettings)
   Set diagram settings object for the style.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetLegendSettings(self,legendSettings):
  """
  SetLegendSettings(self: AnalysisDisplayStyle,legendSettings: AnalysisDisplayLegendSettings)
   Set legend settings object for the style.
  """
  pass
 def SetMarkersAndTextSettings(self,markersAndTextSettings):
  """
  SetMarkersAndTextSettings(self: AnalysisDisplayStyle,markersAndTextSettings: AnalysisDisplayMarkersAndTextSettings)
   Set markers and text settings object for the style.
  """
  pass
 def SetName(self,name):
  """
  SetName(self: AnalysisDisplayStyle,name: str)
   Set name of analysis display style element.
  
   name: Analysis display style element name to be set.
  """
  pass
 def SetVectorSettings(self,vectorSettings):
  """
  SetVectorSettings(self: AnalysisDisplayStyle,vectorSettings: AnalysisDisplayVectorSettings)
   Set vector settings object for the style.
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
