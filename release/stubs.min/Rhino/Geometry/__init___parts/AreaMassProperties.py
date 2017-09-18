class AreaMassProperties(object,IDisposable):
 """
 Contains static initialization methods and allows access to the computed

    metrics of area,area centroid and area moments in closed

    planar curves,in meshes,in surfaces,in hatches and in boundary representations.
 """
 @staticmethod
 def Compute(*__args):
  """
  Compute(brep: Brep) -> AreaMassProperties

  

   Computes an AreaMassProperties for a brep.

  

   brep: Brep to measure.

   Returns: The AreaMassProperties for the given Brep or null on failure.

  Compute(surface: Surface) -> AreaMassProperties

  

   Computes an AreaMassProperties for a surface.

  

   surface: Surface to measure.

   Returns: The AreaMassProperties for the given Surface or null on failure.

  Compute(geometry: IEnumerable[GeometryBase]) -> AreaMassProperties

  Compute(mesh: Mesh) -> AreaMassProperties

  

   Computes an AreaMassProperties for a mesh.

  

   mesh: Mesh to measure.

   Returns: The AreaMassProperties for the given Mesh or null on failure.

  Compute(closedPlanarCurve: Curve) -> AreaMassProperties

  

   Computes an AreaMassProperties for a closed planar curve.

  

   closedPlanarCurve: Curve to measure.

   Returns: The AreaMassProperties for the given curve or null on failure.

  Compute(closedPlanarCurve: Curve,planarTolerance: float) -> AreaMassProperties

  

   Computes an AreaMassProperties for a closed planar curve.

  

   closedPlanarCurve: Curve to measure.

   planarTolerance: absolute tolerance used to insure the closed curve is planar

   Returns: The AreaMassProperties for the given curve or null on failure.

  Compute(hatch: Hatch) -> AreaMassProperties

  

   Computes an AreaMassProperties for a hatch.

  

   hatch: Hatch to measure.

   Returns: The AreaMassProperties for the given hatch or null on failure.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: AreaMassProperties)

   Actively reclaims unmanaged resources that this instance uses.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Area=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the area solution.



Get: Area(self: AreaMassProperties) -> float



"""

 AreaError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the uncertainty in the area calculation.



Get: AreaError(self: AreaMassProperties) -> float



"""

 Centroid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the area centroid in the world coordinate system.



Get: Centroid(self: AreaMassProperties) -> Point3d



"""

 CentroidCoordinatesMomentsOfInertia=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Moments of inertia with respect to centroid coordinate system.

   X=integral of ((y-y0)^2 + (z-z0)^2) dm

   Y=integral of ((z-z0)^2 + (x-x0)^2) dm

   Z=integral of ((z-z0)^2 + (y-y0)^2) dm

   where (x0,y0,z0)=centroid.



Get: CentroidCoordinatesMomentsOfInertia(self: AreaMassProperties) -> Vector3d



"""

 CentroidCoordinatesMomentsOfInertiaError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in centroid coordinates moments of inertia calculation.



Get: CentroidCoordinatesMomentsOfInertiaError(self: AreaMassProperties) -> Vector3d



"""

 CentroidCoordinatesRadiiOfGyration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Radii of gyration with respect to centroid coordinate system.

   X=sqrt(integral of ((y-y0)^2 + (z-z0)^2) dm/M)

   Y=sqrt(integral of ((z-z0)^2 + (x-x0)^2) dm/M)

   Z=sqrt(integral of ((z-z0)^2 + (y-y0)^2) dm/M)

   where (x0,y0,z0)=centroid.



Get: CentroidCoordinatesRadiiOfGyration(self: AreaMassProperties) -> Vector3d



"""

 CentroidCoordinatesSecondMoments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Second moments with respect to centroid coordinate system.

   X=integral of (x-x0)^2 dm

   Y=integral of (y-y0)^2 dm

   Z=integral of (z-z0)^2 dm

   where (x0,y0,z0)=centroid.



Get: CentroidCoordinatesSecondMoments(self: AreaMassProperties) -> Vector3d



"""

 CentroidCoordinatesSecondMomentsError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in centroid coordinates second moments calculation.



Get: CentroidCoordinatesSecondMomentsError(self: AreaMassProperties) -> Vector3d



"""

 CentroidError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the uncertainty in the centroid calculation.



Get: CentroidError(self: AreaMassProperties) -> Vector3d



"""

 WorldCoordinatesFirstMoments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the world coordinate first moments if they were able to be calculated.

   X is integral of "x dm" over the area

   Y is integral of "y dm" over the area

   Z is integral of "z dm" over the area.



Get: WorldCoordinatesFirstMoments(self: AreaMassProperties) -> Vector3d



"""

 WorldCoordinatesFirstMomentsError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in world coordinates first moments calculation.



Get: WorldCoordinatesFirstMomentsError(self: AreaMassProperties) -> Vector3d



"""

 WorldCoordinatesMomentsOfInertia=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The moments of inertia about the world coordinate axes.

   X=integral of (y^2 + z^2) dm

   Y=integral of (z^2 + x^2) dm

   Z=integral of (z^2 + y^2) dm.



Get: WorldCoordinatesMomentsOfInertia(self: AreaMassProperties) -> Vector3d



"""

 WorldCoordinatesMomentsOfInertiaError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in world coordinates moments of inertia calculation.



Get: WorldCoordinatesMomentsOfInertiaError(self: AreaMassProperties) -> Vector3d



"""

 WorldCoordinatesProductMoments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the world coordinate product moments if they were able to be calculated.

   X is integral of "xy dm" over the area

   Y is integral of "yz dm" over the area

   Z is integral of "zx dm" over the area.



Get: WorldCoordinatesProductMoments(self: AreaMassProperties) -> Vector3d



"""

 WorldCoordinatesProductMomentsError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in world coordinates second moments calculation.



Get: WorldCoordinatesProductMomentsError(self: AreaMassProperties) -> Vector3d



"""

 WorldCoordinatesRadiiOfGyration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Radii of gyration with respect to world coordinate system.

   X=sqrt(integral of (y^2 + z^2) dm/M)

   Y=sqrt(integral of (z^2 + x^2) dm/M)

   Z=sqrt(integral of (z^2 + y^2) dm/M)



Get: WorldCoordinatesRadiiOfGyration(self: AreaMassProperties) -> Vector3d



"""

 WorldCoordinatesSecondMoments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the world coordinate first moments if they were able to be calculated.

   X is integral of "xx dm" over the area

   Y is integral of "yy dm" over the area

   Z is integral of "zz dm" over the area.



Get: WorldCoordinatesSecondMoments(self: AreaMassProperties) -> Vector3d



"""

 WorldCoordinatesSecondMomentsError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in world coordinates second moments calculation.



Get: WorldCoordinatesSecondMomentsError(self: AreaMassProperties) -> Vector3d



"""


