class RebarCoupler(Element, IDisposable):
    """ Represents a rebar coupler element in Autodesk Revit. """
    def CouplerLinkTwoBars(self):
        """
        CouplerLinkTwoBars(self: RebarCoupler) -> bool
        
            returns true if the coupler sits on two rebar and false otherwise
        """
        pass

    @staticmethod
    def Create(doc, typeId, pFirstData, pSecondData, error):
        """
        Create(doc: Document, typeId: ElementId, pFirstData: ReinforcementData, pSecondData: ReinforcementData) -> (RebarCoupler, RebarCouplerError)
        
            Creates a new instance of a Rebar Coupler element within the project.
        
            doc: A document.
            typeId: type id for coupler
            pFirstData: information about the first reinforcement to be coupled
            pSecondData: information about the second reinforcement to be coupled; for the default 
             value, coupler is placed on one reinforcement
        
            Returns: The newly created Rebar Coupler instance, or ll if the operation fails.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCoupledReinforcementData(self):
        """
        GetCoupledReinforcementData(self: RebarCoupler) -> IList[ReinforcementData]
        
            gets the reinforcement data. If coupler stays on one bar the list will have 
             size = 1. If coupler connects two bars the size will be 2.
        """
        pass

    def GetCouplerPositionTransform(self, couplerPositionIndex):
        """
        GetCouplerPositionTransform(self: RebarCoupler, couplerPositionIndex: int) -> Transform
        
            Return a transform representing the relative position of the coupler at index 
             couplerPositionIndex in the set.
        
        
            couplerPositionIndex: An index between 0 and (CouplerQuantity-1).
            Returns: The position of a coupler in the set relative (0,0,0).
        """
        pass

    def GetCouplerQuantity(self):
        """
        GetCouplerQuantity(self: RebarCoupler) -> int
        
            Identifies the number of couplers in a set.
            Returns: Returns the number of couplers in a set.
        """
        pass

    def GetPointsForPlacement(self):
        """
        GetPointsForPlacement(self: RebarCoupler) -> IList[XYZ]
        
            gets the point (or points in case of rebar set) where the coupler is placed
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
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

    CouplerMark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """gets and sets the coupler mark

Get: CouplerMark(self: RebarCoupler) -> str

Set: CouplerMark(self: RebarCoupler) = value
"""


