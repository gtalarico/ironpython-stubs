class FamilyThermalProperties(object, IDisposable):
    """
    A class that contains thermal properties for specific types of families
       (doors, windows, and curtain wall panels).
    
    FamilyThermalProperties()
    """
    def Dispose(self):
        """ Dispose(self: FamilyThermalProperties) """
        pass

    @staticmethod
    def Find(pADoc, constructionId):
        """
        Find(pADoc: Document, constructionId: str) -> FamilyThermalProperties
        
            Finds the thermal properties by the 'id' property of a constructionType node in 
             Constructions.xml.
        
        
            pADoc: The document.
            constructionId: The 'id' property of a constructionType node in Constructions.xml
            Returns: The thermal properties found, or ll if no match was found.
        """
        pass

    def IsValid(self):
        """
        IsValid(self: FamilyThermalProperties) -> bool
        
            Confirms that the thermal properties are correctly set for assignment to a 
             FamilySymbol.
        
            Returns: True if the thermal properties are valid, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FamilyThermalProperties, disposing: bool) """
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

    AnalyticConstructionName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The construction gbXML name.
   This value corresponds to the 'Name' property of a constructionType node in Constructions.xml.

Get: AnalyticConstructionName(self: FamilyThermalProperties) -> str

"""

    AnalyticConstructionTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The construction gbXML type.
   This value corresponds to the 'id' property of a constructionType node in Constructions.xml.

Get: AnalyticConstructionTypeId(self: FamilyThermalProperties) -> str

"""

    HeatTransferCoefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The heat transfer coefficient value (U-Value).
   The units are watts per meter-squared kelvin (W/(m^2*K)).

Get: HeatTransferCoefficient(self: FamilyThermalProperties) -> float

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FamilyThermalProperties) -> bool

"""

    SolarHeatGainCoefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The solar heat gain coefficient.

Get: SolarHeatGainCoefficient(self: FamilyThermalProperties) -> float

"""

    ThermalResistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The calculated thermal resistance value (R-Value).
   The units are meter-squared kelvin per watt ((m^2*K)/Watt).

Get: ThermalResistance(self: FamilyThermalProperties) -> float

"""

    VisualLightTransmittance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The visual light transmittance.

Get: VisualLightTransmittance(self: FamilyThermalProperties) -> float

"""


