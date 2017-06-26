class OverflowException(ArithmeticException, ISerializable, _Exception):
    """
    The exception that is thrown when an arithmetic, casting, or conversion operation in a checked context results in an overflow.
    
    OverflowException()
    OverflowException(message: str)
    OverflowException(message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

