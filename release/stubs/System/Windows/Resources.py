# encoding: utf-8
# module System.Windows.Resources calls itself Resources
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
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



