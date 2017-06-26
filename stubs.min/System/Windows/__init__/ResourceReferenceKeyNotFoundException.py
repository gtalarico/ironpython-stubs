class ResourceReferenceKeyNotFoundException(InvalidOperationException, ISerializable, _Exception):
    """
    The exception that is thrown when a resource reference key cannot be found during parsing or serialization of markup extension resources.
    
    ResourceReferenceKeyNotFoundException()
    ResourceReferenceKeyNotFoundException(message: str, resourceKey: object)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ResourceReferenceKeyNotFoundException, info: SerializationInfo, context: StreamingContext)
            Reports specifics of the exception to debuggers or dialogs.
        
            info: Specific information from the serialization process.
            context: The context at the time the exception was thrown.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, resourceKey=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str, resourceKey: object)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the key that was not found and caused the exception to be thrown.

Get: Key(self: ResourceReferenceKeyNotFoundException) -> object

"""


