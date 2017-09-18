# encoding: utf-8
# module System.Windows.Baml2006 calls itself Baml2006
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Baml2006Reader(XamlReader, IDisposable, IXamlLineInfo, IFreezeFreezables):
    """
    Processes XAML in optimized BAML form and produces a XAML node stream.
    
    Baml2006Reader(fileName: str)
    Baml2006Reader(stream: Stream)
    Baml2006Reader(stream: Stream, xamlReaderSettings: XamlReaderSettings)
    """
    def Dispose(self, *args): #cannot find CLR method
        """
        Dispose(self: Baml2006Reader, disposing: bool)
            Releases the unmanaged resources used by the System.Windows.Baml2006.Baml2006Reader and 
             optionally releases the managed resources.
        
        
            disposing: true to release the managed resources; otherwise, false.
        """
        pass

    def Read(self):
        """
        Read(self: Baml2006Reader) -> bool
        
            Provides the next XAML node from the source BAML, if a node is available.
            Returns: true if a node is available; otherwise, false.
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
    def __new__(self, *__args):
        """
        __new__(cls: type, fileName: str)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, xamlReaderSettings: XamlReaderSettings)
        """
        pass

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether System.Xaml.XamlReader.Dispose(System.Boolean) has been called.

"""

    IsEof = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that reports whether the reader position is at the end of file.

Get: IsEof(self: Baml2006Reader) -> bool

"""

    Member = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current member at the reader position, if the reader position is on a System.Xaml.XamlNodeType.StartMember.

Get: Member(self: Baml2006Reader) -> XamlMember

"""

    Namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the XAML namespace from the current node.

Get: Namespace(self: Baml2006Reader) -> NamespaceDeclaration

"""

    NodeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the current node.

Get: NodeType(self: Baml2006Reader) -> XamlNodeType

"""

    SchemaContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that provides schema context information for the information set.

Get: SchemaContext(self: Baml2006Reader) -> XamlSchemaContext

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Xaml.XamlType of the current node.

Get: Type(self: Baml2006Reader) -> XamlType

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the current node.

Get: Value(self: Baml2006Reader) -> object

"""



