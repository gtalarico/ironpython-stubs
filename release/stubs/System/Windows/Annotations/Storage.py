# encoding: utf-8
# module System.Windows.Annotations.Storage calls itself Storage
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AnnotationStore(object, IDisposable):
    """ When overridden in a derived class, represents a data store for writing and reading user annotations. """
    def AddAnnotation(self, newAnnotation):
        """
        AddAnnotation(self: AnnotationStore, newAnnotation: Annotation)
            Adds a new System.Windows.Annotations.Annotation to the store.
        
            newAnnotation: The annotation to add to the store.
        """
        pass

    def DeleteAnnotation(self, annotationId):
        """
        DeleteAnnotation(self: AnnotationStore, annotationId: Guid) -> Annotation
        
            Deletes the annotation with the specified System.Windows.Annotations.Annotation.Id from the 
             store.
        
        
            annotationId: The globally unique identifier (GUID)�System.Windows.Annotations.Annotation.Id property of the 
             annotation to be deleted.
        
            Returns: The annotation that was deleted; otherwise, null if an annotation with the specified 
             annotationId was not found in the store.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: AnnotationStore)
            Releases all managed and unmanaged resources used by the store.
        """
        pass

    def Flush(self):
        """
        Flush(self: AnnotationStore)
            Forces any annotation data retained in internal buffers to be written to the underlying storage 
             device.
        """
        pass

    def GetAnnotation(self, annotationId):
        """
        GetAnnotation(self: AnnotationStore, annotationId: Guid) -> Annotation
        
            Returns the annotation with the specified System.Windows.Annotations.Annotation.Id from the 
             store.
        
        
            annotationId: The globally unique identifier (GUID)�System.Windows.Annotations.Annotation.Id property of the 
             annotation to be returned.
        
            Returns: The annotation with the given annotationId; or null, if an annotation with the specified 
             annotationId was not found in the store.
        """
        pass

    def GetAnnotations(self, anchorLocator=None):
        """
        GetAnnotations(self: AnnotationStore) -> IList[Annotation]
        
            Returns a list of all the annotations in the store.
            Returns: The list of all annotations currently contained in the store.
        GetAnnotations(self: AnnotationStore, anchorLocator: ContentLocator) -> IList[Annotation]
        
            Returns a list of annotations that have System.Windows.Annotations.Annotation.Anchors with 
             locators that begin with a matching System.Windows.Annotations.ContentLocatorPart sequence.
        
        
            anchorLocator: The starting System.Windows.Annotations.ContentLocatorPart sequence to return matching 
             annotations for.
        
            Returns: The list of annotations that have System.Windows.Annotations.Annotation.Anchors with locators 
             that start and match the given anchorLocator; otherwise, null if no matching annotations were 
             found.
        """
        pass

    def OnAnchorChanged(self, *args): #cannot find CLR method
        """
        OnAnchorChanged(self: AnnotationStore, args: AnnotationResourceChangedEventArgs)
            Raises the System.Windows.Annotations.Storage.AnnotationStore.AnchorChanged event.
        
            args: The event data.
        """
        pass

    def OnAuthorChanged(self, *args): #cannot find CLR method
        """
        OnAuthorChanged(self: AnnotationStore, args: AnnotationAuthorChangedEventArgs)
            Raises the System.Windows.Annotations.Storage.AnnotationStore.AuthorChanged event.
        
            args: The event data.
        """
        pass

    def OnCargoChanged(self, *args): #cannot find CLR method
        """
        OnCargoChanged(self: AnnotationStore, args: AnnotationResourceChangedEventArgs)
            Raises the System.Windows.Annotations.Storage.AnnotationStore.CargoChanged event.
        
            args: The event data.
        """
        pass

    def OnStoreContentChanged(self, *args): #cannot find CLR method
        """
        OnStoreContentChanged(self: AnnotationStore, e: StoreContentChangedEventArgs)
            Raises the System.Windows.Annotations.Storage.AnnotationStore.StoreContentChanged event.
        
            e: The event data.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AutoFlush = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether data in annotation buffers is to be written immediately to the physical data store.

Get: AutoFlush(self: AnnotationStore) -> bool

Set: AutoFlush(self: AnnotationStore) = value
"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether erload:System.Windows.Annotations.Storage.AnnotationStore.Dispose has been called.

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object to use as a synchronization lock for System.Windows.Annotations.Storage.AnnotationStore critical sections.

"""


    AnchorChanged = None
    AuthorChanged = None
    CargoChanged = None
    StoreContentChanged = None


class StoreContentAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the actions performed on an System.Windows.Annotations.Annotation in an System.Windows.Annotations.Storage.AnnotationStore.
    
    enum StoreContentAction, values: Added (0), Deleted (1)
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
    Deleted = None
    value__ = None


class StoreContentChangedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Annotations.Storage.AnnotationStore.StoreContentChanged event.
    
    StoreContentChangedEventArgs(action: StoreContentAction, annotation: Annotation)
    """
    @staticmethod # known case of __new__
    def __new__(self, action, annotation):
        """ __new__(cls: type, action: StoreContentAction, annotation: Annotation) """
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the action performed.

Get: Action(self: StoreContentChangedEventArgs) -> StoreContentAction

"""

    Annotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Annotations.Annotation that changed in the store.

Get: Annotation(self: StoreContentChangedEventArgs) -> Annotation

"""



class StoreContentChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Windows.Annotations.Storage.AnnotationStore.StoreContentChanged event raised by the System.Windows.Annotations.Storage.AnnotationStore class.
    
    StoreContentChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: StoreContentChangedEventHandler, sender: object, e: StoreContentChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: StoreContentChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: StoreContentChangedEventHandler, sender: object, e: StoreContentChangedEventArgs) """
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


class XmlStreamStore(AnnotationStore, IDisposable):
    """
    Represents an XML data store for writing and reading user annotations.
    
    XmlStreamStore(stream: Stream)
    XmlStreamStore(stream: Stream, knownNamespaces: IDictionary[Uri, IList[Uri]])
    """
    def AddAnnotation(self, newAnnotation):
        """
        AddAnnotation(self: XmlStreamStore, newAnnotation: Annotation)
            Adds a new System.Windows.Annotations.Annotation to the store.
        
            newAnnotation: The annotation to add to the store.
        """
        pass

    def DeleteAnnotation(self, annotationId):
        """
        DeleteAnnotation(self: XmlStreamStore, annotationId: Guid) -> Annotation
        
            Deletes the annotation with the specified System.Windows.Annotations.Annotation.Id from the 
             store.
        
        
            annotationId: The globally unique identifier (GUID)�System.Windows.Annotations.Annotation.Id property of the 
             annotation to be deleted.
        
            Returns: The annotation that was deleted; otherwise, null if an annotation with the specified 
             annotationId was not found in the store.
        """
        pass

    def Dispose(self):
        """ Dispose(self: XmlStreamStore, disposing: bool) """
        pass

    def Flush(self):
        """
        Flush(self: XmlStreamStore)
            Forces any annotation data retained in internal buffers to be written to the underlying storage 
             device.
        """
        pass

    def GetAnnotation(self, annotationId):
        """
        GetAnnotation(self: XmlStreamStore, annotationId: Guid) -> Annotation
        
            Returns the annotation with the specified System.Windows.Annotations.Annotation.Id from the 
             store.
        
        
            annotationId: The globally unique identifier (GUID)�System.Windows.Annotations.Annotation.Id property of the 
             annotation to be returned.
        
            Returns: The annotation with the given annotationId; otherwise, null if an annotation with the specified 
             annotationId was not found in the store.
        """
        pass

    def GetAnnotations(self, anchorLocator=None):
        """
        GetAnnotations(self: XmlStreamStore) -> IList[Annotation]
        
            Returns a list of all the annotations in the store.
            Returns: The list of all annotations that are currently in the store.
        GetAnnotations(self: XmlStreamStore, anchorLocator: ContentLocator) -> IList[Annotation]
        
            Returns a list of annotations that have System.Windows.Annotations.Annotation.Anchors with 
             locators that begin with a matching System.Windows.Annotations.ContentLocatorPart sequence.
        
        
            anchorLocator: The starting System.Windows.Annotations.ContentLocatorPart sequence to return matching 
             annotations for.
        
            Returns: The list of annotations that have System.Windows.Annotations.Annotation.Anchors with locators 
             that start and match the given anchorLocator; otherwise, null if no matching annotations were 
             found.
        """
        pass

    @staticmethod
    def GetWellKnownCompatibleNamespaces(name):
        """
        GetWellKnownCompatibleNamespaces(name: Uri) -> IList[Uri]
        
            Returns a list of namespaces that are compatible as an input namespace.
        
            name: The starting URI sequence to return the list of namespaces for.
            Returns: A list of compatible namespaces that match name; otherwise, null if there are no compatible 
             namespaces found.
        """
        pass

    def OnAnchorChanged(self, *args): #cannot find CLR method
        """
        OnAnchorChanged(self: AnnotationStore, args: AnnotationResourceChangedEventArgs)
            Raises the System.Windows.Annotations.Storage.AnnotationStore.AnchorChanged event.
        
            args: The event data.
        """
        pass

    def OnAuthorChanged(self, *args): #cannot find CLR method
        """
        OnAuthorChanged(self: AnnotationStore, args: AnnotationAuthorChangedEventArgs)
            Raises the System.Windows.Annotations.Storage.AnnotationStore.AuthorChanged event.
        
            args: The event data.
        """
        pass

    def OnCargoChanged(self, *args): #cannot find CLR method
        """
        OnCargoChanged(self: AnnotationStore, args: AnnotationResourceChangedEventArgs)
            Raises the System.Windows.Annotations.Storage.AnnotationStore.CargoChanged event.
        
            args: The event data.
        """
        pass

    def OnStoreContentChanged(self, *args): #cannot find CLR method
        """ OnStoreContentChanged(self: XmlStreamStore, e: StoreContentChangedEventArgs) """
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
    def __new__(self, stream, knownNamespaces=None):
        """
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, knownNamespaces: IDictionary[Uri, IList[Uri]])
        """
        pass

    AutoFlush = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether data in annotation buffers is to be written immediately to the physical data store.

Get: AutoFlush(self: XmlStreamStore) -> bool

Set: AutoFlush(self: XmlStreamStore) = value
"""

    IgnoredNamespaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a list of the namespaces that were ignored when the XML stream was loaded.

Get: IgnoredNamespaces(self: XmlStreamStore) -> IList[Uri]

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether erload:System.Windows.Annotations.Storage.AnnotationStore.Dispose has been called.

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object to use as a synchronization lock for System.Windows.Annotations.Storage.AnnotationStore critical sections.

"""


    WellKnownNamespaces = None


