class VolumeMassProperties(object,IDisposable):
 """
 Contains static initialization methods and allows access to the computed

    metrics of volume,volume centroid and volume moments in 

    in solid meshes,in solid surfaces and in solid (closed) boundary representations.
 """
 @staticmethod
 def Compute(*__args):
  """
  Compute(surface: Surface) -> VolumeMassProperties

  

   Compute the VolumeMassProperties for a single Surface.

  

   surface: Surface to measure.

   Returns: The VolumeMassProperties for the given Surface or null on failure.

  Compute(brep: Brep) -> VolumeMassProperties

  

   Compute the VolumeMassProperties for a single Brep.

  

   brep: Brep to measure.

   Returns: The VolumeMassProperties for the given Brep or null on failure.

  Compute(mesh: Mesh) -> VolumeMassProperties

  

   Compute the VolumeMassProperties for a single Mesh.

  

   mesh: Mesh to measure.

   Returns: The VolumeMassProperties for the given Mesh or null on failure.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: VolumeMassProperties)

   Actively reclaims unmanaged resources that this instance uses.
  """
  pass
 def Sum(self,summand):
  """
  Sum(self: VolumeMassProperties,summand: VolumeMassProperties) -> bool

  

   Sum mass properties together to get an aggregate mass.

  

   summand: mass properties to add.

   Returns: true if successful.
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
 Centroid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the volume centroid in the world coordinate system.



Get: Centroid(self: VolumeMassProperties) -> Point3d



"""

 CentroidCoordinatesMomentsOfInertia=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Moments of inertia with respect to centroid coordinate system.

   X=integral of ((y-y0)^2 + (z-z0)^2) dm

   Y=integral of ((z-z0)^2 + (x-x0)^2) dm

   Z=integral of ((z-z0)^2 + (y-y0)^2) dm

   where (x0,y0,z0)=centroid.



Get: CentroidCoordinatesMomentsOfInertia(self: VolumeMassProperties) -> Vector3d



"""

 CentroidCoordinatesMomentsOfInertiaError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in centroid coordinates moments of inertia calculation.



Get: CentroidCoordinatesMomentsOfInertiaError(self: VolumeMassProperties) -> Vector3d



"""

 CentroidCoordinatesRadiiOfGyration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Radii of gyration with respect to centroid coordinate system.

   X=sqrt(integral of ((y-y0)^2 + (z-z0)^2) dm/M)

   Y=sqrt(integral of ((z-z0)^2 + (x-x0)^2) dm/M)

   Z=sqrt(integral of ((z-z0)^2 + (y-y0)^2) dm/M)

   where (x0,y0,z0)=centroid.



Get: CentroidCoordinatesRadiiOfGyration(self: VolumeMassProperties) -> Vector3d



"""

 CentroidCoordinatesSecondMoments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Second moments with respect to centroid coordinate system.

   X=integral of (x-x0)^2 dm

   Y=integral of (y-y0)^2 dm

   Z=integral of (z-z0)^2 dm

   where (x0,y0,z0)=centroid.



Get: CentroidCoordinatesSecondMoments(self: VolumeMassProperties) -> Vector3d



"""

 CentroidCoordinatesSecondMomentsError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in centroid coordinates second moments calculation.



Get: CentroidCoordinatesSecondMomentsError(self: VolumeMassProperties) -> Vector3d



"""

 CentroidError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the uncertainty in the Centroid calculation.



Get: CentroidError(self: VolumeMassProperties) -> Vector3d



"""

 Volume=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the volume solution.



Get: Volume(self: VolumeMassProperties) -> float



"""

 VolumeError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the uncertainty in the volume calculation.



Get: VolumeError(self: VolumeMassProperties) -> float



"""

 WorldCoordinatesFirstMoments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the world coordinate first moments if they were able to be calculated.

   X is integral of "x dm" over the volume

   Y is integral of "y dm" over the volume

   Z is integral of "z dm" over the volume.



Get: WorldCoordinatesFirstMoments(self: VolumeMassProperties) -> Vector3d



"""

 WorldCoordinatesFirstMomentsError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in world coordinates first moments calculation.



Get: WorldCoordinatesFirstMomentsError(self: VolumeMassProperties) -> Vector3d



"""

 WorldCoordinatesMomentsOfInertia=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The moments of inertia about the world coordinate axes.

   X=integral of (y^2 + z^2) dm

   Y=integral of (z^2 + x^2) dm

   Z=integral of (z^2 + y^2) dm.



Get: WorldCoordinatesMomentsOfInertia(self: VolumeMassProperties) -> Vector3d



"""

 WorldCoordinatesMomentsOfInertiaError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in world coordinates moments of inertia calculation.



Get: WorldCoordinatesMomentsOfInertiaError(self: VolumeMassProperties) -> Vector3d



"""

 WorldCoordinatesProductMoments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the world coordinate product moments if they were able to be calculated.

   X is integral of "xy dm" over the area

   Y is integral of "yz dm" over the area

   Z is integral of "zx dm" over the area.



Get: WorldCoordinatesProductMoments(self: VolumeMassProperties) -> Vector3d



"""

 WorldCoordinatesProductMomentsError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in world coordinates second moments calculation.



Get: WorldCoordinatesProductMomentsError(self: VolumeMassProperties) -> Vector3d



"""

 WorldCoordinatesRadiiOfGyration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Radii of gyration with respect to world coordinate system.

   X=sqrt(integral of (y^2 + z^2) dm/M)

   Y=sqrt(integral of (z^2 + x^2) dm/M)

   Z=sqrt(integral of (z^2 + y^2) dm/M)



Get: WorldCoordinatesRadiiOfGyration(self: VolumeMassProperties) -> Vector3d



"""

 WorldCoordinatesSecondMoments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the world coordinate first moments if they were able to be calculated.

   X is integral of "xx dm" over the area

   Y is integral of "yy dm" over the area

   Z is integral of "zz dm" over the area.



Get: WorldCoordinatesSecondMoments(self: VolumeMassProperties) -> Vector3d



"""

 WorldCoordinatesSecondMomentsError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Uncertainty in world coordinates second moments calculation.



Get: WorldCoordinatesSecondMomentsError(self: VolumeMassProperties) -> Vector3d



"""



# variables with complex values

