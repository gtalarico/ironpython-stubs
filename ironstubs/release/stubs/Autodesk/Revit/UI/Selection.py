# encoding: utf-8
# module Autodesk.Revit.UI.Selection calls itself Selection
# from RevitAPIUI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ISelectionFilter:
    """ An interface that provides the ability to filter objects during a selection operation. """
    def AllowElement(self, elem):
        """
        AllowElement(self: ISelectionFilter, elem: Element) -> bool
        
            Override this pre-filter method to specify if the element should be permitted 
             to be selected.
        
        
            elem: A candidate element in selection operation.
            Returns: Return true to allow the user to select this candidate element. Return false to 
             prevent selection of this element.
        """
        pass

    def AllowReference(self, reference, position):
        """
        AllowReference(self: ISelectionFilter, reference: Reference, position: XYZ) -> bool
        
            Override this post-filter method to specify if a reference to a piece of 
             geometry is permitted to be selected.
        
        
            reference: A candidate reference in selection operation.
            position: The 3D position of the mouse on the candidate reference.
            Returns: Return true to allow the user to select this candidate reference. Return false 
             to prevent selection of this candidate.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ObjectSnapTypes(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumerated type contains object snap types allowed to be set during PickPoint operations.
    
    enum (flags) ObjectSnapTypes, values: Centers (32), Endpoints (1), Intersections (16), Midpoints (2), Nearest (4), None (0), Perpendicular (64), Points (512), Quadrants (256), Tangents (128), WorkPlaneGrid (8)
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

    Centers = None
    Endpoints = None
    Intersections = None
    Midpoints = None
    Nearest = None
    None = None
    Perpendicular = None
    Points = None
    Quadrants = None
    Tangents = None
    value__ = None
    WorkPlaneGrid = None


class ObjectType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumerated type contains object types allowed to be selected during selection operations.
    
    enum ObjectType, values: Edge (3), Element (1), Face (4), LinkedElement (5), Nothing (0), PointOnElement (2)
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

    Edge = None
    Element = None
    Face = None
    LinkedElement = None
    Nothing = None
    PointOnElement = None
    value__ = None


class PickBoxStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    The enum that controls the style of the pick box.
    
    enum PickBoxStyle, values: Crossing (0), Directional (2), Enclosing (1)
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

    Crossing = None
    Directional = None
    Enclosing = None
    value__ = None


class PickedBox(object):
    """ A class that contains two XYZ points representing the pick box on the screen. """
    Max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum coordinates (upper-right-front corner of the pick box).

Get: Max(self: PickedBox) -> XYZ

Set: Max(self: PickedBox) = value
"""

    Min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minimum coordinates (lower-left-rear corner of the pick box).

Get: Min(self: PickedBox) -> XYZ

Set: Min(self: PickedBox) = value
"""



class SelectableInViewFilter(ElementSlowFilter, IDisposable):
    """
    A filter that passes elements that are selectable in the given view.
    
    SelectableInViewFilter(document: Document, viewId: ElementId, inverted: bool)
    SelectableInViewFilter(document: Document, viewId: ElementId)
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElementFilter, disposing: bool) """
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

    @staticmethod # known case of __new__
    def __new__(self, document, viewId, inverted=None):
        """
        __new__(cls: type, document: Document, viewId: ElementId, inverted: bool)
        __new__(cls: type, document: Document, viewId: ElementId)
        """
        pass


class Selection(object, IDisposable):
    """ Contains the current user selection of elements within the project. """
    def Dispose(self):
        """ Dispose(self: Selection) """
        pass

    def GetElementIds(self):
        """
        GetElementIds(self: Selection) -> ICollection[ElementId]
        
            Returns the ids of the elements that are currently selected.
            Returns: The collection containing the ids of the selected elements.
        """
        pass

    def PickBox(self, style, statusPrompt=None):
        """
        PickBox(self: Selection, style: PickBoxStyle) -> PickedBox
        
            Invokes a general purpose two-click editor that lets the user to specify a 
             rectangular area on the screen.
        
        
            style: Specifies the value that controls the style of the pick box.
            Returns: The picked box that contains two XYZ points.
        PickBox(self: Selection, style: PickBoxStyle, statusPrompt: str) -> PickedBox
        
            Invokes a general purpose two-click editor that lets the user to specify a 
             rectangular area on the screen.
        
        
            style: Specifies the value that controls the style of the pick box.
            statusPrompt: The message shown on the status bar.
            Returns: The picked box that contains two XYZ points.
        """
        pass

    def PickElementsByRectangle(self, *__args):
        """
        PickElementsByRectangle(self: Selection, statusPrompt: str) -> IList[Element]
        
            Prompts the user to select multiple elements by drawing a rectangle while 
             showing a custom status prompt string.
        
        
            statusPrompt: The message shown on the status bar.
            Returns: A collection of elements selected by the user. Note: if the user cancels the 
             operation (for example, through ESC), the method will throw an 
             OperationCanceledException instance.
        
        PickElementsByRectangle(self: Selection) -> IList[Element]
        
            Prompts the user to select multiple elements by drawing a rectangle.
            Returns: A collection of elements selected by the user. Note: if the user cancels the 
             operation (for example, through ESC), the method will throw an 
             OperationCanceledException instance.
        
        PickElementsByRectangle(self: Selection, selectionFilter: ISelectionFilter, statusPrompt: str) -> IList[Element]
        
            Prompts the user to select multiple elements by drawing a rectangle which pass 
             a customer filter while showing a custom status prompt string.
        
        
            selectionFilter: The selection filter.
            statusPrompt: The message shown on the status bar.
            Returns: A collection of elements selected by the user. Note: if the user cancels the 
             operation (for example, through ESC), the method will throw an 
             OperationCanceledException instance.
        
        PickElementsByRectangle(self: Selection, selectionFilter: ISelectionFilter) -> IList[Element]
        
            Prompts the user to select multiple elements by drawing a rectangle which pass 
             a customer filter.
        
        
            selectionFilter: The selection filter.
            Returns: A collection of elements selected by the user. Note: if the user cancels the 
             operation (for example, through ESC), the method will throw an 
             OperationCanceledException instance.
        """
        pass

    def PickObject(self, objectType, *__args):
        """
        PickObject(self: Selection, objectType: ObjectType, statusPrompt: str) -> Reference
        
            Prompts the user to select one object while showing a custom status prompt 
             string.
        
        
            objectType: Specifies the type of object to be selected.
            statusPrompt: The message shown on the status bar.
            Returns: A reference object selected by user.Note: if the user cancels the operation 
             (for example, through ESC), the method will throw an OperationCanceledException 
             instance.
        
        PickObject(self: Selection, objectType: ObjectType) -> Reference
        
            Prompts the user to select one object.
        
            objectType: Specifies the type of object to be selected.
            Returns: A reference object selected by user.Note: if the user cancels the operation 
             (for example, through ESC), the method will throw an OperationCanceledException 
             instance.
        
        PickObject(self: Selection, objectType: ObjectType, selectionFilter: ISelectionFilter, statusPrompt: str) -> Reference
        
            Prompts the user to select one object which passes a custom filter while 
             showing a custom status prompt string.
        
        
            objectType: Specifies the type of object to be selected.
            selectionFilter: The selection filter.
            statusPrompt: The message shown on the status bar.
            Returns: A reference object selected by user.Note: if the user cancels the operation 
             (for example, through ESC), the method will throw an OperationCanceledException 
             instance.
        
        PickObject(self: Selection, objectType: ObjectType, selectionFilter: ISelectionFilter) -> Reference
        
            Prompts the user to select one object which passes a custom filter.
        
            objectType: Specifies the type of object to be selected.
            selectionFilter: The selection filter.
            Returns: A reference object selected by user.Note: if the user cancels the operation 
             (for example, through ESC), the method will throw an OperationCanceledException 
             instance.
        """
        pass

    def PickObjects(self, objectType, *__args):
        """
        PickObjects(self: Selection, objectType: ObjectType, statusPrompt: str) -> IList[Reference]
        
            Prompts the user to select multiple objects while showing a custom status 
             prompt string.
        
        
            objectType: Specifies the type of object to be selected.
            statusPrompt: The message shown on the status bar.
            Returns: A collection of references selected by the user.Note: if the user cancels the 
             operation (for example, through ESC), the method will throw an 
             OperationCanceledException instance.
        
        PickObjects(self: Selection, objectType: ObjectType) -> IList[Reference]
        
            Prompts the user to select multiple objects.
        
            objectType: Specifies the type of object to be selected.
            Returns: A collection of references selected by the user.Note: if the user cancels the 
             operation (for example, through ESC), the method will throw an 
             OperationCanceledException instance.
        
        PickObjects(self: Selection, objectType: ObjectType, selectionFilter: ISelectionFilter) -> IList[Reference]
        
            Prompts the user to select multiple objects which pass a customer filter.
        
            objectType: Specifies the type of object to be selected.
            selectionFilter: The selection filter.
            Returns: A collection of references selected by the user.Note: if the user cancels the 
             operation (for example, through ESC), the method will throw an 
             OperationCanceledException instance.
        
        PickObjects(self: Selection, objectType: ObjectType, selectionFilter: ISelectionFilter, statusPrompt: str, pPreSelected: IList[Reference]) -> IList[Reference]
        PickObjects(self: Selection, objectType: ObjectType, selectionFilter: ISelectionFilter, statusPrompt: str) -> IList[Reference]
        
            Prompts the user to select multiple objects which pass a custom filter while 
             showing a custom status prompt string.
        
        
            objectType: Specifies the type of object to be selected.
            selectionFilter: The selection filter.
            statusPrompt: The message shown on the status bar.
            Returns: A collection of references selected by the user.Note: if the user cancels the 
             operation (for example, through ESC), the method will throw an 
             OperationCanceledException instance.
        """
        pass

    def PickPoint(self, *__args):
        """
        PickPoint(self: Selection, snapSettings: ObjectSnapTypes) -> XYZ
        
            Prompts the user to pick a point on the active work plane using specified snap 
             settings.
        
        
            snapSettings: Specifies the object snap types for this pick. Multiple object snap types can 
             be combined with "|"
        
            Returns: The point picked by user.Note: if the user cancels the operation (for example, 
             through ESC), the method will throw an OperationCanceledException instance.
        
        PickPoint(self: Selection) -> XYZ
        
            Prompts the user to pick a point on the active work plane.
            Returns: The point picked by user.Note: if the user cancels the operation (for example, 
             through ESC), the method will throw an OperationCanceledException instance.
        
        PickPoint(self: Selection, snapSettings: ObjectSnapTypes, statusPrompt: str) -> XYZ
        
            Prompts the user to pick a point on the active work plane using specified snap 
             settings while showing a custom status prompt string.
        
        
            snapSettings: Specifies the object snap types for this pick. Multiple object snap types can 
             be combined with "|"
        
            statusPrompt: Specifies the message shown on the status bar.
            Returns: The point picked by user.Note: if the user cancels the operation (for example, 
             through ESC), the method will throw an OperationCanceledException instance.
        
        PickPoint(self: Selection, statusPrompt: str) -> XYZ
        
            Prompts the user to pick a point on the active work plane while showing a 
             custom status prompt string.
        
        
            statusPrompt: Specifies the message shown on the status bar.
            Returns: The point picked by user.Note: if the user cancels the operation (for example, 
             through ESC), the method will throw an OperationCanceledException instance.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Selection, disposing: bool) """
        pass

    def SetElementIds(self, elementIds):
        """ SetElementIds(self: Selection, elementIds: ICollection[ElementId]) """
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

Get: IsValidObject(self: Selection) -> bool

"""



