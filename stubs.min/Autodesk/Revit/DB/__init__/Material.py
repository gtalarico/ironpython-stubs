class Material(Element, IDisposable):
    """ Represents a material element within an Autodesk Revit project. """
    def ClearMaterialAspect(self, aspect):
        """
        ClearMaterialAspect(self: Material, aspect: MaterialAspect)
            Removes an aspect from the material.
        
            aspect: The material aspect.
        """
        pass

    @staticmethod
    def Create(document, name):
        """
        Create(document: Document, name: str) -> ElementId
        
            Creates a new material.
        
            document: The document in which to create the material.
            name: The name of the new material.
            Returns: Identifier of the new material.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def Duplicate(self, name):
        """
        Duplicate(self: Material, name: str) -> Material
        
            Duplicates the material
        
            name: Name of the new material - this name must be correctly structured for Revit use 
             and not duplicate the name
           of another material in the document.
        
            Returns: The new material.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsMaterialOrValidDefault(pElem, materialId):
        """
        IsMaterialOrValidDefault(pElem: Element, materialId: ElementId) -> bool
        
            Validates whether the specified element id is a material element.
        
            pElem: An element which will be applied the material
            materialId: The element id to be checked.
            Returns: True if the element a material element or invalidElementId, which means take 
             material from category, false otherwise.
        """
        pass

    @staticmethod
    def IsNameUnique(aDocument, name):
        """
        IsNameUnique(aDocument: Document, name: str) -> bool
        
            Validates whether the material name is unique in document.
        
            aDocument: The document in which the name is being tested for uniqueness.
            name: The name tested for uniqueness.
            Returns: Returns true if the name is unique, and false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetMaterialAspectByPropertySet(self, aspect, propertySetId):
        """
        SetMaterialAspectByPropertySet(self: Material, aspect: MaterialAspect, propertySetId: ElementId)
            Sets an aspect of the material to a shared property set.
        
            aspect: The material aspect.
            propertySetId: Identifier of a shared property set (an instance of PropertySetElement).
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

    AppearanceAssetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the AppearanceAssetElement.

Get: AppearanceAssetId(self: Material) -> ElementId

Set: AppearanceAssetId(self: Material) = value
"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The color of the material.

Get: Color(self: Material) -> Color

Set: Color(self: Material) = value
"""

    CutPatternColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The color of the material cut pattern.

Get: CutPatternColor(self: Material) -> Color

Set: CutPatternColor(self: Material) = value
"""

    CutPatternId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FillPatternElement associated to cut views of faces with this material.

Get: CutPatternId(self: Material) -> ElementId

Set: CutPatternId(self: Material) = value
"""

    Glow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The option for glow.

Get: Glow(self: Material) -> bool

Set: Glow(self: Material) = value
"""

    MaterialCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the material category, e.g. 'Wood'

Get: MaterialCategory(self: Material) -> str

Set: MaterialCategory(self: Material) = value
"""

    MaterialClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the general material type, e.g. 'Wood.'

Get: MaterialClass(self: Material) -> str

Set: MaterialClass(self: Material) = value
"""

    Shininess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The shininess of the material.

Get: Shininess(self: Material) -> int

Set: Shininess(self: Material) = value
"""

    Smoothness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The smoothness of the material.

Get: Smoothness(self: Material) -> int

Set: Smoothness(self: Material) = value
"""

    StructuralAssetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the structural PropertySetElement.

Get: StructuralAssetId(self: Material) -> ElementId

Set: StructuralAssetId(self: Material) = value
"""

    SurfacePatternColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The color of the material surface pattern.

Get: SurfacePatternColor(self: Material) -> Color

Set: SurfacePatternColor(self: Material) = value
"""

    SurfacePatternId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the FillPatternElement associated to normal views of faces with this material.

Get: SurfacePatternId(self: Material) -> ElementId

Set: SurfacePatternId(self: Material) = value
"""

    ThermalAssetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the thermal PropertySetElement.

Get: ThermalAssetId(self: Material) -> ElementId

Set: ThermalAssetId(self: Material) = value
"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The transparency of the material.

Get: Transparency(self: Material) -> int

Set: Transparency(self: Material) = value
"""

    UseRenderAppearanceForShading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True to use the render appearance settings for shaded view appearance;
   false to use the material's color and transparency value for shaded view appearance.

Get: UseRenderAppearanceForShading(self: Material) -> bool

Set: UseRenderAppearanceForShading(self: Material) = value
"""


