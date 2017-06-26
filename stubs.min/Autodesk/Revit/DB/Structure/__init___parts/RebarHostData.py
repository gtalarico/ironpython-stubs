class RebarHostData(object,IDisposable):
 """ Interface to rebar-specific data stored in each valid rebar host element. """
 def Dispose(self):
  """ Dispose(self: RebarHostData) """
  pass
 def GetAreaReinforcementsInHost(self):
  """
  GetAreaReinforcementsInHost(self: RebarHostData) -> IList[AreaReinforcement]
  
   Returns all AreaReinforcement elements hosted by the referenced element.
  """
  pass
 def GetCommonCoverType(self):
  """
  GetCommonCoverType(self: RebarHostData) -> RebarCoverType
  
   If all exposed faces of the host have the same associated CoverType,
     return 
    that CoverType; otherwise,return ll.
  
   Returns: The common CoverType for all exposed faces,or ll
     if there are multiple 
    CoverTypes.
  """
  pass
 def GetCoverType(self,face):
  """
  GetCoverType(self: RebarHostData,face: Reference) -> RebarCoverType
  
   Gets the CoverType associated with a face of the element.
   Returns: The cover associated with the face,if it is an exposed face.
     If the face 
    is concealed,returns ll.
  """
  pass
 def GetExposedFaces(self):
  """
  GetExposedFaces(self: RebarHostData) -> IList[Reference]
  
   Returns all the exposed faces,that is,those that have an associated CoverType.
  """
  pass
 def GetFabricAreasInHost(self):
  """
  GetFabricAreasInHost(self: RebarHostData) -> IList[FabricArea]
  
   Returns all FabricArea elements hosted by the referenced element.
  """
  pass
 def GetFabricSheetsInHost(self):
  """
  GetFabricSheetsInHost(self: RebarHostData) -> IList[FabricSheet]
  
   Returns all FabricSheet elements hosted by the referenced element.
  """
  pass
 def GetPathReinforcementsInHost(self):
  """
  GetPathReinforcementsInHost(self: RebarHostData) -> IList[PathReinforcement]
  
   Returns all PathReinforcement elements hosted by the referenced element.
  """
  pass
 def GetRebarContainersInHost(self):
  """
  GetRebarContainersInHost(self: RebarHostData) -> IList[RebarContainer]
  
   Returns all RebarContainer elements hosted by the referenced element.
  """
  pass
 @staticmethod
 def GetRebarHostData(host):
  """
  GetRebarHostData(host: Element) -> RebarHostData
  
   Gets a RebarHostData object referring to the specified
     rebar host element.
  
   host: An element to host rebar.
   Returns: A RebarHostData object,or ll.
  """
  pass
 def GetRebarsInHost(self):
  """
  GetRebarsInHost(self: RebarHostData) -> IList[Rebar]
  
   Returns all Rebar elements hosted by the referenced element.
  """
  pass
 def IsFaceExposed(self,face):
  """
  IsFaceExposed(self: RebarHostData,face: Reference) -> bool
  
   Checks whether the specified face is considered exposed,and
     therefore has 
    an associated CoverType.
  
   Returns: True if %face% is exposed,false otherwise.
  """
  pass
 @staticmethod
 def IsValidHost(element=None):
  """
  IsValidHost(self: RebarHostData) -> bool
  
   Reports whether the element is a valid rebar host.
   Returns: True if the referenced Element can currently host Rebar elements,
     false 
    otherwise.
  
  IsValidHost(element: Element) -> bool
  
   Identifies whether a given element can host reinforcement.
  
   element: The element to check.
   Returns: True if the input Element can host reinforcement elements,
     false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RebarHostData,disposing: bool) """
  pass
 def SetCommonCoverType(self,coverType):
  """
  SetCommonCoverType(self: RebarHostData,coverType: RebarCoverType)
   Associate a single CoverType with all exposed faces of the host element.
  
   coverType: A CoverType object to be applied to all faces.
  """
  pass
 def SetCoverType(self,face,coverType):
  """
  SetCoverType(self: RebarHostData,face: Reference,coverType: RebarCoverType)
   Associates the specified CoverType with the specified face of the element.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarHostData) -> bool

"""


