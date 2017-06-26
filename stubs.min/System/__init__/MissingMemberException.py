class MissingMemberException(MemberAccessException, ISerializable, _Exception):
    """
    The exception that is thrown when there is an attempt to dynamically access a class member that does not exist.
    
    MissingMemberException()
    MissingMemberException(message: str)
    MissingMemberException(message: str, inner: Exception)
    MissingMemberException(className: str, memberName: str)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: MissingMemberException, info: SerializationInfo, context: StreamingContext)
            Sets the System.Runtime.Serialization.SerializationInfo object with the class name, the member name, the signature of the missing member, and additional exception information.
        
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
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, className: str, memberName: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text string showing the class name, the member name, and the signature of the missing member.

Get: Message(self: MissingMemberException) -> str

"""


    ClassName = None
    MemberName = None
    Signature = None

