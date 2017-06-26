class PlanCircuit(APIObject, IDisposable):
    """ An object that represents an enclosed area in a plan view within the Autodesk Revit project. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def GetPointInside(self):
        """
        GetPointInside(self: PlanCircuit) -> UV
        
            Returns a point inside the circuit.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The enclosed area of the circuit.

Get: Area(self: PlanCircuit) -> float

"""

    IsRoomLocated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reports whether there is a room located in this circuit.

Get: IsRoomLocated(self: PlanCircuit) -> bool

"""

    SideNum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of sides in the circuit.

Get: SideNum(self: PlanCircuit) -> int

"""


