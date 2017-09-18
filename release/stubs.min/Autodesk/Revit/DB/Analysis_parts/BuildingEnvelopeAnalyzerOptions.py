class BuildingEnvelopeAnalyzerOptions(object,IDisposable):
 """
 Specific options for the method analyzing the building elements for the building envelope.

 

 BuildingEnvelopeAnalyzerOptions()
 """
 def Dispose(self):
  """ Dispose(self: BuildingEnvelopeAnalyzerOptions) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BuildingEnvelopeAnalyzerOptions,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 AnalyzeEnclosedSpaceVolumes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not to analyze interior connected regions inside the building forming enclosed space volumes.



Get: AnalyzeEnclosedSpaceVolumes(self: BuildingEnvelopeAnalyzerOptions) -> bool



Set: AnalyzeEnclosedSpaceVolumes(self: BuildingEnvelopeAnalyzerOptions)=value

"""

 GridCellSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The cell size for the uniform cubical grid used when analyzing the building envelope.



Get: GridCellSize(self: BuildingEnvelopeAnalyzerOptions) -> float



Set: GridCellSize(self: BuildingEnvelopeAnalyzerOptions)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: BuildingEnvelopeAnalyzerOptions) -> bool



"""

 OptimizeGridCellSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not to use the exact value for the cell size or let the analyzer optimize the cell size based on the specified grid size



Get: OptimizeGridCellSize(self: BuildingEnvelopeAnalyzerOptions) -> bool



Set: OptimizeGridCellSize(self: BuildingEnvelopeAnalyzerOptions)=value

"""


