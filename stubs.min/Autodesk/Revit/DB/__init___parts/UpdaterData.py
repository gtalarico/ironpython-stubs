class UpdaterData(object, IDisposable):
    """ Service class that is passed to an Updater to prove access to update execution context """
    def Dispose(self):
        """ Dispose(self: UpdaterData) """
        pass

    def GetAddedElementIds(self):
        """
        GetAddedElementIds(self: UpdaterData) -> ICollection[ElementId]
        
            Returns set of elements newly added to the document.
           This set is mutually 
             exclusive of elements returned by getDeletedElementIds() and 
             getModifiedElementIds().
        
            Returns: Set of elements that were added to the document and triggered the call to 
             execute()
           Note: This will only return elements if the trigger registered 
             for the associated updater
           contains the ChangeType returned by 
             Element::getChangeTypeElementAddition()
        """
        pass

    def GetDeletedElementIds(self):
        """
        GetDeletedElementIds(self: UpdaterData) -> ICollection[ElementId]
        
            Returns set of elements that were deleted from the document.
           This set is 
             mutually exclusive of elements returned by getAddedElementIds() and 
             getModifiedElementIds().
        
            Returns: Set of elements that were deleted from the document and triggered the call to 
             execute()
           Note: This will only return elements if the trigger registered 
             for the associated updater
           contains the ChangeType returned by 
             Element::getChangeTypeElementDeletion()
        """
        pass

    def GetDocument(self):
        """
        GetDocument(self: UpdaterData) -> Document
        
            Returns document associated with this UpdaterData
        """
        pass

    def GetModifiedElementIds(self):
        """
        GetModifiedElementIds(self: UpdaterData) -> ICollection[ElementId]
        
            Returns set of elements that were modified.
           This set is mutually exclusive 
             of elements returned by getAddedElementIds() and getDeletedElementIds().
        
            Returns: Set of elements that were modified in the document and triggered the call to 
             execute()
           Note: This set only contains modified elements (i.e. it is 
             mutually exclusive of elements returned
           by getAddedElementIds() and 
             getDeletedElementIds()). It does not contain any elements that were
           added 
             to or deleted from the document during the current transaction.
           Newly 
             added/deleted elements will be reported by 
             getAddedElementIds()/getDeletedElementIds(),
           even if they were also 
             modified during the same transaction, but only if 
             ChangeTypeElementAddition/Deletion
           is registered as a trigger for the 
             current Updater. I.e. Element creation and modification in
           the same 
             transaction is considered to be "creation" only. Newly created elements are not 
             considered to be
           "modified" and are therefore not returned as part of 
             getModifiedElementIds()
        """
        pass

    def IsChangeTriggered(self, id, type):
        """
        IsChangeTriggered(self: UpdaterData, id: ElementId, type: ChangeType) -> bool
        
            Allows updater to check if specific change has happened to an element.
           
             Compares input type to the types that caused Updater::execute() to be 
             triggered.
           If input type was not registered as a trigger for the associated 
             Updater, this
           method will always return false for that ChangeType.
           For 
             example, if the only trigger registered for UpdaterX is ChangeTypeAny for 
             Element A,
           then passing in ChangeTypeGeometry will return false even if the 
             geometry of A changed because
           the registered trigger was ChangeTypeAny. 
             However, passing in ChangeTypeAny will return true.
        
        
            id: Id of element to check
            type: ChangeType to check
            Returns: True if ChangeType happened to specified element
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: UpdaterData, disposing: bool) """
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

Get: IsValidObject(self: UpdaterData) -> bool

"""


