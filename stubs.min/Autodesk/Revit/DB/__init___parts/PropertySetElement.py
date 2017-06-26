class PropertySetElement(Element, IDisposable):
    """ An element that groups together a set of related parameters. """
    @staticmethod
    def Create(document, *__args):
        """
        Create(document: Document, structuralAsset: StructuralAsset) -> PropertySetElement
        
            Creates a new PropertySetElement to contain the given asset.
        
            document: The document in which to create the PropertySetElement.
            structuralAsset: The structural asset containing the values that will be present in the 
             PropertySetElement.
        
            Returns: The new PropertySetElement.
        Create(document: Document, thermalAsset: ThermalAsset) -> PropertySetElement
        
            Creates a new PropertySetElement to contain the given asset.
        
            document: The document in which to create the PropertySetElement.
            thermalAsset: The thermal asset containing the values that will be present in the 
             PropertySetElement.
        
            Returns: The new PropertySetElement.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def Duplicate(self, document, name):
        """
        Duplicate(self: PropertySetElement, document: Document, name: str) -> PropertySetElement
        
            Creates a duplicate of this PropertySetElement.
        
            document: The document in which to create the PropertySetElement.
            name: The name to use for the new PropertySetElement.
            Returns: The new PropertySetElement.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetStructuralAsset(self):
        """
        GetStructuralAsset(self: PropertySetElement) -> StructuralAsset
        
            Gets a copy of the StructuralAsset.
        """
        pass

    def GetThermalAsset(self):
        """
        GetThermalAsset(self: PropertySetElement) -> ThermalAsset
        
            Gets a copy of the ThermalAsset.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetStructuralAsset(self, structuralAsset):
        """
        SetStructuralAsset(self: PropertySetElement, structuralAsset: StructuralAsset)
            Sets a copy of the given StucturalAsset to be used in the PropertySetElement.
        """
        pass

    def SetThermalAsset(self, thermalAsset):
        """
        SetThermalAsset(self: PropertySetElement, thermalAsset: ThermalAsset)
            Sets a copy of the given ThermalAsset to be used in the PropertySetElement.
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

