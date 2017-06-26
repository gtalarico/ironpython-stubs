class ClassInterfaceAttribute(Attribute, _Attribute):
    """
    Indicates the type of class interface to be generated for a class exposed to COM, if an interface is generated at all.
    
    ClassInterfaceAttribute(classInterfaceType: ClassInterfaceType)
    ClassInterfaceAttribute(classInterfaceType: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, classInterfaceType):
        """
        __new__(cls: type, classInterfaceType: ClassInterfaceType)
        __new__(cls: type, classInterfaceType: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Runtime.InteropServices.ClassInterfaceType value that describes which type of interface should be generated for the class.

Get: Value(self: ClassInterfaceAttribute) -> ClassInterfaceType

"""


