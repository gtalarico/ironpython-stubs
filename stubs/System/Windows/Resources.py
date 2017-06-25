# encoding: utf-8
# module System.Windows.Resources calls itself Resources
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AssemblyAssociatedContentFileAttribute(Attribute, _Attribute):
    """
    This attribute is interpreted during the Extensible Application Markup Language (XAML) compilation process to associate loose content with a Windows Presentation Foundation (WPF) application.
    
    AssemblyAssociatedContentFileAttribute(relativeContentFilePath: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, relativeContentFilePath):
        """ __new__(cls: type, relativeContentFilePath: str) """
        pass

    RelativeContentFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the path to the associated content.

Get: RelativeContentFilePath(self: AssemblyAssociatedContentFileAttribute) -> str

"""



class ContentTypes(object):
    """
    Supports Extensible Application Markup Language (XAML) as a content type and resource.
    
    ContentTypes()
    """
    XamlContentType = 'applicaton/xaml+xml'


class StreamResourceInfo(object):
    """
    Stores information for a stream resource used in Windows Presentation Foundation (WPF), such as images.
    
    StreamResourceInfo()
    StreamResourceInfo(stream: Stream, contentType: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, stream=None, contentType=None):
        """
        __new__(cls: type)
        __new__(cls: type, stream: Stream, contentType: str)
        """
        pass

    ContentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the content type of a stream.

Get: ContentType(self: StreamResourceInfo) -> str

"""

    Stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the actual stream of the resource.

Get: Stream(self: StreamResourceInfo) -> Stream

"""



