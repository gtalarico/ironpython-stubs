class AnalysisResultSchema(object,IDisposable):
 """
 Contains all information about one analysis result. Each result may contain several measurements.
 
 AnalysisResultSchema(name: str,description: str)
 AnalysisResultSchema(other: AnalysisResultSchema)
 """
 def Dispose(self):
  """ Dispose(self: AnalysisResultSchema) """
  pass
 def GetNumberOfUnits(self):
  """
  GetNumberOfUnits(self: AnalysisResultSchema) -> int
  
   returns number of possible units
  """
  pass
 def GetUnitsMultiplier(self,index):
  """
  GetUnitsMultiplier(self: AnalysisResultSchema,index: int) -> float
  
   returns units multiplier by index
  
   index: index of unit in the list
  """
  pass
 def GetUnitsName(self,index):
  """
  GetUnitsName(self: AnalysisResultSchema,index: int) -> str
  
   returns units name by index
  
   index: index of unit in the list
  """
  pass
 def IsEqual(self,other):
  """
  IsEqual(self: AnalysisResultSchema,other: AnalysisResultSchema) -> bool
  
   Determines if the input object is equivalent to this AnalysisResultSchema.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: AnalysisResultSchema,disposing: bool) """
  pass
 def SetUnits(self,names,multipliers):
  """ SetUnits(self: AnalysisResultSchema,names: IList[str],multipliers: IList[float]) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,name: str,description: str)
  __new__(cls: type,other: AnalysisResultSchema)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 AnalysisDisplayStyleId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """ElementId of analysis display style overriding the style set for view; -1 if the style is not overridden

Get: AnalysisDisplayStyleId(self: AnalysisResultSchema) -> ElementId

Set: AnalysisDisplayStyleId(self: AnalysisResultSchema)=value
"""

 CurrentUnits=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Stores the index in the array of applicable units

Get: CurrentUnits(self: AnalysisResultSchema) -> int

Set: CurrentUnits(self: AnalysisResultSchema)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Description of analysis result in view

Get: Description(self: AnalysisResultSchema) -> str

Set: Description(self: AnalysisResultSchema)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisResultSchema) -> bool

"""

 IsVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true analysis result is visible in view

Get: IsVisible(self: AnalysisResultSchema) -> bool

Set: IsVisible(self: AnalysisResultSchema)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of analysis result in view

Get: Name(self: AnalysisResultSchema) -> str

Set: Name(self: AnalysisResultSchema)=value
"""

 Scale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Multiplier used for displaying diagram or vector values in view.

Get: Scale(self: AnalysisResultSchema) -> float

Set: Scale(self: AnalysisResultSchema)=value
"""


