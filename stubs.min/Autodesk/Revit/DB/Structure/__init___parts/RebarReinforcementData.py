class RebarReinforcementData(ReinforcementData, IDisposable):
    """ class containing the id and the end of rebar on which the coupler stays """
    @staticmethod
    def Create(rebarId, iEnd):
        """
        Create(rebarId: ElementId, iEnd: int) -> RebarReinforcementData
        
            Creates a new instance of RebarReinforcementData, or ll if the operation fails.
        
            rebarId: the Id of the rebar
            iEnd: The end of rebar where the coupler stays. This should be 0 or 1
            Returns: Creates a new instance of RebarReinforcementData
        """
        pass

    def Dispose(self):
        """ Dispose(self: ReinforcementData, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ReinforcementData, disposing: bool) """
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

    End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The end of the rebar. The end should be 0 or 1.

Get: End(self: RebarReinforcementData) -> int

Set: End(self: RebarReinforcementData) = value
"""

    RebarId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the Rebar

Get: RebarId(self: RebarReinforcementData) -> ElementId

Set: RebarId(self: RebarReinforcementData) = value
"""


