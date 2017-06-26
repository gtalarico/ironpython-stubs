class ListChangedType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how the list changed.
    
    enum ListChangedType, values: ItemAdded (1), ItemChanged (4), ItemDeleted (2), ItemMoved (3), PropertyDescriptorAdded (5), PropertyDescriptorChanged (7), PropertyDescriptorDeleted (6), Reset (0)
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

    ItemAdded = None
    ItemChanged = None
    ItemDeleted = None
    ItemMoved = None
    PropertyDescriptorAdded = None
    PropertyDescriptorChanged = None
    PropertyDescriptorDeleted = None
    Reset = None
    value__ = None

