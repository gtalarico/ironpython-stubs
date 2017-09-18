class Light(GeometryBase,IDisposable,ISerializable):
 """
 Represents a light that shines in the modeling space.

 

 Light()
 """
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 @staticmethod
 def CreateSunLight(*__args):
  """
  CreateSunLight(sun: Sun) -> Light

  

   Constructs a light which simulates a Rhino.Render.Sun.

  

   sun: A Sun object from the Rhino.Render namespace.

   Returns: A light.

  CreateSunLight(northAngleDegrees: float,when: DateTime,latitudeDegrees: float,longitudeDegrees: float) -> Light

  

   Constructs a light which simulates the Sun based on a given time and location on Earth.

  

   northAngleDegrees: The angle of North in degrees. North is the angle between positive World Y axis and model North,

    as measured on World XY plane.

  

   when: The time of the measurement. The Kind property of DateTime specifies whether this is in local or 

    universal time.

     Local and Undefined System.DateTimeKinddaytime kinds in this 

    argument are considered local.

  

   latitudeDegrees: The latitude,in degrees,of the location on Earth.

   longitudeDegrees: The longitude,in degrees,of the location on Earth.

   Returns: A newly constructed light object.

  CreateSunLight(northAngleDegrees: float,azimuthDegrees: float,altitudeDegrees: float) -> Light

  

   Constructs a light that represents the Sun.

  

   northAngleDegrees: The angle of North in degrees. North is the angle between positive World Y axis and model North,

    as measured on World XY plane.

  

   azimuthDegrees: The Azimut angle value in degrees. Azimuth is the compass angle from North.

   altitudeDegrees: The Altitude angle in degrees. Altitude is the angle above the ground plane.

   Returns: A new sun light.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: CommonObject,disposing: bool)

   For derived class implementers.

     This method is called with argument true when class 

    user calls Dispose(),while with argument false when

     the Garbage Collector invokes 

    the finalizer,or Finalize() method.You must reclaim all used unmanaged resources in both cases,

    and can use this chance to call Dispose on disposable fields if the argument is true.Also,you 

    must call the base virtual method within your overriding method.

  

  

   disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 

    finalizer.
  """
  pass
 def GetAttenuation(self,d):
  """
  GetAttenuation(self: Light,d: float) -> float

  

   Gets the attenuation settings (ignored for "directional" and "ambient" lights).

     

    attenuation=1/(a0 + d*a1 + d^2*a2) where d=distance to light.

  

  

   d: The distance to evaluate.

   Returns: 0 if a0 + d*a1 + d^2*a2 <= 0.
  """
  pass
 def GetSpotLightRadii(self,innerRadius,outerRadius):
  """
  GetSpotLightRadii(self: Light) -> (bool,float,float)

  

   Gets the spot light radii.

   Returns: true if operation succeeded; otherwise,false.
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: CommonObject)

   For derived classes implementers.

     Defines the necessary implementation to free the 

    instance from being const.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
  """
  pass
 def SetAttenuation(self,a0,a1,a2):
  """
  SetAttenuation(self: Light,a0: float,a1: float,a2: float)

   Sets the attenuation settings (ignored for "directional" and "ambient" lights).

     

    attenuation=1/(a0 + d*a1 + d^2*a2) where d=distance to light.

  

  

   a0: The new constant attenuation divisor term.

   a1: The new reverse linear attenuation divisor term.

   a2: The new reverse quadratic attenuation divisor term.
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
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 Ambient=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the ambient color.



Get: Ambient(self: Light) -> Color



Set: Ambient(self: Light)=value

"""

 AttenuationVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or Sets the attenuation vector.



Get: AttenuationVector(self: Light) -> Vector3d



Set: AttenuationVector(self: Light)=value

"""

 CoordinateSystem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value,determined by LightStyle,that explains whether

   the camera diretions are relative to World or Camera spaces.



Get: CoordinateSystem(self: Light) -> CoordinateSystem



"""

 Diffuse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the diffuse color.



Get: Diffuse(self: Light) -> Color



Set: Diffuse(self: Light)=value

"""

 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the vector direction of the camera.



Get: Direction(self: Light) -> Vector3d



Set: Direction(self: Light)=value

"""

 HotSpot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The hot spot setting runs from 0.0 to 1.0 and is used to

   provides a linear interface for controling the focus or 

   concentration of a spotlight.

   A hot spot setting of 0.0 corresponds to a spot exponent of 128.

   A hot spot setting of 1.0 corresponds to a spot exponent of 0.0.



Get: HotSpot(self: Light) -> float



Set: HotSpot(self: Light)=value

"""

 Intensity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the light intensity.



Get: Intensity(self: Light) -> float



Set: Intensity(self: Light)=value

"""

 IsDirectionalLight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the light style

   is Rhino.Geometry.Light.LightStyle CameraDirectional or WorldDirectional.



Get: IsDirectionalLight(self: Light) -> bool



"""

 IsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that defines if the light is turned on (true) or off (false).



Get: IsEnabled(self: Light) -> bool



Set: IsEnabled(self: Light)=value

"""

 IsLinearLight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the light style

   is Rhino.Geometry.Light.LightStyle WorldLinear.



Get: IsLinearLight(self: Light) -> bool



"""

 IsPointLight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the light style

   is Rhino.Geometry.Light.LightStyle CameraPoint or WorldPoint.



Get: IsPointLight(self: Light) -> bool



"""

 IsRectangularLight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the light style

   is Rhino.Geometry.Light.LightStyle WorldRectangular.



Get: IsRectangularLight(self: Light) -> bool



"""

 IsSpotLight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the light style

   is Rhino.Geometry.Light.LightStyle CameraSpot or WorldSpot.



Get: IsSpotLight(self: Light) -> bool



"""

 IsSunLight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this object is a Sun light.



Get: IsSunLight(self: Light) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height in linear and rectangular lights.

   (ignored for non-linear/rectangular lights.)



Get: Length(self: Light) -> Vector3d



Set: Length(self: Light)=value

"""

 LightStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a light style on this camera.



Get: LightStyle(self: Light) -> LightStyle



Set: LightStyle(self: Light)=value

"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the light or 3D position or location.



Get: Location(self: Light) -> Point3d



Set: Location(self: Light)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the spot light name.



Get: Name(self: Light) -> str



Set: Name(self: Light)=value

"""

 PerpendicularDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a perpendicular vector to the camera direction.



Get: PerpendicularDirection(self: Light) -> Vector3d



"""

 PowerCandela=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the light power in candelas (cd).



Get: PowerCandela(self: Light) -> float



Set: PowerCandela(self: Light)=value

"""

 PowerLumens=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the light power in lumens (lm).



Get: PowerLumens(self: Light) -> float



Set: PowerLumens(self: Light)=value

"""

 PowerWatts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the light power in watts (W).



Get: PowerWatts(self: Light) -> float



Set: PowerWatts(self: Light)=value

"""

 Specular=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the specular color.



Get: Specular(self: Light) -> Color



Set: Specular(self: Light)=value

"""

 SpotAngleRadians=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the spot angle in radians.

   Ignored for non-spot lights.angle=0 to pi/2  (0 to 90 degrees).



Get: SpotAngleRadians(self: Light) -> float



Set: SpotAngleRadians(self: Light)=value

"""

 SpotExponent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The spot exponent varies from 0.0 to 128.0 and provides

   an exponential interface for controling the focus or 

   concentration of a spotlight (like the 

   OpenGL GL_SPOT_EXPONENT parameter).  The spot exponent

   and hot spot parameters are linked; changing one will

   change the other.

   A hot spot setting of 0.0 corresponds to a spot exponent of 128.

   A hot spot setting of 1.0 corresponds to a spot exponent of 0.0.



Get: SpotExponent(self: Light) -> float



Set: SpotExponent(self: Light)=value

"""

 SpotLightShadowIntensity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the spot light shadow intensity.

   (ignored for non-spot lights.)



Get: SpotLightShadowIntensity(self: Light) -> float



Set: SpotLightShadowIntensity(self: Light)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width in linear and rectangular lights.

   (ignored for non-linear/rectangular lights.)



Get: Width(self: Light) -> Vector3d



Set: Width(self: Light)=value

"""


