class BuildingEnvelopeAnalyzer(object,IDisposable):
 """ Analyzes which elements are part of the building envelope,the building elements exposed to the outside. """
 @staticmethod
 def Create(document,options):
  """
  Create(document: Document,options: BuildingEnvelopeAnalyzerOptions) -> BuildingEnvelopeAnalyzer

  

   Creates a new analyzer.

  

   document: The document that contains the physical model of the building.

   options: Options for the method analyzing the building elements for the building 

    envelope.

  

   Returns: The created analyzer.
  """
  pass
 def Dispose(self):
  """ Dispose(self: BuildingEnvelopeAnalyzer) """
  pass
 def GetBoundingElements(self):
  """
  GetBoundingElements(self: BuildingEnvelopeAnalyzer) -> IList[LinkElementId]

  

   Returns the collection of building elements exposed to the outside forming the 

    building envelope.

  

   Returns: The ids of the building elements in the envelope.
  """
  pass
 def GetBoundingElementsForSpaceVolume(self,spaceVolume):
  """
  GetBoundingElementsForSpaceVolume(self: BuildingEnvelopeAnalyzer,spaceVolume: int) -> IList[LinkElementId]

  

   Returns the collection of bounding building elements for an enclosed space 

    volume.

  

   Returns: The ids of the bounding building elements for the enclosed space volume.
  """
  pass
 def GetCenterPointsForConnectedGridCellsInSpaceVolume(self,spaceVolume):
  """
  GetCenterPointsForConnectedGridCellsInSpaceVolume(self: BuildingEnvelopeAnalyzer,spaceVolume: int) -> IList[XYZ]

  

   Returns the collection of connected cells in an enclosed space volume.

   Returns: The center points for the connected analytical grid cells in the enclosed space 

    volume.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BuildingEnvelopeAnalyzer,disposing: bool) """
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
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: BuildingEnvelopeAnalyzer) -> bool



"""


