class AnalysisDisplayDeformedShapeSettings(object,IDisposable):
 """
 Contains deformed shape settings for analysis display style element.

 

 AnalysisDisplayDeformedShapeSettings()

 AnalysisDisplayDeformedShapeSettings(other: AnalysisDisplayDeformedShapeSettings)
 """
 def Dispose(self):
  """ Dispose(self: AnalysisDisplayDeformedShapeSettings) """
  pass
 def IsEqual(self,other):
  """
  IsEqual(self: AnalysisDisplayDeformedShapeSettings,other: AnalysisDisplayDeformedShapeSettings) -> bool

  

   Compares two deformed shape settings objects.

  

   other: Deformed shape settings object to compare with.

   Returns: True if objects are equal,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: AnalysisDisplayDeformedShapeSettings,disposing: bool) """
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
 def __new__(self,other=None):
  """
  __new__(cls: type)

  __new__(cls: type,other: AnalysisDisplayDeformedShapeSettings)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 GridColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Color of grid lines.



Get: GridColor(self: AnalysisDisplayDeformedShapeSettings) -> Color



Set: GridColor(self: AnalysisDisplayDeformedShapeSettings)=value

"""

 GridLineWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Line weight of grid lines.



Get: GridLineWeight(self: AnalysisDisplayDeformedShapeSettings) -> int



Set: GridLineWeight(self: AnalysisDisplayDeformedShapeSettings)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: AnalysisDisplayDeformedShapeSettings) -> bool



"""

 Rounding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Increment to which numeric values of analysis results are rounded in deformed shape.



Get: Rounding(self: AnalysisDisplayDeformedShapeSettings) -> float



Set: Rounding(self: AnalysisDisplayDeformedShapeSettings)=value

"""

 ShowContourLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true,show contour lines in the analysis display.



Get: ShowContourLines(self: AnalysisDisplayDeformedShapeSettings) -> bool



Set: ShowContourLines(self: AnalysisDisplayDeformedShapeSettings)=value

"""

 ShowGridLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true,show grid lines in the analysis display.



Get: ShowGridLines(self: AnalysisDisplayDeformedShapeSettings) -> bool



Set: ShowGridLines(self: AnalysisDisplayDeformedShapeSettings)=value

"""

 TextLabelType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Type of deformed shape text visualization.



Get: TextLabelType(self: AnalysisDisplayDeformedShapeSettings) -> AnalysisDisplayStyleDeformedShapeTextLabelType



Set: TextLabelType(self: AnalysisDisplayDeformedShapeSettings)=value

"""

 TextTypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Element id of text associated with the settings.



Get: TextTypeId(self: AnalysisDisplayDeformedShapeSettings) -> ElementId



Set: TextTypeId(self: AnalysisDisplayDeformedShapeSettings)=value

"""

 Transparency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Transparency percentage of deformed shape color fill on surfaces



Get: Transparency(self: AnalysisDisplayDeformedShapeSettings) -> int



Set: Transparency(self: AnalysisDisplayDeformedShapeSettings)=value

"""


