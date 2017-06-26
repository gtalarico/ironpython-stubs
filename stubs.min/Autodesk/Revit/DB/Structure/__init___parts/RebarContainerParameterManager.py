class RebarContainerParameterManager(object, IDisposable):
    """ Provides implementation of RebarContainer parameters overrides. """
    def AddOverride(self, paramId, value):
        """
        AddOverride(self: RebarContainerParameterManager, paramId: ElementId, value: int)
            Adds an override for the given parameter as its value will be displayed for the 
             Rebar Container element.
        
        
            paramId: The id of the parameter
            value: The override value of the parameter.
        AddOverride(self: RebarContainerParameterManager, paramId: ElementId, value: float)
            Adds an override for the given parameter as its value will be displayed for the 
             Rebar Container element.
        
        
            paramId: The id of the parameter
            value: The override value of the parameter.
        AddOverride(self: RebarContainerParameterManager, paramId: ElementId, value: ElementId)
            Adds an override for the given parameter as its value will be displayed for the 
             Rebar Container element.
        
        
            paramId: The id of the parameter
            value: The override value of the parameter.
        AddOverride(self: RebarContainerParameterManager, paramId: ElementId, value: str)
            Adds an override for the given parameter as its value will be displayed for the 
             Rebar Container element.
        
        
            paramId: The id of the parameter
            value: The override value of the parameter.
        """
        pass

    def AddSharedParameterAsOverride(self, paramId):
        """
        AddSharedParameterAsOverride(self: RebarContainerParameterManager, paramId: ElementId)
            Adds a shared parameter as one of the parameter overrides stored by this Rebar 
             Container element.
        
        
            paramId: The id of the shared parameter element
        """
        pass

    def ClearOverrides(self):
        """
        ClearOverrides(self: RebarContainerParameterManager)
            Clears any overridden values from all parameters of the associated 
             RebarContainer element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RebarContainerParameterManager) """
        pass

    def IsOverriddenParameterModifiable(self, paramId):
        """
        IsOverriddenParameterModifiable(self: RebarContainerParameterManager, paramId: ElementId) -> bool
        
            Checks if overridden parameter is modifiable.
        
            paramId: Overridden parameter id
            Returns: True if the parameter is modifiable, false if the parameter is readonly.
        """
        pass

    def IsParameterOverridden(self, paramId):
        """
        IsParameterOverridden(self: RebarContainerParameterManager, paramId: ElementId) -> bool
        
            Checks if the parameter has an override
        
            paramId: The id of the parameter element
            Returns: True if the parameter has an override
        """
        pass

    def IsRebarContainerParameter(self, paramId):
        """
        IsRebarContainerParameter(self: RebarContainerParameterManager, paramId: ElementId) -> bool
        
            Checks if the parameter is a Rebar Container parameter
        
            paramId: The id of the parameter element
            Returns: True if the parameter is  a Rebar Container parameter
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarContainerParameterManager, disposing: bool) """
        pass

    def RemoveOverride(self, paramId):
        """
        RemoveOverride(self: RebarContainerParameterManager, paramId: ElementId)
            Removes an overridden value from the given parameter.
        
            paramId: The id of the parameter
        """
        pass

    def SetOverriddenParameterModifiable(self, paramId):
        """
        SetOverriddenParameterModifiable(self: RebarContainerParameterManager, paramId: ElementId)
            Sets this overridden parameter to be modifiable.
        
            paramId: Overridden parameter id
        """
        pass

    def SetOverriddenParameterReadonly(self, paramId):
        """
        SetOverriddenParameterReadonly(self: RebarContainerParameterManager, paramId: ElementId)
            Sets this overridden parameter to be readonly.
        
            paramId: Overridden parameter id
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

Get: IsValidObject(self: RebarContainerParameterManager) -> bool

"""


