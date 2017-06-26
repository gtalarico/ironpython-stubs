class ManagedToNativeComInteropStubAttribute(Attribute, _Attribute):
    """
    Provides support for user customization of interop stubs in managed-to-COM interop scenarios.
    
    ManagedToNativeComInteropStubAttribute(classType: Type, methodName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, classType, methodName):
        """ __new__(cls: type, classType: Type, methodName: str) """
        pass

    ClassType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the class that contains the required stub method.

Get: ClassType(self: ManagedToNativeComInteropStubAttribute) -> Type

"""

    MethodName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the stub method.

Get: MethodName(self: ManagedToNativeComInteropStubAttribute) -> str

"""


