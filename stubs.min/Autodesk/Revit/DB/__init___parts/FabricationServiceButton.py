class FabricationServiceButton(object, IDisposable):
    """ The object contains information about a fabricaton button. """
    def ContainsFabricationPartType(self, partType):
        """
        ContainsFabricationPartType(self: FabricationServiceButton, partType: FabricationPartType) -> bool
        
            Checks to see if the fabrication part type exists on one of the button 
             conditions.
        
        
            partType: The fabrication part type to check.
            Returns: Returns true if the fabrication part type exists on the fabrication service 
             button.
        """
        pass

    def Dispose(self):
        """ Dispose(self: FabricationServiceButton) """
        pass

    def GetConditionDescription(self, condition):
        """
        GetConditionDescription(self: FabricationServiceButton, condition: int) -> str
        
            Gets the description for the condition size range.
        
            condition: The index of the condition in the service button.
            Returns: A user-defined string that describes the condition range, as defined in the 
             fabrication configuration.
           For example, this may describe the size of the 
             range or describe the type of fitting.
        """
        pass

    def GetConditionImage(self, condition):
        """ GetConditionImage(self: FabricationServiceButton, condition: int) -> Bitmap """
        pass

    def GetConditionLowerValue(self, condition):
        """
        GetConditionLowerValue(self: FabricationServiceButton, condition: int) -> float
        
            Gets the condition lower value (valid if greater or equal) for a given 
             condition index.
        
        
            condition: The condition index.
            Returns: The condition lower value.
        """
        pass

    def GetConditionName(self, condition):
        """
        GetConditionName(self: FabricationServiceButton, condition: int) -> str
        
            Gets the name of the specified condition on the fabrication service button.
        
            condition: The condition index.
            Returns: The name of the specified condition on the fabrication service button.
        """
        pass

    def GetConditionUpperValue(self, condition):
        """
        GetConditionUpperValue(self: FabricationServiceButton, condition: int) -> float
        
            Gets the condition upper value (valid if less) for a given condition index.
        
            condition: The condition index.
            Returns: The condition upper value.
        """
        pass

    def GetImage(self):
        """
        GetImage(self: FabricationServiceButton) -> Bitmap
        
            Gets the image for fabrication service button.
            Returns: System.Drawing.Bitmap represents the fabrication service button image. ll if 
             there is no preview image.
        """
        pass

    def IsUnrestrictedCondition(self, condition):
        """
        IsUnrestrictedCondition(self: FabricationServiceButton, condition: int) -> bool
        
            Checks if the condition is unrestricted.
        
            condition: The condition index.
            Returns: True if the condition is unrestricted.
        """
        pass

    def IsValid(self):
        """
        IsValid(self: FabricationServiceButton) -> bool
        
            Checks if the button contains only valid fittings.
            Returns: True if the button contains only valid fittings.
        """
        pass

    @staticmethod
    def IsValidConditionIndex(button, condition):
        """
        IsValidConditionIndex(button: FabricationServiceButton, condition: int) -> bool
        
            Validates if the given condition index is valid or not.
        
            button: The button to check.
            condition: The condition index.
            Returns: True if larger or equal to 0 and less than ConditionCount.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FabricationServiceButton, disposing: bool) """
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

    ButtonIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The button index for this button.

Get: ButtonIndex(self: FabricationServiceButton) -> int

"""

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The code of the button.

Get: Code(self: FabricationServiceButton) -> str

"""

    ConditionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of conditions.

Get: ConditionCount(self: FabricationServiceButton) -> int

"""

    GroupIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The group index for this button.

Get: GroupIndex(self: FabricationServiceButton) -> int

"""

    IsAHanger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks if the fabrication service button is hanger.

Get: IsAHanger(self: FabricationServiceButton) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricationServiceButton) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the button.

Get: Name(self: FabricationServiceButton) -> str

"""

    ServiceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fabrication service identifier for the fabrication service this button belongs to.

Get: ServiceId(self: FabricationServiceButton) -> int

"""


