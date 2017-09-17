class AdaptiveComponentFamilyUtils(object):
 """ An interface for Adaptive Component Instances. """
 @staticmethod
 def GetNumberOfAdaptivePoints(family):
  """
  GetNumberOfAdaptivePoints(family: Family) -> int
  
   Gets number of Adaptive Point Elements in Adaptive Component Family.
  
   family: The Family
   Returns: Number of Adaptive Point Element References in Adaptive Component Family.
  """
  pass
 @staticmethod
 def GetNumberOfPlacementPoints(family):
  """
  GetNumberOfPlacementPoints(family: Family) -> int
  
   Gets number of Placement Point Elements in Adaptive Component Family.
  
   family: The Family
   Returns: Number of Adaptive Placement Point Element References in Adaptive Component 
    Family.
  """
  pass
 @staticmethod
 def GetNumberOfShapeHandlePoints(family):
  """
  GetNumberOfShapeHandlePoints(family: Family) -> int
  
   Gets number of Shape Handle Point Elements in Adaptive Component Family.
  
   family: The Family
   Returns: Number of Adaptive Shape Handle Point Element References in the Adaptive 
    Component Family.
  """
  pass
 @staticmethod
 def GetPlacementNumber(doc,refPointId):
  """
  GetPlacementNumber(doc: Document,refPointId: ElementId) -> int
  
   Gets Placement number of an Adaptive Placement Point.
  
   doc: The Document
   refPointId: The ReferencePoint id
   Returns: Placement number of the Adaptive Placement Point.
  """
  pass
 @staticmethod
 def GetPointConstraintType(doc,refPointId):
  """
  GetPointConstraintType(doc: Document,refPointId: ElementId) -> AdaptivePointConstraintType
  
   Gets constrain type of an Adaptive Shape Handle Point.
  
   doc: The Document
   refPointId: The ReferencePoint id
   Returns: Constraint type of the Adaptive Shape Handle Point.
  """
  pass
 @staticmethod
 def GetPointOrientationType(doc,refPointId):
  """
  GetPointOrientationType(doc: Document,refPointId: ElementId) -> AdaptivePointOrientationType
  
   Gets orientation type of an Adaptive Placement Point.
  
   doc: The Document
   refPointId: The ReferencePoint id
   Returns: Orientation type of Adaptive Placement Point.
  """
  pass
 @staticmethod
 def IsAdaptiveComponentFamily(family):
  """
  IsAdaptiveComponentFamily(family: Family) -> bool
  
   Verifies if the Family is an Adaptive Component Family.
  
   family: The Family
   Returns: True if the Family is an Adaptive Component Family.
  """
  pass
 @staticmethod
 def IsAdaptivePlacementPoint(doc,refPointId):
  """
  IsAdaptivePlacementPoint(doc: Document,refPointId: ElementId) -> bool
  
   Verifies if the Reference Point is an Adaptive Placement Point.
  
   doc: The Document
   refPointId: The ReferencePoint id
   Returns: True if the Point is an Adaptive Placement Point.
  """
  pass
 @staticmethod
 def IsAdaptivePoint(doc,refPointId):
  """
  IsAdaptivePoint(doc: Document,refPointId: ElementId) -> bool
  
   Verifies if the Reference Point is an Adaptive Point.
  
   doc: The Document
   refPointId: The ReferencePoint id
   Returns: True if the Point is an Adaptive Point (Placement Point or Shape Handle Point).
  """
  pass
 @staticmethod
 def IsAdaptiveShapeHandlePoint(doc,refPointId):
  """
  IsAdaptiveShapeHandlePoint(doc: Document,refPointId: ElementId) -> bool
  
   Verifies if the Reference Point is an Adaptive Shape Handle Point.
  
   doc: The Document
   refPointId: The ReferencePoint id
   Returns: True if the Point is an Adaptive Shape Handle Point.
  """
  pass
 @staticmethod
 def MakeAdaptivePoint(doc,refPointId,type):
  """
  MakeAdaptivePoint(doc: Document,refPointId: ElementId,type: AdaptivePointType)
   Makes Reference Point an Adaptive Point or makes an Adaptive Point a Reference 
    Point.
  
  
   doc: The Document
   refPointId: The ReferencePoint id
   type: The Adaptive Point Type
  """
  pass
 @staticmethod
 def SetPlacementNumber(doc,refPointId,placementNumber):
  """
  SetPlacementNumber(doc: Document,refPointId: ElementId,placementNumber: int)
   Sets Placement Number of an Adaptive Placement Point.
  
   doc: The Document
   refPointId: The ReferencePoint id
   placementNumber: Placement number of the Adaptive Placement Point.
  """
  pass
 @staticmethod
 def SetPointConstraintType(doc,refPointId,constraintType):
  """
  SetPointConstraintType(doc: Document,refPointId: ElementId,constraintType: AdaptivePointConstraintType)
   Sets constrain type of an Adaptive Shape Handle Point.
  
   doc: The Document
   refPointId: The ReferencePoint id
   constraintType: Constraint type of the Adaptive Shape Handle Point.
  """
  pass
 @staticmethod
 def SetPointOrientationType(doc,refPointId,orientationType):
  """
  SetPointOrientationType(doc: Document,refPointId: ElementId,orientationType: AdaptivePointOrientationType)
   Sets orientation type of an Adaptive Placement Point.
  
   doc: The Document
   refPointId: The ReferencePoint id
   orientationType: Orientation type of the Adaptive Placement Point.
  """
  pass
 __all__=[
  'GetNumberOfAdaptivePoints',
  'GetNumberOfPlacementPoints',
  'GetNumberOfShapeHandlePoints',
  'GetPlacementNumber',
  'GetPointConstraintType',
  'GetPointOrientationType',
  'IsAdaptiveComponentFamily',
  'IsAdaptivePlacementPoint',
  'IsAdaptivePoint',
  'IsAdaptiveShapeHandlePoint',
  'MakeAdaptivePoint',
  'SetPlacementNumber',
  'SetPointConstraintType',
  'SetPointOrientationType',
 ]

