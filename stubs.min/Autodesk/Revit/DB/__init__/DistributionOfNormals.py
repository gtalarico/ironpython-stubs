class DistributionOfNormals(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumeration containing the choices of how normal vectors are assigned
       and distributed along the surface of a polymesh. Planar faces would typically
       have only normal vector associated, but curved faces can have a different
       normal either for each facet (triangle) or each point of the tessellated polymesh.
    
    enum DistributionOfNormals, values: AtEachPoint (0), OnEachFacet (2), OnePerFace (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AtEachPoint = None
    OnEachFacet = None
    OnePerFace = None
    value__ = None

