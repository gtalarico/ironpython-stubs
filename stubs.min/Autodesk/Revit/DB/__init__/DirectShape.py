class DirectShape(Element, IDisposable):
    """
    This class is used to store externally created geometric shapes. Primary intended use is for importing shapes from other data formats such as IFC or STEP.
       A DirectShape object may be assigned a category. That will affect how that object is displayed in Revit.
    """
    def AppendShape(self, *__args):
        """
        AppendShape(self: DirectShape, pGeomArr: IList[GeometryObject])AppendShape(self: DirectShape, pGeomArr: IList[GeometryObject], viewType: DirectShapeTargetViewType)AppendShape(self: DirectShape, ShapeBuilder: ShapeBuilder)
            Appends shape built by the supplied ShapeBuilderObject to shape representation 
             stored in this DirectShape.
           The data stored in the supplied ShapeBuilder 
             object will be cleared.
        
        
            ShapeBuilder: The ShapeBuilder object that was used to build the shape to be appended.
        """
        pass

    def AreOptionsValid(self, options):
        """
        AreOptionsValid(self: DirectShape, options: DirectShapeOptions) -> bool
        
            Validates that the given DirectShapeOptions are allowed for this particular 
             DirectShape.
        
        
            options: The options object.
            Returns: True if the DirectShapeOptions are valid; false otherwise.
        """
        pass

    def AreOptionsValidForTransientDirectShape(self, options):
        """
        AreOptionsValidForTransientDirectShape(self: DirectShape, options: DirectShapeOptions) -> bool
        
            Validates that the given DirectShapeOptions are allowed if this DirectShape is 
             transient.
        
        
            options: The options object.
            Returns: True if the DirectShapeOptions are valid; false otherwise.
        """
        pass

    @staticmethod
    def CreateElement(document, categoryId, applicationId=None, applicationDataId=None):
        """
        CreateElement(document: Document, categoryId: ElementId, applicationId: str, applicationDataId: str) -> DirectShape
        
            Creates a DirectShape object and adds it to document.
        
            document: Document to which the created element will be added.
            categoryId: Id of the category assigned to this DirectShape. Must be a valid category id.
            applicationId: An optional text string that identifies the creating application. May not be 
             empty.
        
            applicationDataId: An optional text string that identifies the data to the creating application.
         
               The intended use is to identify the native data that was the source of this 
             DirectShape.
        
            Returns: The created DirectShape object.
        CreateElement(document: Document, categoryId: ElementId) -> DirectShape
        
            Creates a DirectShape object and adds it to document.
        
            document: Document to which the created element will be added.
            categoryId: Id of the category assigned to this DirectShape. Must be a valid category id.
            Returns: The created DirectShape object.
        """
        pass

    @staticmethod
    def CreateElementInstance(document, typeId, categoryId, definitionId, trf, applicationId=None, applicationDataId=None):
        """
        CreateElementInstance(document: Document, typeId: ElementId, categoryId: ElementId, definitionId: str, trf: Transform, applicationId: str, applicationDataId: str) -> DirectShape
        
            Creates a DirectShape object and adds it to document.
           The shape stored in 
             the element is either a reference or a copy of a definition shape
           that was 
             created earlier. How the definitions are stored will determine whether an 
             instance or a copy of the
           shape will be created. See DirectShapeLibrary for 
             more details.
           This function is included for convenience. It essentially 
             combines CreateGeometryInstance and CreateElement.
        
        
            document: Document to which the created element will be added.
            typeId: Element id of a DirectShapeType element.
            categoryId: Id of the category assigned to this DirectShape. Must be a valid category id.
            definitionId: Id of the shape definition that was created earlier and stored via 
             DirectShapeLibrary.
        
            trf: Transform to be applied to the definition
            applicationId: A text string that identifies the creating application. May not be empty.
            applicationDataId: An optional text string that identifies the data to the creating application.
         
               The intended use is to identify the native data that was the source of this 
             DirectShape.
        
            Returns: The created DirectShape object.
        CreateElementInstance(document: Document, typeId: ElementId, categoryId: ElementId, definitionId: str, trf: Transform) -> DirectShape
        
            Creates a DirectShape object and adds it to document.
        
            document: Document to which the created element will be added.
            typeId: Element id of a DirectShapeType element.
            categoryId: Id of the category assigned to this DirectShape. Must be a valid category id.
            definitionId: Id of the shape definition that was created earlier and stored via 
             DirectShapeLibrary.
        
            trf: Transform to be applied to the definition.
            Returns: The created DirectShape object.
        """
        pass

    @staticmethod
    def CreateGeometryInstance(document, definition_id, trf):
        """
        CreateGeometryInstance(document: Document, definition_id: str, trf: Transform) -> IList[GeometryObject]
        
            Creates a copy of a definition shape that was created earlier.
        
            document: Document to which the created element will be added
            definition_id: ID of the shape definition that was created earlier and stored via 
             DirectShapeLibrary
        
            trf: Transform to be applied to the definition
            Returns: A collection of geometry objects representing a placed instance of the 
             pre-defined shape
           The caller function takes ownership
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetOptions(self):
        """
        GetOptions(self: DirectShape) -> DirectShapeOptions
        
            Gets a copy of the current options for this DirectShape.
            Returns: Options currently set for this DirectShape.
        """
        pass

    @staticmethod
    def IsSupportedDocument(document):
        """
        IsSupportedDocument(document: Document) -> bool
        
            Tests whether a DirectShape or a DirectShapeType may be created in this 
             document.
        
        
            document: Document to be tested.
            Returns: True if a DirectShape or a DirectShapeType object can be created in this 
             document, false otherwise.
        """
        pass

    @staticmethod
    def IsValidCategoryId(categoryId, doc):
        """
        IsValidCategoryId(categoryId: ElementId, doc: Document) -> bool
        
            Test the category id to make sure it is indeed a top-level built-in category.
        
            categoryId: Category id to be tested.
            doc: Document to look up the category by id.
            Returns: False unless categoryId corresponds to a valid built-in top-level model 
             category.
        """
        pass

    def IsValidGeometry(self, Geom):
        """
        IsValidGeometry(self: DirectShape, Geom: Solid) -> bool
        
            Validates geometry to be stored in a DirectShape. Suitable geometry validation 
             is performed. Additionally, the geometry
           must make sense as a shape 
             representation for the category assigned to this DirectShape object.
        
        
            Geom: Geometry object to be validated.
            Returns: True if the supplied geometry object passes the validation criteria.
        """
        pass

    def IsValidShape(self, shape, viewType=None):
        """
        IsValidShape(self: DirectShape, shape: IList[GeometryObject]) -> bool
        IsValidShape(self: DirectShape, shape: IList[GeometryObject], viewType: DirectShapeTargetViewType) -> bool
        """
        pass

    def IsValidTypeId(self, typeId):
        """
        IsValidTypeId(self: DirectShape, typeId: ElementId) -> bool
        
            Tests the type id to make sure it satisfies the following conditions
           It is 
             a valid element id.It corresponds to a valid DirectShapeType.The 
             DirectShapeType has the same category assigned.
           Additionally, this 
             functions tests that the current type id in this DirectShape is invalid.
           
             The type id is initialized to invalidElementId by the create functions. Once it 
             is set, it may no longer be changed.
        
        
            typeId: Type id to be tested.
            Returns: False unless typeId satisfies the conditions listed above and the type id of 
             this object was not set previously.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetGUIDs(self, appGUID, appDataGUID):
        """
        SetGUIDs(self: DirectShape, appGUID: str, appDataGUID: str)
            Sets the GUID of the application that has created this DirectShape element and
        
                the GUID of the native data that was the source of this DirectShape.
        
        
            appGUID: GUID of the application.
            appDataGUID: GUID of the native data.
        """
        pass

    def SetName(self, name):
        """
        SetName(self: DirectShape, name: str)
            Sets the name for the DirectShape element.
        
            name: The name.
        """
        pass

    def SetOptions(self, options):
        """
        SetOptions(self: DirectShape, options: DirectShapeOptions)
            Sets the options to use for this DirectShape.
        
            options: Options to use for this DirectShape.
        """
        pass

    def SetShape(self, *__args):
        """
        SetShape(self: DirectShape, pGeomArr: IList[GeometryObject])SetShape(self: DirectShape, pGeomArr: IList[GeometryObject], viewType: DirectShapeTargetViewType)SetShape(self: DirectShape, pBuilder: ShapeBuilder)
            Sets the shape of this object to the one accumulated in the supplied Builder 
             object.
           If the new shape is identical to the old one, the old shape will be 
             kept.
        
        
            pBuilder: A ShapeBuilder object that was used to successfully build geometry to store in 
             this DirectShape.
           The built shape will be transferred to the DirectShape, 
             and the ShapeBuilder object will be reset.
        """
        pass

    def SetTypeId(self, typeId):
        """
        SetTypeId(self: DirectShape, typeId: ElementId)
            Sets the DirectShapeType for the DirectShape element.
        
            typeId: The ID of the type corresponding to this DirectShape element. May only be set 
             once.
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

    ApplicationDataId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A text string that identifies the data to the creating application.

Get: ApplicationDataId(self: DirectShape) -> str

Set: ApplicationDataId(self: DirectShape) = value
"""

    ApplicationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A text string that identifies the creating application.

Get: ApplicationId(self: DirectShape) -> str

Set: ApplicationId(self: DirectShape) = value
"""

    TypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Element id of a DirectShapeType object that holds properties to be shared by this element. Optional.

Get: TypeId(self: DirectShape) -> ElementId

"""


