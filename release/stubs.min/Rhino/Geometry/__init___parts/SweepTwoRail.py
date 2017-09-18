class SweepTwoRail(object):
 """
 Utility class for generating breps by sweeping cross section curves over

    two rail curves.

 

 SweepTwoRail()
 """
 def PerformSweep(self,rail1,rail2,*__args):
  """
  PerformSweep(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSections: IEnumerable[Curve]) -> Array[Brep]

  PerformSweep(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSections: IEnumerable[Curve],crossSectionParameters1: IEnumerable[float],crossSectionParameters2: IEnumerable[float]) -> Array[Brep]

  PerformSweep(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSection: Curve) -> Array[Brep]

  PerformSweep(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSection: Curve,crossSectionParameterRail1: float,crossSectionParameterRail2: float) -> Array[Brep]
  """
  pass
 def PerformSweepRebuild(self,rail1,rail2,*__args):
  """
  PerformSweepRebuild(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSections: IEnumerable[Curve],rebuildCount: int) -> Array[Brep]

  PerformSweepRebuild(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSections: IEnumerable[Curve],crossSectionParametersRail1: IEnumerable[float],crossSectionParametersRail2: IEnumerable[float],rebuildCount: int) -> Array[Brep]

  PerformSweepRebuild(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSection: Curve,rebuildCount: int) -> Array[Brep]

  PerformSweepRebuild(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSection: Curve,crossSectionParameterRail1: float,crossSectionParameterRail2: float,rebuildCount: int) -> Array[Brep]
  """
  pass
 def PerformSweepRefit(self,rail1,rail2,*__args):
  """
  PerformSweepRefit(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSections: IEnumerable[Curve],refitTolerance: float) -> Array[Brep]

  PerformSweepRefit(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSections: IEnumerable[Curve],crossSectionParametersRail1: IEnumerable[float],crossSectionParametersRail2: IEnumerable[float],refitTolerance: float) -> Array[Brep]

  PerformSweepRefit(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSection: Curve,refitTolerance: float) -> Array[Brep]

  PerformSweepRefit(self: SweepTwoRail,rail1: Curve,rail2: Curve,crossSection: Curve,crossSectionParameterRail1: float,crossSectionParameterRail2: float,refitTolerance: float) -> Array[Brep]
  """
  pass
 AngleToleranceRadians=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AngleToleranceRadians(self: SweepTwoRail) -> float



Set: AngleToleranceRadians(self: SweepTwoRail)=value

"""

 ClosedSweep=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If the input rails are closed,ClosedSweep determines if the swept breps

   will also be closed.



Get: ClosedSweep(self: SweepTwoRail) -> bool



Set: ClosedSweep(self: SweepTwoRail)=value

"""

 MaintainHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaintainHeight(self: SweepTwoRail) -> bool



Set: MaintainHeight(self: SweepTwoRail)=value

"""

 SweepTolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SweepTolerance(self: SweepTwoRail) -> float



Set: SweepTolerance(self: SweepTwoRail)=value

"""


