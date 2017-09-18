class MassInstanceUtils(object,IDisposable):
 """ A static class that contains methods for processing curves driven by points. """
 @staticmethod
 def AddMassLevelDataToMassInstance(document,massInstanceId,levelId):
  """
  AddMassLevelDataToMassInstance(document: Document,massInstanceId: ElementId,levelId: ElementId) -> ElementId

  

   Create a MassLevelData (Mass Floor) to associate a Level with a mass instance.

  

   document: The Document.

   massInstanceId: The ElementId of the mass instance.

   levelId: The ElementId of the Level to associate with the mass instance.

   Returns: The ElementId of the MassLevelData that was created,or the existing ElementId 

    if it was already in added.
  """
  pass
 def Dispose(self):
  """ Dispose(self: MassInstanceUtils) """
  pass
 @staticmethod
 def GetGrossFloorArea(document,massInstanceId):
  """
  GetGrossFloorArea(document: Document,massInstanceId: ElementId) -> float

  

   Get the total occupiable floor area represented by a mass instance.

  

   document: The Document.

   massInstanceId: The ElementId of the mass instance.

   Returns: The gross floor area in square feet.
  """
  pass
 @staticmethod
 def GetGrossSurfaceArea(document,massInstanceId):
  """
  GetGrossSurfaceArea(document: Document,massInstanceId: ElementId) -> float

  

   Get the total exterior building surface area represented by a mass instance.

  

   document: The Document.

   massInstanceId: The ElementId of the mass instance.

   Returns: The gross surface area in square feet.
  """
  pass
 @staticmethod
 def GetGrossVolume(document,massInstanceId):
  """
  GetGrossVolume(document: Document,massInstanceId: ElementId) -> float

  

   Get the total building volume represented by a mass instance.

  

   document: The Document.

   massInstanceId: The ElementId of the mass instance.

   Returns: The gross volume in cubic feet.
  """
  pass
 @staticmethod
 def GetJoinedElementIds(document,massInstanceId):
  """
  GetJoinedElementIds(document: Document,massInstanceId: ElementId) -> IList[ElementId]

  

   Get the ElementIds of Elements that are joined to a mass instance.

  

   document: The Document.

   massInstanceId: The ElementId of the mass instance.

   Returns: ElementIds of Elements joined to the mass instance.
  """
  pass
 @staticmethod
 def GetMassLevelDataIds(document,massInstanceId):
  """
  GetMassLevelDataIds(document: Document,massInstanceId: ElementId) -> IList[ElementId]

  

   Get the ElementIds of the MassLevelDatas (Mass Floors) associated with a mass 

    instance.

  

  

   document: The Document.

   massInstanceId: The ElementId of the mass instance.

   Returns: The ElementIds of the MassLevelDatas.
  """
  pass
 @staticmethod
 def GetMassLevelIds(document,massInstanceId):
  """
  GetMassLevelIds(document: Document,massInstanceId: ElementId) -> IList[ElementId]

  

   Get the ElementIds of the Levels associated with a mass instance.

  

   document: The Document.

   massInstanceId: The ElementId of the mass instance.

   Returns: The ElementIds of the Levels
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: MassInstanceUtils,disposing: bool) """
  pass
 @staticmethod
 def RemoveMassLevelDataFromMassInstance(document,massInstanceId,levelId):
  """
  RemoveMassLevelDataFromMassInstance(document: Document,massInstanceId: ElementId,levelId: ElementId)

   Delete the MassLevelData (Mass Floor) that associates a Level with a mass 

    instance.

  

  

   document: The Document.

   massInstanceId: The ElementId of the mass instance.

   levelId: The ElementId of the Level to disassociate from the mass instance.
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



Get: IsValidObject(self: MassInstanceUtils) -> bool



"""


