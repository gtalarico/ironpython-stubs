class TessellatedBuildIssueType(Enum,IComparable,IFormattable,IConvertible):
 """
 Issues,which can be encountered while building a polymesh,
    or a shell,or a solid from data,describing
    tessellated shapes.
 
 enum TessellatedBuildIssueType,values: AllFine (0),DegenOriginalLoop (18),EdgeTraversalForFlip (24),EdgeTwiceUsedByFace (20),EmptyFace (1),EmptyLoop (2),FaceWithIslands (15),InconsistentInnerOuterOriginalLoopCCW (19),InconsitentMultiEdgeTraversalForFlip (25),InternalError (28),InternalLightError (29),InternalMissingError (30),InternalUtilityError (27),IntersectingOriginalLoops (14),LoopOnBestFitSelfIntersects (13),LostAllLoops (9),LostTooManyLoopVertices (6),NonManifoldEdge (21),NonPlanarFace (10),NotSetYet (32),NumberOfIssueTypes (33),OriginalLoopGeomAcuteAngle (7),OriginalLoopMeshAcuteAngle (8),OriginalLoopsProximity (16),OriginalPointsTooFarFromTheirPlane (11),OuterLoopIsNotFirst (17),OverlappingAdjacentFaces (22),PartitionPointsTooFarFromTrueEdge (23),TooFewOriginalVertices (3),TooShortOriginalLoopGeomSegment (5),TooShortOriginalLoopMeshSegment (4),TooSmallVertexSegementDistInFinalLoop (26),TooSmallVertexSegementDistInOriginalLoop (12),UnarticulatedNonManifoldEdge (31)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 AllFine=None
 DegenOriginalLoop=None
 EdgeTraversalForFlip=None
 EdgeTwiceUsedByFace=None
 EmptyFace=None
 EmptyLoop=None
 FaceWithIslands=None
 InconsistentInnerOuterOriginalLoopCCW=None
 InconsitentMultiEdgeTraversalForFlip=None
 InternalError=None
 InternalLightError=None
 InternalMissingError=None
 InternalUtilityError=None
 IntersectingOriginalLoops=None
 LoopOnBestFitSelfIntersects=None
 LostAllLoops=None
 LostTooManyLoopVertices=None
 NonManifoldEdge=None
 NonPlanarFace=None
 NotSetYet=None
 NumberOfIssueTypes=None
 OriginalLoopGeomAcuteAngle=None
 OriginalLoopMeshAcuteAngle=None
 OriginalLoopsProximity=None
 OriginalPointsTooFarFromTheirPlane=None
 OuterLoopIsNotFirst=None
 OverlappingAdjacentFaces=None
 PartitionPointsTooFarFromTrueEdge=None
 TooFewOriginalVertices=None
 TooShortOriginalLoopGeomSegment=None
 TooShortOriginalLoopMeshSegment=None
 TooSmallVertexSegementDistInFinalLoop=None
 TooSmallVertexSegementDistInOriginalLoop=None
 UnarticulatedNonManifoldEdge=None
 value__=None

