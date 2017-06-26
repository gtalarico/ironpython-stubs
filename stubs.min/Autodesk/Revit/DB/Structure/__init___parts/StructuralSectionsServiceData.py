class StructuralSectionsServiceData(object, IDisposable):
    """
    The data needed by section type server to perform type definition.
    
    StructuralSectionsServiceData(document: Document, currentElementIds: IList[ElementId])
    """
    def Dispose(self):
        """ Dispose(self: StructuralSectionsServiceData) """
        pass

    def GetCurrentElements(self):
        """
        GetCurrentElements(self: StructuralSectionsServiceData) -> IList[ElementId]
        
            Returns the list of Ids of the current elements.
            Returns: Ids of the current elements. Contains the family base element to which the 
             section shape type parameter belongs.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSectionsServiceData, disposing: bool) """
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
    def __new__(self, document, currentElementIds):
        """ __new__(cls: type, document: Document, currentElementIds: IList[ElementId]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current document.

Get: Document(self: StructuralSectionsServiceData) -> Document

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: StructuralSectionsServiceData) -> bool

"""


