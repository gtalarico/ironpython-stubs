# encoding: utf-8
# module System.Windows.Annotations calls itself Annotations
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Annotation(object, IXmlSerializable):
    """
    Represents a user annotation in the Microsoft Annotations Framework.
    
    Annotation()
    Annotation(annotationType: XmlQualifiedName)
    Annotation(annotationType: XmlQualifiedName, id: Guid, creationTime: DateTime, lastModificationTime: DateTime)
    """
    def GetSchema(self):
        """
        GetSchema(self: Annotation) -> XmlSchema
        
            Always returns null.  See Annotations Schema for schema details.
            Returns: Always null.  See Annotations Schema for schema details.
        """
        pass

    def ReadXml(self, reader):
        """
        ReadXml(self: Annotation, reader: XmlReader)
            Deserializes the System.Windows.Annotations.Annotation from a specified System.Xml.XmlReader.
        
            reader: The XML reader to use to deserialize the annotation.
        """
        pass

    def WriteXml(self, writer):
        """
        WriteXml(self: Annotation, writer: XmlWriter)
            Serializes the annotation to a specified System.Xml.XmlWriter.
        
            writer: The XML writer to use to serialize the annotation.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, annotationType=None, id=None, creationTime=None, lastModificationTime=None):
        """
        __new__(cls: type)
        __new__(cls: type, annotationType: XmlQualifiedName)
        __new__(cls: type, annotationType: XmlQualifiedName, id: Guid, creationTime: DateTime, lastModificationTime: DateTime)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Anchors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of zero or more System.Windows.Annotations.AnnotationResource anchor elements that define the data selection(s) being annotated.

Get: Anchors(self: Annotation) -> Collection[AnnotationResource]

"""

    AnnotationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Xml.XmlQualifiedName of the annotation type.

Get: AnnotationType(self: Annotation) -> XmlQualifiedName

"""

    Authors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of zero or more author strings that identify who created the System.Windows.Annotations.Annotation.

Get: Authors(self: Annotation) -> Collection[str]

"""

    Cargos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of zero or more System.Windows.Annotations.AnnotationResource cargo elements that contain data for the annotation.

Get: Cargos(self: Annotation) -> Collection[AnnotationResource]

"""

    CreationTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the date and the time that the annotation was created.

Get: CreationTime(self: Annotation) -> DateTime

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the globally unique identifier (GUID) of the System.Windows.Annotations.Annotation.

Get: Id(self: Annotation) -> Guid

"""

    LastModificationTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the date and the time that the annotation was last modified.

Get: LastModificationTime(self: Annotation) -> DateTime

"""


    AnchorChanged = None
    AuthorChanged = None
    CargoChanged = None


class AnnotationAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the actions that occur with System.Windows.Annotations.Annotation author, anchor, and cargo resources.
    
    enum AnnotationAction, values: Added (0), Modified (2), Removed (1)
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

    Added = None
    Modified = None
    Removed = None
    value__ = None


class AnnotationAuthorChangedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Annotations.Annotation.AuthorChanged event.
    
    AnnotationAuthorChangedEventArgs(annotation: Annotation, action: AnnotationAction, author: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, annotation, action, author):
        """ __new__(cls: type, annotation: Annotation, action: AnnotationAction, author: object) """
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the author change operation for the event.

Get: Action(self: AnnotationAuthorChangedEventArgs) -> AnnotationAction

"""

    Annotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the annotation that raised the event.

Get: Annotation(self: AnnotationAuthorChangedEventArgs) -> Annotation

"""

    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the author object that is the target of the event.

Get: Author(self: AnnotationAuthorChangedEventArgs) -> object

"""



class AnnotationAuthorChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Windows.Annotations.Annotation.AuthorChanged event raised by the System.Windows.Annotations.Annotation class.
    
    AnnotationAuthorChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: AnnotationAuthorChangedEventHandler, sender: object, e: AnnotationAuthorChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AnnotationAuthorChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: AnnotationAuthorChangedEventHandler, sender: object, e: AnnotationAuthorChangedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class AnnotationDocumentPaginator(DocumentPaginator):
    """
    Provides a System.Windows.Documents.DocumentPaginator for printing a document together with its associated annotations.
    
    AnnotationDocumentPaginator(originalPaginator: DocumentPaginator, annotationStore: Stream)
    AnnotationDocumentPaginator(originalPaginator: DocumentPaginator, annotationStore: Stream, flowDirection: FlowDirection)
    AnnotationDocumentPaginator(originalPaginator: DocumentPaginator, annotationStore: AnnotationStore)
    AnnotationDocumentPaginator(originalPaginator: DocumentPaginator, annotationStore: AnnotationStore, flowDirection: FlowDirection)
    """
    def CancelAsync(self, userState):
        """
        CancelAsync(self: AnnotationDocumentPaginator, userState: object)
            Cancels all asynchronous operations initiated with a given userState object.
        
            userState: The unique application-defined identifier passed in the call to start the asynchronous operation.
        """
        pass

    def ComputePageCount(self):
        """
        ComputePageCount(self: AnnotationDocumentPaginator)
            Forces a pagination of the content, updates 
             System.Windows.Annotations.AnnotationDocumentPaginator.PageCount with the new total, and sets 
             System.Windows.Annotations.AnnotationDocumentPaginator.IsPageCountValid to true.
        """
        pass

    def ComputePageCountAsync(self, userState=None):
        """
        ComputePageCountAsync(self: AnnotationDocumentPaginator, userState: object)
            Starts an asynchronous pagination of the content, updates 
             System.Windows.Annotations.AnnotationDocumentPaginator.PageCount with the new total, and sets 
             System.Windows.Annotations.AnnotationDocumentPaginator.IsPageCountValid to true when it is 
             finished.
        
        
            userState: An application-defined object for identifying the asynchronous operation.
        """
        pass

    def GetPage(self, pageNumber):
        """
        GetPage(self: AnnotationDocumentPaginator, pageNumber: int) -> DocumentPage
        
            Returns a System.Windows.Documents.DocumentPage together with associated user-annotations for a 
             specified page number.
        
        
            pageNumber: The zero-based page number of the System.Windows.Documents.DocumentPage to return.
            Returns: The System.Windows.Documents.DocumentPage for the specified pageNumber; or 
             System.Windows.Documents.DocumentPage.Missing, if the specified pageNumber does not exist.
        """
        pass

    def GetPageAsync(self, pageNumber, userState=None):
        """
        GetPageAsync(self: AnnotationDocumentPaginator, pageNumber: int, userState: object)
            asynchronously returns a System.Windows.Documents.DocumentPage together with associated 
             user-annotations for a specified page number.
        
        
            pageNumber: The zero-based page number of the System.Windows.Documents.DocumentPage to retrieve.
            userState: An application-defined object that is used to identify the asynchronous operation.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, originalPaginator, annotationStore, flowDirection=None):
        """
        __new__(cls: type, originalPaginator: DocumentPaginator, annotationStore: Stream)
        __new__(cls: type, originalPaginator: DocumentPaginator, annotationStore: Stream, flowDirection: FlowDirection)
        __new__(cls: type, originalPaginator: DocumentPaginator, annotationStore: AnnotationStore)
        __new__(cls: type, originalPaginator: DocumentPaginator, annotationStore: AnnotationStore, flowDirection: FlowDirection)
        """
        pass

    IsPageCountValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether System.Windows.Annotations.AnnotationDocumentPaginator.PageCount is the total number of pages.

Get: IsPageCountValid(self: AnnotationDocumentPaginator) -> bool

"""

    PageCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the number of pages currently formatted.

Get: PageCount(self: AnnotationDocumentPaginator) -> int

"""

    PageSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the suggested width and height of each page.

Get: PageSize(self: AnnotationDocumentPaginator) -> Size

Set: PageSize(self: AnnotationDocumentPaginator) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the source document that is being paginated.

Get: Source(self: AnnotationDocumentPaginator) -> IDocumentPaginatorSource

"""



class AnnotationHelper(object):
    """ Provides utility methods and commands to create and delete highlight, ink sticky note, and text sticky note annotations. """
    @staticmethod
    def ClearHighlightsForSelection(service):
        """
        ClearHighlightsForSelection(service: AnnotationService)
            Clears all highlight annotations from the current selection of the viewer control associated 
             with the given System.Windows.Annotations.AnnotationService.
        
        
            service: The annotation service from which to remove highlight annotations.
        """
        pass

    @staticmethod
    def CreateHighlightForSelection(service, author, highlightBrush):
        """
        CreateHighlightForSelection(service: AnnotationService, author: str, highlightBrush: Brush) -> Annotation
        
            Creates a highlight annotation on the current selection of the viewer control associated with 
             the specified System.Windows.Annotations.AnnotationService.
        
        
            service: The annotation service to use to create the highlight annotation.
            author: The author of the annotation.
            highlightBrush: The brush to use to draw the highlight over the selected content.
            Returns: The highlight annotation; or null, if there is no selected content to highlight.
        """
        pass

    @staticmethod
    def CreateInkStickyNoteForSelection(service, author):
        """
        CreateInkStickyNoteForSelection(service: AnnotationService, author: str) -> Annotation
        
            Creates an ink sticky note annotation on the current selection of the viewer control associated 
             with the specified System.Windows.Annotations.AnnotationService..
        
        
            service: The annotation service to use to create the ink sticky note annotation.
            author: The author of the annotation.
            Returns: The ink sticky note annotation; or null, if there is no selected content to annotate.
        """
        pass

    @staticmethod
    def CreateTextStickyNoteForSelection(service, author):
        """
        CreateTextStickyNoteForSelection(service: AnnotationService, author: str) -> Annotation
        
            Creates a text sticky note annotation on the current selection of the viewer control associated 
             with the specified System.Windows.Annotations.AnnotationService.
        
        
            service: The annotation service to use to create the text sticky note annotation.
            author: The author of the annotation.
            Returns: The text sticky note annotation; or null, if there is no selected content to annotate.
        """
        pass

    @staticmethod
    def DeleteInkStickyNotesForSelection(service):
        """
        DeleteInkStickyNotesForSelection(service: AnnotationService)
            Deletes ink sticky note annotations that are wholly contained within the current selection of 
             the viewer control associated with the given System.Windows.Annotations.AnnotationService.
        
        
            service: The annotation service from which to delete ink sticky note annotations.
        """
        pass

    @staticmethod
    def DeleteTextStickyNotesForSelection(service):
        """
        DeleteTextStickyNotesForSelection(service: AnnotationService)
            Deletes text sticky note annotations that are wholly contained within the current selection of 
             the viewer control associated with the given System.Windows.Annotations.AnnotationService.
        
        
            service: The annotation service from which to delete text sticky note annotations.
        """
        pass

    @staticmethod
    def GetAnchorInfo(service, annotation):
        """
        GetAnchorInfo(service: AnnotationService, annotation: Annotation) -> IAnchorInfo
        
            Returns an System.Windows.Annotations.IAnchorInfo object that provides anchoring information, 
             such as the anchor location, about the specified annotation.
        
        
            service: The annotation service to use for this operation.
            annotation: The annotation to get anchoring information for.
            Returns: An System.Windows.Annotations.IAnchorInfo object that provides anchoring information about the 
             specified annotation, or null if it cannot be resolved.
        """
        pass

    __all__ = [
        'ClearHighlightsForSelection',
        'CreateHighlightForSelection',
        'CreateInkStickyNoteForSelection',
        'CreateTextStickyNoteForSelection',
        'DeleteInkStickyNotesForSelection',
        'DeleteTextStickyNotesForSelection',
        'GetAnchorInfo',
    ]


class AnnotationResource(object, IXmlSerializable, INotifyPropertyChanged2, INotifyPropertyChanged, IOwnedObject):
    """
    Represents a content anchor or cargo resource for an System.Windows.Annotations.Annotation.
    
    AnnotationResource()
    AnnotationResource(name: str)
    AnnotationResource(id: Guid)
    """
    def GetSchema(self):
        """
        GetSchema(self: AnnotationResource) -> XmlSchema
        
            Always returns null.  See Annotations Schema for schema details.
            Returns: Always null.  See Annotations Schema for schema details.
        """
        pass

    def ReadXml(self, reader):
        """
        ReadXml(self: AnnotationResource, reader: XmlReader)
            Deserializes the System.Windows.Annotations.AnnotationResource from a specified 
             System.Xml.XmlReader.
        
        
            reader: The XML reader to deserialize the System.Windows.Annotations.AnnotationResource from.
        """
        pass

    def WriteXml(self, writer):
        """
        WriteXml(self: AnnotationResource, writer: XmlWriter)
            Serializes the System.Windows.Annotations.AnnotationResource to a specified System.Xml.XmlWriter.
        
            writer: The XML writer to serialize the System.Windows.Annotations.AnnotationResource.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, id: Guid)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ContentLocators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Annotations.ContentLocatorBase elements contained in this resource.

Get: ContentLocators(self: AnnotationResource) -> Collection[ContentLocatorBase]

"""

    Contents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of the System.Xml.XmlElement objects that define the content of this resource.

Get: Contents(self: AnnotationResource) -> Collection[XmlElement]

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the GUID of this resource.

Get: Id(self: AnnotationResource) -> Guid

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a name for this System.Windows.Annotations.AnnotationResource.

Get: Name(self: AnnotationResource) -> str

Set: Name(self: AnnotationResource) = value
"""



class AnnotationResourceChangedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Annotations.Annotation.AnchorChanged and System.Windows.Annotations.Annotation.CargoChanged events.
    
    AnnotationResourceChangedEventArgs(annotation: Annotation, action: AnnotationAction, resource: AnnotationResource)
    """
    @staticmethod # known case of __new__
    def __new__(self, annotation, action, resource):
        """ __new__(cls: type, annotation: Annotation, action: AnnotationAction, resource: AnnotationResource) """
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the action of the annotation System.Windows.Annotations.AnnotationResourceChangedEventArgs.Resource.

Get: Action(self: AnnotationResourceChangedEventArgs) -> AnnotationAction

"""

    Annotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Annotations.Annotation that raised the event.

Get: Annotation(self: AnnotationResourceChangedEventArgs) -> Annotation

"""

    Resource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Annotations.Annotation.Anchors or System.Windows.Annotations.Annotation.Cargos resource associated with the event.

Get: Resource(self: AnnotationResourceChangedEventArgs) -> AnnotationResource

"""



class AnnotationResourceChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Windows.Annotations.Annotation.AnchorChanged or System.Windows.Annotations.Annotation.CargoChanged events raised by the System.Windows.Annotations.Annotation class.
    
    AnnotationResourceChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: AnnotationResourceChangedEventHandler, sender: object, e: AnnotationResourceChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AnnotationResourceChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: AnnotationResourceChangedEventHandler, sender: object, e: AnnotationResourceChangedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class AnnotationService(DispatcherObject):
    """
    Provides core services of the Microsoft Annotations Framework�to manage and display user annotations.
    
    AnnotationService(viewer: DocumentViewerBase)
    AnnotationService(viewer: FlowDocumentScrollViewer)
    AnnotationService(viewer: FlowDocumentReader)
    """
    def Disable(self):
        """
        Disable(self: AnnotationService)
            Disables annotations processing and hides all visible annotations.
        """
        pass

    def Enable(self, annotationStore):
        """
        Enable(self: AnnotationService, annotationStore: AnnotationStore)
            Enables the System.Windows.Annotations.AnnotationService for use with a given 
             System.Windows.Annotations.Storage.AnnotationStore and displays all visible annotations.
        
        
            annotationStore: The annotation store to use for reading, writing, and displaying annotations.
        """
        pass

    @staticmethod
    def GetService(*__args):
        """
        GetService(viewer: FlowDocumentScrollViewer) -> AnnotationService
        
            Returns the System.Windows.Annotations.AnnotationService associated with a specified 
             System.Windows.Controls.FlowDocumentScrollViewer.
        
        
            viewer: The document viewer control to return the System.Windows.Annotations.AnnotationService instance 
             for.
        
            Returns: The System.Windows.Annotations.AnnotationService associated with the given document viewer 
             control; or null if the specified viewer control has no 
             System.Windows.Annotations.AnnotationService.
        
        GetService(reader: FlowDocumentReader) -> AnnotationService
        
            Returns the System.Windows.Annotations.AnnotationService associated with a specified 
             System.Windows.Controls.FlowDocumentReader.
        
        
            reader: The document reader control to return the System.Windows.Annotations.AnnotationService instance 
             for.
        
            Returns: The System.Windows.Annotations.AnnotationService associated with the given document reader 
             control; or null if the specified document reader has no 
             System.Windows.Annotations.AnnotationService.
        
        GetService(viewer: DocumentViewerBase) -> AnnotationService
        
            Returns the System.Windows.Annotations.AnnotationService instance associated with a specified 
             document viewing control.
        
        
            viewer: The document viewing control to return the System.Windows.Annotations.AnnotationService instance 
             for.
        
            Returns: The System.Windows.Annotations.AnnotationService associated with the given document viewing 
             control; or null if the specified document viewing control has no 
             System.Windows.Annotations.AnnotationService.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, viewer):
        """
        __new__(cls: type, viewer: DocumentViewerBase)
        __new__(cls: type, viewer: FlowDocumentScrollViewer)
        __new__(cls: type, viewer: FlowDocumentReader)
        """
        pass

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Annotations.AnnotationService is enabled.

Get: IsEnabled(self: AnnotationService) -> bool

"""

    Store = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Annotations.Storage.AnnotationStore used by this System.Windows.Annotations.AnnotationService.

Get: Store(self: AnnotationService) -> AnnotationStore

"""


    ClearHighlightsCommand = None
    CreateHighlightCommand = None
    CreateInkStickyNoteCommand = None
    CreateTextStickyNoteCommand = None
    DeleteAnnotationsCommand = None
    DeleteStickyNotesCommand = None


class ContentLocatorBase(object, INotifyPropertyChanged2, INotifyPropertyChanged, IOwnedObject):
    """ Represents an object that identifies an item of content. """
    def Clone(self):
        """
        Clone(self: ContentLocatorBase) -> object
        
            Creates a modifiable deep copy clone of this System.Windows.Annotations.ContentLocatorBase.
            Returns: A modifiable deep copy clone of this System.Windows.Annotations.ContentLocatorBase.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ContentLocator(ContentLocatorBase, INotifyPropertyChanged2, INotifyPropertyChanged, IOwnedObject, IXmlSerializable):
    """
    Represents an ordered set of System.Windows.Annotations.ContentLocatorPart elements that identify an item of content.
    
    ContentLocator()
    """
    def Clone(self):
        """
        Clone(self: ContentLocator) -> object
        
            Creates a modifiable deep copy clone of this System.Windows.Annotations.ContentLocator.
            Returns: A modifiable deep copy clone of this System.Windows.Annotations.ContentLocator.
        """
        pass

    def GetSchema(self):
        """
        GetSchema(self: ContentLocator) -> XmlSchema
        
            Always returns null.  See Annotations Schema for schema details.
            Returns: Always null.  See Annotations Schema for schema details
        """
        pass

    def ReadXml(self, reader):
        """
        ReadXml(self: ContentLocator, reader: XmlReader)
            Deserializes the System.Windows.Annotations.ContentLocator from a specified System.Xml.XmlReader.
        
            reader: The XML reader to use to deserialize the System.Windows.Annotations.ContentLocator.
        """
        pass

    def StartsWith(self, locator):
        """
        StartsWith(self: ContentLocator, locator: ContentLocator) -> bool
        
            Returns a value that indicates whether the starting sequence of 
             System.Windows.Annotations.ContentLocatorPart elements in a specified 
             System.Windows.Annotations.ContentLocator are identical to those in this 
             System.Windows.Annotations.ContentLocator.
        
        
            locator: The System.Windows.Annotations.ContentLocator with the list of 
             System.Windows.Annotations.ContentLocatorPart elements to compare with this 
             System.Windows.Annotations.ContentLocator.
        
            Returns: true if the starting sequence of System.Windows.Annotations.ContentLocatorPart elements in this 
             System.Windows.Annotations.ContentLocator matches those in the specified locator; otherwise, 
             false.
        """
        pass

    def WriteXml(self, writer):
        """
        WriteXml(self: ContentLocator, writer: XmlWriter)
            Serializes the System.Windows.Annotations.ContentLocator to a specified System.Xml.XmlWriter.
        
            writer: The XML writer to use to serialize the System.Windows.Annotations.ContentLocator.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Parts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Annotations.ContentLocatorPart elements that make up this System.Windows.Annotations.ContentLocator.

Get: Parts(self: ContentLocator) -> Collection[ContentLocatorPart]

"""



class ContentLocatorGroup(ContentLocatorBase, INotifyPropertyChanged2, INotifyPropertyChanged, IOwnedObject, IXmlSerializable):
    """
    Represents an ordered set of System.Windows.Annotations.ContentLocator elements that identify an item of content.
    
    ContentLocatorGroup()
    """
    def Clone(self):
        """
        Clone(self: ContentLocatorGroup) -> object
        
            Creates a modifiable deep copy clone of this System.Windows.Annotations.ContentLocatorGroup.
            Returns: A modifiable deep copy clone of this System.Windows.Annotations.ContentLocatorGroup.
        """
        pass

    def GetSchema(self):
        """
        GetSchema(self: ContentLocatorGroup) -> XmlSchema
        
            Always returns null.  See Annotations Schema for schema details.
            Returns: Always null.  See Annotations Schema for schema details.
        """
        pass

    def ReadXml(self, reader):
        """
        ReadXml(self: ContentLocatorGroup, reader: XmlReader)
            Deserializes the System.Windows.Annotations.ContentLocatorGroup from a specified 
             System.Xml.XmlReader.
        
        
            reader: The XML reader to use to deserialize the System.Windows.Annotations.ContentLocatorGroup.
        """
        pass

    def WriteXml(self, writer):
        """
        WriteXml(self: ContentLocatorGroup, writer: XmlWriter)
            Serializes the System.Windows.Annotations.ContentLocatorGroup to a specified 
             System.Xml.XmlWriter.
        
        
            writer: The XML writer to use to serialize the System.Windows.Annotations.ContentLocatorGroup.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Locators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of the System.Windows.Annotations.ContentLocator elements that make up this System.Windows.Annotations.ContentLocatorGroup.

Get: Locators(self: ContentLocatorGroup) -> Collection[ContentLocator]

"""



class ContentLocatorPart(object, INotifyPropertyChanged2, INotifyPropertyChanged, IOwnedObject):
    """
    Represents a set of name/value pairs that identify an item of content.
    
    ContentLocatorPart(partType: XmlQualifiedName)
    """
    def Clone(self):
        """
        Clone(self: ContentLocatorPart) -> object
        
            Creates a modifiable deep copy clone of this System.Windows.Annotations.ContentLocatorPart.
            Returns: A modifiable deep copy clone of this System.Windows.Annotations.ContentLocatorPart.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ContentLocatorPart, obj: object) -> bool
        
            Returns a value that indicates whether a given System.Windows.Annotations.ContentLocatorPart is 
             identical to this System.Windows.Annotations.ContentLocatorPart.
        
        
            obj: The part to compare for equality.
            Returns: true if the System.Windows.Annotations.ContentLocatorPart.NameValuePairs within both parts are 
             identical; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ContentLocatorPart) -> int
        
            Returns the hash code for this part.
            Returns: The hash code for this part.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, partType):
        """ __new__(cls: type, partType: XmlQualifiedName) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    NameValuePairs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of the name/value pairs that define this part.

Get: NameValuePairs(self: ContentLocatorPart) -> IDictionary[str, str]

"""

    PartType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type name and namespace of the part.

Get: PartType(self: ContentLocatorPart) -> XmlQualifiedName

"""



class IAnchorInfo:
    """ Provides the capabilities for matching annotations with the corresponding annotated objects. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Anchor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the anchor of the annotation.

Get: Anchor(self: IAnchorInfo) -> AnnotationResource

"""

    Annotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the annotation object.

Get: Annotation(self: IAnchorInfo) -> Annotation

"""

    ResolvedAnchor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object that represents the location on the tree where the System.Windows.Annotations.IAnchorInfo.Anchor is resolved.

Get: ResolvedAnchor(self: IAnchorInfo) -> object

"""



class TextAnchor(object):
    """ Represents a selection of content that an annotation is anchored to. """
    def Equals(self, obj):
        """
        Equals(self: TextAnchor, obj: object) -> bool
        
            Returns a value that indicates whether the text anchor is equal to the specified object.
        
            obj: The object to compare to.
            Returns: true if the two instances are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: TextAnchor) -> int
        
            Returns the hash code of the text anchor instance.
            Returns: The hash code of the text anchor instance.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    BoundingEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the end position of the text anchor.

Get: BoundingEnd(self: TextAnchor) -> ContentPosition

"""

    BoundingStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the beginning position of the text anchor.

Get: BoundingStart(self: TextAnchor) -> ContentPosition

"""



# variables with complex values

