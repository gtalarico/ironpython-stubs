class UnitUtils(object):
    """ A utility class of functions related to units. """
    @staticmethod
    def Convert(value, currentDisplayUnit, desiredDisplayUnit):
        """
        Convert(value: float, currentDisplayUnit: DisplayUnitType, desiredDisplayUnit: DisplayUnitType) -> float
        
            Converts a value from one display unit to another, such as square feet to 
             square meters.
        
        
            value: The value to convert.
            currentDisplayUnit: The current display unit.
            desiredDisplayUnit: The desired display unit.
            Returns: The converted value.
        """
        pass

    @staticmethod
    def ConvertFromInternalUnits(value, displayUnit):
        """
        ConvertFromInternalUnits(value: float, displayUnit: DisplayUnitType) -> float
        
            Converts a value from Revit's internal units to a given display unit.
        
            value: The value to convert.
            displayUnit: The desired display unit.
            Returns: The converted value.
        """
        pass

    @staticmethod
    def ConvertToInternalUnits(value, displayUnit):
        """
        ConvertToInternalUnits(value: float, displayUnit: DisplayUnitType) -> float
        
            Converts a value from a given display unit to Revit's internal units.
        
            value: The value to convert.
            displayUnit: The value's display unit.
            Returns: The converted value.
        """
        pass

    @staticmethod
    def GetTypeCatalogString(*__args):
        """
        GetTypeCatalogString(unitType: UnitType) -> str
        
            Gets the string used in type catalogs to identify a given unit type.
        
            unitType: The unit type.
            Returns: The type catalog string, or an empty string if the unit type cannot be used in 
             type catalogs.
        
        GetTypeCatalogString(displayUnit: DisplayUnitType) -> str
        
            Gets the string used in type catalogs to identify a given display unit.
        
            displayUnit: The display unit.
            Returns: The type catalog string, or an empty string if the display unit cannot be used 
             in type catalogs.
        """
        pass

    @staticmethod
    def GetUnitGroup(unitType):
        """
        GetUnitGroup(unitType: UnitType) -> UnitGroup
        
            Gets the unit group for a given unit type.
        
            unitType: The unit type.
            Returns: The unit group.
        """
        pass

    @staticmethod
    def GetValidDisplayUnits(unitType=None):
        """
        GetValidDisplayUnits() -> IList[DisplayUnitType]
        
            Gets all valid display units.
            Returns: The valid display units.
        GetValidDisplayUnits(unitType: UnitType) -> IList[DisplayUnitType]
        
            Gets all valid display units for a given unit type.
        
            unitType: The unit type.
            Returns: The valid display units.
        """
        pass

    @staticmethod
    def GetValidUnitTypes():
        """
        GetValidUnitTypes() -> IList[UnitType]
        
            Gets all valid unit types.
            Returns: The valid unit types.
        """
        pass

    @staticmethod
    def IsValidDisplayUnit(*__args):
        """
        IsValidDisplayUnit(displayUnit: DisplayUnitType) -> bool
        
            Checks whether a display unit is valid.
        
            displayUnit: The display unit to check.
            Returns: True if the display unit is valid, false otherwise.
        IsValidDisplayUnit(unitType: UnitType, displayUnit: DisplayUnitType) -> bool
        
            Checks whether a display unit is valid for a given unit type.
        
            unitType: The unit type.
            displayUnit: The display unit to check.
            Returns: True if the display unit is valid, false otherwise.
        """
        pass

    @staticmethod
    def IsValidUnitType(unitType):
        """
        IsValidUnitType(unitType: UnitType) -> bool
        
            Checks whether a unit type is valid.
        
            unitType: The unit type to check.
            Returns: True if the unit type is valid, false otherwise.
        """
        pass

    __all__ = [
        'Convert',
        'ConvertFromInternalUnits',
        'ConvertToInternalUnits',
        'GetTypeCatalogString',
        'GetUnitGroup',
        'GetValidDisplayUnits',
        'GetValidUnitTypes',
        'IsValidDisplayUnit',
        'IsValidUnitType',
    ]

