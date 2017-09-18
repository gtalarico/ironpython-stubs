class PartMakerMethodToDivideVolumes(object,IDisposable):
 """ By-References dividing strategy used by PartMaker element. """
 def AddIntersectingReference(self,intersectingReference,offset):
  """
  AddIntersectingReference(self: PartMakerMethodToDivideVolumes,intersectingReference: ElementId,offset: float) -> bool

  

   Adds intersecting reference with an offset.

  

   intersectingReference: Id of the new intersecting reference.

   offset: The Offste for the new intersecting reference.

   Returns: True if the PartMaker did not already use this

     intersecting reference and 

    it was added,false if the PartMaker

     already used this intersecting 

    reference and this call

     only updated its offset.
  """
  pass
 @staticmethod
 def AreElementsValidIntersectingReferences(*__args):
  """
  AreElementsValidIntersectingReferences(self: PartMakerMethodToDivideVolumes,elementIds: ICollection[ElementId]) -> bool

  AreElementsValidIntersectingReferences(document: Document,elementIds: ICollection[ElementId]) -> bool
  """
  pass
 def CanBeDivisionProfile(self,familyId,familyDocument=None):
  """
  CanBeDivisionProfile(familyId: ElementId,familyDocument: Document) -> bool

  

   Checks whether a family defines a profile which can be used by this method.

  

   familyId: Element id of the family.

   familyDocument: The document containing the family to be tested.

   Returns: True if the family defines a profile which can be used by a part maker,

     

    false otherwise.

  

  CanBeDivisionProfile(self: PartMakerMethodToDivideVolumes,familyId: ElementId) -> bool

  

   Checks whether a family defines a profile which can be used by this method.

  

   familyId: Element id of the family.

   Returns: True if the family defines a profile which can be used by a part maker,

     

    false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: PartMakerMethodToDivideVolumes) """
  pass
 def GetOffsetForIntersectingReference(self,intersectingReference):
  """
  GetOffsetForIntersectingReference(self: PartMakerMethodToDivideVolumes,intersectingReference: ElementId) -> float

  

   Gets offset for the intersecting reference.

  

   intersectingReference: The intersecting reference to obtain offset value from.

   Returns: The offset for the intersecting reference
  """
  pass
 def GetPlaneOfSketch(self):
  """
  GetPlaneOfSketch(self: PartMakerMethodToDivideVolumes) -> Plane

  

   Gets the plane of the sketch.

   Returns: The plane of the sketch.
  """
  pass
 def GetSketchCurves(self,curveArray):
  """ GetSketchCurves(self: PartMakerMethodToDivideVolumes) -> IList[Curve] """
  pass
 def GetSplitRefsOffsets(self):
  """
  GetSplitRefsOffsets(self: PartMakerMethodToDivideVolumes) -> IDictionary[ElementId,float]

  

   Returns offsets for plane-defining splitters.
  """
  pass
 @staticmethod
 def IsElementValidIntersectingReference(*__args):
  """
  IsElementValidIntersectingReference(self: PartMakerMethodToDivideVolumes,elementId: ElementId) -> bool

  

   Identifies if the provided member is valid.

  

   elementId: Element ids to be tested for validity for intersecting references.

   Returns: True if the reference is valid,false otherwise.

  IsElementValidIntersectingReference(document: Document,elementId: ElementId) -> bool

  

   Identifies if the provided member is valid.

  

   document: The document.

   elementId: Element ids to be tested for validity for intersecting references.

   Returns: True if the reference is valid,false otherwise.
  """
  pass
 @staticmethod
 def IsValidSketchPlane(document,sketchPlaneId):
  """
  IsValidSketchPlane(document: Document,sketchPlaneId: ElementId) -> bool

  

   Identifies if provided sketch plane is valid.

  

   document: The document.

   sketchPlaneId: SketchPlane ids to be tested for validity for PartMaker.

   Returns: True if SketchPlane valid,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: PartMakerMethodToDivideVolumes,disposing: bool) """
  pass
 def RemoveIntersectingReference(self,intersectingReference):
  """
  RemoveIntersectingReference(self: PartMakerMethodToDivideVolumes,intersectingReference: ElementId) -> bool

  

   Removed intersecting reference.

  

   intersectingReference: Id of the intersecting reference to remove.

   Returns: True if the PartMaker used this intersecting reference and

     this call 

    removed it,false if the PartMaker did not use this

     intersecting reference.
  """
  pass
 def SetOffsetForIntersectingReference(self,intersectingReference,offset):
  """
  SetOffsetForIntersectingReference(self: PartMakerMethodToDivideVolumes,intersectingReference: ElementId,offset: float)

   Sets offset for the intersecting reference.

  

   intersectingReference: The intersecting reference that will be offset.

   offset: The new offset.
  """
  pass
 def UsesReference(self,intersectingReference):
  """
  UsesReference(self: PartMakerMethodToDivideVolumes,intersectingReference: ElementId) -> bool

  

   Identifies if the PartMaker uses the intersecting reference.

  

   intersectingReference: Intersecting reference to be tested.

   Returns: True if the intersecting reference is used by the PartMaker.
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
 DivisionGap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The gap which is created between matching profiles of parts.



Get: DivisionGap(self: PartMakerMethodToDivideVolumes) -> float



Set: DivisionGap(self: PartMakerMethodToDivideVolumes)=value

"""

 DivisionPatternMirror=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether pattern defined by the division rule should be mirrored before application

   Mirroring is similar to changing indices of u-const gridlines.



Get: DivisionPatternMirror(self: PartMakerMethodToDivideVolumes) -> bool



Set: DivisionPatternMirror(self: PartMakerMethodToDivideVolumes)=value

"""

 DivisionRotationAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Angle by which both u- and v- gridlines of the division are rotated with respect

   to the natural u/v-const directions of the sketch plane.



Get: DivisionRotationAngle(self: PartMakerMethodToDivideVolumes) -> float



Set: DivisionRotationAngle(self: PartMakerMethodToDivideVolumes)=value

"""

 DivisionRuleId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the 'DivisionRule' which is used to augment the cutting sketch.



Get: DivisionRuleId(self: PartMakerMethodToDivideVolumes) -> ElementId



Set: DivisionRuleId(self: PartMakerMethodToDivideVolumes)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: PartMakerMethodToDivideVolumes) -> bool



"""

 ProfileFlipAcross=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the corresponding left/upper parts profile are mirrored with respect

   to the division line. False if the profile of left/upper parts are defined

   directly by the profile family.



Get: ProfileFlipAcross(self: PartMakerMethodToDivideVolumes) -> bool



Set: ProfileFlipAcross(self: PartMakerMethodToDivideVolumes)=value

"""

 ProfileFlipAlong=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the corresponding left/upper parts profile are mirrored with respect

   to the center line of the hosts to be divided. False if the profile of

   left/upper parts are defined directly by the profile family.



Get: ProfileFlipAlong(self: PartMakerMethodToDivideVolumes) -> bool



Set: ProfileFlipAlong(self: PartMakerMethodToDivideVolumes)=value

"""

 ProfileMatch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines how two profiles match.



Get: ProfileMatch(self: PartMakerMethodToDivideVolumes) -> PartEdgeConditionOrientation



Set: ProfileMatch(self: PartMakerMethodToDivideVolumes)=value

"""

 ProfileOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset which is applied to a family-defined profile in the

   direction away from the division line and toward left/upper part

   to obtain its profile.



Get: ProfileOffset(self: PartMakerMethodToDivideVolumes) -> float



Set: ProfileOffset(self: PartMakerMethodToDivideVolumes)=value

"""

 ProfileType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the profile family applied to boundaries between parts.



Get: ProfileType(self: PartMakerMethodToDivideVolumes) -> ElementId



Set: ProfileType(self: PartMakerMethodToDivideVolumes)=value

"""

 UConstDivisionIndent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indentation for the application of division rule's pattern across u-const gridlines

   (i.e.,similar to changing indices of u-const gridlines).



Get: UConstDivisionIndent(self: PartMakerMethodToDivideVolumes) -> int



Set: UConstDivisionIndent(self: PartMakerMethodToDivideVolumes)=value

"""

 VConstDivisionIndent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indentation for the application of division rule's pattern across v-const gridlines

   (i.e.,similar to changing indices of v-const gridlines).



Get: VConstDivisionIndent(self: PartMakerMethodToDivideVolumes) -> int



Set: VConstDivisionIndent(self: PartMakerMethodToDivideVolumes)=value

"""


