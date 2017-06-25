# encoding: utf-8
# module Autodesk.Revit.DB.Lighting calls itself Lighting
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class LossFactor(object, IDisposable):
    """ This class is the base class for calculating lighting loss factor. """
    def Clone(self):
        """
        Clone(self: LossFactor) -> LossFactor
        
            Creates a copy of the LossFactor derived object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: LossFactor) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LossFactor, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LossFactor) -> bool

"""

    LossFactorValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The calculated loss factor value

Get: LossFactorValue(self: LossFactor) -> float

"""



class AdvancedLossFactor(LossFactor, IDisposable):
    """
    This class encapsulates advanced lighting loss factor calculation.
    
    AdvancedLossFactor(other: AdvancedLossFactor)
    AdvancedLossFactor(ballastLossFactorIn: float, lampLumenDepreciationIn: float, lampTiltLossFactorIn: float, luminaireDirtDepreciationIn: float, surfaceDepreciationLossFactorIn: float, temperatureLossFactorIn: float, voltageLossFactorIn: float)
    AdvancedLossFactor()
    """
    def Dispose(self):
        """ Dispose(self: LossFactor, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LossFactor, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: AdvancedLossFactor)
        __new__(cls: type, ballastLossFactorIn: float, lampLumenDepreciationIn: float, lampTiltLossFactorIn: float, luminaireDirtDepreciationIn: float, surfaceDepreciationLossFactorIn: float, temperatureLossFactorIn: float, voltageLossFactorIn: float)
        __new__(cls: type)
        """
        pass

    BallastLossFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ballast loss factor.

Get: BallastLossFactor(self: AdvancedLossFactor) -> float

Set: BallastLossFactor(self: AdvancedLossFactor) = value
"""

    LampLumenDepreciation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The lamp lumen depreciation loss factor.

Get: LampLumenDepreciation(self: AdvancedLossFactor) -> float

Set: LampLumenDepreciation(self: AdvancedLossFactor) = value
"""

    LampTiltLossFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The lamp tilt loss factor.

Get: LampTiltLossFactor(self: AdvancedLossFactor) -> float

Set: LampTiltLossFactor(self: AdvancedLossFactor) = value
"""

    LuminaireDirtDepreciation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The luminaire dirt depreciation loss factor.

Get: LuminaireDirtDepreciation(self: AdvancedLossFactor) -> float

Set: LuminaireDirtDepreciation(self: AdvancedLossFactor) = value
"""

    SurfaceDepreciationLossFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The surface depreciation loss factor.

Get: SurfaceDepreciationLossFactor(self: AdvancedLossFactor) -> float

Set: SurfaceDepreciationLossFactor(self: AdvancedLossFactor) = value
"""

    TemperatureLossFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The temperature loss factor.

Get: TemperatureLossFactor(self: AdvancedLossFactor) -> float

Set: TemperatureLossFactor(self: AdvancedLossFactor) = value
"""

    VoltageLossFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The voltage loss factor.

Get: VoltageLossFactor(self: AdvancedLossFactor) -> float

Set: VoltageLossFactor(self: AdvancedLossFactor) = value
"""



class BasicLossFactor(LossFactor, IDisposable):
    """
    This class encapsulates basic lighting loss factor calculation.
    
    BasicLossFactor(other: BasicLossFactor)
    BasicLossFactor(lossFactorIn: float)
    BasicLossFactor()
    """
    def Dispose(self):
        """ Dispose(self: LossFactor, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LossFactor, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: BasicLossFactor)
        __new__(cls: type, lossFactorIn: float)
        __new__(cls: type)
        """
        pass

    LossFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The loss factor.

Get: LossFactor(self: BasicLossFactor) -> float

Set: LossFactor(self: BasicLossFactor) = value
"""



class LightShape(object, IDisposable):
    """ This class is the base class for specifying light shape. """
    def Clone(self):
        """
        Clone(self: LightShape) -> LightShape
        
            Creates a copy of the LightShape derived object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: LightShape) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightShape, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LightShape) -> bool

"""



class CircleLightShape(LightShape, IDisposable):
    """
    This class encapsulates a circle light shape.
    
    CircleLightShape(other: CircleLightShape)
    CircleLightShape(emitDiameter: float)
    CircleLightShape()
    """
    def Dispose(self):
        """ Dispose(self: LightShape, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightShape, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: CircleLightShape)
        __new__(cls: type, emitDiameter: float)
        __new__(cls: type)
        """
        pass

    EmitDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The emit diameter.

Get: EmitDiameter(self: CircleLightShape) -> float

Set: EmitDiameter(self: CircleLightShape) = value
"""



class ColorPreset(Enum, IComparable, IFormattable, IConvertible):
    """
    Preset values of initial colors for specific lighting types
    
    enum ColorPreset, values: D50 (1), D65 (0), FluorescentCool (7), FluorescentDayLight (9), FluorescentLightWhite (10), FluorescentWarm (6), FluorescentWhite (8), Halogen (2), HighPressureSodium (12), Incandescent (3), LowPressureSodium (13), Mercury (14), MetalHalide (11), PhosphorMercury (15), Quartz (5), Xenon (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    D50 = None
    D65 = None
    FluorescentCool = None
    FluorescentDayLight = None
    FluorescentLightWhite = None
    FluorescentWarm = None
    FluorescentWhite = None
    Halogen = None
    HighPressureSodium = None
    Incandescent = None
    LowPressureSodium = None
    Mercury = None
    MetalHalide = None
    PhosphorMercury = None
    Quartz = None
    value__ = None
    Xenon = None


class InitialColor(object, IDisposable):
    """ This class is the base class for calculating initial light color. """
    def Clone(self):
        """
        Clone(self: InitialColor) -> InitialColor
        
            Creates a copy of the InitialColor derived object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: InitialColor) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InitialColor, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: InitialColor) -> bool

"""

    TemperatureValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The light color temperature value in Kelvins.

Get: TemperatureValue(self: InitialColor) -> float

"""



class CustomInitialColor(InitialColor, IDisposable):
    """
    This class encapsulates a custom initial lighting color.
    
    CustomInitialColor(other: CustomInitialColor)
    CustomInitialColor(temperature: float)
    """
    def Dispose(self):
        """ Dispose(self: InitialColor, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InitialColor, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: CustomInitialColor)
        __new__(cls: type, temperature: float)
        """
        pass

    Temperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The custom color temperature value.

Get: Temperature(self: CustomInitialColor) -> float

Set: Temperature(self: CustomInitialColor) = value
"""



class LightDistribution(object, IDisposable):
    """ This class is the base class for specifying light distribution. """
    def Clone(self):
        """
        Clone(self: LightDistribution) -> LightDistribution
        
            Creates a copy of the LightDistribution derived object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: LightDistribution) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightDistribution, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LightDistribution) -> bool

"""



class HemisphericalLightDistribution(LightDistribution, IDisposable):
    """
    This class encapsulates a hemispherical light distribution.
    
    HemisphericalLightDistribution(other: HemisphericalLightDistribution)
    HemisphericalLightDistribution()
    """
    def Dispose(self):
        """ Dispose(self: LightDistribution, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightDistribution, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type, other: HemisphericalLightDistribution)
        __new__(cls: type)
        """
        pass


class InitialIntensity(object, IDisposable):
    """ This class is the base class for calculating lighting initial intensity. """
    def Clone(self):
        """
        Clone(self: InitialIntensity) -> InitialIntensity
        
            Creates a copy of the InitialIntensity derived object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: InitialIntensity) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InitialIntensity, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    InitialIntensityValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The calculated initial intensity value.

Get: InitialIntensityValue(self: InitialIntensity) -> float

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: InitialIntensity) -> bool

"""



class InitialFluxIntensity(InitialIntensity, IDisposable):
    """
    This class encapsulates initial flux intensity calculation.
    
    InitialFluxIntensity(other: InitialFluxIntensity)
    InitialFluxIntensity(flux: float)
    """
    def Dispose(self):
        """ Dispose(self: InitialIntensity, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InitialIntensity, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: InitialFluxIntensity)
        __new__(cls: type, flux: float)
        """
        pass

    Flux = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flux intensity value.

Get: Flux(self: InitialFluxIntensity) -> float

Set: Flux(self: InitialFluxIntensity) = value
"""



class InitialIlluminanceIntensity(InitialIntensity, IDisposable):
    """
    This class encapsulates initial illuminance intensity calculation.
    
    InitialIlluminanceIntensity(other: InitialIlluminanceIntensity)
    InitialIlluminanceIntensity(distance: float, illuminance: float)
    """
    def Dispose(self):
        """ Dispose(self: InitialIntensity, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InitialIntensity, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: InitialIlluminanceIntensity)
        __new__(cls: type, distance: float, illuminance: float)
        """
        pass

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The illuminance intensity distance value.

Get: Distance(self: InitialIlluminanceIntensity) -> float

Set: Distance(self: InitialIlluminanceIntensity) = value
"""

    Illuminance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The illuminance intensity value.

Get: Illuminance(self: InitialIlluminanceIntensity) -> float

Set: Illuminance(self: InitialIlluminanceIntensity) = value
"""



class InitialLuminousIntensity(InitialIntensity, IDisposable):
    """
    This class encapsulates initial luminous intensity calculation.
    
    InitialLuminousIntensity(other: InitialLuminousIntensity)
    InitialLuminousIntensity(luminosity: float)
    """
    def Dispose(self):
        """ Dispose(self: InitialIntensity, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InitialIntensity, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: InitialLuminousIntensity)
        __new__(cls: type, luminosity: float)
        """
        pass

    Luminosity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The luminosity value.

Get: Luminosity(self: InitialLuminousIntensity) -> float

Set: Luminosity(self: InitialLuminousIntensity) = value
"""



class InitialWattageIntensity(InitialIntensity, IDisposable):
    """
    This class encapsulates initial wattage intensity calculation.
    
    InitialWattageIntensity(other: InitialWattageIntensity)
    InitialWattageIntensity(efficacy: float, wattage: float)
    """
    def Dispose(self):
        """ Dispose(self: InitialIntensity, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InitialIntensity, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: InitialWattageIntensity)
        __new__(cls: type, efficacy: float, wattage: float)
        """
        pass

    Efficacy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The efficacy value.

Get: Efficacy(self: InitialWattageIntensity) -> float

Set: Efficacy(self: InitialWattageIntensity) = value
"""

    Wattage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The wattage value.

Get: Wattage(self: InitialWattageIntensity) -> float

Set: Wattage(self: InitialWattageIntensity) = value
"""



class LightDimmingColor(Enum, IComparable, IFormattable, IConvertible):
    """
    Tags for specific light dimming colors
    
    enum LightDimmingColor, values: Incandescent (1), None (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Incandescent = None
    None = None
    value__ = None


class LightDistributionStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Tags for specific light distribution styles
    
    enum LightDistributionStyle, values: Hemispherical (1), PhotometricWeb (3), Spherical (0), Spot (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Hemispherical = None
    PhotometricWeb = None
    Spherical = None
    Spot = None
    value__ = None


class LightFamily(object, IDisposable):
    """ This class encapsulates light family information. """
    def Dispose(self):
        """ Dispose(self: LightFamily) """
        pass

    def GetLightDistributionStyle(self):
        """
        GetLightDistributionStyle(self: LightFamily) -> LightDistributionStyle
        
            Returns a LightDistributionStyle value for the light distribution
        """
        pass

    @staticmethod
    def GetLightFamily(document):
        """
        GetLightFamily(document: Document) -> LightFamily
        
            Creates a light family object from the given family document
        
            document: The family document
            Returns: The newly created LightFamily object
        """
        pass

    def GetLightShapeStyle(self):
        """
        GetLightShapeStyle(self: LightFamily) -> LightShapeStyle
        
            Returns a LightShapeStyle value for the light shape
        """
        pass

    def GetLightSourceTransform(self):
        """
        GetLightSourceTransform(self: LightFamily) -> Transform
        
            Returns a Transform value for the transform of light source.
            Returns: The light source transform.
        """
        pass

    def GetLightType(self, index):
        """
        GetLightType(self: LightFamily, index: int) -> LightType
        
            Return a LightType object for the light type at the given index
        
            index: The index of the light type
            Returns: A LightType object for the light type at the given index
        """
        pass

    def GetLightTypeName(self, index):
        """
        GetLightTypeName(self: LightFamily, index: int) -> str
        
            Return the name for the light type at the given index
        
            index: The index of the light type
            Returns: The name of the light type at the given index
        """
        pass

    def GetNumberOfLightTypes(self):
        """
        GetNumberOfLightTypes(self: LightFamily) -> int
        
            Return the number of light types contained in this light family
            Returns: The number of light types contained in this light family
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightFamily, disposing: bool) """
        pass

    def SetLightDistributionStyle(self, lightDistributionStyle):
        """
        SetLightDistributionStyle(self: LightFamily, lightDistributionStyle: LightDistributionStyle)
            Set the light distribution style to the given shape distribution
        
            lightDistributionStyle: The light distribution style to set the light distribution type to
        """
        pass

    def SetLightShapeStyle(self, lightShapeStyle):
        """
        SetLightShapeStyle(self: LightFamily, lightShapeStyle: LightShapeStyle)
            Set the light shape style to the given shape style
        
            lightShapeStyle: The light shape style value to set the light shape style to
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LightFamily) -> bool

"""



class LightGroup(object, IDisposable):
    """ This class represents a set of lights grouped together for easier management of various lighting scenarios """
    def AddLight(self, lightId):
        """
        AddLight(self: LightGroup, lightId: ElementId)
            Add a new light instance to the group
        
            lightId: The ID of the light instance to add to the group
        """
        pass

    def Dispose(self):
        """ Dispose(self: LightGroup) """
        pass

    def GetLights(self):
        """
        GetLights(self: LightGroup) -> ICollection[ElementId]
        
            Get the set of contained light instances
           The set of light instances
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightGroup, disposing: bool) """
        pass

    def RemoveLight(self, lightId):
        """
        RemoveLight(self: LightGroup, lightId: ElementId)
            Remove the given light instance from the set of light instances in this group
        
            lightId: The light instance to remove
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the LightGroup

Get: Id(self: LightGroup) -> ElementId

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LightGroup) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the LightGroup

Get: Name(self: LightGroup) -> str

Set: Name(self: LightGroup) = value
"""



class LightGroupManager(object, IDisposable):
    """ This class represents a set of light groups that are used for easier management of various lighting scenarios """
    def CreateGroup(self, name):
        """
        CreateGroup(self: LightGroupManager, name: str) -> LightGroup
        
            Create a new LightGroup object with the given name
        
            name: The name to use for the new LightGroup object
            Returns: The new LightGroup object that was created
        """
        pass

    def DeleteGroup(self, groupId):
        """
        DeleteGroup(self: LightGroupManager, groupId: ElementId)
            Remove the given LightGroup object from the set of LightGroup objects
        
            groupId: The Id of the LightGroup object to remove
        """
        pass

    def Dispose(self):
        """ Dispose(self: LightGroupManager) """
        pass

    def GetGroups(self):
        """
        GetGroups(self: LightGroupManager) -> IList[LightGroup]
        
            Get the set of contained LightGroup objects
           The set of LightGroup objects
        """
        pass

    def GetLightDimmer(self, viewId, lightId):
        """
        GetLightDimmer(self: LightGroupManager, viewId: ElementId, lightId: ElementId) -> float
        
            Gets the dimmer value for the given light for rendering the given view
        
            viewId: The Id of the view
            lightId: The Id of the light to turn on or off
        """
        pass

    @staticmethod
    def GetLightGroupManager(document):
        """
        GetLightGroupManager(document: Document) -> LightGroupManager
        
            Creates a light group manager object from the given document
        
            document: The document the manager is from
            Returns: The newly created Light group manager object
        """
        pass

    def IsLightGroupOn(self, viewId, groupId):
        """
        IsLightGroupOn(self: LightGroupManager, viewId: ElementId, groupId: ElementId) -> bool
        
            Returns true if the given light group is on
        
            viewId: The Id of the view
            groupId: The Id of the light group
        """
        pass

    def IsLightOn(self, viewId, lightId):
        """
        IsLightOn(self: LightGroupManager, viewId: ElementId, lightId: ElementId) -> bool
        
            Returns true if the given light is on for rendering the given view
        
            viewId: The Id of the view
            lightId: The Id of the light
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightGroupManager, disposing: bool) """
        pass

    def SetLightDimmer(self, viewId, lightId, dimmingValue):
        """
        SetLightDimmer(self: LightGroupManager, viewId: ElementId, lightId: ElementId, dimmingValue: float)
            Sets the dimmer value for the given light for rendering the given view
        
            viewId: The Id of the view
            lightId: The Id of the light to turn on or off
            dimmingValue: The dimmer value to set int the range of [0.0, 1.0]
        """
        pass

    def SetLightGroupOn(self, viewId, groupId, turnOn):
        """
        SetLightGroupOn(self: LightGroupManager, viewId: ElementId, groupId: ElementId, turnOn: bool)
            Turns the given light group on or off for rendering the given view depending on 
             the bool argument
        
        
            viewId: The Id of the view
            groupId: The Id of the light group
            turnOn: Turns the light group on if true, off if false
        """
        pass

    def SetLightOn(self, viewId, lightId, turnOn):
        """
        SetLightOn(self: LightGroupManager, viewId: ElementId, lightId: ElementId, turnOn: bool)
            Turns the given light on or off for rendering the given view depending on the 
             bool argument
        
        
            viewId: The Id of the view
            lightId: The Id of the light to turn on or off
            turnOn: Turns the light on if true, off if false
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LightGroupManager) -> bool

"""



class LightShapeStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Tags for specific light shape styles
    
    enum LightShapeStyle, values: Circle (3), Line (1), Point (0), Rectangle (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Circle = None
    Line = None
    Point = None
    Rectangle = None
    value__ = None


class LightType(object, IDisposable):
    """ This class encapsulates light information. """
    def Dispose(self):
        """ Dispose(self: LightType) """
        pass

    def GetInitialColor(self):
        """
        GetInitialColor(self: LightType) -> InitialColor
        
            Return a copy of an object derived from InitialColor
        """
        pass

    def GetInitialIntensity(self):
        """
        GetInitialIntensity(self: LightType) -> InitialIntensity
        
            Return a copy of an object derived from InitialIntensity
        """
        pass

    def GetLightDistribution(self):
        """
        GetLightDistribution(self: LightType) -> LightDistribution
        
            Return a copy of an object derived from LightDistribution
        """
        pass

    def GetLightShape(self):
        """
        GetLightShape(self: LightType) -> LightShape
        
            Return a copy of an object derived from LightShape
        """
        pass

    @staticmethod
    def GetLightType(document, typeId):
        """
        GetLightType(document: Document, typeId: ElementId) -> LightType
        
            Creates a light type object from the given document and family type ID
        
            document: The document the typeId is from
            typeId: The ID of the light family type
            Returns: The newly created LightType object
        """
        pass

    @staticmethod
    def GetLightTypeFromInstance(document, instanceId):
        """
        GetLightTypeFromInstance(document: Document, instanceId: ElementId) -> LightType
        
            Creates a light type object from the given document and element ID
        
            document: The document the instanceId is from
            instanceId: The ID of the light fixture instance
            Returns: The newly created LightType object
        """
        pass

    def GetLossFactor(self):
        """
        GetLossFactor(self: LightType) -> LossFactor
        
            Return a copy of an object derived from LossFactor
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightType, disposing: bool) """
        pass

    def SetInitialColor(self, initialColor):
        """
        SetInitialColor(self: LightType, initialColor: InitialColor)
            Replace the current initial color object with the given object
        
            initialColor: An object derived from an InitialColor object
           The object pointed to is 
             cloned internally
        """
        pass

    def SetInitialIntensity(self, initialIntensity):
        """
        SetInitialIntensity(self: LightType, initialIntensity: InitialIntensity)
            Replace the current initial intensity object with the given object
        
            initialIntensity: An object derived from an InitialIntensity object
        """
        pass

    def SetLightDistribution(self, lightDistribution):
        """
        SetLightDistribution(self: LightType, lightDistribution: LightDistribution)
            Replace the current LightDistribution object with the given object
        
            lightDistribution: An instance of an object derived from LightDistribution
        """
        pass

    def SetLightShape(self, lightShape):
        """
        SetLightShape(self: LightType, lightShape: LightShape)
            Replace the current LightShape object with the given object
        
            lightShape: An instance of an object derived from LightShape
        """
        pass

    def SetLossFactor(self, lossFactor):
        """
        SetLossFactor(self: LightType, lossFactor: LossFactor)
            Replace the current loss factor object with the given object
        
            lossFactor: An object derived from a LossFactor object
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ColorFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The light filter color.

Get: ColorFilter(self: LightType) -> Color

Set: ColorFilter(self: LightType) = value
"""

    DimmingColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The dimming temperature value in Kelvins.

Get: DimmingColor(self: LightType) -> LightDimmingColor

Set: DimmingColor(self: LightType) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LightType) -> bool

"""



class LineLightShape(LightShape, IDisposable):
    """
    This class encapsulates a line light shape.
    
    LineLightShape(other: LineLightShape)
    LineLightShape(emitLength: float)
    LineLightShape()
    """
    def Dispose(self):
        """ Dispose(self: LightShape, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightShape, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: LineLightShape)
        __new__(cls: type, emitLength: float)
        __new__(cls: type)
        """
        pass

    EmitLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The emit length.

Get: EmitLength(self: LineLightShape) -> float

Set: EmitLength(self: LineLightShape) = value
"""



class PhotometricWebLightDistribution(LightDistribution, IDisposable):
    """
    This class encapsulates a photometric web light distribution.
    
    PhotometricWebLightDistribution(other: PhotometricWebLightDistribution)
    PhotometricWebLightDistribution(photometricWebFile: str, tiltAngle: float)
    """
    def Dispose(self):
        """ Dispose(self: LightDistribution, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightDistribution, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: PhotometricWebLightDistribution)
        __new__(cls: type, photometricWebFile: str, tiltAngle: float)
        """
        pass

    PhotometricWebFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The filename of an IES photometric web file.

Get: PhotometricWebFile(self: PhotometricWebLightDistribution) -> str

Set: PhotometricWebFile(self: PhotometricWebLightDistribution) = value
"""

    TiltAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The tilt angle.

Get: TiltAngle(self: PhotometricWebLightDistribution) -> float

Set: TiltAngle(self: PhotometricWebLightDistribution) = value
"""



class PointLightShape(LightShape, IDisposable):
    """
    This class encapsulates a point light shape.
    
    PointLightShape(other: PointLightShape)
    PointLightShape()
    """
    def Dispose(self):
        """ Dispose(self: LightShape, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightShape, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type, other: PointLightShape)
        __new__(cls: type)
        """
        pass


class PresetInitialColor(InitialColor, IDisposable):
    """
    This class encapsulates a preset initial lighting color.
    
    PresetInitialColor(other: PresetInitialColor)
    PresetInitialColor(presetIn: ColorPreset)
    """
    def Dispose(self):
        """ Dispose(self: InitialColor, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InitialColor, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: PresetInitialColor)
        __new__(cls: type, presetIn: ColorPreset)
        """
        pass

    Preset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The preset value

Get: Preset(self: PresetInitialColor) -> ColorPreset

Set: Preset(self: PresetInitialColor) = value
"""



class RectangleLightShape(LightShape, IDisposable):
    """
    This class encapsulates a rectangle light shape.
    
    RectangleLightShape(other: RectangleLightShape)
    RectangleLightShape(emitLength: float, emitWidth: float)
    RectangleLightShape()
    """
    def Dispose(self):
        """ Dispose(self: LightShape, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightShape, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: RectangleLightShape)
        __new__(cls: type, emitLength: float, emitWidth: float)
        __new__(cls: type)
        """
        pass

    EmitLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The emit length.

Get: EmitLength(self: RectangleLightShape) -> float

Set: EmitLength(self: RectangleLightShape) = value
"""

    EmitWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The emit width.

Get: EmitWidth(self: RectangleLightShape) -> float

Set: EmitWidth(self: RectangleLightShape) = value
"""



class SphericalLightDistribution(LightDistribution, IDisposable):
    """
    This class encapsulates a spherical light distribution.
    
    SphericalLightDistribution(other: SphericalLightDistribution)
    SphericalLightDistribution()
    """
    def Dispose(self):
        """ Dispose(self: LightDistribution, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightDistribution, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type, other: SphericalLightDistribution)
        __new__(cls: type)
        """
        pass


class SpotLightDistribution(LightDistribution, IDisposable):
    """
    This class encapsulates a spot light distribution.
    
    SpotLightDistribution(other: SpotLightDistribution)
    SpotLightDistribution(spotBeamAngle: float, spotFieldAngle: float, tiltAngle: float)
    SpotLightDistribution()
    """
    def Dispose(self):
        """ Dispose(self: LightDistribution, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LightDistribution, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: SpotLightDistribution)
        __new__(cls: type, spotBeamAngle: float, spotFieldAngle: float, tiltAngle: float)
        __new__(cls: type)
        """
        pass

    SpotBeamAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The spot beam angle.

Get: SpotBeamAngle(self: SpotLightDistribution) -> float

Set: SpotBeamAngle(self: SpotLightDistribution) = value
"""

    SpotFieldAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The spot field angle.

Get: SpotFieldAngle(self: SpotLightDistribution) -> float

Set: SpotFieldAngle(self: SpotLightDistribution) = value
"""

    TiltAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The tilt angle.

Get: TiltAngle(self: SpotLightDistribution) -> float

Set: TiltAngle(self: SpotLightDistribution) = value
"""



