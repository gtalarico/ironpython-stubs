class DoubleClickTarget(Enum, IComparable, IFormattable, IConvertible):
    """
    Elements that support double-click in Revit.  Note that this is meant to cover cases
       where the element itself is a double-click target.  Individual controls that are targets
       are handled separately.
    
    enum DoubleClickTarget, values: Assembly (3), ComponentStairs (5), Family (0), Group (4), OutsideViewOnSheet (6), SketchedElement (1), ViewOnSheet (2)
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

    Assembly = None
    ComponentStairs = None
    Family = None
    Group = None
    OutsideViewOnSheet = None
    SketchedElement = None
    value__ = None
    ViewOnSheet = None

