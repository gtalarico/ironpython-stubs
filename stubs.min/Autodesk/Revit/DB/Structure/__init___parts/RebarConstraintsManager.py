class RebarConstraintsManager(object, IDisposable):
    """
    A class used to obtain information about the constraints (RebarConstraints) acting
       on the shape handles (RebarConstrainedHandles) of a Rebar element, and to replace
       default constraints with user-preferred choices.
    """
    def ClearHandleConstraintPairHighlighting(self, aDoc):
        """
        ClearHandleConstraintPairHighlighting(self: RebarConstraintsManager, aDoc: Document)
            Clears all highlighting in all views.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RebarConstraintsManager) """
        pass

    def GetAllConstrainedHandles(self):
        """
        GetAllConstrainedHandles(self: RebarConstraintsManager) -> IList[RebarConstrainedHandle]
        
            Retrieves all handles on the Rebar that are constrained to external references.
            Returns: A collection of RebarConstrainedHandles
        """
        pass

    def GetConstraintCandidatesForHandle(self, handle):
        """
        GetConstraintCandidatesForHandle(self: RebarConstraintsManager, handle: RebarConstrainedHandle) -> IList[RebarConstraint]
        
            Returns all possible RebarConstraints that could be used for a specified 
             RebarConstrainedHandle.
        
        
            handle: The RebarConstrainedHandle for which constraint candidates are sought.
            Returns: A collection of RebarConstraints
        """
        pass

    def GetCurrentConstraintOnHandle(self, handle):
        """
        GetCurrentConstraintOnHandle(self: RebarConstraintsManager, handle: RebarConstrainedHandle) -> RebarConstraint
        
            Retrieves the RebarConstraint that acts on the specified RebarConstraintHandle.
        """
        pass

    def GetPreferredConstraintOnHandle(self, handle):
        """
        GetPreferredConstraintOnHandle(self: RebarConstraintsManager, handle: RebarConstrainedHandle) -> RebarConstraint
        
            Returns the RebarConstraint that has been set as preferred for the specified 
             RebarConstrainedHandle.
        
        
            handle: The RebarConstrainedHandle for which the user RebarConstraint is to be returned.
            Returns: The user prefered RebarConstraint applied to the RebarConstrainedHandle.
        """
        pass

    def HasValidRebar(self):
        """
        HasValidRebar(self: RebarConstraintsManager) -> bool
        
            Checks whether the Manager's Rebar is still valid.
        """
        pass

    def HighlightHandleConstraintPairInAllViews(self, aDoc, handle, constraint):
        """
        HighlightHandleConstraintPairInAllViews(self: RebarConstraintsManager, aDoc: Document, handle: RebarConstrainedHandle, constraint: RebarConstraint)
            Highlights the specified RebarConstrainedHandle and RebarConstraint in all 
             views.
        
        
            handle: The RebarConstrainedHandle to be highlighted in all views.
            constraint: The RebarConstraint to be highlighted in all views.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarConstraintsManager, disposing: bool) """
        pass

    def RemovePreferredConstraintFromHandle(self, handle):
        """
        RemovePreferredConstraintFromHandle(self: RebarConstraintsManager, handle: RebarConstrainedHandle)
            Clears the user-preferred RebarConstraint from the specified 
             RebarConstrainedHandle.
        
        
            handle: The RebarConstrainedHandle for which the user RebarConstraint is to be deleted.
        """
        pass

    def SetPreferredConstraintForHandle(self, handle, constraint):
        """
        SetPreferredConstraintForHandle(self: RebarConstraintsManager, handle: RebarConstrainedHandle, constraint: RebarConstraint)
            Sets the RebarConstraint as preferred constraint target for the specified 
             RebarConstrainedHandle.
        
        
            handle: The RebarConstrainedHandle to which the new RebarConstraint is to be applied.
            constraint: The new RebarConstraint to be applied to the RebarConstrainedHandle.
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

Get: IsValidObject(self: RebarConstraintsManager) -> bool

"""


    IsRebarConstrainedPlacementEnabled = False

