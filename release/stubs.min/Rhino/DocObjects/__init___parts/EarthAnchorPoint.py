class EarthAnchorPoint(object,IDisposable):
 """
 Contains information about the model's position in latitude,longitude,

    and elevation for GIS mapping applications.

 

 EarthAnchorPoint()
 """
 def Dispose(self):
  """
  Dispose(self: EarthAnchorPoint)

   Actively reclaims unmanaged resources that this instance uses.
  """
  pass
 def GetModelCompass(self):
  """
  GetModelCompass(self: EarthAnchorPoint) -> Plane

  

   Returns a plane in model coordinates whose X axis points East,

     Y axis points North 

    and Z axis points Up. The origin

     is set to ModelBasepoint.

  

   Returns: A plane value. This might be invalid on error.
  """
  pass
 def GetModelToEarthTransform(self,modelUnitSystem):
  """
  GetModelToEarthTransform(self: EarthAnchorPoint,modelUnitSystem: UnitSystem) -> Transform

  

   Gets a transformation from model coordinates to earth coordinates.

     This 

    transformation assumes the model is small enough that

     the curvature of the earth 

    can be ignored.

  

  

   modelUnitSystem: The model unit system.

   Returns: Transform on success. Inalid Transform on error.
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
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the long form of the identifying information about this location.



Get: Description(self: EarthAnchorPoint) -> str



Set: Description(self: EarthAnchorPoint)=value

"""

 EarthBasepointElevation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the point elevation on earth,in meters.



Get: EarthBasepointElevation(self: EarthAnchorPoint) -> float



Set: EarthBasepointElevation(self: EarthAnchorPoint)=value

"""

 EarthBasepointElevationZero=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the zero level convention relating to a location on Earth.



Get: EarthBasepointElevationZero(self: EarthAnchorPoint) -> BasepointZero



Set: EarthBasepointElevationZero(self: EarthAnchorPoint)=value

"""

 EarthBasepointLatitude=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a point latitude on earth,in decimal degrees.

   +90=north pole,0=equator,-90=south pole.



Get: EarthBasepointLatitude(self: EarthAnchorPoint) -> float



Set: EarthBasepointLatitude(self: EarthAnchorPoint)=value

"""

 EarthBasepointLongitude=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the point longitude on earth,in decimal degrees.

   0=prime meridian (Greenwich meridian)Values increase towards West



Get: EarthBasepointLongitude(self: EarthAnchorPoint) -> float



Set: EarthBasepointLongitude(self: EarthAnchorPoint)=value

"""

 ModelBasePoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Corresponding model point in model coordinates.



Get: ModelBasePoint(self: EarthAnchorPoint) -> Point3d



Set: ModelBasePoint(self: EarthAnchorPoint)=value

"""

 ModelEast=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Earth directions in model coordinates.



Get: ModelEast(self: EarthAnchorPoint) -> Vector3d



Set: ModelEast(self: EarthAnchorPoint)=value

"""

 ModelNorth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Earth directions in model coordinates.



Get: ModelNorth(self: EarthAnchorPoint) -> Vector3d



Set: ModelNorth(self: EarthAnchorPoint)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the short form of the identifying information about this location.



Get: Name(self: EarthAnchorPoint) -> str



Set: Name(self: EarthAnchorPoint)=value

"""


