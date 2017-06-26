class NotFiniteNumberException(ArithmeticException, ISerializable, _Exception):
    """
    The exception that is thrown when a floating-point value is positive infinity, negative infinity, or Not-a-Number (NaN).
    
    NotFiniteNumberException()
    NotFiniteNumberException(offendingNumber: float)
    NotFiniteNumberException(message: str)
    NotFiniteNumberException(message: str, offendingNumber: float)
    NotFiniteNumberException(message: str, innerException: Exception)
    NotFiniteNumberException(message: str, offendingNumber: float, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: NotFiniteNumberException, info: SerializationInfo, context: StreamingContext)
            Sets the System.Runtime.Serialization.SerializationInfo object with the invalid number and additional exception information.
        
            info: The object that holds the serialized object data.
            context: The contextual information about the source or destination.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, offendingNumber: float)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, offendingNumber: float)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str, offendingNumber: float, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    OffendingNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the invalid number that is a positive infinity, a negative infinity, or Not-a-Number (NaN).

Get: OffendingNumber(self: NotFiniteNumberException) -> float

"""


