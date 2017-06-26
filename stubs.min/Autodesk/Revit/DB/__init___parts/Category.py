class Category(APIObject, IDisposable):
    """ Represents the category or subcategory to which an element belongs. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    @staticmethod
    def GetCategory(document, categoryId):
        """
        GetCategory(document: Document, categoryId: BuiltInCategory) -> Category
        
            Retrieves a category object corresponding to a BuiltInCategory id.
        
            document: The document.
            categoryId: A build in category id.
            Returns: Returns a category object corresponding to a BuiltInCategory id.
        GetCategory(document: Document, categoryId: ElementId) -> Category
        
            Retrieves a category object corresponding to the category id.
        
            document: The document.
            categoryId: An category id.
            Returns: Returns a category object corresponding to the category id.
        """
        pass

    def GetGraphicsStyle(self, graphicsStyleType):
        """
        GetGraphicsStyle(self: Category, graphicsStyleType: GraphicsStyleType) -> GraphicsStyle
        
            Gets the graphics style associated with this category for the given graphics 
             style type.
        
        
            graphicsStyleType: The type of graphics style.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Category) -> int """
        pass

    def GetLinePatternId(self, graphicsStyleType):
        """
        GetLinePatternId(self: Category, graphicsStyleType: GraphicsStyleType) -> ElementId
        
            Gets the line pattern id associated with this category for the given graphics 
             style type.
        
        
            graphicsStyleType: The type of graphics style.
            Returns: Returns the line pattern id associated with this category for the given 
             graphics style type.
        """
        pass

    def GetLineWeight(self, graphicsStyleType):
        """
        GetLineWeight(self: Category, graphicsStyleType: GraphicsStyleType) -> Nullable[int]
        
            Retrieves the line weight assigned to the category for the given graphics style 
             type.
        
        
            graphicsStyleType: The type of graphics style.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
        pass

    def SetLinePatternId(self, linePatternId, graphicsStyleType):
        """
        SetLinePatternId(self: Category, linePatternId: ElementId, graphicsStyleType: GraphicsStyleType)
            Sets the line pattern id associated with this category for the given graphics 
             style type.
        
        
            linePatternId: The line pattern id for the graphics style.
            graphicsStyleType: The type of graphics style.
        """
        pass

    def SetLineWeight(self, lineWeight, graphicsStyleType):
        """
        SetLineWeight(self: Category, lineWeight: int, graphicsStyleType: GraphicsStyleType)
            Sets the line weight for the given graphics style type.
        
            graphicsStyleType: The type of graphics style.
        """
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

    AllowsBoundParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """To check if the category can have project parameters.

Get: AllowsBoundParameters(self: Category) -> bool

"""

    CanAddSubcategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if subcategories can be assigned to the category.

Get: CanAddSubcategory(self: Category) -> bool

"""

    CategoryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the category type of this category.

Get: CategoryType(self: Category) -> CategoryType

"""

    HasMaterialQuantities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if elements of the category are able to report what materials they contain in what quantities.

Get: HasMaterialQuantities(self: Category) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the category id associated with the category object.

Get: Id(self: Category) -> ElementId

"""

    IsCuttable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the category is cuttable or not.

Get: IsCuttable(self: Category) -> bool

"""

    IsTagCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the category is associated with a type of tag for a different category.

Get: IsTagCategory(self: Category) -> bool

"""

    LineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The color of lines shown for elements of this category.

Get: LineColor(self: Category) -> Color

Set: LineColor(self: Category) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves or changes the material of the category.

Get: Material(self: Category) -> Material

Set: Material(self: Category) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The category name.

Get: Name(self: Category) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the parent category of this category.

Get: Parent(self: Category) -> Category

"""

    SubCategories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a map containing all of the subcategories of this category.

Get: SubCategories(self: Category) -> CategoryNameMap

"""


