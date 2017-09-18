# encoding: utf-8
# module System.Windows.Diagnostics calls itself Diagnostics
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class VisualDiagnostics(object):
    # no doc
    @staticmethod
    def GetXamlSourceInfo(obj):
        """ GetXamlSourceInfo(obj: object) -> XamlSourceInfo """
        pass

    VisualTreeChanged = None
    __all__ = [
        'GetXamlSourceInfo',
        'VisualTreeChanged',
    ]


class VisualTreeChangeEventArgs(EventArgs):
    """ VisualTreeChangeEventArgs(parent: DependencyObject, child: DependencyObject, childIndex: int, changeType: VisualTreeChangeType) """
    @staticmethod # known case of __new__
    def __new__(self, parent, child, childIndex, changeType):
        """ __new__(cls: type, parent: DependencyObject, child: DependencyObject, childIndex: int, changeType: VisualTreeChangeType) """
        pass

    ChangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChangeType(self: VisualTreeChangeEventArgs) -> VisualTreeChangeType

"""

    Child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Child(self: VisualTreeChangeEventArgs) -> DependencyObject

"""

    ChildIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChildIndex(self: VisualTreeChangeEventArgs) -> int

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: VisualTreeChangeEventArgs) -> DependencyObject

"""



class VisualTreeChangeType(Enum, IComparable, IFormattable, IConvertible):
    """ enum VisualTreeChangeType, values: Add (0), Remove (1) """
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

    Add = None
    Remove = None
    value__ = None


class XamlSourceInfo(object):
    """ XamlSourceInfo(sourceUri: Uri, lineNumber: int, linePosition: int) """
    @staticmethod # known case of __new__
    def __new__(self, sourceUri, lineNumber, linePosition):
        """ __new__(cls: type, sourceUri: Uri, lineNumber: int, linePosition: int) """
        pass

    LineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineNumber(self: XamlSourceInfo) -> int

"""

    LinePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinePosition(self: XamlSourceInfo) -> int

"""

    SourceUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceUri(self: XamlSourceInfo) -> Uri

"""



