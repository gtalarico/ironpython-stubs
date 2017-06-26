class Object:
    """
    Supports all classes in the .NET Framework class hierarchy and provides low-level services to derived classes. This is the ultimate base class of all classes in the .NET Framework; it is the root of the type hierarchy.
    
    object()
    """
    def __delattr__(self, *args): #cannot find CLR method
        """
        __delattr__(self: object, name: str)
            Removes an attribute from the provided member
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(self: object, formatSpec: str) -> str """
        pass

    def __getattribute__(self, *args): #cannot find CLR method
        """
        __getattribute__(self: object, name: str) -> object
        
            Gets the specified attribute from the object without running any custom lookup behavior
                    (__getattr__ and __getattribute__)
        """
        pass

    def __hash__(self, *args): #cannot find CLR method
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type, **kwargs�: dict, *args�: Array[object]) -> object
        __new__(cls: type, *args�: Array[object]) -> object
        
            Creates a new instance of the type
        __new__(cls: type) -> object
        
            Creates a new instance of the type
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __reduce__(self, *args): #cannot find CLR method
        """ helper for pickle """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """
        __repr__(self: object) -> str
        
            Returns the code representation of the object.  The default implementation returns
                    a string which consists of the type and a unique numerical identifier.
        """
        pass

    def __setattr__(self, *args): #cannot find CLR method
        """
        __setattr__(self: object, name: str, value: object)
            Sets an attribute on the object without running any custom object defined behavior.
        """
        pass

    def __sizeof__(self, *args): #cannot find CLR method
        """
        __sizeof__(self: object) -> int
        
            Returns the number of bytes of memory required to allocate the object.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __subclasshook__(self, *args): #cannot find CLR method
        """ __subclasshook__(*args: Array[object]) -> NotImplementedType """
        pass

    __class__ = None

