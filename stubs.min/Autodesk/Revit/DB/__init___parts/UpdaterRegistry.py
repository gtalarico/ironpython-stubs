class UpdaterRegistry(object, IDisposable):
    """ An object that stores and manages all updaters registered in the current session. """
    @staticmethod
    def AddTrigger(id, *__args):
        """
        AddTrigger(id: UpdaterId, document: Document, elements: ICollection[ElementId], change: ChangeType)AddTrigger(id: UpdaterId, document: Document, filter: ElementFilter, change: ChangeType)
            Adds trigger with the specified element filter and ChangeType for the specified 
             document
        
        
            id: Id of updater that trigger should be added to
            document: Document that elements in 'elements' are contained in
            filter: Element filter that defines elements that affect this trigger
            change: ChangeType associated with this trigger
        AddTrigger(id: UpdaterId, filter: ElementFilter, change: ChangeType)
            Adds trigger with the specified element filter and ChangeType for all documents 
             associated with this Updater
        
        
            id: Id of updater that trigger should be added to
            filter: Element filter that defines elements that affect this trigger
            change: ChangeType associated with this trigger
        """
        pass

    @staticmethod
    def DisableUpdater(id):
        """
        DisableUpdater(id: UpdaterId)
            Disables the updater.
        
            id: The updater id.
        """
        pass

    def Dispose(self):
        """ Dispose(self: UpdaterRegistry) """
        pass

    @staticmethod
    def EnableUpdater(id):
        """
        EnableUpdater(id: UpdaterId)
            Enables the updater.
        
            id: The updater id.
        """
        pass

    @staticmethod
    def GetIsUpdaterOptional(id):
        """
        GetIsUpdaterOptional(id: UpdaterId) -> bool
        
            Check if the updater is optional or not.
        
            id: Id of the updater to check
            Returns: Returns True if the updater is optional, False otherwise.
        """
        pass

    @staticmethod
    def GetRegisteredUpdaterInfos(document=None):
        """
        GetRegisteredUpdaterInfos(document: Document) -> IList[UpdaterInfo]
        
            Returns information about all updaters applicable to the given document.
        
            document: The document to which sought updaters are applicable to.
            Returns: List of UpdaterInfo structures
        GetRegisteredUpdaterInfos() -> IList[UpdaterInfo]
        
            Returns UpdaterInfos for all the application-wide updaters.
            Returns: List of UpdaterInfo structures
        """
        pass

    @staticmethod
    def IsUpdaterEnabled(id):
        """
        IsUpdaterEnabled(id: UpdaterId) -> bool
        
            Checks if the updater is enabled or not.
        
            id: The updater id.
            Returns: Returns true if the updater is enabled, false otherwise.
        """
        pass

    @staticmethod
    def IsUpdaterRegistered(id, document=None):
        """
        IsUpdaterRegistered(id: UpdaterId) -> bool
        
            Checks whether updater with the given id is registered
        
            id: Id of the updater being tested.
            Returns: Returns true if the updater is registered.
        IsUpdaterRegistered(id: UpdaterId, document: Document) -> bool
        
            Checks whether updater with the given id is registered in a document.
        
            id: Id of the updater being tested.
            document: Document in which this updater is tested whether it's registered or not.
            Returns: Returns True if the updater is registered in the given document.
        """
        pass

    @staticmethod
    def RegisterUpdater(updater, *__args):
        """
        RegisterUpdater(updater: IUpdater, document: Document)
            Registers the updater for a specified document, which means
           the updater can 
             only be triggered by changes made in that document.
        
        
            updater: Updater to be registered
            document: Document for which this updater is to be registered
        RegisterUpdater(updater: IUpdater)
            Registers an updater application-wide, which means
           the updater may get 
             triggered in any open document.
        
        
            updater: Updater to be registered
        RegisterUpdater(updater: IUpdater, document: Document, isOptional: bool)
            Registers the updater for a specified document, which means
           the updater can 
             only be triggered by changes made in that document.
        
        
            updater: Updater to be registered.
            document: Document for which this updater is to be registered.
            isOptional: This argument controls whether the updater should be required next time a 
             document
           is open in which the updater had been previously used. If a 
             non-optional updater is
           not found (i.e. currently not registered), the end 
             user will be presented with a warning
           and choices to resolve the situation.
        
        RegisterUpdater(updater: IUpdater, isOptional: bool)
            Registers an updater application-wide, which means
           the updater may get 
             triggered in any open document.
        
        
            updater: Updater to be registered
            isOptional: This argument controls whether the updater should be required next time a 
             document
           is open in which the updater had been previously used. If a 
             non-optional updater is
           not found (i.e. currently not registered), the end 
             user will be presented with a warning
           and choices to resolve the situation.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: UpdaterRegistry, disposing: bool) """
        pass

    @staticmethod
    def RemoveAllTriggers(id):
        """
        RemoveAllTriggers(id: UpdaterId)
            Removes all triggers associated with Updater with specified UpdaterId.
           Does 
             not unregister updater.
        
        
            id: Id of specified updater
        """
        pass

    @staticmethod
    def RemoveDocumentTriggers(id, document):
        """
        RemoveDocumentTriggers(id: UpdaterId, document: Document)
            Removes all triggers associated with specified document and Updater
           Does 
             not unregister updater.
        
        
            id: Id of specified updater
            document: Document for which to remove triggers
        """
        pass

    @staticmethod
    def SetExecutionOrder(first, second):
        """
        SetExecutionOrder(first: UpdaterId, second: UpdaterId)
            Forces execution order between two updaters
           Execution order: first before 
             second
        
        
            first: Id of first Updater
            second: Id of second Updater
        """
        pass

    @staticmethod
    def SetIsUpdaterOptional(id, isOptional):
        """
        SetIsUpdaterOptional(id: UpdaterId, isOptional: bool)
            Sets a flag indicating whether an updater is optional or not.
        
            id: Id of the updater
            isOptional: Use True to make the updater optional, false to make it a mandatory updater.
        """
        pass

    @staticmethod
    def UnregisterUpdater(id, document=None):
        """
        UnregisterUpdater(id: UpdaterId)
            Removes the updater associated with the input id from the UpdaterRegistry.
           
             Also removes all triggers associated with the Updater.
        
        
            id: Id of updater to be removed
        UnregisterUpdater(id: UpdaterId, document: Document)
            Unregisters an updater for the given document.
        
            id: Id of updater to be unregistered.
            document: Document for which this updater is to be unregistered.
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: UpdaterRegistry) -> bool

"""


