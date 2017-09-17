class MassEnergyAnalyticalModel(Element,IDisposable):
 """ This class associates a mass instance with an energy analytical model data and geometry. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetCoincidentEnergyAnalyticalModelFaceReference(document,referenceToFace):
  """
  GetCoincidentEnergyAnalyticalModelFaceReference(document: Document,referenceToFace: Reference) -> Reference
  
   Returns a Reference to a Face from the same or a different 
    MassEnergyAnalyticalModel
     that is coincident with the input Face.
  
  
   document: The Document.
   referenceToFace: A Reference to a Face of a MassEnergyAnalyticalModel.
  """
  pass
 @staticmethod
 def GetCoincidentMassZoneFaceReferences(document,referenceToFace):
  """
  GetCoincidentMassZoneFaceReferences(document: Document,referenceToFace: Reference) -> IList[Reference]
  
   Returns References to Faces from MassZones coincident with an input Face from a
    
     MassEnergyAnalyticalModel.
  
  
   document: The Document.
   referenceToFace: A Reference to a Face of a MassEnergyAnalyticalModel.
   Returns: Returns References to Faces from MassZones coincident with an input Face from a
    
     MassEnergyAnalyticalModel.
  """
  pass
 def GetJoinedMassEnergyAnalyticalModelElementIds(self):
  """
  GetJoinedMassEnergyAnalyticalModelElementIds(self: MassEnergyAnalyticalModel) -> ICollection[ElementId]
  
   The ElementIds of other MassEnergyAnalyticalModels that are "joined" to this 
    one.
  
   Returns: ElementIds of other MassEnergyAnalyticalModels that are joined to this one.
  """
  pass
 @staticmethod
 def GetMassEnergyAnalyticalModelIdForMassInstance(document,massInstanceId):
  """
  GetMassEnergyAnalyticalModelIdForMassInstance(document: Document,massInstanceId: ElementId) -> ElementId
  
   Get the ElementId of the MassEnergyAnalyticalModel for a mass instance.
  
   document: The Document.
   massInstanceId: ElementId of a mass instance.
   Returns: ElementId of a MassEnergyAnalyticalModel.
  """
  pass
 def GetMassSurfaceDataIdForReference(self,reference):
  """
  GetMassSurfaceDataIdForReference(self: MassEnergyAnalyticalModel,reference: Reference) -> ElementId
  
   Get the ElementId of the MassSurfaceData corresponding to the Reference.
  
   reference: A Reference to a face of this MassEnergyAnalyticalModel.
   Returns: ElementId of a MassSurfaceData.
  """
  pass
 def GetMassZoneIds(self):
  """
  GetMassZoneIds(self: MassEnergyAnalyticalModel) -> ICollection[ElementId]
  
   Get the MassZone ElementIds that are created from this 
    MassEnergyAnalyticalModel.
  
   Returns: Returns the ElementIds of MassZones.
  """
  pass
 def GetReferencesToAllFaces(self):
  """
  GetReferencesToAllFaces(self: MassEnergyAnalyticalModel) -> IList[Reference]
  
   Get References to all Faces which are meaningful for the 
    MassEnergyAnalyticalModel.
     Array of References to Faces of the 
    MassEnergyAnalyticalModel.
  """
  pass
 def GetReferencesToAllShadingFaces(self):
  """
  GetReferencesToAllShadingFaces(self: MassEnergyAnalyticalModel) -> IList[Reference]
  
   Get References to all Faces of the MassEnergyAnalyticalModel which are of Mass 
    Shade subcategory.
  
   Returns: Array of Reference to Faces that represent Mass Shades.
  """
  pass
 def GetValidSurfaceCategoryIdsForReference(self,reference,recommendedDefaultSubcategoryId):
  """
  GetValidSurfaceCategoryIdsForReference(self: MassEnergyAnalyticalModel,reference: Reference) -> (IList[ElementId],ElementId)
  
   The Mass surface subcategory ids that are appropriate values for the input 
    Reference.
  
  
   reference: A Reference to a Face of this MassEnergyAnalyticalModel.
   Returns: Returns the ElementIds of appropriate values for input Reference.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 MassId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ElementId of the mass instance the MassEnergyAnalyticalModel is associated with.

Get: MassId(self: MassEnergyAnalyticalModel) -> ElementId

"""

 MassZoneCoreOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If this value is greater than 0.0,in the MassEnergyAnalytical model a building "core" geometry
   will be created for each solid geometry of the mass instance.

Get: MassZoneCoreOffset(self: MassEnergyAnalyticalModel) -> float

Set: MassZoneCoreOffset(self: MassEnergyAnalyticalModel)=value
"""


