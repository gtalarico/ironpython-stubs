class ThermalProperties(APIObject, IDisposable):
    """
    Class specific to thermal properties for assembly types, such as Wall,
       Floor, Ceiling, Roof and Building Pad.
    """
    def Dispose(self):
        """ Dispose(self: ThermalProperties, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ThermalProperties, disposing: bool)ReleaseUnmanagedResources(self: APIObject) """
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

    Absorptance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of absorptance.

Get: Absorptance(self: ThermalProperties) -> float

Set: Absorptance(self: ThermalProperties) = value
"""

    HeatTransferCoefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The heat transfer coefficient value (U-Value).
   The unit is watts per meter-squared kelvin (W/(m^2*K)).

Get: HeatTransferCoefficient(self: ThermalProperties) -> float

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ThermalProperties) -> bool

"""

    Roughness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of roughness.

Get: Roughness(self: ThermalProperties) -> int

Set: Roughness(self: ThermalProperties) = value
"""

    ThermalMass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The calculated thermal mass value.
   The unit is kilogram feet-squared per second squared kelvin (kg ft^2/(s^2 K)).

Get: ThermalMass(self: ThermalProperties) -> float

"""

    ThermalResistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The calculated thermal resistance value (R-Value).
   The unit is meter-squared kelvin per watt ((m^2*K)/Watt).

Get: ThermalResistance(self: ThermalProperties) -> float

"""


