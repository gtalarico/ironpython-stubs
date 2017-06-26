class MissingFieldException(MissingMemberException, ISerializable, _Exception):
    """
    The exception that is thrown when there is an attempt to dynamically access a field that does not exist.
    
    MissingFieldException()
    MissingFieldException(message: str)
    MissingFieldException(message: str, inner: Exception)
    MissingFieldException(className: str, fieldName: str)
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
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, className: str, fieldName: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text string showing the signature of the missing field, the class name, and the field name. This property is read-only.

Get: Message(self: MissingFieldException) -> str

"""


    ClassName = None
    MemberName = None
    Signature = None

