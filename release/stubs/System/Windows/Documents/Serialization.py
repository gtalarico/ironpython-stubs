# encoding: utf-8
# module System.Windows.Documents.Serialization calls itself Serialization
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ISerializerFactory:
    """ Provides a means for creating a software component that can serialize any part of a Windows Presentation Foundation (WPF) application's content to a manufacturer's proprietary format. """
    def CreateSerializerWriter(self, stream):
        """
        CreateSerializerWriter(self: ISerializerFactory, stream: Stream) -> SerializerWriter
        
            Initializes an object derived from the abstract 
             System.Windows.Documents.Serialization.SerializerWriter class for the specified 
             System.IO.Stream.
        
        
            stream: The System.IO.Stream to which the returned object writes.
            Returns: An object of a class derived from System.Windows.Documents.Serialization.SerializerWriter.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultFileExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default extension for files of the manufacturer's proprietary format.

Get: DefaultFileExtension(self: ISerializerFactory) -> str

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the public name of the manufacturer's serializing component.

Get: DisplayName(self: ISerializerFactory) -> str

"""

    ManufacturerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the serializing component's manufacturer.

Get: ManufacturerName(self: ISerializerFactory) -> str

"""

    ManufacturerWebsite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the web address of the serializing component's manufacturer.

Get: ManufacturerWebsite(self: ISerializerFactory) -> Uri

"""



class SerializerDescriptor(object):
    """ Provides information about installed plug-in serializers. """
    @staticmethod
    def CreateFromFactoryInstance(factoryInstance):
        """
        CreateFromFactoryInstance(factoryInstance: ISerializerFactory) -> SerializerDescriptor
        
            Creates a new System.Windows.Documents.Serialization.SerializerDescriptor through a given 
             System.Windows.Documents.Serialization.ISerializerFactory implementation.
        
        
            factoryInstance: The source of data for the new System.Windows.Documents.Serialization.SerializerDescriptor.
            Returns: A new System.Windows.Documents.Serialization.SerializerDescriptor with its properties 
             initialized with values from the given System.Windows.Documents.Serialization.ISerializerFactory 
             implementation.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: SerializerDescriptor, obj: object) -> bool
        
            Tests two System.Windows.Documents.Serialization.SerializerDescriptor objects for equality.
        
            obj: The object to be compared with this System.Windows.Documents.Serialization.SerializerDescriptor.
            Returns: true if both are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: SerializerDescriptor) -> int
        
            Gets the unique hash code value of the serializer.
            Returns: The unique hash code value of the serializer.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the assembly that contains the serializer.

Get: AssemblyName(self: SerializerDescriptor) -> str

"""

    AssemblyPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the path to the assembly file that contains the serializer.

Get: AssemblyPath(self: SerializerDescriptor) -> str

"""

    AssemblyVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version of the assembly that contains the serializer.

Get: AssemblyVersion(self: SerializerDescriptor) -> Version

"""

    DefaultFileExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default extension associated with files that the serializer outputs.

Get: DefaultFileExtension(self: SerializerDescriptor) -> str

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the public display name of the serializer.

Get: DisplayName(self: SerializerDescriptor) -> str

"""

    FactoryInterfaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the System.Windows.Documents.Serialization.ISerializerFactory derived class that implements the serializer.

Get: FactoryInterfaceName(self: SerializerDescriptor) -> str

"""

    IsLoadable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the serializer can be loaded with the currently installed version of Microsoft .NET Framework.

Get: IsLoadable(self: SerializerDescriptor) -> bool

"""

    ManufacturerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the company that developed the serializer.

Get: ManufacturerName(self: SerializerDescriptor) -> str

"""

    ManufacturerWebsite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the web address of the company that developed the serializer.

Get: ManufacturerWebsite(self: SerializerDescriptor) -> Uri

"""

    WinFXVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version of Microsoft .NET Framework required by the serializer.

Get: WinFXVersion(self: SerializerDescriptor) -> Version

"""



class SerializerProvider(object):
    """
    Manages serialization plug-ins created, using System.Windows.Documents.Serialization.ISerializerFactory and System.Windows.Documents.Serialization.SerializerDescriptor, by manufacturers who have their own proprietary serialization formats.
    
    SerializerProvider()
    """
    def CreateSerializerWriter(self, serializerDescriptor, stream):
        """
        CreateSerializerWriter(self: SerializerProvider, serializerDescriptor: SerializerDescriptor, stream: Stream) -> SerializerWriter
        
            Initializes an object derived from the abstract 
             System.Windows.Documents.Serialization.SerializerWriter class for the specified System.IO.Stream 
             that will use the specified descriptor.
        
        
            serializerDescriptor: A System.Windows.Documents.Serialization.SerializerDescriptor that contains serialization 
             information for the System.Windows.Documents.Serialization.SerializerWriter.
        
            stream: The System.IO.Stream to which the returned object writes.
            Returns: An object of a class derived from System.Windows.Documents.Serialization.SerializerWriter.
        """
        pass

    @staticmethod
    def RegisterSerializer(serializerDescriptor, overwrite):
        """
        RegisterSerializer(serializerDescriptor: SerializerDescriptor, overwrite: bool)
            Registers a serializer plug-in.
        
            serializerDescriptor: The System.Windows.Documents.Serialization.SerializerDescriptor for the plug-in.
            overwrite: true to overwrite an existing registration for the same plug-in; otherwise, false. See Remarks.
        """
        pass

    @staticmethod
    def UnregisterSerializer(serializerDescriptor):
        """
        UnregisterSerializer(serializerDescriptor: SerializerDescriptor)
            Deletes a serializer plug-in from the registry.
        
            serializerDescriptor: The System.Windows.Documents.Serialization.SerializerDescriptor for the plug-in.
        """
        pass

    InstalledSerializers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of the installed plug-in serializers.

Get: InstalledSerializers(self: SerializerProvider) -> ReadOnlyCollection[SerializerDescriptor]

"""



class SerializerWriter(object):
    """ Defines the abstract methods and events that are required to implement a plug-in document output serializer. """
    def CancelAsync(self):
        """
        CancelAsync(self: SerializerWriter)
            When overridden in a derived class, cancels an asynchronous write operation.
        """
        pass

    def CreateVisualsCollator(self, documentSequencePT=None, documentPT=None):
        """
        CreateVisualsCollator(self: SerializerWriter, documentSequencePT: PrintTicket, documentPT: PrintTicket) -> SerializerWriterCollator
        
            When overridden in a derived class, returns a 
             System.Windows.Documents.Serialization.SerializerWriterCollator that writes collated 
             System.Windows.Media.Visual elements together with the given print tickets.
        
        
            documentSequencePT: The default print preferences for System.Windows.Documents.FixedDocumentSequence content.
            documentPT: The default print preferences for System.Windows.Documents.FixedDocument content.
            Returns: A System.Windows.Documents.Serialization.SerializerWriterCollator that writes collated 
             System.Windows.Media.Visual elements to the document output serialization�System.IO.Stream.
        
        CreateVisualsCollator(self: SerializerWriter) -> SerializerWriterCollator
        
            When overridden in a derived class, returns a 
             System.Windows.Documents.Serialization.SerializerWriterCollator that writes collated 
             System.Windows.Media.Visual elements.
        
            Returns: A System.Windows.Documents.Serialization.SerializerWriterCollator that writes collated 
             System.Windows.Media.Visual elements to the document output serialization�System.IO.Stream.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: SerializerWriter, fixedDocument: FixedDocument)
            When overridden in a derived class, synchronously writes a given 
             System.Windows.Documents.FixedDocument to the serialization�System.IO.Stream.
        
        
            fixedDocument: The document to write to the serialization System.IO.Stream.
        Write(self: SerializerWriter, fixedPage: FixedPage, printTicket: PrintTicket)
            When overridden in a derived class, synchronously writes a given 
             System.Windows.Documents.FixedPage together with an associated System.Printing.PrintTicket to 
             the serialization�System.IO.Stream.
        
        
            fixedPage: The page to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the fixedPage content.
        Write(self: SerializerWriter, fixedDocument: FixedDocument, printTicket: PrintTicket)
            When overridden in a derived class, synchronously writes a given 
             System.Windows.Documents.FixedDocument together with an associated System.Printing.PrintTicket 
             to the serialization�System.IO.Stream.
        
        
            fixedDocument: The document to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the fixedDocument content.
        Write(self: SerializerWriter, fixedDocumentSequence: FixedDocumentSequence, printTicket: PrintTicket)
            When overridden in a derived class, synchronously writes a given 
             System.Windows.Documents.FixedDocumentSequence together with an associated 
             System.Printing.PrintTicket to the serialization�System.IO.Stream.
        
        
            fixedDocumentSequence: The document sequence that defines the content to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the fixedDocumentSequence content.
        Write(self: SerializerWriter, fixedDocumentSequence: FixedDocumentSequence)
            When overridden in a derived class, synchronously writes a given 
             System.Windows.Documents.FixedDocumentSequence to the serialization�System.IO.Stream.
        
        
            fixedDocumentSequence: The document sequence that defines the content to write to the serialization System.IO.Stream.
        Write(self: SerializerWriter, visual: Visual, printTicket: PrintTicket)
            When overridden in a derived class, synchronously writes a given System.Windows.Media.Visual 
             element together with an associated System.Printing.PrintTicket to the serialization�
             System.IO.Stream.
        
        
            visual: The System.Windows.Media.Visual element to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the visual element.
        Write(self: SerializerWriter, visual: Visual)
            When overridden in a derived class, synchronously writes a given System.Windows.Media.Visual 
             element to the serialization�System.IO.Stream.
        
        
            visual: The System.Windows.Media.Visual element to write to the serialization System.IO.Stream.
        Write(self: SerializerWriter, documentPaginator: DocumentPaginator)
            When overridden in a derived class, synchronously writes the content of a given 
             System.Windows.Documents.DocumentPaginator to the serialization�System.IO.Stream.
        
        
            documentPaginator: The document paginator that defines the content to write to the serialization System.IO.Stream.
        Write(self: SerializerWriter, fixedPage: FixedPage)
            When overridden in a derived class, synchronously writes a given 
             System.Windows.Documents.FixedPage to the serialization�System.IO.Stream.
        
        
            fixedPage: The page to write to the serialization System.IO.Stream.
        Write(self: SerializerWriter, documentPaginator: DocumentPaginator, printTicket: PrintTicket)
            When overridden in a derived class, synchronously writes paginated content together with an 
             associated System.Printing.PrintTicket to the serialization�System.IO.Stream.
        
        
            documentPaginator: The document paginator that defines the content to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the documentPaginator content.
        """
        pass

    def WriteAsync(self, *__args):
        """
        WriteAsync(self: SerializerWriter, fixedDocument: FixedDocument, printTicket: PrintTicket)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedDocument together with an associated System.Printing.PrintTicket 
             to the serialization�System.IO.Stream.
        
        
            fixedDocument: The document to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the fixedDocument content.
        WriteAsync(self: SerializerWriter, fixedDocument: FixedDocument, userState: object)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedDocument to the serialization�System.IO.Stream.
        
        
            fixedDocument: The document to write to the serialization System.IO.Stream.
            userState: A caller-specified object to identify the asynchronous write operation.
        WriteAsync(self: SerializerWriter, fixedDocument: FixedDocument)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedDocument to the serialization�System.IO.Stream.
        
        
            fixedDocument: The document to write to the serialization System.IO.Stream.
        WriteAsync(self: SerializerWriter, fixedPage: FixedPage, userState: object)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedPage to the serialization�System.IO.Stream.
        
        
            fixedPage: The page to write to the serialization System.IO.Stream.
            userState: A caller-specified object to identify the asynchronous write operation.
        WriteAsync(self: SerializerWriter, fixedPage: FixedPage, printTicket: PrintTicket, userState: object)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedPage together with an associated System.Printing.PrintTicket to 
             the serialization�System.IO.Stream.
        
        
            fixedPage: The page to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the fixedPage content.
            userState: A caller-specified object to identify the asynchronous write operation.
        WriteAsync(self: SerializerWriter, fixedDocumentSequence: FixedDocumentSequence, userState: object)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedDocumentSequence to the serialization�System.IO.Stream.
        
        
            fixedDocumentSequence: The document sequence that defines the content to write to the serialization System.IO.Stream.
            userState: A caller-specified object to identify the asynchronous write operation.
        WriteAsync(self: SerializerWriter, fixedDocumentSequence: FixedDocumentSequence, printTicket: PrintTicket, userState: object)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedDocumentSequence together with an associated 
             System.Printing.PrintTicket to the serialization�System.IO.Stream.
        
        
            fixedDocumentSequence: The document sequence that defines the content to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the fixedDocumentSequence content.
            userState: A caller-specified object to identify the asynchronous write operation.
        WriteAsync(self: SerializerWriter, fixedDocumentSequence: FixedDocumentSequence, printTicket: PrintTicket)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedDocumentSequence together with an associated 
             System.Printing.PrintTicket to the serialization�System.IO.Stream.
        
        
            fixedDocumentSequence: The document sequence that defines the content to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the fixedDocumentSequence content.
        WriteAsync(self: SerializerWriter, fixedDocument: FixedDocument, printTicket: PrintTicket, userState: object)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedDocument together with an associated System.Printing.PrintTicket 
             to the serialization�System.IO.Stream.
        
        
            fixedDocument: The document to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the fixedDocument content.
            userState: A caller-specified object to identify the asynchronous write operation.
        WriteAsync(self: SerializerWriter, fixedDocumentSequence: FixedDocumentSequence)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedDocumentSequence to the serialization�System.IO.Stream.
        
        
            fixedDocumentSequence: The document sequence that defines the content to write to the serialization System.IO.Stream.
        WriteAsync(self: SerializerWriter, visual: Visual, printTicket: PrintTicket, userState: object)
            When overridden in a derived class, asynchronously writes a given System.Windows.Media.Visual 
             element together with an associated System.Printing.PrintTicket and identifier to the 
             serialization�System.IO.Stream.
        
        
            visual: The System.Windows.Media.Visual element to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the visual element.
            userState: A caller-specified object to identify the asynchronous write operation.
        WriteAsync(self: SerializerWriter, documentPaginator: DocumentPaginator)
            When overridden in a derived class, asynchronously writes the content of a given 
             System.Windows.Documents.DocumentPaginator to the serialization�System.IO.Stream.
        
        
            documentPaginator: The document paginator that defines the content to write to the serialization System.IO.Stream.
        WriteAsync(self: SerializerWriter, visual: Visual, printTicket: PrintTicket)
            When overridden in a derived class, asynchronously writes a given System.Windows.Media.Visual 
             element together with an associated System.Printing.PrintTicket to the serialization�
             System.IO.Stream.
        
        
            visual: The System.Windows.Media.Visual element to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the visual element.
        WriteAsync(self: SerializerWriter, visual: Visual)
            When overridden in a derived class, asynchronously writes a given System.Windows.Media.Visual 
             element to the serialization�System.IO.Stream.
        
        
            visual: The System.Windows.Media.Visual element to write to the serialization System.IO.Stream.
        WriteAsync(self: SerializerWriter, visual: Visual, userState: object)
            When overridden in a derived class, asynchronously writes a given System.Windows.Media.Visual 
             element to the serialization�System.IO.Stream.
        
        
            visual: The System.Windows.Media.Visual element to write to the serialization System.IO.Stream.
            userState: A caller-specified object to identify the asynchronous write operation.
        WriteAsync(self: SerializerWriter, fixedPage: FixedPage)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedPage to the serialization�System.IO.Stream.
        
        
            fixedPage: The page to write to the serialization System.IO.Stream.
        WriteAsync(self: SerializerWriter, fixedPage: FixedPage, printTicket: PrintTicket)
            When overridden in a derived class, asynchronously writes a given 
             System.Windows.Documents.FixedPage together with an associated System.Printing.PrintTicket to 
             the serialization�System.IO.Stream.
        
        
            fixedPage: The page to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the fixedPage content.
        WriteAsync(self: SerializerWriter, documentPaginator: DocumentPaginator, printTicket: PrintTicket, userState: object)
            When overridden in a derived class, asynchronously writes paginated content together with an 
             associated System.Printing.PrintTicket to the serialization�System.IO.Stream.
        
        
            documentPaginator: The document paginator that defines the content to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the documentPaginator content.
            userState: A caller-specified object to identify the asynchronous write operation.
        WriteAsync(self: SerializerWriter, documentPaginator: DocumentPaginator, printTicket: PrintTicket)
            When overridden in a derived class, asynchronously writes the content of a given 
             System.Windows.Documents.DocumentPaginator to the serialization�System.IO.Stream.
        
        
            documentPaginator: The document paginator that defines the content to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the documentPaginator content.
        WriteAsync(self: SerializerWriter, documentPaginator: DocumentPaginator, userState: object)
            When overridden in a derived class, asynchronously writes the content of a given 
             System.Windows.Documents.DocumentPaginator to the serialization�System.IO.Stream.
        
        
            documentPaginator: The document paginator that defines the content to write to the serialization System.IO.Stream.
            userState: A caller-specified object to identify the asynchronous write operation.
        """
        pass

    WritingCancelled = None
    WritingCompleted = None
    WritingPrintTicketRequired = None
    WritingProgressChanged = None


class SerializerWriterCollator(object):
    """ Defines the abstract methods required to implement a plug-in document serialization�System.Windows.Media.Visual collator. """
    def BeginBatchWrite(self):
        """
        BeginBatchWrite(self: SerializerWriterCollator)
            When overridden in a derived class, initiates the start of a batch write operation.
        """
        pass

    def Cancel(self):
        """
        Cancel(self: SerializerWriterCollator)
            When overridden in a derived class, cancels a synchronous�
             erload:System.Windows.Documents.Serialization.SerializerWriterCollator.Write operation.
        """
        pass

    def CancelAsync(self):
        """
        CancelAsync(self: SerializerWriterCollator)
            When overridden in a derived class, cancels an asynchronous�
             erload:System.Windows.Documents.Serialization.SerializerWriterCollator.WriteAsync operation.
        """
        pass

    def EndBatchWrite(self):
        """
        EndBatchWrite(self: SerializerWriterCollator)
            When overridden in a derived class, completes a batch write operation.
        """
        pass

    def Write(self, visual, printTicket=None):
        """
        Write(self: SerializerWriterCollator, visual: Visual, printTicket: PrintTicket)
            When overridden in a derived class, synchronously writes a given System.Windows.Media.Visual 
             element together with an associated print ticket to the serialization stream.
        
        
            visual: A System.Windows.Media.Visual that is written to the stream.
            printTicket: An object specifying preferences for how the material should be printed.
        Write(self: SerializerWriterCollator, visual: Visual)
            When overridden in a derived class, synchronously writes a given System.Windows.Media.Visual 
             element to the serialization stream.
        
        
            visual: The visual element to write to the serialization System.IO.Stream.
        """
        pass

    def WriteAsync(self, visual, *__args):
        """
        WriteAsync(self: SerializerWriterCollator, visual: Visual, printTicket: PrintTicket)
            When overridden in a derived class, asynchronously writes a given System.Windows.Media.Visual 
             element together with an associated print ticket to the serialization stream.
        
        
            visual: The visual element to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the visual element.
        WriteAsync(self: SerializerWriterCollator, visual: Visual, printTicket: PrintTicket, userState: object)
            When overridden in a derived class, asynchronously writes a given System.Windows.Media.Visual 
             element together with an associated print ticket and identifier to the serialization stream.
        
        
            visual: The visual element to write to the serialization System.IO.Stream.
            printTicket: The default print preferences for the visual element.
            userState: A caller-specified object to identify the asynchronous write operation.
        WriteAsync(self: SerializerWriterCollator, visual: Visual)
            When overridden in a derived class, asynchronously writes a given System.Windows.Media.Visual 
             element to the serialization stream.
        
        
            visual: The visual element to write to the serialization System.IO.Stream.
        WriteAsync(self: SerializerWriterCollator, visual: Visual, userState: object)
            When overridden in a derived class, asynchronously writes a given System.Windows.Media.Visual 
             element with a specified event identifier to the serialization stream.
        
        
            visual: The visual element to write to the serialization System.IO.Stream.
            userState: A caller-specified object to identify the asynchronous write operation.
        """
        pass


class WritingCancelledEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Xps.XpsDocumentWriter.WritingCancelled event.
    
    WritingCancelledEventArgs(exception: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, exception):
        """ __new__(cls: type, exception: Exception) """
        pass

    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the exception that canceled the write operation.

Get: Error(self: WritingCancelledEventArgs) -> Exception

"""



class WritingCancelledEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents a method that will handle the System.Windows.Xps.XpsDocumentWriter.WritingCancelled event.
    
    WritingCancelledEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: WritingCancelledEventHandler, sender: object, e: WritingCancelledEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: WritingCancelledEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: WritingCancelledEventHandler, sender: object, e: WritingCancelledEventArgs) """
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


class WritingCompletedEventArgs(AsyncCompletedEventArgs):
    """
    Provides data for the System.Windows.Documents.Serialization.SerializerWriter.WritingCompleted event.
    
    WritingCompletedEventArgs(cancelled: bool, state: object, exception: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, cancelled, state, exception):
        """ __new__(cls: type, cancelled: bool, state: object, exception: Exception) """
        pass


class WritingCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents a method that handles the System.Windows.Xps.XpsDocumentWriter.WritingCompleted event of the System.Windows.Xps.XpsDocumentWriter class.
    
    WritingCompletedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: WritingCompletedEventHandler, sender: object, e: WritingCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: WritingCompletedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: WritingCompletedEventHandler, sender: object, e: WritingCompletedEventArgs) """
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


class WritingPrintTicketRequiredEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Documents.Serialization.SerializerWriter.WritingPrintTicketRequired event.
    
    WritingPrintTicketRequiredEventArgs(printTicketLevel: PrintTicketLevel, sequence: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, printTicketLevel, sequence):
        """ __new__(cls: type, printTicketLevel: PrintTicketLevel, sequence: int) """
        pass

    CurrentPrintTicket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default printer settings to use when the document is printed.

Get: CurrentPrintTicket(self: WritingPrintTicketRequiredEventArgs) -> PrintTicket

Set: CurrentPrintTicket(self: WritingPrintTicketRequiredEventArgs) = value
"""

    CurrentPrintTicketLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the scope of the System.Windows.Documents.Serialization.SerializerWriter.WritingPrintTicketRequired event.

Get: CurrentPrintTicketLevel(self: WritingPrintTicketRequiredEventArgs) -> PrintTicketLevel

"""

    Sequence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of documents or pages output with the System.Windows.Documents.Serialization.WritingPrintTicketRequiredEventArgs.CurrentPrintTicket.

Get: Sequence(self: WritingPrintTicketRequiredEventArgs) -> int

"""



class WritingPrintTicketRequiredEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Windows.Xps.XpsDocumentWriter.WritingPrintTicketRequired event of an System.Windows.Xps.XpsDocumentWriter.
    
    WritingPrintTicketRequiredEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: WritingPrintTicketRequiredEventHandler, sender: object, e: WritingPrintTicketRequiredEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: WritingPrintTicketRequiredEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: WritingPrintTicketRequiredEventHandler, sender: object, e: WritingPrintTicketRequiredEventArgs) """
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


class WritingProgressChangedEventArgs(ProgressChangedEventArgs):
    """
    Provides data for the System.Windows.Xps.XpsDocumentWriter.WritingProgressChanged event.
    
    WritingProgressChangedEventArgs(writingLevel: WritingProgressChangeLevel, number: int, progressPercentage: int, state: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, writingLevel, number, progressPercentage, state):
        """ __new__(cls: type, writingLevel: WritingProgressChangeLevel, number: int, progressPercentage: int, state: object) """
        pass

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of documents or pages that have been written.

Get: Number(self: WritingProgressChangedEventArgs) -> int

"""

    WritingLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the scope of the writing progress.

Get: WritingLevel(self: WritingProgressChangedEventArgs) -> WritingProgressChangeLevel

"""



class WritingProgressChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents a method that will handle the System.Windows.Xps.XpsDocumentWriter.WritingProgressChanged event of an System.Windows.Xps.XpsDocumentWriter.
    
    WritingProgressChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: WritingProgressChangedEventHandler, sender: object, e: WritingProgressChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: WritingProgressChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: WritingProgressChangedEventHandler, sender: object, e: WritingProgressChangedEventArgs) """
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


class WritingProgressChangeLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the scope of a System.Windows.Documents.Serialization.SerializerWriter.WritingProgressChanged event.
    
    enum WritingProgressChangeLevel, values: FixedDocumentSequenceWritingProgress (1), FixedDocumentWritingProgress (2), FixedPageWritingProgress (3), None (0)
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

    FixedDocumentSequenceWritingProgress = None
    FixedDocumentWritingProgress = None
    FixedPageWritingProgress = None
    None = None
    value__ = None


