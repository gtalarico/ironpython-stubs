class SweepOneRail(object):
 """
 Utility class for generating breps by sweeping cross section curves over

    a single rail curve.

 

 SweepOneRail()
 """
 def PerformSweep(self,rail,*__args):
  """
  PerformSweep(self: SweepOneRail,rail: Curve,crossSections: IEnumerable[Curve]) -> Array[Brep]

  PerformSweep(self: SweepOneRail,rail: Curve,crossSections: IEnumerable[Curve],crossSectionParameters: IEnumerable[float]) -> Array[Brep]

  PerformSweep(self: SweepOneRail,rail: Curve,crossSection: Curve) -> Array[Brep]

  PerformSweep(self: SweepOneRail,rail: Curve,crossSection: Curve,crossSectionParameter: float) -> Array[Brep]
  """
  pass
 def PerformSweepRebuild(self,rail,*__args):
  """
  PerformSweepRebuild(self: SweepOneRail,rail: Curve,crossSections: IEnumerable[Curve],rebuildCount: int) -> Array[Brep]

  PerformSweepRebuild(self: SweepOneRail,rail: Curve,crossSections: IEnumerable[Curve],crossSectionParameters: IEnumerable[float],rebuildCount: int) -> Array[Brep]

  PerformSweepRebuild(self: SweepOneRail,rail: Curve,crossSection: Curve,rebuildCount: int) -> Array[Brep]

  PerformSweepRebuild(self: SweepOneRail,rail: Curve,crossSection: Curve,crossSectionParameter: float,rebuildCount: int) -> Array[Brep]
  """
  pass
 def PerformSweepRefit(self,rail,*__args):
  """
  PerformSweepRefit(self: SweepOneRail,rail: Curve,crossSections: IEnumerable[Curve],refitTolerance: float) -> Array[Brep]

  PerformSweepRefit(self: SweepOneRail,rail: Curve,crossSections: IEnumerable[Curve],crossSectionParameters: IEnumerable[float],refitTolerance: float) -> Array[Brep]

  PerformSweepRefit(self: SweepOneRail,rail: Curve,crossSection: Curve,refitTolerance: float) -> Array[Brep]

  PerformSweepRefit(self: SweepOneRail,rail: Curve,crossSection: Curve,crossSectionParameter: float,refitTolerance: float) -> Array[Brep]
  """
  pass
 def SetRoadlikeUpDirection(self,up):
  """ SetRoadlikeUpDirection(self: SweepOneRail,up: Vector3d) """
  pass
 def SetToRoadlikeFront(self):
  """ SetToRoadlikeFront(self: SweepOneRail) """
  pass
 def SetToRoadlikeRight(self):
  """ SetToRoadlikeRight(self: SweepOneRail) """
  pass
 def SetToRoadlikeTop(self):
  """ SetToRoadlikeTop(self: SweepOneRail) """
  pass
 AngleToleranceRadians=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AngleToleranceRadians(self: SweepOneRail) -> float



Set: AngleToleranceRadians(self: SweepOneRail)=value

"""

 ClosedSweep=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If the input rail is closed,ClosedSweep determines if the swept breps will also

   be closed.



Get: ClosedSweep(self: SweepOneRail) -> bool



Set: ClosedSweep(self: SweepOneRail)=value

"""

 GlobalShapeBlending=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true,the sweep is linearly blended from one end to the other,

   creating sweeps that taper from one cross-section curve to the other.

   If false,the sweep stays constant at the ends and changes more

   rapidly in the middle.



Get: GlobalShapeBlending(self: SweepOneRail) -> bool



Set: GlobalShapeBlending(self: SweepOneRail)=value

"""

 IsFreeform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsFreeform(self: SweepOneRail) -> bool



"""

 IsRoadlike=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsRoadlike(self: SweepOneRail) -> bool



"""

 IsRoadlikeFront=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsRoadlikeFront(self: SweepOneRail) -> bool



"""

 IsRoadlikeTop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsRoadlikeTop(self: SweepOneRail) -> bool



"""

 IsRoadlineRight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsRoadlineRight(self: SweepOneRail) -> bool



"""

 MiterType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """0: don't miter, 1: intersect surfaces and trim sweeps, 2: rotate shapes at kinks and don't trim.



Get: MiterType(self: SweepOneRail) -> int



Set: MiterType(self: SweepOneRail)=value

"""

 SweepTolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SweepTolerance(self: SweepOneRail) -> float



Set: SweepTolerance(self: SweepOneRail)=value

"""


