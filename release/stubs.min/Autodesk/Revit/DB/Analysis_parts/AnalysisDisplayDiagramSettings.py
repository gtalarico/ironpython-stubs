class AnalysisDisplayDiagramSettings(object,IDisposable):
 """
 Contains diagram settings for analysis display style element.

 

 AnalysisDisplayDiagramSettings()

 AnalysisDisplayDiagramSettings(other: AnalysisDisplayDiagramSettings)
 """
 def Dispose(self):
  """ Dispose(self: AnalysisDisplayDiagramSettings) """
  pass
 def IsEqual(self,other):
  """
  IsEqual(self: AnalysisDisplayDiagramSettings,other: AnalysisDisplayDiagramSettings) -> bool

  

   Compares two diagram settings objects.

  

   other: Diagram settings object to compare with.

   Returns: True if objects are equal,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: AnalysisDisplayDiagramSettings,disposing: bool) """
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

  __new__(cls: type,other: AnalysisDisplayDiagramSettings)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 FenceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Type of diagram fence visualization.



Get: FenceType(self: AnalysisDisplayDiagramSettings) -> AnalysisDisplayStyleDiagramFenceType



Set: FenceType(self: AnalysisDisplayDiagramSettings)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: AnalysisDisplayDiagramSettings) -> bool



"""

 OutlineColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Color of outline and fence lines in the diagram.



Get: OutlineColor(self: AnalysisDisplayDiagramSettings) -> Color



Set: OutlineColor(self: AnalysisDisplayDiagramSettings)=value

"""

 OutlineLineWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Line weight of outline and fence lines in the diagram.



Get: OutlineLineWeight(self: AnalysisDisplayDiagramSettings) -> int



Set: OutlineLineWeight(self: AnalysisDisplayDiagramSettings)=value

"""

 Rounding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Increment to which numeric values of analysis results are rounded in diagram.



Get: Rounding(self: AnalysisDisplayDiagramSettings) -> float



Set: Rounding(self: AnalysisDisplayDiagramSettings)=value

"""

 TextLabelType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Type of diagram text label visualization.



Get: TextLabelType(self: AnalysisDisplayDiagramSettings) -> AnalysisDisplayStyleDiagramTextLabelType



Set: TextLabelType(self: AnalysisDisplayDiagramSettings)=value

"""

 TextTypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Element id of text associated with the settings.



Get: TextTypeId(self: AnalysisDisplayDiagramSettings) -> ElementId



Set: TextTypeId(self: AnalysisDisplayDiagramSettings)=value

"""

 Transparency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Transparency percentage of diagram color fill



Get: Transparency(self: AnalysisDisplayDiagramSettings) -> int



Set: Transparency(self: AnalysisDisplayDiagramSettings)=value

"""


