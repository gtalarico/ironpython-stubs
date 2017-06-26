class AnalysisDisplayColorSettings(object,IDisposable):
 """
 Contains color settings for analysis display style element.
 
 AnalysisDisplayColorSettings()
 AnalysisDisplayColorSettings(other: AnalysisDisplayColorSettings)
 """
 def AreIntermediateColorsValid(self,map):
  """ AreIntermediateColorsValid(self: AnalysisDisplayColorSettings,map: IList[AnalysisDisplayColorEntry]) -> bool """
  pass
 def Colors(self):
  """
  Colors(self: AnalysisDisplayColorSettings) -> int
  
   Get number of colors,including min,max and intermediate.
   Returns: Number of colors,including min,max and intermediate.
  """
  pass
 def Dispose(self):
  """ Dispose(self: AnalysisDisplayColorSettings) """
  pass
 def GetIntermediateColors(self):
  """
  GetIntermediateColors(self: AnalysisDisplayColorSettings) -> IList[AnalysisDisplayColorEntry]
  
   Get intermediate color entries (other than the minimum and maximum settings).
   Returns: Array of intermediate color entries.
  """
  pass
 def IsEqual(self,other):
  """
  IsEqual(self: AnalysisDisplayColorSettings,other: AnalysisDisplayColorSettings) -> bool
  
   Compares two color settings objects.
  
   other: Color settings object to compare to.
   Returns: True if objects are equal,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: AnalysisDisplayColorSettings,disposing: bool) """
  pass
 def SetIntermediateColors(self,map):
  """ SetIntermediateColors(self: AnalysisDisplayColorSettings,map: IList[AnalysisDisplayColorEntry]) """
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
  __new__(cls: type,other: AnalysisDisplayColorSettings)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ColorSettingsType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Stores type of color settings

Get: ColorSettingsType(self: AnalysisDisplayColorSettings) -> AnalysisDisplayStyleColorSettingsType

Set: ColorSettingsType(self: AnalysisDisplayColorSettings)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisDisplayColorSettings) -> bool

"""

 MaxColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Color assigned to the maximum value.

Get: MaxColor(self: AnalysisDisplayColorSettings) -> Color

Set: MaxColor(self: AnalysisDisplayColorSettings)=value
"""

 MinColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Color assigned to the minimum value.

Get: MinColor(self: AnalysisDisplayColorSettings) -> Color

Set: MinColor(self: AnalysisDisplayColorSettings)=value
"""


