# encoding: utf-8
# module Autodesk.Revit.DB.Events calls itself Events
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RevitAPIEventArgs(EventArgs, IDisposable):
    """ The class is used as base class for all event argument classes. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs) """
        pass

    def IsCancelled(self):
        """
        IsCancelled(self: RevitAPIEventArgs) -> bool
        
            Indicates whether the event is being cancelled.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Cancellable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether an event may be cancelled by an event delegate.

Get: Cancellable(self: RevitAPIEventArgs) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RevitAPIEventArgs) -> bool

"""



class RevitAPISingleEventArgs(RevitAPIEventArgs, IDisposable):
    """ The class is used as a base class for arguments of any single-event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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


class ApplicationInitializedEventArgs(RevitAPISingleEventArgs, IDisposable):
    """ The event arguments used by the ApplicationLaunched event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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


class DocumentChangedEventArgs(RevitAPISingleEventArgs, IDisposable):
    """ The event arguments used by the DocumentChanged event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def GetAddedElementIds(self, filter=None):
        """
        GetAddedElementIds(self: DocumentChangedEventArgs) -> ICollection[ElementId]
        
            Returns set of elements newly added to the document.
            Returns: The set of ElementId for elements newly added to the document.
        GetAddedElementIds(self: DocumentChangedEventArgs, filter: ElementFilter) -> ICollection[ElementId]
        
            Returns set of newly added elements that pass the filter.
        
            filter: The element filter to be applied.
            Returns: The set of ElementId for newly added elements that pass the filter.
           Returns 
             empty set if no elements are found which pass the filter.
        """
        pass

    def GetDeletedElementIds(self):
        """
        GetDeletedElementIds(self: DocumentChangedEventArgs) -> ICollection[ElementId]
        
            Returns set of elements that were deleted from the document.
            Returns: The set of ElementId for elements that were deleted from the document.
        """
        pass

    def GetDocument(self):
        """
        GetDocument(self: DocumentChangedEventArgs) -> Document
        
            Returns document associated with this event
            Returns: The document associated with this event.
        """
        pass

    def GetModifiedElementIds(self, filter=None):
        """
        GetModifiedElementIds(self: DocumentChangedEventArgs) -> ICollection[ElementId]
        
            Returns set of elements that were modified.
            Returns: The set of ElementId for elements that were modified.
        GetModifiedElementIds(self: DocumentChangedEventArgs, filter: ElementFilter) -> ICollection[ElementId]
        
            Returns set of elements  that were modified according to the given element 
             filter.
        
        
            filter: The element filter to be applied.
            Returns: The set of ElementId for modified elements that pass the filter.
           Returns 
             empty set if no elements are found which pass the filter.
        """
        pass

    def GetTransactionNames(self):
        """
        GetTransactionNames(self: DocumentChangedEventArgs) -> IList[str]
        
            Returns names of the transactions associated with this event
            Returns: The names of the transactions associated with this event
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The operation associated with this event

Get: Operation(self: DocumentChangedEventArgs) -> UndoOperation

"""



class RevitAPIPostEventArgs(RevitAPIEventArgs, IDisposable):
    """ The class is used as a base class for arguments of any post-event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the action associated with this event succeeded, failed, or was cancelled (by an API event handler).

Get: Status(self: RevitAPIPostEventArgs) -> RevitAPIEventStatus

"""



class DocumentClosedEventArgs(RevitAPIPostEventArgs, IDisposable):
    """ The event arguments used by the DocumentClosed event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    DocumentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the document that has just been closed.

Get: DocumentId(self: DocumentClosedEventArgs) -> int

"""



class RevitAPIPreEventArgs(RevitAPIEventArgs, IDisposable):
    """ The class is used as a base class for the arguments for any pre-event. """
    def Cancel(self):
        """
        Cancel(self: RevitAPIPreEventArgs)
            When the event is cancellable, may call the Cancel() method to cancel it.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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


class RevitAPIPreDocEventArgs(RevitAPIPreEventArgs, IDisposable):
    """ The base class used for pre events where the arguments must supply access to the document. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The document associated with the event.

Get: Document(self: RevitAPIPreDocEventArgs) -> Document

"""



class DocumentClosingEventArgs(RevitAPIPreDocEventArgs, IDisposable):
    """ The event arguments used by the DocumentClosing event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    DocumentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the document that is about to be closed.

Get: DocumentId(self: DocumentClosingEventArgs) -> int

"""



class RevitAPIPostDocEventArgs(RevitAPIPostEventArgs, IDisposable):
    """ The base class used for post events where the arguments must supply access to the document. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The document associated with the event.

Get: Document(self: RevitAPIPostDocEventArgs) -> Document

"""



class DocumentCreatedEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the DocumentCreated event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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


class DocumentCreatingEventArgs(RevitAPIPreEventArgs, IDisposable):
    """ The event arguments used by the DocumentCreating event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    DocumentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of the document which is about to be created, e.g. Project or Template.

Get: DocumentType(self: DocumentCreatingEventArgs) -> DocumentType

"""

    Template = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The template file path to be used for creating the new document.

Get: Template(self: DocumentCreatingEventArgs) -> str

"""



class DocumentOpenedEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the DocumentOpened event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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


class DocumentOpeningEventArgs(RevitAPIPreEventArgs, IDisposable):
    """ The event arguments used by the DocumentOpening event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    DocumentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of the document, e.g. Project or Template.

Get: DocumentType(self: DocumentOpeningEventArgs) -> DocumentType

"""

    PathName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Path of the document to be opened.

Get: PathName(self: DocumentOpeningEventArgs) -> str

"""



class DocumentPrintedEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the DocumentPrinted event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def GetFailedViewElementIds(self):
        """
        GetFailedViewElementIds(self: DocumentPrintedEventArgs) -> IList[ElementId]
        
            Returns ElementIds of the views that that failed to print (if any).
            Returns: ElementIds of the views that that failed to print (if any).
        """
        pass

    def GetPrintedViewElementIds(self):
        """
        GetPrintedViewElementIds(self: DocumentPrintedEventArgs) -> IList[ElementId]
        
            Returns ElementIds of the views that printed successfully.
            Returns: ElementIds of the views that printed successfully.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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


class DocumentPrintingEventArgs(RevitAPIPreDocEventArgs, IDisposable):
    """ The event arguments used by the DocumentPrinting event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def GetSettings(self):
        """
        GetSettings(self: DocumentPrintingEventArgs) -> IPrintSetting
        
            Gets the print settings of the active printing session.
            Returns: The print settings of the active printing session.
        """
        pass

    def GetViewElementIds(self):
        """
        GetViewElementIds(self: DocumentPrintingEventArgs) -> IList[ElementId]
        
            Returns ElementIds of the views to be printed.
            Returns: ElementIds of the views to be printed.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The print settings of the active printing session.

Get: Settings(self: DocumentPrintingEventArgs) -> IPrintSetting

"""



class DocumentSavedAsEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the DocumentSavedAs event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    IsSavingAsMasterFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the document is to be saved as master file.

Get: IsSavingAsMasterFile(self: DocumentSavedAsEventArgs) -> bool

"""

    OriginalPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Original path of the document.

Get: OriginalPath(self: DocumentSavedAsEventArgs) -> str

"""



class DocumentSavedEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the DocumentSaved event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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


class DocumentSavingAsEventArgs(RevitAPIPreDocEventArgs, IDisposable):
    """ The event arguments used by the DocumentSavingAs event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    IsSavingAsMasterFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the document is to be saved as master file.

Get: IsSavingAsMasterFile(self: DocumentSavingAsEventArgs) -> bool

"""

    PathName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Target path to which the document is to be saved.

Get: PathName(self: DocumentSavingAsEventArgs) -> str

"""



class DocumentSavingEventArgs(RevitAPIPreDocEventArgs, IDisposable):
    """ The event arguments used by the DocumentSaving event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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


class DocumentSynchronizedWithCentralEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the DocumentSynchronizedWithCentralEventArgs event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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


class DocumentSynchronizingWithCentralEventArgs(RevitAPIPreDocEventArgs, IDisposable):
    """ The event arguments used by the DocumentSynchronizingWithCentralEventArgs event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Comments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """User's comments for synchronization.

Get: Comments(self: DocumentSynchronizingWithCentralEventArgs) -> str

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full path of the central model which is to be synchronized.

Get: Location(self: DocumentSynchronizingWithCentralEventArgs) -> str

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """User's options associated with the synchronization operation.

Get: Options(self: DocumentSynchronizingWithCentralEventArgs) -> SynchronizeWithCentralOptions

"""



class DocumentWorksharingEnabledEventArgs(RevitAPISingleEventArgs, IDisposable):
    """ The event arguments used by the DocumentWorksharingEnabled event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def GetDocument(self):
        """
        GetDocument(self: DocumentWorksharingEnabledEventArgs) -> Document
        
            Returns document associated with this event
            Returns: The document associated with this event.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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


class ElementTypeDuplicatedEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the ElementTypeDuplicated event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    NewElementTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the newly duplicated ElementType.

Get: NewElementTypeId(self: ElementTypeDuplicatedEventArgs) -> ElementId

"""

    NewName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the newly duplicated ElementType.

Get: NewName(self: ElementTypeDuplicatedEventArgs) -> str

"""

    OriginalElementTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the element type that is duplicated.

Get: OriginalElementTypeId(self: ElementTypeDuplicatedEventArgs) -> ElementId

"""



class ElementTypeDuplicatingEventArgs(RevitAPIPreDocEventArgs, IDisposable):
    """ The event arguments used by the ElementTypeDuplicating event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    ElementTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the ElementType to be duplicated.

Get: ElementTypeId(self: ElementTypeDuplicatingEventArgs) -> ElementId

"""



class EventStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the status of an action which triggered a post event.
    
    enum EventStatus, values: Cancelled (1), Failed (-1), Succeeded (0)
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

    Cancelled = None
    Failed = None
    Succeeded = None
    value__ = None


class FailuresProcessingEventArgs(RevitAPISingleEventArgs, IDisposable):
    """ The event arguments used by the FailuresProcessing event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def GetFailuresAccessor(self):
        """
        GetFailuresAccessor(self: FailuresProcessingEventArgs) -> FailuresAccessor
        
            Provides access to the failure information in the document.
            Returns: The accessor to the failures in the document.
        """
        pass

    def GetProcessingResult(self):
        """
        GetProcessingResult(self: FailuresProcessingEventArgs) -> FailureProcessingResult
        
            Retrieves current status of the failures processing result.
            Returns: The current failures processing result.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
        pass

    def SetProcessingResult(self, result):
        """
        SetProcessingResult(self: FailuresProcessingEventArgs, result: FailureProcessingResult)
            Sets the result of the failures processing accomplished during this event 
             callback.
        
        
            result: The result.
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


class FamilyLoadedIntoDocumentEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the FamilyLoadedInto event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    FamilyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The file name of the family that is loaded into the document.

Get: FamilyName(self: FamilyLoadedIntoDocumentEventArgs) -> str

"""

    FamilyPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The file path of the family that is loaded into the document.

Get: FamilyPath(self: FamilyLoadedIntoDocumentEventArgs) -> str

"""

    NewFamilyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The newly loaded family id.

Get: NewFamilyId(self: FamilyLoadedIntoDocumentEventArgs) -> ElementId

"""

    OriginalFamilyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The original family id that is overridden by the newly loaded family.

Get: OriginalFamilyId(self: FamilyLoadedIntoDocumentEventArgs) -> ElementId

"""



class FamilyLoadingIntoDocumentEventArgs(RevitAPIPreDocEventArgs, IDisposable):
    """ The event arguments used by the FamilyLoadingInto event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    FamilyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The file name of the family that is being loaded into the document.

Get: FamilyName(self: FamilyLoadingIntoDocumentEventArgs) -> str

"""

    FamilyPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The file path of the family that is being loaded into the document.

Get: FamilyPath(self: FamilyLoadingIntoDocumentEventArgs) -> str

"""



class FileExportedEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the FileExported event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the export format, e.g. DWG or image.

Get: Format(self: FileExportedEventArgs) -> ImportExportFileFormat

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Target path for the exported file (or files).

Get: Path(self: FileExportedEventArgs) -> str

"""



class FileExportingEventArgs(RevitAPIPreDocEventArgs, IDisposable):
    """ The event arguments used by the FileExporting event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the export format, e.g. DWG or image.

Get: Format(self: FileExportingEventArgs) -> ImportExportFileFormat

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The target path for the export.

Get: Path(self: FileExportingEventArgs) -> str

"""



class FileImportedEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the FileImported event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the import format, e.g. DWG or image.

Get: Format(self: FileImportedEventArgs) -> ImportExportFileFormat

"""

    ImportedInstanceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the imported instance that represents the imported object(s) after a successful import.
   It could be used for further manipulation of that instance.

Get: ImportedInstanceId(self: FileImportedEventArgs) -> ElementId

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Path of the source file that was imported.

Get: Path(self: FileImportedEventArgs) -> str

"""



class FileImportingEventArgs(RevitAPIPreDocEventArgs, IDisposable):
    """ The event arguments used by the FileImporting event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the import format, e.g. DWG or image.

Get: Format(self: FileImportingEventArgs) -> ImportExportFileFormat

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Path of the source file which is about to be imported.

Get: Path(self: FileImportingEventArgs) -> str

"""



class RevitEventArgs(EventArgs):
    """ The class is used as base class for all event argument classes. """
    def getEventKey_(self, *args): #cannot find CLR method
        """ getEventKey_(self: RevitEventArgs) -> Type """
        pass

    Cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the event is being cancelled. 
When the event is cancellable, set the property to True to cancel it.

Get: Cancel(self: RevitEventArgs) -> bool

Set: Cancel(self: RevitEventArgs) = value
"""

    Cancellable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether an event may be cancelled by an event delegate.

Get: Cancellable(self: RevitEventArgs) -> bool

"""



class PostEventArgs(RevitEventArgs):
    """ The class is used as a base class for arguments of any post-event. """
    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the action associated with this event succeeded, failed, or was cancelled (by an APIevent handler).

Get: Status(self: PostEventArgs) -> EventStatus

"""



class PostDocEventArgs(PostEventArgs):
    """ The class is used as base class for arguments of any post-event that is associated to a particular Document. """
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The document associated with the event.

Get: Document(self: PostDocEventArgs) -> Document

"""



class PreEventArgs(RevitEventArgs):
    """ The class is used as a base class for the arguments for any pre-event. """

class PreDocEventArgs(PreEventArgs):
    """ The class is used as base class for the arguments of any pre-event arguments that is associated to a particular Document. """
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The document associated with the event.

Get: Document(self: PreDocEventArgs) -> Document

"""



class ProgressChangedEventArgs(RevitAPISingleEventArgs, IDisposable):
    """ The event arguments used by the ProgressChanged event. """
    def Cancel(self):
        """
        Cancel(self: ProgressChangedEventArgs)
            Requests to cancel the progress bar's operation.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Caption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The text from the progress bar caption that describes the operation in progress

Get: Caption(self: ProgressChangedEventArgs) -> str

"""

    LowerRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lower part of progress bar range - always zero

Get: LowerRange(self: ProgressChangedEventArgs) -> int

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Progress bar position - value is always between zero and upperRange and is incremented by one with each event of stage "PositionChanged"

Get: Position(self: ProgressChangedEventArgs) -> int

"""

    Stage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current stage of the progress bar

Get: Stage(self: ProgressChangedEventArgs) -> ProgressStage

"""

    UpperRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Upper part of progress bar range - will be any non-zero number

Get: UpperRange(self: ProgressChangedEventArgs) -> int

"""



class ProgressStage(Enum, IComparable, IFormattable, IConvertible):
    """
    The associated action of a ProgressChanged event
    
    enum ProgressStage, values: CaptionChanged (3), Finished (5), PositionChanged (2), RangeChanged (1), Started (0), Unchanged (4)
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

    CaptionChanged = None
    Finished = None
    PositionChanged = None
    RangeChanged = None
    Started = None
    Unchanged = None
    value__ = None


class RevitAPIEventStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the status of an action which triggered a post event.
    
    enum RevitAPIEventStatus, values: Cancelled (1), Failed (-1), Succeeded (0)
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

    Cancelled = None
    Failed = None
    Succeeded = None
    value__ = None


class UndoOperation(Enum, IComparable, IFormattable, IConvertible):
    """
    The operation associated with DocumentChanged event
    
    enum UndoOperation, values: TransactionCommitted (0), TransactionGroupRolledBack (2), TransactionRedone (4), TransactionRolledBack (1), TransactionUndone (3)
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

    TransactionCommitted = None
    TransactionGroupRolledBack = None
    TransactionRedone = None
    TransactionRolledBack = None
    TransactionUndone = None
    value__ = None


class ViewPrintedEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the ViewPrinted event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the view being printed out of the set of all views being printed.

Get: Index(self: ViewPrintedEventArgs) -> int

"""

    TotalViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of all views being printed.

Get: TotalViews(self: ViewPrintedEventArgs) -> int

"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The view that was printed.

Get: View(self: ViewPrintedEventArgs) -> View

"""



class ViewPrintingEventArgs(RevitAPIPreDocEventArgs, IDisposable):
    """ The event arguments used by the ViewPrinting event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def GetSettings(self):
        """
        GetSettings(self: ViewPrintingEventArgs) -> IPrintSetting
        
            Get the print settings of the active printing session.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the view being printed out of the set of all views being printed.

Get: Index(self: ViewPrintingEventArgs) -> int

"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The print settings of the active printing session.

Get: Settings(self: ViewPrintingEventArgs) -> IPrintSetting

"""

    TotalViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of all views being printed.

Get: TotalViews(self: ViewPrintingEventArgs) -> int

"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The view to be printed.

Get: View(self: ViewPrintingEventArgs) -> View

"""



