class TemperatureRatingType(ElementType, IDisposable):
    """ Represents temperature rating type definition information. """
    def AddCorrectionFactor(self, temperature, factor):
        """
        AddCorrectionFactor(self: TemperatureRatingType, temperature: Int64, factor: float) -> CorrectionFactor
        
            Add a new electrical correction factor type to this temperature rating type.
        
            temperature: Temperature of correction factor to be added.
            factor: Factor of correction factor to be added.
            Returns: New constructed correction factor.
        """
        pass

    def AddInsulationType(self, name):
        """
        AddInsulationType(self: TemperatureRatingType, name: str) -> InsulationType
        
            Add a new kind of insulation type into this temperature rating type.
        
            name: Name of insulation type symbol to be constructed and added.
            Returns: Constructed insulation type instance.
        """
        pass

    def AddWireSize(self, size, ampacity, diameter):
        """
        AddWireSize(self: TemperatureRatingType, size: str, ampacity: Int64, diameter: float) -> WireSize
        
            Add a new kind of wire size type into this temperature rating type.
        
            size: Size of wire size.
            ampacity: Ampacity of wire size to be added.
            diameter: Diameter of wire size to be added.
            Returns: Constructed wire size type.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveCorrectionFactor(self, correctionFactor):
        """
        RemoveCorrectionFactor(self: TemperatureRatingType, correctionFactor: CorrectionFactor)
            Remove an existing correction factor from this temperature rating type in Revit 
             MEP project.
        
        
            correctionFactor: The correction factor to be removed.
            Returns: New constructed correction factor.
        """
        pass

    def RemoveInsulationType(self, insulationType):
        """
        RemoveInsulationType(self: TemperatureRatingType, insulationType: InsulationType)
            Remove an existing insulation type from this temperature rating type.
        
            insulationType: Insulation type to be removed.
        """
        pass

    def RemoveWireSize(self, wireSize):
        """
        RemoveWireSize(self: TemperatureRatingType, wireSize: WireSize)
            Remove an existing wire size type from this temperature rating type.
        
            wireSize: The wire size type to be removed.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    CorrectionFactors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all correction factors defined in this temperature rating type and its corresponding material type.

Get: CorrectionFactors(self: TemperatureRatingType) -> CorrectionFactorSet

"""

    InsulationTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all insulation types defined in this temperature rating type and its corresponding material type.

Get: InsulationTypes(self: TemperatureRatingType) -> InsulationTypeSet

"""

    IsInUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicate whether the temperature rating type is in use.

Get: IsInUse(self: TemperatureRatingType) -> bool

"""

    MaterialType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the material type information which this temperature rating type belongs to.

Get: MaterialType(self: TemperatureRatingType) -> WireMaterialType

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get name of temperature rating type.

Set: Name(self: TemperatureRatingType) = value
"""

    WireSizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all electrical wire sizes defined in this temperature rating type and its corresponding material type.

Get: WireSizes(self: TemperatureRatingType) -> WireSizeSet

"""


