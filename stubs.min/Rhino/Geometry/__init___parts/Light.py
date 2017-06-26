class Light(GeometryBase, IDisposable, ISerializable):
    """ Light() """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def GetAttenuation(self, d):
        """ GetAttenuation(self: Light, d: float) -> float """
        pass

    def GetSpotLightRadii(self, innerRadius, outerRadius):
        """ GetSpotLightRadii(self: Light) -> (bool, float, float) """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: CommonObject) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: GeometryBase) """
        pass

    def SetAttenuation(self, a0, a1, a2):
        """ SetAttenuation(self: Light, a0: float, a1: float, a2: float) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Ambient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ambient(self: Light) -> Color

Set: Ambient(self: Light) = value
"""

    AttenuationVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttenuationVector(self: Light) -> Vector3d

Set: AttenuationVector(self: Light) = value
"""

    CoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystem(self: Light) -> CoordinateSystem

"""

    Diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diffuse(self: Light) -> Color

Set: Diffuse(self: Light) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: Light) -> Vector3d

Set: Direction(self: Light) = value
"""

    HotSpot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HotSpot(self: Light) -> float

Set: HotSpot(self: Light) = value
"""

    Intensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Intensity(self: Light) -> float

Set: Intensity(self: Light) = value
"""

    IsDirectionalLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDirectionalLight(self: Light) -> bool

"""

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabled(self: Light) -> bool

Set: IsEnabled(self: Light) = value
"""

    IsLinearLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLinearLight(self: Light) -> bool

"""

    IsPointLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPointLight(self: Light) -> bool

"""

    IsRectangularLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRectangularLight(self: Light) -> bool

"""

    IsSpotLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpotLight(self: Light) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Light) -> Vector3d

Set: Length(self: Light) = value
"""

    LightStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LightStyle(self: Light) -> LightStyle

Set: LightStyle(self: Light) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Light) -> Point3d

Set: Location(self: Light) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Light) -> str

Set: Name(self: Light) = value
"""

    PerpendicularDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PerpendicularDirection(self: Light) -> Vector3d

"""

    PowerCandela = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PowerCandela(self: Light) -> float

Set: PowerCandela(self: Light) = value
"""

    PowerLumens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PowerLumens(self: Light) -> float

Set: PowerLumens(self: Light) = value
"""

    PowerWatts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PowerWatts(self: Light) -> float

Set: PowerWatts(self: Light) = value
"""

    Specular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Specular(self: Light) -> Color

Set: Specular(self: Light) = value
"""

    SpotAngleRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpotAngleRadians(self: Light) -> float

Set: SpotAngleRadians(self: Light) = value
"""

    SpotExponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpotExponent(self: Light) -> float

Set: SpotExponent(self: Light) = value
"""

    SpotLightShadowIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpotLightShadowIntensity(self: Light) -> float

Set: SpotLightShadowIntensity(self: Light) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: Light) -> Vector3d

Set: Width(self: Light) = value
"""


