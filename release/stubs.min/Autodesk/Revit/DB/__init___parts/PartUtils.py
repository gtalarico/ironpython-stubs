class PartUtils(object):
 """ General Part utility methods """
 @staticmethod
 def AreElementsValidForCreateParts(document,elementIds):
  """ AreElementsValidForCreateParts(document: Document,elementIds: ICollection[ElementId]) -> bool """
  pass
 @staticmethod
 def ArePartsValidForDivide(document,elementIdsToDivide):
  """ ArePartsValidForDivide(document: Document,elementIdsToDivide: ICollection[ElementId]) -> bool """
  pass
 @staticmethod
 def ArePartsValidForMerge(document,partIds):
  """ ArePartsValidForMerge(document: Document,partIds: ICollection[ElementId]) -> bool """
  pass
 @staticmethod
 def CreateMergedPart(document,partIds):
  """ CreateMergedPart(document: Document,partIds: ICollection[ElementId]) -> PartMaker """
  pass
 @staticmethod
 def CreateParts(document,*__args):
  """ CreateParts(document: Document,hostOrLinkElementIds: ICollection[LinkElementId])CreateParts(document: Document,elementIds: ICollection[ElementId]) """
  pass
 @staticmethod
 def DivideParts(document,elementIdsToDivide,intersectingReferenceIds,curveArray,sketchPlaneId):
  """ DivideParts(document: Document,elementIdsToDivide: ICollection[ElementId],intersectingReferenceIds: ICollection[ElementId],curveArray: IList[Curve],sketchPlaneId: ElementId) -> PartMaker """
  pass
 @staticmethod
 def FindMergeableClusters(doc,partIds):
  """ FindMergeableClusters(doc: Document,partIds: ICollection[ElementId]) -> IList[ICollection[ElementId]] """
  pass
 @staticmethod
 def GetAssociatedPartMaker(hostDocument,*__args):
  """
  GetAssociatedPartMaker(hostDocument: Document,hostOrLinkElementId: LinkElementId) -> PartMaker

  

   Gets associated PartMaker for an element.

  

   hostDocument: The document

   hostOrLinkElementId: The id for the element to be checked for associated Parts

   Returns: The PartMaker element that is making Parts for this element.

     ll if there is 

    no associated PartMaker.

  

  GetAssociatedPartMaker(hostDocument: Document,elementId: ElementId) -> PartMaker

  

   Gets associated PartMaker for an element.

  

   hostDocument: The document

   elementId: The id for the element to be checked for associated Parts

   Returns: The PartMaker element that is making Parts for this element.

     ll if there is 

    no associated PartMaker.
  """
  pass
 @staticmethod
 def GetAssociatedParts(hostDocument,*__args):
  """
  GetAssociatedParts(hostDocument: Document,hostOrLinkElementId: LinkElementId,includePartsWithAssociatedParts: bool,includeAllChildren: bool) -> ICollection[ElementId]

  

   Returns all Parts that are associated with the given element

  

   hostDocument: The document of the element

   hostOrLinkElementId: The element to be checked for associated Parts.

   includePartsWithAssociatedParts: If true,include parts that have associated parts

   includeAllChildren: If true,return all associated Parts recursively for all children

     If false,

    only return immediate children

  

   Returns: Parts that are associated to the element

  GetAssociatedParts(hostDocument: Document,elementId: ElementId,includePartsWithAssociatedParts: bool,includeAllChildren: bool) -> ICollection[ElementId]

  

   Returns all Parts that are associated with the given element.

  

   hostDocument: The document of the element.

   elementId: The element to be checked for associated Parts.

   includePartsWithAssociatedParts: If true,include parts that have associated parts.

   includeAllChildren: If true,return all associated Parts recursively for all children.

     If 

    false,only return immediate children.

  

   Returns: Parts that are associated to the element.
  """
  pass
 @staticmethod
 def GetChainLengthToOriginal(part):
  """
  GetChainLengthToOriginal(part: Part) -> int

  

   Calculates the length of the longest chain of divisions/merges to reach to an 

    original non-Part element that is the source of the tested part.

  

  

   part: The part to be tested

   Returns: The length of the longest chain.
  """
  pass
 @staticmethod
 def GetMergedParts(part):
  """
  GetMergedParts(part: Part) -> ICollection[ElementId]

  

   Retrieves the element ids of the source elements of a merged part.

  

   part: A merged part.

   Returns: The element ids of the parts that were merged to create the specified merged 

    part.
  """
  pass
 @staticmethod
 def GetPartMakerMethodToDivideVolumeFW(partMaker):
  """
  GetPartMakerMethodToDivideVolumeFW(partMaker: PartMaker) -> PartMakerMethodToDivideVolumes

  

   Obtains the object allowing access to the divided volume

     properties of the 

    PartMaker.

  

  

   partMaker: The PartMaker.

   Returns: The object handle. Returns ll if the

     PartMaker does not represent divided 

    volumes.
  """
  pass
 @staticmethod
 def HasAssociatedParts(hostDocument,*__args):
  """
  HasAssociatedParts(hostDocument: Document,hostOrLinkElementId: LinkElementId) -> bool

  

   Checks if an element has associated parts.

  

   hostDocument: The document.

   hostOrLinkElementId: The element to be checked for associated Parts.

   Returns: True if the element has associated Parts.

  HasAssociatedParts(hostDocument: Document,elementId: ElementId) -> bool

  

   Checks if an element has associated parts.

  

   hostDocument: The document.

   elementId: The element to be checked for associated Parts

   Returns: True if the element has associated Parts.
  """
  pass
 @staticmethod
 def IsMergedPart(part):
  """
  IsMergedPart(part: Part) -> bool

  

   Is the Part the result of a merge.

   Returns: True if the Part is the result of a merge operation.
  """
  pass
 @staticmethod
 def IsPartDerivedFromLink(dPart):
  """
  IsPartDerivedFromLink(dPart: Part) -> bool

  

   Is the Part derived from link geometry.
  """
  pass
 @staticmethod
 def IsValidForCreateParts(document,hostOrLinkElementId):
  """
  IsValidForCreateParts(document: Document,hostOrLinkElementId: LinkElementId) -> bool

  

   Identifies if the given element can be used to create parts.

  

   document: The document.

   hostOrLinkElementId: Id to be tested for validity for creating part.

   Returns: True if this id is valid,false otherwise.
  """
  pass
 __all__=[
  'AreElementsValidForCreateParts',
  'ArePartsValidForDivide',
  'ArePartsValidForMerge',
  'CreateMergedPart',
  'CreateParts',
  'DivideParts',
  'FindMergeableClusters',
  'GetAssociatedPartMaker',
  'GetAssociatedParts',
  'GetChainLengthToOriginal',
  'GetMergedParts',
  'GetPartMakerMethodToDivideVolumeFW',
  'HasAssociatedParts',
  'IsMergedPart',
  'IsPartDerivedFromLink',
  'IsValidForCreateParts',
 ]

