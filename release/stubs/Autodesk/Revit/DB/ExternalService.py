# encoding: utf-8
# module Autodesk.Revit.DB.ExternalService calls itself ExternalService
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DisparityResponse(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated value to return from OnServerDiparity indicating
       what the service wants Revit to do as the post-action of the call.
    
    enum DisparityResponse, values: ApplyDefaults (1), DoNothing (0), LetUserDecide (2)
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

    ApplyDefaults = None
    DoNothing = None
    LetUserDecide = None
    value__ = None


class ExecutionPolicy(Enum, IComparable, IFormattable, IConvertible):
    """
    Controls how servers of multi-server external services are executed.
    
    enum ExecutionPolicy, values: AllApplicableServers (1), FirstApplicableServer (0)
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

    AllApplicableServers = None
    FirstApplicableServer = None
    value__ = None


class ExternalService(object, IDisposable):
    """ This base class represents an external service inside Revit application. """
    def AddServer(self, server):
        """
        AddServer(self: ExternalService, server: IExternalServer)
            Registers a server with its service.
        
            server: The instance of the server. The server must implement the interface provided by 
             the service.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ExternalService) """
        pass

    def GetDefaultServerId(self):
        """
        GetDefaultServerId(self: ExternalService) -> Guid
        
            Returns the Id of the default server if one was assigned to the service.
            Returns: The GUID of the default server, or an invalid GUID if there is none assigned.
        """
        pass

    def GetOptions(self):
        """
        GetOptions(self: ExternalService) -> ExternalServiceOptions
        
            A copy of the options the service was registered with.
            Returns: An instance of the options class.
        """
        pass

    def GetPublicAccessKey(self):
        """
        GetPublicAccessKey(self: ExternalService) -> Guid
        
            Access key to use to execute a service.
            Returns: GUID representing the access key.
        """
        pass

    def GetRegisteredServerIds(self):
        """
        GetRegisteredServerIds(self: ExternalService) -> IList[Guid]
        
            Returns Ids of all servers registered for the service.
            Returns: An array of Ids of all registered servers. The array may be empty.
        """
        pass

    def GetServer(self, serverId):
        """
        GetServer(self: ExternalService, serverId: Guid) -> IExternalServer
        
            Returns the instance that provides implementation for a registered server.
        
            serverId: Id of a registered server
            Returns: An instance of the server interface. NULL is returned if the server is invalid 
             (e.g. destroyed)
        """
        pass

    def IsRegisteredServerId(self, serverId):
        """
        IsRegisteredServerId(self: ExternalService, serverId: Guid) -> bool
        
            Checks if the Id represents a valid server that has been registered for the 
             service.
        
        
            serverId: An Id of a server
            Returns: True if the specified server is currently registed for this service, false 
             otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExternalService, disposing: bool) """
        pass

    def RemoveServer(self, serverId):
        """
        RemoveServer(self: ExternalService, serverId: Guid)
            Removes/unregisters a server from the service.
        
            serverId: Id of the server to be unregistered.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The description for the service

Get: Description(self: ExternalService) -> str

"""

    IsSerializable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether executions of the service requires serialization in documents or not.

Get: IsSerializable(self: ExternalService) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExternalService) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the service

Get: Name(self: ExternalService) -> str

"""

    NumberOfServers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the number of servers currently registered with the service.

Get: NumberOfServers(self: ExternalService) -> int

"""

    ServiceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of the service

Get: ServiceId(self: ExternalService) -> ExternalServiceId

"""

    VendorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vendor who provided the service

Get: VendorId(self: ExternalService) -> str

"""



class ExternalServiceId(GuidEnum):
    """
    Unique identifier of an external service.
    
    ExternalServiceId(guid: Guid)
    """
    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass


class ExternalServiceOptions(object, IDisposable):
    """
    Various options affecting the behavior of an External Service
    
    ExternalServiceOptions()
    """
    def Dispose(self):
        """ Dispose(self: ExternalServiceOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExternalServiceOptions, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property denotes a service as either public or private.

Get: IsPublic(self: ExternalServiceOptions) -> bool

Set: IsPublic(self: ExternalServiceOptions) = value
"""

    IsRecordable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether executions of the service is recorded in documents or not.

Get: IsRecordable(self: ExternalServiceOptions) -> bool

Set: IsRecordable(self: ExternalServiceOptions) = value
"""

    IsSelfsynchronizing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the service's record of used services (in a particular document)
   can independently wary between local clients and the corresponding central model.
   It is then up to the service's owner to assure proper local-central synchronization.

Get: IsSelfsynchronizing(self: ExternalServiceOptions) -> bool

Set: IsSelfsynchronizing(self: ExternalServiceOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExternalServiceOptions) -> bool

"""



class ExternalServiceRegistry(object):
    """
    This class gives access to external services.
       Use it to register external services with Revit and execute them.
       Only the application that registers a service is allowed to execute it.
    """
    @staticmethod
    def ExecuteService(executionKey, *__args):
        """
        ExecuteService(executionKey: Guid, data: IExternalData) -> ExternalServiceResult
        
            Execute a service independently of any document.
        
            executionKey: Access key of the service to be executed.
           The key is not the same as the 
             service's Id. It is the value
           that was returned to the caller who 
             registered the service.
        
            data: The associated data. The type is defined by the service.
            Returns: The result of executing the external service.
        ExecuteService(executionKey: Guid, document: Document, data: IExternalData) -> ExternalServiceResult
        
            Execute the service for the given document.
        
            executionKey: Access key of the service to be executed.
           The key is not the same as the 
             service's Id. It is the value
           that was returned to the caller who 
             registered the service.
        
            document: The document for which the service is going to be executed.
            data: The associated data. The type must be of the class defined by the service.
            Returns: The result of executing the external service.
        ExecuteService(executionKey: Guid, serverId: Guid, data: IExternalData) -> ExternalServiceResult
        
            Execute the service by the given server.
        
            executionKey: Access key of the service to be executed.
           The key is not the same as the 
             service's Id. It is the value
           that was returned to the caller who 
             registered the service.
        
            serverId: the specific server to execute
            data: The associated data. The type must be of the class defined by the service.
            Returns: The result of executing the external service.
        """
        pass

    @staticmethod
    def GetService(serviceId):
        """
        GetService(serviceId: ExternalServiceId) -> ExternalService
        
            Returns an instance of an object that represents the external service with the 
             given Id.
        
        
            serviceId: Id of the service.
            Returns: The instance of the service or NULL if it cannot be found.
        """
        pass

    @staticmethod
    def GetServices():
        """
        GetServices() -> IList[ExternalService]
        
            Returns a collection of all external services currently registered in Revit.
            Returns: Array of ExternalService instances.
        """
        pass

    @staticmethod
    def RegisterService(service, *__args):
        """
        RegisterService(service: ISingleServerService, options: ExternalServiceOptions) -> Guid
        
            A method to register a single-server service.
        
            service: An instance of the external service class that implements ISingleServerService 
             interface.
        
            options: Optional settings to control the service's behavior.
            Returns: An access key to the service. The key is needed to execute the service.
        RegisterService(service: IMultiServerService, options: ExternalServiceOptions, policy: ExecutionPolicy) -> Guid
        
            A method to register a multi-server service.
        
            service: An instance of the external service class that implements IMultiServerService 
             interface.
        
            options: Optional settings to control the service's behavior.
            policy: Specifies how the service handles servers during its execution.
            Returns: An execution key to access the service when executing it.
        RegisterService(service: ISingleServerService, defaultServerId: Guid, options: ExternalServiceOptions) -> Guid
        
            A method to register a mandatory, single-server service.
        
            service: An instance of the external service class that implements ISingleServerService 
             interface.
        
            defaultServerId: Id of the server that will become the service's default server (once the server 
             is registered).
        
            options: Optional settings to control the service's behavior.
            Returns: An access key to the service. The key is needed to execute the service.
        """
        pass

    __all__ = [
        'ExecuteService',
        'GetService',
        'GetServices',
        'RegisterService',
    ]


class ExternalServiceResult(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated value representing a result from executing an external service.
    
    enum ExternalServiceResult, values: Failed (1), Succeeded (0), Unhandled (2)
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

    Failed = None
    Succeeded = None
    Unhandled = None
    value__ = None


class ExternalServices(object):
    """ Provides a container of all Revit built-in ExternalServiceId instances. """
    BuiltInExternalServices = None
    __all__ = [
        'BuiltInExternalServices',
    ]


class IExternalData:
    """ The base interface for data classes used when executing servers of external services. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExternalServer:
    """ The base interface for all external servers. """
    def GetDescription(self):
        """
        GetDescription(self: IExternalServer) -> str
        
            Implement this method to return a description of the server.
            Returns: Description of the server.
        """
        pass

    def GetName(self):
        """
        GetName(self: IExternalServer) -> str
        
            Implement this method to return the name of the server.
            Returns: Name of the server.
        """
        pass

    def GetServerId(self):
        """
        GetServerId(self: IExternalServer) -> Guid
        
            Implement this method to return the id of the server.
            Returns: The id of the server.
        """
        pass

    def GetServiceId(self):
        """
        GetServiceId(self: IExternalServer) -> ExternalServiceId
        
            Implement this method to return the id of the service.
            Returns: The id of the service to which the server belongs.
        """
        pass

    def GetVendorId(self):
        """
        GetVendorId(self: IExternalServer) -> str
        
            Implement this method to return the id of the vendor of the server.
            Returns: Vendor Id of the server.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExternalService:
    """ The base interface class for all external services. """
    def Execute(self, server, document, data):
        """
        Execute(self: IExternalService, server: IExternalServer, document: Document, data: IExternalData) -> bool
        
            Implement this method to execute the given server.
        
            server: An instance of a server that is to be executed.
            document: The associated document. It may be NULL if the service is not being executed
          
              in a document.
        
            data: The associated service data.
            Returns: True indicates a successful execution of the call. False indicates a failure.
         
               
           If a multi-server service returns false from the call, the service 
             manager
           will stop the execution loop and marks the service execution as 
             unsuccessful.
        """
        pass

    def GetDescription(self):
        """
        GetDescription(self: IExternalService) -> str
        
            Implement this method to return a description of the service.
            Returns: Description of the service.
        """
        pass

    def GetName(self):
        """
        GetName(self: IExternalService) -> str
        
            Implement this method to return the name of the service.
            Returns: Name of the service.
        """
        pass

    def GetServiceId(self):
        """
        GetServiceId(self: IExternalService) -> ExternalServiceId
        
            Implement this method to return the unique Id of the service.
            Returns: The extensible enum value representing the Id of the service.
        """
        pass

    def GetVendorId(self):
        """
        GetVendorId(self: IExternalService) -> str
        
            Implement this method to return the vendor Id of the service.
            Returns: Vendor Id of the service.
        """
        pass

    def IsValidServer(self, server):
        """
        IsValidServer(self: IExternalService, server: IExternalServer) -> bool
        
            Implement this method to check if the given instance represents a valid server 
             of this service.
        
        
            server: An instance of a server that is to be validated.
            Returns: True if the server is valid, False otherwise
        """
        pass

    def OnServersChanged(self, document, cause, oldServers):
        """ OnServersChanged(self: IExternalService, document: Document, cause: ServerChangeCause, oldServers: IList[Guid]) """
        pass

    def OnServersDisparity(self, document, oldServers):
        """ OnServersDisparity(self: IExternalService, document: Document, oldServers: IList[Guid]) -> DisparityResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IMultiServerService(IExternalService):
    """ The base interface class for all multi-server services. """
    def CanExecute(self, server, document, data):
        """
        CanExecute(self: IMultiServerService, server: IExternalServer, document: Document, data: IExternalData) -> bool
        
            Implement this to test whether a particular server should be executed.
        
            server: An instance of a server that is to be tested.
            document: The associated document. It may be NULL if not applicable.
            data: The associated service data. It is the same data the Execute method would 
             receive.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISingleServerService(IExternalService):
    """ The base interface class for all single-server services. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class MultiServerService(ExternalService, IDisposable):
    """
    This class represents a multi-server service inside Revit application.
       It is created when an instance of IMultiServerService is registered with Revit.
    """
    def Dispose(self):
        """ Dispose(self: ExternalService, A_0: bool) """
        pass

    def GetActiveServerIds(self, document=None):
        """
        GetActiveServerIds(self: MultiServerService) -> IList[Guid]
        
            Returns Ids of the currently active application-level servers registered for 
             the service.
        
            Returns: A set of GUIDs of the application-wide active servers; the list may be empty.
        GetActiveServerIds(self: MultiServerService, document: Document) -> IList[Guid]
        
            Returns Ids of the servers currently applicable to the given document for the 
             service.
        
        
            document: The associated document.
            Returns: A set of GUIDs of the document-applicable active servers; the list may be empty.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExternalService, disposing: bool) """
        pass

    def SetActiveServers(self, serverIds, document=None):
        """ SetActiveServers(self: MultiServerService, serverIds: IList[Guid])SetActiveServers(self: MultiServerService, serverIds: IList[Guid], document: Document) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ExecutionPolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies how a multi-server service executes servers during its execution.

Get: ExecutionPolicy(self: MultiServerService) -> ExecutionPolicy

"""



class ServerChangeCause(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates the cause for the active server to be changed
    
    enum ServerChangeCause, values: ImposedChange (0), UserChange (1)
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

    ImposedChange = None
    UserChange = None
    value__ = None


class SingleServerService(ExternalService, IDisposable):
    """
    This class represents a single-server service inside Revit application.
       It is created when an instance of ISingleServerService is registered with Revit.
    """
    def Dispose(self):
        """ Dispose(self: ExternalService, A_0: bool) """
        pass

    def GetActiveServerId(self, document=None):
        """
        GetActiveServerId(self: SingleServerService) -> Guid
        
            Returns the Id of the currently active application-level server of the service.
            Returns: The GUID of the active server, or an invalid GUID if there is no active server 
             assigned.
        
        GetActiveServerId(self: SingleServerService, document: Document) -> Guid
        
            Returns the Id of the server currently associated with the given document for 
             the service.
        
        
            document: The document for which the server is being set as active.
            Returns: The Guid of the active server, or an invalid Guid if there is no active server 
             assigned.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExternalService, disposing: bool) """
        pass

    def SetActiveServer(self, serverId, document=None):
        """
        SetActiveServer(self: SingleServerService, serverId: Guid)
            Set an active server applicable application-wide for the service.
        
            serverId: Id of the application server.
        SetActiveServer(self: SingleServerService, serverId: Guid, document: Document)
            Change the active server for a specific document.
        
            serverId: Id of the server.
            document: The document for which the server is being set as active.
        """
        pass

    def UnsetActiveServer(self, document):
        """
        UnsetActiveServer(self: SingleServerService, document: Document)
            Unset the active server for the particular document.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


