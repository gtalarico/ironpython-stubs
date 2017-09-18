# encoding: utf-8
# module System.Windows.Documents calls itself Documents
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ContentPosition(object):
    """ Abstract class that represents the position of content. This position is content specific. """
    Missing = None


class DocumentPage(object, IDisposable):
    """
    Represents a document page produced by a paginator.
    
    DocumentPage(visual: Visual)
    DocumentPage(visual: Visual, pageSize: Size, bleedBox: Rect, contentBox: Rect)
    """
    def Dispose(self):
        """
        Dispose(self: DocumentPage)
            Releases all resources used by the System.Windows.Documents.DocumentPage.
        """
        pass

    def OnPageDestroyed(self, *args): #cannot find CLR method
        """
        OnPageDestroyed(self: DocumentPage, e: EventArgs)
            Raises the System.Windows.Documents.DocumentPage.PageDestroyed event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def SetBleedBox(self, *args): #cannot find CLR method
        """
        SetBleedBox(self: DocumentPage, bleedBox: Rect)
            Sets the dimensions and location of the System.Windows.Documents.DocumentPage.BleedBox.
        
            bleedBox: An object that specifies the size and location of a rectangle.
        """
        pass

    def SetContentBox(self, *args): #cannot find CLR method
        """
        SetContentBox(self: DocumentPage, contentBox: Rect)
            Sets the dimension and location of the System.Windows.Documents.DocumentPage.ContentBox.
        
            contentBox: An object that specifies the size and location of a rectangle.
        """
        pass

    def SetSize(self, *args): #cannot find CLR method
        """
        SetSize(self: DocumentPage, size: Size)
            Sets the System.Windows.Documents.DocumentPage.Size of the physical page as it will be after any 
             cropping.
        
        
            size: The size of the page.
        """
        pass

    def SetVisual(self, *args): #cannot find CLR method
        """
        SetVisual(self: DocumentPage, visual: Visual)
            Sets the System.Windows.Documents.DocumentPage.Visual that depicts the page.
        
            visual: The visual representation of the page.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, visual, pageSize=None, bleedBox=None, contentBox=None):
        """
        __new__(cls: type, visual: Visual)
        __new__(cls: type, visual: Visual, pageSize: Size, bleedBox: Rect, contentBox: Rect)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BleedBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the area for print production-related bleeds, registration marks, and crop marks that may appear on the physical sheet outside the logical page boundaries.

Get: BleedBox(self: DocumentPage) -> Rect

"""

    ContentBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the area of the page within the margins.

Get: ContentBox(self: DocumentPage) -> Rect

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the actual size of a page as it will be following any cropping.

Get: Size(self: DocumentPage) -> Size

"""

    Visual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the visual representation of the page.

Get: Visual(self: DocumentPage) -> Visual

"""


    Missing = None
    PageDestroyed = None


class DocumentPaginator(object):
    """ Provides an abstract base class that supports creation of multiple-page elements from a single document. """
    def CancelAsync(self, userState):
        """
        CancelAsync(self: DocumentPaginator, userState: object)
            Cancels a previous erload:System.Windows.Documents.DocumentPaginator.GetPageAsync or 
             erload:System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberAsync operation.
        
        
            userState: The original userState passed to erload:System.Windows.Documents.DocumentPaginator.GetPageAsync, 
             erload:System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberAsync, or 
             erload:System.Windows.Documents.DocumentPaginator.ComputePageCountAsync that identifies the 
             asynchronous task to cancel.
        """
        pass

    def ComputePageCount(self):
        """
        ComputePageCount(self: DocumentPaginator)
            Forces a pagination of the content, updates System.Windows.Documents.DocumentPaginator.PageCount 
             with the new total, and sets System.Windows.Documents.DocumentPaginator.IsPageCountValid to 
             true.
        """
        pass

    def ComputePageCountAsync(self, userState=None):
        """
        ComputePageCountAsync(self: DocumentPaginator, userState: object)
            Asynchronously, forces a pagination of the content, updates 
             System.Windows.Documents.DocumentPaginator.PageCount with the new total, sets 
             System.Windows.Documents.DocumentPaginator.IsPageCountValid to true.
        
        
            userState: A unique identifier for the asynchronous task.
        ComputePageCountAsync(self: DocumentPaginator)
            Asynchronously, forces a pagination of the content, updates 
             System.Windows.Documents.DocumentPaginator.PageCount with the new total, and sets 
             System.Windows.Documents.DocumentPaginator.IsPageCountValid to true.
        """
        pass

    def GetPage(self, pageNumber):
        """
        GetPage(self: DocumentPaginator, pageNumber: int) -> DocumentPage
        
            When overridden in a derived class, gets the System.Windows.Documents.DocumentPage for the 
             specified page number.
        
        
            pageNumber: The zero-based page number of the document page that is needed.
            Returns: The System.Windows.Documents.DocumentPage for the specified pageNumber, or 
             System.Windows.Documents.DocumentPage.Missing if the page does not exist.
        """
        pass

    def GetPageAsync(self, pageNumber, userState=None):
        """
        GetPageAsync(self: DocumentPaginator, pageNumber: int, userState: object)
            Asynchronously returns (through the System.Windows.Documents.DocumentPaginator.GetPageCompleted 
             event) the System.Windows.Documents.DocumentPage for the specified page number and assigns the 
             specified ID to the asynchronous task.
        
        
            pageNumber: The zero-based page number of the System.Windows.Documents.DocumentPage to get.
            userState: A unique identifier for the asynchronous task.
        GetPageAsync(self: DocumentPaginator, pageNumber: int)
            Asynchronously returns (through the System.Windows.Documents.DocumentPaginator.GetPageCompleted 
             event) the System.Windows.Documents.DocumentPage for the specified page number.
        
        
            pageNumber: The zero-based page number of the document page that is needed.
        """
        pass

    def OnComputePageCountCompleted(self, *args): #cannot find CLR method
        """
        OnComputePageCountCompleted(self: DocumentPaginator, e: AsyncCompletedEventArgs)
            Raises the System.Windows.Documents.DocumentPaginator.ComputePageCountCompleted event.
        
            e: An System.ComponentModel.AsyncCompletedEventArgs that contains the event data.
        """
        pass

    def OnGetPageCompleted(self, *args): #cannot find CLR method
        """
        OnGetPageCompleted(self: DocumentPaginator, e: GetPageCompletedEventArgs)
            Raises the System.Windows.Documents.DocumentPaginator.GetPageCompleted event.
        
            e: A System.Windows.Documents.GetPageCompletedEventArgs that contains the event data.
        """
        pass

    def OnPagesChanged(self, *args): #cannot find CLR method
        """
        OnPagesChanged(self: DocumentPaginator, e: PagesChangedEventArgs)
            Raises the System.Windows.Documents.DocumentPaginator.PagesChanged event.
        
            e: A System.Windows.Documents.PagesChangedEventArgs that contains the event data.
        """
        pass

    IsPageCountValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether System.Windows.Documents.DocumentPaginator.PageCount is the total number of pages.

Get: IsPageCountValid(self: DocumentPaginator) -> bool

"""

    PageCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a count of the number of pages currently formatted

Get: PageCount(self: DocumentPaginator) -> int

"""

    PageSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets or sets the suggested width and height of each page.

Get: PageSize(self: DocumentPaginator) -> Size

Set: PageSize(self: DocumentPaginator) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, returns the element being paginated.

Get: Source(self: DocumentPaginator) -> IDocumentPaginatorSource

"""


    ComputePageCountCompleted = None
    GetPageCompleted = None
    PagesChanged = None


class DynamicDocumentPaginator(DocumentPaginator):
    """ Provides an abstract base class that supports automatic background pagination and tracking content positions across repaginations in addition to the methods and properties of its own base class. """
    def GetObjectPosition(self, value):
        """
        GetObjectPosition(self: DynamicDocumentPaginator, value: object) -> ContentPosition
        
            When overridden in a derived class, returns a System.Windows.Documents.ContentPosition for the 
             specified System.Object.
        
        
            value: The object to return the System.Windows.Documents.ContentPosition of.
            Returns: The System.Windows.Documents.ContentPosition of the given object.
        """
        pass

    def GetPageNumber(self, contentPosition):
        """
        GetPageNumber(self: DynamicDocumentPaginator, contentPosition: ContentPosition) -> int
        
            When overridden in a derived class, returns the zero-based page number of the specified 
             System.Windows.Documents.ContentPosition.
        
        
            contentPosition: The content position whose page number is needed.
            Returns: An System.Int32 representing zero-based page number where the specified contentPosition appears.
        """
        pass

    def GetPageNumberAsync(self, contentPosition, userState=None):
        """
        GetPageNumberAsync(self: DynamicDocumentPaginator, contentPosition: ContentPosition, userState: object)
            Asynchronously, returns (through the This method raises the 
             System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberCompleted event) the zero-based 
             page number of the specified System.Windows.Documents.ContentPosition.
        
        
            contentPosition: The content position element to return the page number of.
            userState: A unique identifier for the asynchronous task.
        GetPageNumberAsync(self: DynamicDocumentPaginator, contentPosition: ContentPosition)
            Asynchronously, returns (through the This method raises the 
             System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberCompleted event) the zero-based 
             page number of the specified System.Windows.Documents.ContentPosition.
        
        
            contentPosition: The content position whose page number is needed.
        """
        pass

    def GetPagePosition(self, page):
        """
        GetPagePosition(self: DynamicDocumentPaginator, page: DocumentPage) -> ContentPosition
        
            When overridden in a derived class, gets the position of the specified page in the document's 
             content.
        
        
            page: The page whose position is needed.
            Returns: A System.Windows.Documents.ContentPosition representing the position of page.
        """
        pass

    def OnGetPageNumberCompleted(self, *args): #cannot find CLR method
        """
        OnGetPageNumberCompleted(self: DynamicDocumentPaginator, e: GetPageNumberCompletedEventArgs)
            Raises the System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberCompleted event.
        
            e: A System.Windows.Documents.GetPageNumberCompletedEventArgs that contains the event data.
        """
        pass

    def OnPaginationCompleted(self, *args): #cannot find CLR method
        """
        OnPaginationCompleted(self: DynamicDocumentPaginator, e: EventArgs)
            Raises the System.Windows.Documents.DynamicDocumentPaginator.PaginationCompleted event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnPaginationProgress(self, *args): #cannot find CLR method
        """
        OnPaginationProgress(self: DynamicDocumentPaginator, e: PaginationProgressEventArgs)
            Raises the System.Windows.Documents.DynamicDocumentPaginator.PaginationProgress event.
        
            e: A System.Windows.Documents.PaginationProgressEventArgs that contains the event data.
        """
        pass

    IsBackgroundPaginationEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether pagination is performed automatically in the background in response to certain events, such as a change in page size.

Get: IsBackgroundPaginationEnabled(self: DynamicDocumentPaginator) -> bool

Set: IsBackgroundPaginationEnabled(self: DynamicDocumentPaginator) = value
"""


    GetPageNumberCompleted = None
    PaginationCompleted = None
    PaginationProgress = None


class GetPageCompletedEventArgs(AsyncCompletedEventArgs):
    """
    Provides data for the System.Windows.Documents.DocumentPaginator.GetPageCompleted event.
    
    GetPageCompletedEventArgs(page: DocumentPage, pageNumber: int, error: Exception, cancelled: bool, userState: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, page, pageNumber, error, cancelled, userState):
        """ __new__(cls: type, page: DocumentPage, pageNumber: int, error: Exception, cancelled: bool, userState: object) """
        pass

    DocumentPage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Documents.DocumentPage for the page specified in the call to System.Windows.Documents.DocumentPaginator.GetPageAsync(System.Int32,System.Object).

Get: DocumentPage(self: GetPageCompletedEventArgs) -> DocumentPage

"""

    PageNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the page number passed to System.Windows.Documents.DocumentPaginator.GetPageAsync(System.Int32,System.Object).

Get: PageNumber(self: GetPageCompletedEventArgs) -> int

"""



class GetPageCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Documents.DocumentPaginator.GetPageCompleted event of a System.Windows.Documents.FixedDocument or other classes implementing System.Windows.Documents.DocumentPaginator.
    
    GetPageCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: GetPageCompletedEventHandler, sender: object, e: GetPageCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: GetPageCompletedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: GetPageCompletedEventHandler, sender: object, e: GetPageCompletedEventArgs) """
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


class GetPageNumberCompletedEventArgs(AsyncCompletedEventArgs):
    """
    Provides data for the System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberCompleted event.
    
    GetPageNumberCompletedEventArgs(contentPosition: ContentPosition, pageNumber: int, error: Exception, cancelled: bool, userState: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, contentPosition, pageNumber, error, cancelled, userState):
        """ __new__(cls: type, contentPosition: ContentPosition, pageNumber: int, error: Exception, cancelled: bool, userState: object) """
        pass

    ContentPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Documents.ContentPosition passed to System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberAsync(System.Windows.Documents.ContentPosition).

Get: ContentPosition(self: GetPageNumberCompletedEventArgs) -> ContentPosition

"""

    PageNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the page number for the System.Windows.Documents.ContentPosition passed to System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberAsync(System.Windows.Documents.ContentPosition).

Get: PageNumber(self: GetPageNumberCompletedEventArgs) -> int

"""



class GetPageNumberCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberCompleted event of a System.Windows.Documents.FixedDocument, or System.Windows.Documents.FlowDocument.
    
    GetPageNumberCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: GetPageNumberCompletedEventHandler, sender: object, e: GetPageNumberCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: GetPageNumberCompletedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: GetPageNumberCompletedEventHandler, sender: object, e: GetPageNumberCompletedEventArgs) """
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


class IDocumentPaginatorSource:
    """ Defines the source object that performs actual content pagination. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DocumentPaginator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When implemented in a derived class, gets the object that performs content pagination.

Get: DocumentPaginator(self: IDocumentPaginatorSource) -> DocumentPaginator

"""



class PagesChangedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Documents.DocumentPaginator.PagesChanged event.
    
    PagesChangedEventArgs(start: int, count: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, start, count):
        """ __new__(cls: type, start: int, count: int) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of continuous pages that changed.

Get: Count(self: PagesChangedEventArgs) -> int

"""

    Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the page number of the first page that changed.

Get: Start(self: PagesChangedEventArgs) -> int

"""



class PagesChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Documents.DocumentPaginator.PagesChanged event.
    
    PagesChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: PagesChangedEventHandler, sender: object, e: PagesChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: PagesChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PagesChangedEventHandler, sender: object, e: PagesChangedEventArgs) """
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


class PaginationProgressEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Documents.DynamicDocumentPaginator.PaginationProgress event.
    
    PaginationProgressEventArgs(start: int, count: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, start, count):
        """ __new__(cls: type, start: int, count: int) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of continuous pages that were paginated.

Get: Count(self: PaginationProgressEventArgs) -> int

"""

    Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the page number of the first page that was paginated.

Get: Start(self: PaginationProgressEventArgs) -> int

"""



class PaginationProgressEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Documents.DynamicDocumentPaginator.PaginationProgress event.
    
    PaginationProgressEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: PaginationProgressEventHandler, sender: object, e: PaginationProgressEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: PaginationProgressEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaginationProgressEventHandler, sender: object, e: PaginationProgressEventArgs) """
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


