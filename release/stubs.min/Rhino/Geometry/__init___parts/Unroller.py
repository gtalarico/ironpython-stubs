class Unroller(object):
 """
 Represents the operation of unrolling a single surface.

 

 Unroller(surface: Surface)

 Unroller(brep: Brep)
 """
 def AddFollowingGeometry(self,*__args):
  """
  AddFollowingGeometry(self: Unroller,dot: TextDot)

   Adds a text dot that should be unrolled along with the surface/brep.

  

   dot: A text dot.

  AddFollowingGeometry(self: Unroller,dots: IEnumerable[TextDot])AddFollowingGeometry(self: Unroller,dotLocation: Point3d,dotText: str)

   Adds a text dot that should be unrolled along with the surface/brep.

  

   dotLocation: A dot point.

   dotText: A dot text.

  AddFollowingGeometry(self: Unroller,dotLocations: IEnumerable[Point3d],dotText: IEnumerable[str])AddFollowingGeometry(self: Unroller,point: Point)

   Adds a point that should be unrolled along with the surface/brep.

  

   point: A point.

  AddFollowingGeometry(self: Unroller,curve: Curve)

   Adds a curve that should be unrolled along with the surface/brep.

  

   curve: The curve.

  AddFollowingGeometry(self: Unroller,curves: IEnumerable[Curve])AddFollowingGeometry(self: Unroller,point: Point3d)

   Adds a point that should be unrolled along with the surface/brep.

  

   point: A point.

  AddFollowingGeometry(self: Unroller,points: IEnumerable[Point3d])
  """
  pass
 def PerformUnroll(self,unrolledCurves,unrolledPoints,unrolledDots):
  """
  PerformUnroll(self: Unroller) -> (Array[Brep],Array[Curve],Array[Point3d],Array[TextDot])

  

   Executes unrolling operations.

   Returns: An array of breps. This array can be empty.
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,surface: Surface)

  __new__(cls: type,brep: Brep)
  """
  pass
 AbsoluteTolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the absolute tolerance for the unrolling operation.

   Absolute tolerance is used in the evaluation of new entities,

   such as intersections,reprojections and splits.In the current implementation,absolute tolerance is used 

   in tessellating rails,fitting curves and pulling back trims.



Get: AbsoluteTolerance(self: Unroller) -> float



Set: AbsoluteTolerance(self: Unroller)=value

"""

 ExplodeOutput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value determining whether geometry should be exploded.



Get: ExplodeOutput(self: Unroller) -> bool



Set: ExplodeOutput(self: Unroller)=value

"""

 ExplodeSpacing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value determining whether spacing should be exploded.



Get: ExplodeSpacing(self: Unroller) -> float



Set: ExplodeSpacing(self: Unroller)=value

"""

 RelativeTolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the relative tolerance for the unrolling operation.

   Relative tolerance is used in the evaluation of intrinsic properties,

   such as computations "along" the surface or brep.In the current implementation,relative tolerance is used to decide

   if a surface is flat enough to try to unroll. That helps ease the scale dependency.

   The surface has to be linear in one direction within (length * RelativeTolerance)

   to be considered linear for that purpose. Otherwise smash will ignore that tolerance and

   unroll anything.



Get: RelativeTolerance(self: Unroller) -> float



Set: RelativeTolerance(self: Unroller)=value

"""


