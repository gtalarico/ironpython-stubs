# encoding: utf-8
# module Autodesk.Revit.Exceptions calls itself Exceptions
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ApplicationException(Exception):
    """ The exception that is thrown when a non-fatal application error occurs. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ApplicationException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    FunctionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The information of the function throwing the exception.

Get: FunctionId(self: ApplicationException) -> FunctionId

"""



class ArgumentException(ApplicationException):
    """ The exception that is thrown when one of the arguments provided to a method is not valid. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ArgumentException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error message and the parameter name, or only the error message if no parameter name is set.

Get: Message(self: ArgumentException) -> str

"""

    ParamName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the parameter that causes this exception.

Get: ParamName(self: ArgumentException) -> str

"""



class ArgumentNullException(ArgumentException):
    """ The exception that is thrown when ll is passed to a method that does not accept it as a valid argument. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ArgumentNullException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class ArgumentOutOfRangeException(ArgumentException):
    """ The exception that is thrown when the value of an argument is outside the allowable range of values as defined by the invoked method. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ArgumentOutOfRangeException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class ArgumentsInconsistentException(ArgumentException):
    """ The exception that is thrown when each individual argument is OK, but a joint constraint is violated. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ArgumentsInconsistentException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class InvalidOperationException(ApplicationException):
    """ The exception that is thrown when a method call is invalid for the object's current state. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: InvalidOperationException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class AutoJoinFailedException(InvalidOperationException):
    """ The exception that is thrown when an autojoin operation failed. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: AutoJoinFailedException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class BackgroundTaskCancelledException(ApplicationException):
    """
    The exception thrown when Revit cancels a background operation. Third-party 
    developers are not expected to catch and handle this exception. Instead, if allowed
    to propagate back to Revit code, it will be handled by Revit.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: BackgroundTaskCancelledException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class CannotOpenBothCentralAndLocalException(InvalidOperationException):
    """
    The exception thrown when both a central model
    and also a local file for the same central model are opened in the same session.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: CannotOpenBothCentralAndLocalException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class CentralModelException(ApplicationException):
    """
    The base class for exceptions that are 
    common to both file-based and server-based central models or 
    specific to just file-based central models.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: CentralModelException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class CentralFileCommunicationException(CentralModelException):
    """ The exception thrown when there is a network communication error involving a file-based central model. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: CentralFileCommunicationException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class CentralModelAccessDeniedException(CentralModelException):
    """
    The exceptions thrown when a central model can be reached but 
    access is denied due to a lack of access privileges.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: CentralModelAccessDeniedException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class CentralModelAlreadyExistsException(CentralModelException):
    """ Exception is thrown when the central model already exists at the specified location. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: CentralModelAlreadyExistsException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class CentralModelContentionException(CentralModelException):
    """
    The exception thrown when a central model is busy (locked) 
    and the operation is canceled.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: CentralModelContentionException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class CorruptModelException(ApplicationException):
    """ The exception that is thrown when the model is or seems corrupt. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: CorruptModelException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class IOException(ApplicationException):
    """ The exception that is thrown when an I/O error occurs. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: IOException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class DirectoryNotFoundException(IOException):
    """ The exception that is thrown when the specified directory could not be found. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: DirectoryNotFoundException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class DisabledDisciplineException(InvalidOperationException):
    """
    The exception that is thrown when the function cannot execute because
    a discipline is disabled. The exception specifies which discipline(s) would let 
    the operation succeed.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: DisabledDisciplineException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class ExternalApplicationException(ApplicationException):
    """ The exception that is thrown when an issue in the Add-Ins resulted in an unexpected error. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ExternalApplicationException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class FamilyContextException(InvalidOperationException):
    """ The exception that is thrown when an operation is invalid in the current family document, because of the type of family. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: FamilyContextException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class FileAccessException(IOException):
    """ The exception that is thrown when the specified file could not be accessed, e.g. read-only, locked by the OS etc. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: FileAccessException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class FileArgumentAlreadyExistsException(ArgumentException):
    """ The exception that is thrown when the specified file exists. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: FileArgumentAlreadyExistsException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class FileArgumentNotFoundException(ArgumentException):
    """ The exception that is thrown when a method received a filename as an argument and requires it to exist as a precondition. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: FileArgumentNotFoundException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class FileNotFoundException(IOException):
    """ The exception that is thrown when the specified file could not be found. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: FileNotFoundException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class ForbiddenForDynamicUpdateException(InvalidOperationException):
    """ The exception that is thrown when making or attempting to make changes that are forbidden during dynamic updates to the model. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ForbiddenForDynamicUpdateException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class FunctionId(object):
    """ The information of a function throwing an exception. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: FunctionId, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    File = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the file including the function throwing an exception.

Get: File(self: FunctionId) -> str

"""

    Function = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the function throwing an exception.

Get: Function(self: FunctionId) -> str

"""

    Line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The line number of the function throwing an exception.

Get: Line(self: FunctionId) -> int

"""



class InapplicableDataException(InvalidOperationException):
    """ The exception that is thrown when attempting to access a piece of data that is structurally not part of an object at the moment. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: InapplicableDataException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class InsufficientResourcesException(InvalidOperationException):
    """
    The exception that is thrown when the OS runs out of resources, 
    e.g. memory, disk space, or USER or GDI objects.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: InsufficientResourcesException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class InternalException(ApplicationException):
    """ The exception that is thrown when an issue in the Revit code resulted in an unexpected error. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: InternalException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class InvalidDataStreamException(IOException):
    """ The exception that is thrown when the reading or saving operation failed due to parsing error. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: InvalidDataStreamException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class InvalidObjectException(InvalidOperationException):
    """ The exception that is thrown when referencing an object that is no longer valid. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: InvalidObjectException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class InvalidPathArgumentException(ArgumentException):
    """
    The exception that is thrown when a method received a pathname as an argument, but the pathname is 
    illegal: too long, invalid characters, etc.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: InvalidPathArgumentException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class ModificationForbiddenException(InvalidOperationException):
    """ The exception that is thrown by the undo transaction framework when a modification operation is not allowed. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ModificationForbiddenException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class ModificationOutsideTransactionException(InvalidOperationException):
    """ The exception that is thrown by the undo transaction framework when the modification operation to the model is outside of a transaction. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ModificationOutsideTransactionException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class NotTransmittedModelException(InvalidOperationException):
    """
    The exception thrown when OpenOptions were provided to deal with
    a transmitted model, but the model is not transmitted.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: NotTransmittedModelException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class ObjectAccessException(InvalidOperationException):
    """ The exception that is thrown when an operation is denied, e.g. an attempt was made to set a read-only property. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ObjectAccessException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class OperationCanceledException(ApplicationException):
    """ The exception that is thrown when an operation is unexpectedly cancelled. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: OperationCanceledException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class OptionalFunctionalityNotAvailableException(InvalidOperationException):
    """ The exception that is thrown when the optional functionality is not available in the installed Revit """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: OptionalFunctionalityNotAvailableException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class OutdatedDirectlyOpenedCentralException(CentralModelException):
    """
    The exception thrown when a central model is opened directly and its copy in the session is 
    outdated.  If the operation is supported for local files, first resave as local, and try again.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: OutdatedDirectlyOpenedCentralException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class RegenerationFailedException(InvalidOperationException):
    """ The exception that is thrown when a regeneration operation failed. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: RegenerationFailedException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class RevitServerException(ApplicationException):
    """ The exception that is base class for all exceptions originating from the Revit server. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: RevitServerException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class RevitServerCollaborationNotAvailableException(RevitServerException):
    """ The exception that is thrown when Collaboration fails because of an external resource (e.g., Amazon S3) failure. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: RevitServerCollaborationNotAvailableException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class RevitServerCommunicationException(RevitServerException):
    """ The exception that is thrown when there is any network communication error happening. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: RevitServerCommunicationException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class RevitServerInternalException(RevitServerException):
    """ The exception that is thrown when there is any server internal error happening. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: RevitServerInternalException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class RevitServerUnauthenticatedUserException(RevitServerException):
    """ The exception that is thrown when an unauthenticated user attempts to initiate a call to RevitServer. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: RevitServerUnauthenticatedUserException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class RevitServerUnauthorizedException(RevitServerException):
    """ The exception that is thrown when a call to the server is unauthorized. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: RevitServerUnauthorizedException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class TransientElementCreationException(InvalidOperationException):
    """ The exception that is thrown when TransientElementCreationScope is used incorrectly. """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: TransientElementCreationException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class TransmittedModelException(InvalidOperationException):
    """
    The exception thrown when model was transmitted (sent by eTransmit)
    and insufficient OpenOptions were provided to handle its transmitted flag.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: TransmittedModelException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


class WrongUserException(InvalidOperationException):
    """
    The exception thrown when a local model is manipulated under 
    a different username than it was created with.
    """
    def GetObjectData(self, info, context):
        """
        GetObjectData(self: WrongUserException, info: SerializationInfo, context: StreamingContext)
            Retrieves data needed to serialize the target object.
        
            info: Data needed to serialize or deserialize the object.
            context: The destination of the serialized stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass


