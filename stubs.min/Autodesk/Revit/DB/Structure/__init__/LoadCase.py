class LoadCase(Element, IDisposable):
    """ An object that represents a load usage. """
    @staticmethod
    def Create(document, name, natureId, *__args):
        """
        Create(document: Document, name: str, natureId: ElementId, loadCaseCategory: LoadCaseCategory) -> LoadCase
        
            Creates a new LoadCase.
        
            document: The Document to which new load case element will be added.
            name: The name of the load case.
            natureId: The load nature ID.
            loadCaseCategory: The predefined load case category.
            Returns: The newly created load case element if successful, ll otherwise.
        Create(document: Document, name: str, natureId: ElementId, subcategoryId: ElementId) -> LoadCase
        
            Creates a new LoadCase.
        
            document: The Document to which new load case element will be added.
            name: The name of the load case.
            natureId: The load nature ID.
            subcategoryId: The load case subcategory ID. Could be one of predefined or user defined load 
             case category.
           Built-in structural Load Cases 
             (Autodesk.Revit.DB.BuiltInCategory.OST_LoadCases) subcategories are:
           
             Autodesk.Revit.DB.BuiltInCategory.OST_LoadCasesDeadAutodesk.Revit.DB.BuiltInCate
             gory.OST_LoadCasesLiveAutodesk.Revit.DB.BuiltInCategory.OST_LoadCasesWindAutodes
             k.Revit.DB.BuiltInCategory.OST_LoadCasesSnowAutodesk.Revit.DB.BuiltInCategory.OS
             T_LoadCasesRoofLiveAutodesk.Revit.DB.BuiltInCategory.OST_LoadCasesAccidentalAuto
             desk.Revit.DB.BuiltInCategory.OST_LoadCasesTemperatureAutodesk.Revit.DB.BuiltInC
             ategory.OST_LoadCasesSeismic
        
            Returns: The newly created load case element if successful, ll otherwise.
        Create(document: Document, name: str, natureId: ElementId, natureCategory: LoadNatureCategory) -> LoadCase
        
            Creates a new LoadCase.
        
            document: The Document to which new load case element will be added.
            name: The name of the load case.
            natureId: The load nature ID.
            natureCategory: The predefined load nature category.
            Returns: The newly created load case element if successful, ll otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsLoadCaseSubcategoryId(self, loadCaseSubcategoryId):
        """
        IsLoadCaseSubcategoryId(self: LoadCase, loadCaseSubcategoryId: ElementId) -> bool
        
            Checks whether provided element ID refer to subcategory of Structural Load 
             Cases (Autodesk.Revit.DB.BuiltInCategory.OST_LoadCases) category - one of 
             built-in or user defined.
        
        
            loadCaseSubcategoryId: The ID to check.
            Returns: True if the ID refers to load case category element, false otherwise.
        """
        pass

    def IsLoadNatureId(self, natureId):
        """
        IsLoadNatureId(self: LoadCase, natureId: ElementId) -> bool
        
            Checks whether provided element ID refer to LoadNature element.
        
            natureId: The ID to check.
            Returns: True if the ID refers to LoadNature element, false otherwise.
        """
        pass

    @staticmethod
    def IsNumberUnique(document, number):
        """
        IsNumberUnique(document: Document, number: int) -> bool
        
            Checks that a given number is unique among all load cases.
        
            number: The number to check.
            Returns: True if the given number is unique among all load cases, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    NatureCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The nature category of the load case.

Get: NatureCategory(self: LoadCase) -> LoadNatureCategory

Set: NatureCategory(self: LoadCase) = value
"""

    NatureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The nature ID of the load case.

Get: NatureId(self: LoadCase) -> ElementId

Set: NatureId(self: LoadCase) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns unique load case number.

Get: Number(self: LoadCase) -> int

Set: Number(self: LoadCase) = value
"""

    SubcategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Build-in or user defined subcategory of Structural Load Cases (Autodesk.Revit.DB.BuiltInCategory.OST_LoadCases) category.

Get: SubcategoryId(self: LoadCase) -> ElementId

Set: SubcategoryId(self: LoadCase) = value
"""


