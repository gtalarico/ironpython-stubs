class RebarShapeConstraint(object, IDisposable):
    """ A dimension or other constraint that takes part in a RebarShapeDefinition. """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint) """
        pass

    def GetParamId(self):
        """
        GetParamId(self: RebarShapeConstraint) -> ElementId
        
            Return the Id of the parameter associated with this constraint.
            Returns: The Id of the parameter, or InvalidElementId if the constraint
           does not 
             have one.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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

Get: IsValidObject(self: RebarShapeConstraint) -> bool

"""


