# encoding: utf-8
# module Autodesk.Revit.Creation calls itself Creation
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Application(APIObject, IDisposable):
    """ The Application Creation object is used to create new instances of utility objects. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def NewAreaCreationData(self, areaView, point):
        """
        NewAreaCreationData(self: Application, areaView: ViewPlan, point: UV) -> AreaCreationData
        
            Creates an object which wraps the arguments of Area for batch creation.
        
            areaView: The view of area element.
            point: A point which lies in an enclosed region of area boundary where the new area 
             will reside.
        
            Returns: The object containing the data needed for area creation.
        """
        pass

    def NewBoundingBoxUV(self, min_u=None, min_v=None, max_u=None, max_v=None):
        """
        NewBoundingBoxUV(self: Application) -> BoundingBoxUV
        
            Creates an empty two-dimensional rectangle.
        NewBoundingBoxUV(self: Application, min_u: float, min_v: float, max_u: float, max_v: float) -> BoundingBoxUV
        
            Creates a two-dimensional rectangle with supplied values.
        
            min_u: The first coordinate of min.
            min_v: The second coordinate of min.
            max_u: The first coordinate of max.
            max_v: The second coordinate of max.
        """
        pass

    def NewBoundingBoxXYZ(self):
        """
        NewBoundingBoxXYZ(self: Application) -> BoundingBoxXYZ
        
            Creates a three-dimensional rectangular box.
        """
        pass

    def NewBuildingSiteExportOptions(self):
        """
        NewBuildingSiteExportOptions(self: Application) -> BuildingSiteExportOptions
        
            Creates Building Site Export options.
        """
        pass

    def NewCategorySet(self):
        """
        NewCategorySet(self: Application) -> CategorySet
        
            Creates a new instance of a set specifically for holding category objects.
            Returns: A new instance of a Category Set.
        """
        pass

    def NewColor(self):
        """
        NewColor(self: Application) -> Color
        
            Returns a new color object.
            Returns: The new color object.
        """
        pass

    def NewCombinableElementArray(self):
        """
        NewCombinableElementArray(self: Application) -> CombinableElementArray
        
            Returns an array that can hold combinable element objects.
            Returns: An empty array that can contain any CombinableElement derived objects.
        """
        pass

    def NewCurveArrArray(self):
        """
        NewCurveArrArray(self: Application) -> CurveArrArray
        
            Creates an empty array that can store geometric curve loops.
            Returns: The empty array of curve loops.
        """
        pass

    def NewCurveArray(self):
        """
        NewCurveArray(self: Application) -> CurveArray
        
            Creates an empty array that can store geometric curves.
            Returns: An empty array that can hold geometric curves.
        """
        pass

    def NewCurveLoopsProfile(self, curveLoops):
        """
        NewCurveLoopsProfile(self: Application, curveLoops: CurveArrArray) -> CurveLoopsProfile
        
            Creates a new CurveLoopsProfile object.
        
            curveLoops: The curve loops of the Profile.
            Returns: The new CurveLoopsProfile object.
        """
        pass

    def NewDoubleArray(self):
        """
        NewDoubleArray(self: Application) -> DoubleArray
        
            Creates a new instance of a double array.
        """
        pass

    def NewDWFExportOptions(self):
        """
        NewDWFExportOptions(self: Application) -> DWFExportOptions
        
            Creates DWF Export options.
        """
        pass

    def NewDWFXExportOptions(self):
        """
        NewDWFXExportOptions(self: Application) -> DWFXExportOptions
        
            Creates DWFX Export options.
        """
        pass

    def NewElementId(self):
        """
        NewElementId(self: Application) -> ElementId
        
            Creates a new Autodesk::Revit::DB::ElementId^ object.
            Returns: The new Autodesk::Revit::DB::ElementId^ object.
        """
        pass

    def NewElementSet(self):
        """
        NewElementSet(self: Application) -> ElementSet
        
            Creates a new instance of a set specifically for holding elements.
            Returns: A new Element Set.
        """
        pass

    def NewFaceArray(self):
        """
        NewFaceArray(self: Application) -> FaceArray
        
            Creates a new instance of a face array.
        """
        pass

    def NewFamilyInstanceCreationData(self, *__args):
        """
        NewFamilyInstanceCreationData(self: Application, location: XYZ, symbol: FamilySymbol, level: Level, structuralType: StructuralType) -> FamilyInstanceCreationData
        
            Creates an object which wraps the arguments of NewFamilyInstance() for batch 
             creation.
        
        
            location: The physical location where the instance is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            level: A Level object that is used as the base level for the object.
            structuralType: If structural then specify the type of the component.
        NewFamilyInstanceCreationData(self: Application, location: XYZ, symbol: FamilySymbol, host: Element, structuralType: StructuralType) -> FamilyInstanceCreationData
        
            Creates an object which wraps the arguments of NewFamilyInstance() for batch 
             creation.
        
        
            location: The physical location where the instance is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            host: The object into which the family instance is to be inserted, often known as the 
             host.
        
            structuralType: If structural then specify the type of the component.
        NewFamilyInstanceCreationData(self: Application, location: XYZ, symbol: FamilySymbol, structuralType: StructuralType) -> FamilyInstanceCreationData
        
            Creates an object which wraps the arguments of NewFamilyInstance() for batch 
             creation.
        
        
            location: The physical location where the instance is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            structuralType: Specify if the family instance is structural.
        NewFamilyInstanceCreationData(self: Application, curve: Curve, symbol: FamilySymbol, level: Level, structuralType: StructuralType) -> FamilyInstanceCreationData
        
            Creates an object which wraps the arguments of NewFamilyInstance() for batch 
             creation.
        
        
            curve: The curve where the instance is based.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            level: A Level object that is used as the base level for the object.
            structuralType: If structural then specify the type of the component.
        NewFamilyInstanceCreationData(self: Application, location: XYZ, symbol: FamilySymbol, host: Element, level: Level, structuralType: StructuralType) -> FamilyInstanceCreationData
        
            Creates an object which wraps the arguments of NewFamilyInstance() for batch 
             creation.
        
        
            location: The physical location where the instance is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            host: The object into which the family instance is to be inserted, often known as the 
             host.
        
            level: A Level object that is used as the base level for the object.
            structuralType: If structural then specify the type of the component.
        NewFamilyInstanceCreationData(self: Application, face: Face, position: Line, symbol: FamilySymbol) -> FamilyInstanceCreationData
        
            Creates an object which wraps the arguments of NewFamilyInstance() for batch 
             creation.
        
        
            face: A face of a geometry object.
            position: A line on the face defining where the symbol is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
        NewFamilyInstanceCreationData(self: Application, symbol: FamilySymbol, adaptivePoints: IList[XYZ]) -> FamilyInstanceCreationData
        NewFamilyInstanceCreationData(self: Application, location: XYZ, symbol: FamilySymbol, referenceDirection: XYZ, host: Element, structuralType: StructuralType) -> FamilyInstanceCreationData
        
            Creates an object which wraps the arguments of NewFamilyInstance() for batch 
             creation.
        
        
            location: The physical location where the instance is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            referenceDirection: A vector that dictates the direction of certain family instances.
            host: The object into which the family instance is to be inserted, often known as the 
             host.
        
            structuralType: If structural then specify the type of the component.
        NewFamilyInstanceCreationData(self: Application, face: Face, location: XYZ, referenceDirection: XYZ, symbol: FamilySymbol) -> FamilyInstanceCreationData
        
            Creates an object which wraps the arguments of NewFamilyInstance() for batch 
             creation.
        
        
            face: A face of a geometry object.
            location: Point on the face where the instance is to be placed.
            referenceDirection: A vector that defines the direction of the family instance.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        """
        pass

    def NewFamilySymbolProfile(self, familySymbol):
        """
        NewFamilySymbolProfile(self: Application, familySymbol: FamilySymbol) -> FamilySymbolProfile
        
            Creates a new FamilySymbolProfile object.
        
            familySymbol: The family symbol of the Profile.
            Returns: The new FamilySymbolProfile object.
        """
        pass

    def NewFBXExportOptions(self):
        """
        NewFBXExportOptions(self: Application) -> FBXExportOptions
        
            Creates 3D-Studio Max (FBX) Export options.
        """
        pass

    def NewGBXMLImportOptions(self):
        """
        NewGBXMLImportOptions(self: Application) -> GBXMLImportOptions
        
            Creates Green-Building XML Import options.
        """
        pass

    def NewGeometryOptions(self):
        """
        NewGeometryOptions(self: Application) -> Options
        
            Creates an object to specify user preferences in parsing of geometry.
        """
        pass

    def NewImageImportOptions(self):
        """
        NewImageImportOptions(self: Application) -> ImageImportOptions
        
            Creates Image Import options.
        """
        pass

    def NewInstanceBinding(self, categorySet=None):
        """
        NewInstanceBinding(self: Application) -> InstanceBinding
        
            Creates a new empty instance binding object.
            Returns: A new instance binding object.
        NewInstanceBinding(self: Application, categorySet: CategorySet) -> InstanceBinding
        
            Creates a new instance binding object containing the categories passed as a 
             parameter.
        
        
            categorySet: A set of categories that will be added to the binding.
            Returns: A new instance binding object.
        """
        pass

    def NewIntersectionResultArray(self):
        """
        NewIntersectionResultArray(self: Application) -> IntersectionResultArray
        
            Creates a new instance of an IntersectionResult array.
        """
        pass

    def NewPlane(self, *__args):
        """
        NewPlane(self: Application, xVec: XYZ, yVec: XYZ, origin: XYZ) -> Plane
        
            Creates a new geometric plane object based on two coordinate vectors and an 
             origin.
        
        
            xVec: X vector of the plane coordinate system.
            yVec: Y vector of the plane coordinate system.
            origin: Origin of the plane coordinate system.
            Returns: A new plane object.
        NewPlane(self: Application, norm: XYZ, origin: XYZ) -> Plane
        
            Creates a new geometric plane object based on a normal vector and an origin.
        
            norm: Z vector of the plane coordinate system.
            origin: Origin of the plane coordinate system.
            Returns: A new plane object.
        NewPlane(self: Application, curveloop: CurveArray) -> Plane
        
            Creates a new geometric plane from a loop of planar curves.
        
            curveloop: The closed loop of planar curves to locate plane.
            Returns: If successful a new geometric plane will be returned. Otherwise ll.
        """
        pass

    def NewPointOnEdge(self, edgeReference, locationOnCurve):
        """
        NewPointOnEdge(self: Application, edgeReference: Reference, locationOnCurve: PointLocationOnCurve) -> PointOnEdge
        
            Create a PointOnEdge object which is used to define the placement of a 
             ReferencePoint.
        
        
            edgeReference: The reference whose edge the object will be created on.
            locationOnCurve: The location on the edge.
            Returns: If creation was successful then a new object is returned,
        otherwise an 
             exception with failure information will be thrown.
        """
        pass

    def NewPointOnEdgeEdgeIntersection(self, edgeReference1, edgeReference2):
        """
        NewPointOnEdgeEdgeIntersection(self: Application, edgeReference1: Reference, edgeReference2: Reference) -> PointOnEdgeEdgeIntersection
        
            Construct a PointOnEdgeEdgeIntersection object which is used to define the 
             placement of a ReferencePoint given two references to edge.
        
        
            edgeReference1: The first edge reference.
            edgeReference2: The second edge reference.
            Returns: A new PointOnEdgeEdgeIntersection object.
        """
        pass

    def NewPointOnEdgeFaceIntersection(self, edgeReference, faceReference, orientWithEdge):
        """
        NewPointOnEdgeFaceIntersection(self: Application, edgeReference: Reference, faceReference: Reference, orientWithEdge: bool) -> PointOnEdgeFaceIntersection
        
            Construct a PointOnEdgeFaceIntersection object which is used to define the 
             placement of a ReferencePoint given a references to edge and a reference to 
             face.
        
        
            edgeReference: The edge reference.
            faceReference: The face reference.
            Returns: A new PointOnEdgeFaceIntersection object.
        """
        pass

    def NewPointOnFace(self, faceReference, uv):
        """
        NewPointOnFace(self: Application, faceReference: Reference, uv: UV) -> PointOnFace
        
            Construct a PointOnFace object which is used to define the placement of a 
             ReferencePoint given a reference and a location on the face.
        
        
            faceReference: The reference whose face the object will be created on.
            uv: A 2-dimensional position.
            Returns: A new PointOnFace object.
        """
        pass

    def NewPointOnPlane(self, planeReference, position, xvec, offset):
        """
        NewPointOnPlane(self: Application, planeReference: Reference, position: UV, xvec: UV, offset: float) -> PointOnPlane
        
            Construct a PointOnPlane object which is used to define the placement of a 
             ReferencePoint from its property values.
        
        
            planeReference: A reference to some plane
        in the document. (Note: the reference must satisfy
        
             IsValidPlaneReference(), 
        but this is not checked until this PointOnPlane 
             object
        is assigned to a ReferencePoint.)
        
            position: Coordinates of the point's projection onto the plane;
        see the Position 
             property.
        
            xvec: The direction of the point's
        X-coordinate vector in the plane's coordinates; 
             see the XVec property. Optional;
        default value is (1, 0).
        
            offset: Signed offset from the plane; see the Offset property.
            Returns: A new PointOnPlane object with 2-dimensional Position, XVec, and Offset
        
             properties set to match the given 3-dimensional arguments.
        """
        pass

    def NewPointRelativeToPoint(self, hostPointReference):
        """
        NewPointRelativeToPoint(self: Application, hostPointReference: Reference) -> PointRelativeToPoint
        
            Create a PointRelativeToPoint object, which is used to define 
        the placement 
             of a ReferencePoint relative to a host point.
        
        
            hostPointReference: The reference of the host point.
            Returns: If creation is successful then a new PointRelativeToPoint object is returned,
        
             otherwise an exception with failure information will be thrown.
        """
        pass

    def NewProjectPosition(self, ew, ns, elevation, angle):
        """
        NewProjectPosition(self: Application, ew: float, ns: float, elevation: float, angle: float) -> ProjectPosition
        
            Creates a new project position object.
        
            ew: East to West offset in feet.
            ns: North to South offset in feet.
            elevation: Elevation above sea level in feet.
            angle: Rotation angle away from true north in the range of -PI to +PI.
        """
        pass

    def NewReferenceArray(self):
        """
        NewReferenceArray(self: Application) -> ReferenceArray
        
            Creates a new instance of a reference array.
        """
        pass

    def NewReferencePointArray(self):
        """
        NewReferencePointArray(self: Application) -> ReferencePointArray
        
            Creates an empty array that can store ReferencePoint objects.
            Returns: An empty array that can hold ReferencePoint objects.
        """
        pass

    def NewSpaceSet(self):
        """
        NewSpaceSet(self: Application) -> SpaceSet
        
            Creates a new instance of a space set.
        """
        pass

    def NewTypeBinding(self, categorySet=None):
        """
        NewTypeBinding(self: Application) -> TypeBinding
        
            Creates a new empty type binding object.
            Returns: A new type binding object.
        NewTypeBinding(self: Application, categorySet: CategorySet) -> TypeBinding
        
            Creates a new type binding object containing the categories passed as a 
             parameter.
        
        
            categorySet: A set of categories that will be added to the binding.
            Returns: A new type binding object.
        """
        pass

    def NewUV(self, *__args):
        """
        NewUV(self: Application) -> UV
        
            Creates a UV object at the origin.
        NewUV(self: Application, u: float, v: float) -> UV
        
            Creates a UV object representing coordinates in 2-space with supplied values.
        
            u: The first coordinate.
            v: The second coordinate.
        NewUV(self: Application, uv: UV) -> UV
        
            Creates a UV object by copying the supplied UV object.
        
            uv: The supplied UV object
        """
        pass

    def NewVertexIndexPair(self, iTop, iBottom):
        """
        NewVertexIndexPair(self: Application, iTop: int, iBottom: int) -> VertexIndexPair
        
            Creates a new VertexIndexPair object.
        
            iTop: The index of the vertex pair from the top profile of a blend.
            iBottom: The index of the vertex pair from the bottom profile of a blend.
            Returns: The new VertexIndexPair object.
        """
        pass

    def NewVertexIndexPairArray(self):
        """
        NewVertexIndexPairArray(self: Application) -> VertexIndexPairArray
        
            Returns an array that can hold VertexIndexPair objects.
            Returns: The new VertexIndexPairArray objects.
        """
        pass

    def NewViewSet(self):
        """
        NewViewSet(self: Application) -> ViewSet
        
            Creates a new instance of a View set.
        """
        pass

    def NewXYZ(self, *__args):
        """
        NewXYZ(self: Application) -> XYZ
        
            Creates a XYZ object at the origin.
        NewXYZ(self: Application, x: float, y: float, z: float) -> XYZ
        
            Creates a XYZ object representing coordinates in 3-space with supplied values.
        
            x: The first coordinate.
            y: The second coordinate.
            z: The third coordinate.
        NewXYZ(self: Application, xyz: XYZ) -> XYZ
        
            Creates a XYZ object by copying the supplied XYZ object.
        
            xyz: The supplied XYZ object
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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


class AreaCreationData(object):
    """
    A class which wraps the arguments of Area for batch creation
    
    AreaCreationData(proxy: object)
    AreaCreationData(areaView: ViewPlan, point: UV)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, proxy: object)
        __new__(cls: type, areaView: ViewPlan, point: UV)
        """
        pass

    TagPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specify the location of the area tag.

Get: TagPoint(self: AreaCreationData) -> UV

Set: TagPoint(self: AreaCreationData) = value
"""



class ItemFactoryBase(APIObject, IDisposable):
    """
    The ItemFactoryBase object is used to create new instances of elements within the
    Autodesk Revit document.
    """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def NewAlignment(self, view, reference1, reference2):
        """
        NewAlignment(self: ItemFactoryBase, view: View, reference1: Reference, reference2: Reference) -> Dimension
        
            Add a new locked alignment into the Autodesk Revit document.
        
            view: The view that determines the orientation of the alignment.
            reference1: The first reference.
            reference2: The second reference.
            Returns: If creation was successful the new locked alignment dimension is returned, 
        
             otherwise an exception with failure information will be thrown.
        """
        pass

    def NewDetailCurve(self, view, geometryCurve):
        """
        NewDetailCurve(self: ItemFactoryBase, view: View, geometryCurve: Curve) -> DetailCurve
        
            Creates a new detail curve element.
        
            view: The view in which the detail curve is to be visible.
            geometryCurve: The internal geometry curve for detail curve. It should be a bound curve.
            Returns: If successful a new detail curve element. Otherwise ll.
        """
        pass

    def NewDetailCurveArray(self, view, geometryCurveArray):
        """
        NewDetailCurveArray(self: ItemFactoryBase, view: View, geometryCurveArray: CurveArray) -> DetailCurveArray
        
            Creates an array of new detail curve elements.
        
            view: The view in which the detail curves are to be visible.
            geometryCurveArray: An array containing the internal geometry curves for detail lines.
         The curve 
             in array should be bound curve.
        
            Returns: If successful an array of new detail curve elements. Otherwise ll.
        """
        pass

    def NewDimension(self, view, line, references, dimensionType=None):
        """
        NewDimension(self: ItemFactoryBase, view: View, line: Line, references: ReferenceArray) -> Dimension
        
            Creates a new linear dimension object using the default dimension style.
        
            view: The view in which the dimension is to be visible.
            line: The line drawn for the dimension.
            references: An array of geometric references to which the dimension is to be bound.
            Returns: If successful a new dimension object, otherwise ll.
        NewDimension(self: ItemFactoryBase, view: View, line: Line, references: ReferenceArray, dimensionType: DimensionType) -> Dimension
        
            Creates a new linear dimension object using the specified dimension style.
        
            view: The view in which the dimension is to be visible.
            line: The line drawn for the dimension.
            references: An array of geometric references to which the dimension is to be bound.
            dimensionType: The dimension style to be used for the dimension.
            Returns: If successful a new dimension object, otherwise ll.
        """
        pass

    def NewFamilyInstance(self, *__args):
        """
        NewFamilyInstance(self: ItemFactoryBase, location: XYZ, symbol: FamilySymbol, structuralType: StructuralType) -> FamilyInstance
        
            Inserts a new instance of a family into the document, using a location and a
        
             type/symbol.
        
        
            location: The physical location where the instance is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            structuralType: If structural then specify the type of the component.
            Returns: A valid instance of the given family if the creation is successful. An 
             exception will be thrown otherwise.
        
        NewFamilyInstance(self: ItemFactoryBase, face: Face, location: XYZ, referenceDirection: XYZ, symbol: FamilySymbol) -> FamilyInstance
        
            Inserts a new instance of a family onto a face of an existing element,
         using 
             a location, reference direction, and a type/symbol.
        
        
            face: A face of a geometry object.
            location: Point on the face where the instance is to be placed.
            referenceDirection: A vector that defines the direction of the family instance.
        Note that this 
             direction defines the rotation of the instance on the face, and thus cannot be 
             parallel
        to the face normal.
        
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        Note that this symbol must represent a family whose 
             Autodesk.Revit.DB.Family.FamilyPlacementType 
        is WorkPlaneBased.
        
            Returns: An instance of the new object if creation was successful, otherwise ll.
        NewFamilyInstance(self: ItemFactoryBase, location: XYZ, symbol: FamilySymbol, referenceDirection: XYZ, host: Element, structuralType: StructuralType) -> FamilyInstance
        
            Inserts a new instance of a family into the document,
        using a location, 
             type/symbol, the host element and a reference direction.
        
        
            location: The physical location where the instance is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            referenceDirection: A vector that dictates the direction of certain family instances.
            host: A host object into which the instance will be embedded
            structuralType: If structural then specify the type of the component.
            Returns: If creation was successful then an instance to the new object is returned, 
             otherwise ll.
        
        NewFamilyInstance(self: ItemFactoryBase, location: XYZ, symbol: FamilySymbol, host: Element, structuralType: StructuralType) -> FamilyInstance
        
            Inserts a new instance of a family into the document,
        using a location, 
             type/symbol, and the host element.
        
        
            location: The physical location where the instance is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            host: The object into which the FamilyInstance is to be inserted, often known as the 
             host.
        
            structuralType: If structural then specify the type of the component.
            Returns: If creation was successful then an instance to the new object is returned, 
             otherwise ll.
        
        NewFamilyInstance(self: ItemFactoryBase, face: Face, position: Line, symbol: FamilySymbol) -> FamilyInstance
        
            Inserts a new instance of a family onto a face of an existing element,
         using 
             a line on that face for its position, and a type/symbol.
        
        
            face: A face of a geometry object.
            position: A line on the face defining where the symbol is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        Note that this symbol must represent a family whose 
             Autodesk.Revit.DB.Family.FamilyPlacementType 
        is WorkPlaneBased or CurveBased.
        
            Returns: An instance of the new object if creation was successful, otherwise ll.
        NewFamilyInstance(self: ItemFactoryBase, origin: XYZ, symbol: FamilySymbol, specView: View) -> FamilyInstance
        
            Add a new family instance into the Autodesk Revit document, 
        using an origin 
             and a view where the instance should be placed.
        
        
            origin: The origin of family instance. If created on a Autodesk.Revit.DB.ViewPlan, 
        
             the origin will be projected onto the Autodesk.Revit.DB.ViewPlan.
        
            symbol: A family symbol object that represents the type of the instance that is to be 
             inserted.
        
            specView: The 2D view in which to place the family instance.
            Returns: If creation was successful then an instance to the new object is returned.
        NewFamilyInstance(self: ItemFactoryBase, line: Line, symbol: FamilySymbol, specView: View) -> FamilyInstance
        
            Add a line based detail family instance into the Autodesk Revit document, 
        
             using an line and a view where the instance should be placed.
        
        
            line: The line location of family instance. The line must in the plane of the view.
            symbol: A family symbol object that represents the type of the instance that is to be 
             inserted.
        
            specView: A 2D view in which to display the family instance.
        NewFamilyInstance(self: ItemFactoryBase, reference: Reference, location: XYZ, referenceDirection: XYZ, symbol: FamilySymbol) -> FamilyInstance
        
            Inserts a new instance of a family onto a face referenced by the input 
             Reference instance,
         using a location, reference direction, and a type/symbol.
        
        
            reference: A reference to a face.
            location: Point on the face where the instance is to be placed.
            referenceDirection: A vector that defines the direction of the family instance.
        Note that this 
             direction defines the rotation of the instance on the face, and thus cannot be 
             parallel
        to the face normal.
        
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        Note that this symbol must represent a family whose 
             Autodesk.Revit.DB.Family.FamilyPlacementType 
        is WorkPlaneBased.
        
            Returns: An instance of the new object if creation was successful, otherwise ll.
        NewFamilyInstance(self: ItemFactoryBase, reference: Reference, position: Line, symbol: FamilySymbol) -> FamilyInstance
        
            Inserts a new instance of a family onto a face referenced by the input 
             Reference instance,
         using a line on that face for its position, and a 
             type/symbol.
        
        
            reference: A reference to a face.
            position: A line on the face defining where the symbol is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted. 
        Note that this symbol must represent a family whose 
             Autodesk.Revit.DB.Family.FamilyPlacementType 
        is WorkPlaneBased or CurveBased.
        
            Returns: An instance of the new object if creation was successful, otherwise ll.
        """
        pass

    def NewFamilyInstances2(self, dataList):
        """ NewFamilyInstances2(self: ItemFactoryBase, dataList: List[FamilyInstanceCreationData]) -> ICollection[ElementId] """
        pass

    def NewGroup(self, elementIds):
        """ NewGroup(self: ItemFactoryBase, elementIds: ICollection[ElementId]) -> Group """
        pass

    def NewModelCurve(self, geometryCurve, sketchPlane):
        """
        NewModelCurve(self: ItemFactoryBase, geometryCurve: Curve, sketchPlane: SketchPlane) -> ModelCurve
        
            Creates a new model line element.
        
            geometryCurve: The internal geometry curve for model line.
            sketchPlane: The sketch plane this new model line resides in.
            Returns: If successful a new model line element. Otherwise ll.
        """
        pass

    def NewModelCurveArray(self, geometryCurveArray, sketchPlane):
        """
        NewModelCurveArray(self: ItemFactoryBase, geometryCurveArray: CurveArray, sketchPlane: SketchPlane) -> ModelCurveArray
        
            Creates an array of new model line elements.
        
            geometryCurveArray: An array containing the internal geometry curves for model lines.
            Returns: If successful an array of new model line elements. Otherwise ll.
        """
        pass

    def NewReferencePlane(self, bubbleEnd, freeEnd, cutVec, pView):
        """
        NewReferencePlane(self: ItemFactoryBase, bubbleEnd: XYZ, freeEnd: XYZ, cutVec: XYZ, pView: View) -> ReferencePlane
        
            Creates a new instance of ReferencePlane.
        
            bubbleEnd: The bubble end applied to reference plane.
            freeEnd: The free end applied to reference plane.
            cutVec: The cut vector apply to reference plane, should perpendicular 
        to the vector  
             (bubbleEnd-freeEnd).
        
            pView: The specific view apply to the Reference plane.
            Returns: The newly created reference plane.
        """
        pass

    def NewReferencePlane2(self, bubbleEnd, freeEnd, thirdPnt, pView):
        """
        NewReferencePlane2(self: ItemFactoryBase, bubbleEnd: XYZ, freeEnd: XYZ, thirdPnt: XYZ, pView: View) -> ReferencePlane
        
            Creates a new instance of ReferencePlane.
        
            bubbleEnd: The bubble end applied to reference plane.
            freeEnd: The free end applied to reference plane.
            thirdPnt: A third point needed to define the reference plane.
            pView: The specific view apply to the Reference plane.
            Returns: The newly created reference plane.
        """
        pass

    def PlaceGroup(self, location, groupType):
        """
        PlaceGroup(self: ItemFactoryBase, location: XYZ, groupType: GroupType) -> Group
        
            Place an instance of a Model Group into the Autodesk Revit document, using a 
             location
        and a group type.
        
        
            location: The physical location where the group is to be placed.
            groupType: A GroupType object that represents the type of group that is to be placed.
            Returns: If creation was successful then an instance to the new group is returned, 
             otherwise ll.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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


class Document(ItemFactoryBase, IDisposable):
    """
    The Document Creation object is used to create new instances of elements within the
    Autodesk Revit project.
    """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def NewArea(self, areaView, point):
        """
        NewArea(self: Document, areaView: ViewPlan, point: UV) -> Area
        
            Creates a new area
        
            areaView: The view of area element.
            point: The point which lies in the enclosed region of AreaBoundaryLines to put the new 
             created Area
        """
        pass

    def NewAreaBoundaryConditions(self, *__args):
        """
        NewAreaBoundaryConditions(self: Document, reference: Reference, X_Translation: TranslationRotationValue, X_TranslationSpringModulus: float, Y_Translation: TranslationRotationValue, Y_TranslationSpringModulus: float, Z_Translation: TranslationRotationValue, Z_TranslationSpringModulus: float) -> BoundaryConditions
        
            Creates a new Area BoundaryConditions element on a reference.
        
            reference: The Geometry reference obtained from a Wall, Slab or 
        Slab Foundation.
            X_Translation: A value indicating the X axis translation option.
            X_TranslationSpringModulus: Translation Spring Modulus for X axis. Ignored if X_Translation is not "Spring".
            Y_Translation: A value indicating the Y axis translation option.
            Y_TranslationSpringModulus: Translation Spring Modulus for Y axis. Ignored if Y_Translation is not "Spring".
            Z_Translation: A value indicating the Z axis translation option.
            Z_TranslationSpringModulus: Translation Spring Modulus for Z axis. Ignored if Z_Translation is not "Spring".
            Returns: If successful, NewAreaBoundaryConditions returns an object for the newly 
             created BoundaryConditions
        with the BoundaryType = 2 - "Area". ll is returned 
             if the operation fails.
        
        NewAreaBoundaryConditions(self: Document, hostElement: Element, X_Translation: TranslationRotationValue, X_TranslationSpringModulus: float, Y_Translation: TranslationRotationValue, Y_TranslationSpringModulus: float, Z_Translation: TranslationRotationValue, Z_TranslationSpringModulus: float) -> BoundaryConditions
        
            Creates a new Area BoundaryConditions element on a host element.
        
            hostElement: A Wall, Slab or Slab Foundation to host the boundary conditions.
            X_Translation: A value indicating the X axis translation option.
            X_TranslationSpringModulus: Translation Spring Modulus for X axis. Ignored if X_Translation is not "Spring".
            Y_Translation: A value indicating the Y axis translation option.
            Y_TranslationSpringModulus: Translation Spring Modulus for Y axis. Ignored if Y_Translation is not "Spring".
            Z_Translation: A value indicating the Z axis translation option.
            Z_TranslationSpringModulus: Translation Spring Modulus for Z axis. Ignored if Z_Translation is not "Spring".
            Returns: If successful, NewAreaBoundaryConditions returns an object for the newly 
             created BoundaryConditions
        with the BoundaryType = 2 - "Area". ll is returned 
             if the operation fails.
        """
        pass

    def NewAreaBoundaryLine(self, sketchPlane, geometryCurve, areaView):
        """
        NewAreaBoundaryLine(self: Document, sketchPlane: SketchPlane, geometryCurve: Curve, areaView: ViewPlan) -> ModelCurve
        
            Creates a new boundary line as an Area border.
        
            sketchPlane: The sketch plane.
            geometryCurve: The geometry curve on which the boundary line are
            areaView: The View for the new Area
        """
        pass

    def NewAreas(self, dataList):
        """ NewAreas(self: Document, dataList: List[AreaCreationData]) -> ElementSet """
        pass

    def NewAreaTag(self, areaView, room, point):
        """
        NewAreaTag(self: Document, areaView: ViewPlan, room: Area, point: UV) -> AreaTag
        
            Creates a new area tag.
        
            areaView: The area view
            room: The area to tag
            point: The position of the area tag
        """
        pass

    def NewCrossFitting(self, connector1, connector2, connector3, connector4):
        """
        NewCrossFitting(self: Document, connector1: Connector, connector2: Connector, connector3: Connector, connector4: Connector) -> FamilyInstance
        
            Add a new family instance of a cross fitting into the Autodesk Revit document,
        
             using four connectors.
        
        
            connector1: The first connector to be connected to the cross.
            connector2: The second connector to be connected to the cross.
            connector3: The third connector to be connected to the cross.
            connector4: The fourth connector to be connected to the cross.
            Returns: If creation was successful then an family instance to the new object is 
             returned,
        and the transition fitting will be added at the connectors' end if 
             necessary, 
        otherwise an exception with failure information will be thrown.
        """
        pass

    def NewCurtainSystem(self, faces, curtainSystemType):
        """
        NewCurtainSystem(self: Document, faces: FaceArray, curtainSystemType: CurtainSystemType) -> CurtainSystem
        
            Creates a new CurtainSystem element from a set of faces.
        
            faces: The faces new CurtainSystem will be created on.
            curtainSystemType: The Type of CurtainSystem to be created.
            Returns: The CurtainSystem created will be returned when the operation succeeds.
        """
        pass

    def NewCurtainSystem2(self, faces, curtainSystemType):
        """
        NewCurtainSystem2(self: Document, faces: ReferenceArray, curtainSystemType: CurtainSystemType) -> ICollection[ElementId]
        
            Creates a new CurtainSystem element from a set of face references.
        
            faces: The faces new CurtainSystem will be created on.
            curtainSystemType: The Type of CurtainSystem to be created.
            Returns: A set of ElementIds of CurtainSystems will be returned when the operation 
             succeeds.
        """
        pass

    def NewDuct(self, *__args):
        """
        NewDuct(self: Document, point1: XYZ, point2: XYZ, ductType: DuctType) -> Duct
        
            Adds a new duct into the document, 
        using two points and duct type.
        
            point1: The first point of the duct.
            point2: The second point of the duct.
            ductType: The type of the duct.
            Returns: If creation was successful then a new duct is returned, 
        otherwise an 
             exception with failure information will be thrown.
        
        NewDuct(self: Document, point: XYZ, connector: Connector, ductType: DuctType) -> Duct
        
            Adds a new duct into the document, 
        using a point, connector and duct type.
        
            point: The first point of the duct.
            connector: The connector to be connected to the duct.
            ductType: The type of the duct.
            Returns: If creation was successful then a new duct is returned,  
        otherwise an 
             exception with failure information will be thrown.
        
        NewDuct(self: Document, connector1: Connector, connector2: Connector, ductType: DuctType) -> Duct
        
            Adds a new duct into the document, 
        using two connectors and duct type.
        
            connector1: The first connector to be connected to the duct.
            connector2: The second connector to be connected to the duct.
            ductType: The type of the duct.
            Returns: If creation was successful then a new duct is returned, 
        otherwise an 
             exception with failure information will be thrown.
        """
        pass

    def NewElbowFitting(self, connector1, connector2):
        """
        NewElbowFitting(self: Document, connector1: Connector, connector2: Connector) -> FamilyInstance
        
            Add a new family instance of an elbow fitting into the Autodesk Revit document,
             
        using two connectors.
        
        
            connector1: The first connector to be connected to the elbow.
            connector2: The second connector to be connected to the elbow.
            Returns: If creation was successful then an family instance to the new object is 
             returned,
        otherwise an exception with failure information will be thrown.
        """
        pass

    def NewElectricalSystem(self, *__args):
        """
        NewElectricalSystem(self: Document, connector: Connector, elecSysType: ElectricalSystemType) -> ElectricalSystem
        
            Creates a new MEP Electrical System element from an unused Connector.
        
            connector: The Connector to create this Electrical System.
            elecSysType: The System Type of electrical system.
            Returns: If successful a new MEP Electrical System element within the project, otherwise 
             ll.
        
        NewElectricalSystem(self: Document, electComponents: ICollection[ElementId], elecSysType: ElectricalSystemType) -> ElectricalSystem
        """
        pass

    def NewExtrusionRoof(self, profile, refPlane, level, roofType, extrusionStart, extrusionEnd):
        """
        NewExtrusionRoof(self: Document, profile: CurveArray, refPlane: ReferencePlane, level: Level, roofType: RoofType, extrusionStart: float, extrusionEnd: float) -> ExtrusionRoof
        
            Creates a new Extrusion Roof.
        
            profile: The profile of the extrusion roof.
            refPlane: The work plane for the extrusion roof.
            level: The level of the extrusion roof.
            roofType: Type of the extrusion roof.
            extrusionStart: Start the extrusion.
            extrusionEnd: End the extrusion.
        """
        pass

    def NewFamilyInstance(self, *__args):
        """
        NewFamilyInstance(self: Document, location: XYZ, symbol: FamilySymbol, host: Element, level: Level, structuralType: StructuralType) -> FamilyInstance
        
            Inserts a new instance of a family into the document,
        using a location, 
             type/symbol, the host element and a base level.
        
        
            location: The physical location where the instance is to be placed on the specified level.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            host: A host object into which the instance will be embedded
            level: A Level object that is used as the base level for the object.
            structuralType: If structural then specify the type of the component.
            Returns: If creation was successful then an instance to the new object is returned, 
             otherwise ll.
        
        NewFamilyInstance(self: Document, location: XYZ, symbol: FamilySymbol, level: Level, structuralType: StructuralType) -> FamilyInstance
        
            Inserts a new instance of a family into the document, using a location,
        
             type/symbol and a base level.
        
        
            location: The physical location where the instance is to be placed.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            level: A Level object that is used as the base level for the object.
            structuralType: If structural then specify the type of the component.
            Returns: If creation was successful then an instance to the new object is returned, 
             otherwise ll.
        
        NewFamilyInstance(self: Document, curve: Curve, symbol: FamilySymbol, level: Level, structuralType: StructuralType) -> FamilyInstance
        
            Inserts a new instance of a family into the document, 
        using a curve, 
             type/symbol and reference level.
        
        
            curve: The curve where the instance is based.
            symbol: A FamilySymbol object that represents the type of the instance that is to be 
             inserted.
        
            level: A Level object that is used as the base level for the object.
            structuralType: If structural then specify the type of the component.
            Returns: If creation was successful then an instance to the new object is returned, 
             otherwise ll.
        """
        pass

    def NewFascia(self, FasciaType, *__args):
        """
        NewFascia(self: Document, FasciaType: FasciaType, references: ReferenceArray) -> Fascia
        
            Creates a fascia along a reference array.
        
            FasciaType: The type of the fascia to create
            references: An array of planar lines and arcs that represents the place where you
        want to 
             place the fascia.
        
            Returns: If successful a new fascia object within the project, otherwise ll.
        NewFascia(self: Document, FasciaType: FasciaType, reference: Reference) -> Fascia
        
            Creates a fascia along a reference.
        
            FasciaType: The type of the fascia to create
            reference: A planar line or arc that represents the place where you
        want to place the 
             fascia.
        
            Returns: If successful a new fascia object within the project, otherwise ll.
        """
        pass

    def NewFlexDuct(self, *__args):
        """
        NewFlexDuct(self: Document, points: IList[XYZ], ductType: FlexDuctType) -> FlexDuct
        NewFlexDuct(self: Document, connector: Connector, points: IList[XYZ], ductType: FlexDuctType) -> FlexDuct
        NewFlexDuct(self: Document, connector1: Connector, connector2: Connector, ductType: FlexDuctType) -> FlexDuct
        
            Adds a new flexible duct into the document, 
        using two connector, and duct 
             type.
        
        
            connector1: The first connector to be connected to the duct.
            connector2: The second connector to be connected to the duct.
            ductType: The type of the flexible duct.
            Returns: If creation was successful then a new flexible duct is returned, 
        otherwise an 
             exception with failure information will be thrown.
        """
        pass

    def NewFlexPipe(self, *__args):
        """
        NewFlexPipe(self: Document, points: IList[XYZ], pipeType: FlexPipeType) -> FlexPipe
        NewFlexPipe(self: Document, connector: Connector, points: IList[XYZ], pipeType: FlexPipeType) -> FlexPipe
        NewFlexPipe(self: Document, connector1: Connector, connector2: Connector, pipeType: FlexPipeType) -> FlexPipe
        
            Adds a new flexible pipe into the document, 
        using two connector, and flexible 
             pipe type.
        
        
            connector1: The first connector to be connected to the pipe.
            connector2: The second connector to be connected to the pipe.
            pipeType: The type of the flexible pipe.
            Returns: If creation was successful then a new flexible pipe is returned, 
        otherwise an 
             exception with failure information will be thrown.
        """
        pass

    def NewFloor(self, profile, *__args):
        """
        NewFloor(self: Document, profile: CurveArray, structural: bool) -> Floor
        
            Creates a floor within the project with the given horizontal profile using the 
             default floor style.
        
        
            profile: An array of planar lines and arcs that represent the horizontal profile of the 
             floor.
        
            structural: If set, specifies that the floor is structural in nature.
            Returns: If successful a new floor object within the project, otherwise ll.
        NewFloor(self: Document, profile: CurveArray, floorType: FloorType, level: Level, structural: bool) -> Floor
        
            Creates a floor within the project with the given horizontal profile and floor 
             style on the specified level.
        
        
            profile: An array of planar lines and arcs that represent the horizontal profile of the 
             floor.
        
            floorType: A floor type to be used by the new floor instead of the default type.
            level: The level on which the floor is to be placed.
            structural: If set, specifies that the floor is structural in nature.
            Returns: if successful, a new floor object within the project, otherwise ll.
        NewFloor(self: Document, profile: CurveArray, floorType: FloorType, level: Level, structural: bool, normal: XYZ) -> Floor
        
            Creates a floor within the project with the given horizontal profile and floor 
             style on the specified level with the specified normal vector.
        
        
            profile: An array of planar lines and arcs that represent the horizontal profile of the 
             floor.
        
            floorType: A floor type to be used by the new floor instead of the default type.
            level: The level on which the floor is to be placed.
            structural: If set, specifies that the floor is structural in nature.
            normal: A vector that must be perpendicular to the profile which dictates which side of 
             the floor is considered
        to be upper and down.
        
            Returns: if successful, a new floor object within the project, otherwise ll.
        """
        pass

    def NewFootPrintRoof(self, footPrint, level, roofType, footPrintToModelCurvesMapping):
        """
        NewFootPrintRoof(self: Document, footPrint: CurveArray, level: Level, roofType: RoofType) -> (FootPrintRoof, ModelCurveArray)
        
            Creates a new FootPrintRoof element.
        
            footPrint: The footprint of the FootPrintRoof.
            level: The level of the FootPrintRoof.
            roofType: Type of the FootPrintRoof.
        """
        pass

    def NewFoundationSlab(self, profile, floorType, level, structural, normal):
        """
        NewFoundationSlab(self: Document, profile: CurveArray, floorType: FloorType, level: Level, structural: bool, normal: XYZ) -> Floor
        
            Creates a foundation slab within the project with the given horizontal profile 
             and floor style on the specified level.
        
        
            profile: An array of planar lines and arcs that represent the horizontal profile of the 
             floor.
        
            floorType: A floor type to be used by the new floor instead of the default type.
            level: The level on which the floor is to be placed.
            structural: If set, specifies that the floor is structural in nature.
            normal: A vector that must be perpendicular to the profile which dictates which side of 
             the floor is considered
        to be upper and down.
        
            Returns: if successful, a new foundation slab object within the project, otherwise ll.
        """
        pass

    def NewFoundationWall(self, wallFoundationType, wall):
        """
        NewFoundationWall(self: Document, wallFoundationType: WallFoundationType, wall: Wall) -> WallFoundation
        
            Creates a new wall foundation object.
        
            wallFoundationType: The WallFoundation type.
            wall: The Wall to append a WallFoundation.
        """
        pass

    def NewGutter(self, GutterType, *__args):
        """
        NewGutter(self: Document, GutterType: GutterType, references: ReferenceArray) -> Gutter
        
            Creates a gutter along a reference array.
        
            GutterType: The type of the gutter to create
            references: An array of planar lines and arcs that represents the place where you
        want to 
             place the gutter.
        
            Returns: If successful a new gutter object within the project, otherwise ll.
        NewGutter(self: Document, GutterType: GutterType, reference: Reference) -> Gutter
        
            Creates a gutter along a reference.
        
            GutterType: The type of the gutter to create
            reference: A planar line or arc that represents the place where you
        want to place the 
             gutter.
        
            Returns: If successful a new gutter object within the project, otherwise ll.
        """
        pass

    def NewLineBoundaryConditions(self, *__args):
        """
        NewLineBoundaryConditions(self: Document, reference: Reference, X_Translation: TranslationRotationValue, X_TranslationSpringModulus: float, Y_Translation: TranslationRotationValue, Y_TranslationSpringModulus: float, Z_Translation: TranslationRotationValue, Z_TranslationSpringModulus: float, X_Rotation: TranslationRotationValue, X_RotationSpringModulus: float) -> BoundaryConditions
        
            Creates a new Line BoundaryConditions element on a reference.
        
            reference: The Geometry reference to a Beam's, Wall's, Wall Foundation's, Slab's or 
        Slab 
             Foundation's analytical line.
        
            X_Translation: A value indicating the X axis translation option.
            X_TranslationSpringModulus: Translation Spring Modulus for X axis. Ignored if X_Translation is not "Spring".
            Y_Translation: A value indicating the Y axis translation option.
            Y_TranslationSpringModulus: Translation Spring Modulus for Y axis. Ignored if Y_Translation is not "Spring".
            Z_Translation: A value indicating the Z axis translation option.
            Z_TranslationSpringModulus: Translation Spring Modulus for Z axis. Ignored if Z_Translation is not "Spring".
            X_Rotation: A value indicating the option for rotation about the X axis.
            X_RotationSpringModulus: Rotation Spring Modulus for X axis. Ignored if X_Rotation is not "Spring"
            Returns: If successful, NewLineBoundaryConditions returns an object for the newly 
             created BoundaryConditions
        with the BoundaryType = 1 - "Line". ll is returned 
             if the operation fails.
        
        NewLineBoundaryConditions(self: Document, hostElement: Element, X_Translation: TranslationRotationValue, X_TranslationSpringModulus: float, Y_Translation: TranslationRotationValue, Y_TranslationSpringModulus: float, Z_Translation: TranslationRotationValue, Z_TranslationSpringModulus: float, X_Rotation: TranslationRotationValue, X_RotationSpringModulus: float) -> BoundaryConditions
        
            Creates a new Line BoundaryConditions element on a host element.
        
            hostElement: A Beam.
            X_Translation: A value indicating the X axis translation option.
            X_TranslationSpringModulus: Translation Spring Modulus for X axis. Ignored if X_Translation is not "Spring".
            Y_Translation: A value indicating the Y axis translation option.
            Y_TranslationSpringModulus: Translation Spring Modulus for Y axis. Ignored if Y_Translation is not "Spring".
            Z_Translation: A value indicating the Z axis translation option.
            Z_TranslationSpringModulus: Translation Spring Modulus for Z axis. Ignored if Z_Translation is not "Spring".
            X_Rotation: A value indicating the option for rotation about the X axis.
            X_RotationSpringModulus: Rotation Spring Modulus for X axis. Ignored if X_Rotation is not "Spring"
            Returns: If successful, NewLineBoundaryConditions returns an object for the newly 
             created BoundaryConditions
        with the BoundaryType = 1 - "Line". ll is returned 
             if the operation fails.
        """
        pass

    def NewMechanicalSystem(self, baseEquipmentConnector, connectors, ductSystemType):
        """
        NewMechanicalSystem(self: Document, baseEquipmentConnector: Connector, connectors: ConnectorSet, ductSystemType: DuctSystemType) -> MechanicalSystem
        
            Creates a new MEP mechanical system element.
        
            baseEquipmentConnector: One connector within base equipment which is used to connect with the system. 
        
             The base equipment is optional for the system, so this argument may be ll.
        The 
             baseEquipmentConnector should not be included in the connectors.
        
            connectors: Connectors that will connect to the system.
        The owner elements of these 
             connectors will be added into system as its elements.
        
            ductSystemType: The system type.
            Returns: If creation was successful then an instance of mechanical system is returned, 
        
             otherwise an exception with information will be thrown.
        """
        pass

    def NewOpening(self, *__args):
        """
        NewOpening(self: Document, bottomLevel: Level, topLevel: Level, profile: CurveArray) -> Opening
        
            Creates a new shaft opening between a set of levels.
        
            bottomLevel: bottom level
            topLevel: top level
            profile: profile of the opening.
            Returns: If successful, an Opening object is returned.
        NewOpening(self: Document, famInstElement: Element, profile: CurveArray, iFace: eRefFace) -> Opening
        
            Creates a new opening in a beam, brace and column.
        
            famInstElement: host element of the opening, can be a beam, brace and column.
            profile: profile of the opening.
            iFace: face on which opening is based on.
            Returns: If successful, an Opening object is returned.
        NewOpening(self: Document, hostElement: Element, profile: CurveArray, bPerpendicularFace: bool) -> Opening
        
            Creates a new opening in a roof, floor and ceiling.
        
            hostElement: Host element of the opening. Can be a roof, floor, or ceiling.
            profile: Profile of the opening.
            bPerpendicularFace: True if the profile is cut perpendicular to the intersecting face of the host. 
             False if the profile is cut vertically.
        
            Returns: If successful, an Opening object is returned.
        NewOpening(self: Document, wall: Wall, pntStart: XYZ, pntEnd: XYZ) -> Opening
        
            Creates a rectangular opening on a wall.
        
            wall: Host element of the opening.
            pntStart: One corner of the rectangle.
            pntEnd: The opposite corner of the rectangle.
            Returns: If successful, an Opening object is returned.
        """
        pass

    def NewPipingSystem(self, baseEquipmentConnector, connectors, pipingSystemType):
        """
        NewPipingSystem(self: Document, baseEquipmentConnector: Connector, connectors: ConnectorSet, pipingSystemType: PipeSystemType) -> PipingSystem
        
            Creates a new MEP piping system element.
        
            baseEquipmentConnector: One connector within base equipment which is used to connect with the system. 
        
             The base equipment is optional for the system, so this argument may be ll.
        The 
             baseEquipmentConnector should not be included in the connectors.
        
            connectors: Connectors that will connect to the system.
        The owner elements of these 
             connectors will be added into system as its elements.
        
            pipingSystemType: The System type.
            Returns: If creation was successful then an instance of piping system is returned, 
        
             otherwise an exception with information will be thrown.
        """
        pass

    def NewPointBoundaryConditions(self, reference, X_Translation, X_TranslationSpringModulus, Y_Translation, Y_TranslationSpringModulus, Z_Translation, Z_TranslationSpringModulus, X_Rotation, X_RotationSpringModulus, Y_Rotation, Y_RotationSpringModulus, Z_Rotation, Z_RotationSpringModulus):
        """
        NewPointBoundaryConditions(self: Document, reference: Reference, X_Translation: TranslationRotationValue, X_TranslationSpringModulus: float, Y_Translation: TranslationRotationValue, Y_TranslationSpringModulus: float, Z_Translation: TranslationRotationValue, Z_TranslationSpringModulus: float, X_Rotation: TranslationRotationValue, X_RotationSpringModulus: float, Y_Rotation: TranslationRotationValue, Y_RotationSpringModulus: float, Z_Rotation: TranslationRotationValue, Z_RotationSpringModulus: float) -> BoundaryConditions
        
            Creates a new Point BoundaryConditions Element.
        
            reference: A Geometry reference to a Beam's, Brace's or Column's analytical line end.
            X_Translation: A value indicating the X axis translation option.
            X_TranslationSpringModulus: Translation Spring Modulus for X axis. Ignored if X_Translation is not "Spring".
            Y_Translation: A value indicating the Y axis translation option.
            Y_TranslationSpringModulus: Translation Spring Modulus for Y axis. Ignored if Y_Translation is not "Spring".
            Z_Translation: A value indicating the Z axis translation option.
            Z_TranslationSpringModulus: Translation Spring Modulus for Z axis. Ignored if Z_Translation is not "Spring".
            X_Rotation: A value indicating the option for rotation about the X axis.
            X_RotationSpringModulus: Rotation Spring Modulus for X axis. Ignored if X_Rotation is not "Spring".
            Y_Rotation: A value indicating the option for rotation about the Y axis.
            Y_RotationSpringModulus: Rotation Spring Modulus for Y axis. Ignored if Y_Rotation is not "Spring".
            Z_Rotation: A value indicating the option for rotation about the Z axis.
            Z_RotationSpringModulus: Rotation Spring Modulus for Z axis. Ignored if Y_Rotation is not "Spring".
            Returns: If successful, NewPointBoundaryConditions returns an object for the newly 
             created BoundaryConditions
        with the BoundaryType = 0 - "Point". ll is returned 
             if the operation fails.
        """
        pass

    def NewRoom(self, *__args):
        """
        NewRoom(self: Document, level: Level, point: UV) -> Room
        
            Creates a new room on a level at a specified point.
        
            level: The level on which the room is to exist.
            point: A 2D point that dictates the location of the room on that specified level.
            Returns: If successful the new room will be returned, otherwise ll.
        NewRoom(self: Document, phase: Phase) -> Room
        
            Creates a new unplaced room and with an assigned phase.
        
            phase: The phase in which the room is to exist.
            Returns: If successful the new room , otherwise ll.
        NewRoom(self: Document, room: Room, circuit: PlanCircuit) -> Room
        
            Creates a new room within the confines of a plan circuit, or places an unplaced 
             room within the confines of the plan circuit.
        
        
            room: The room which you want to locate in the circuit.  Pass ll to create a new room.
            circuit: The circuit in which you want to locate a room.
            Returns: If successful the room is returned, otherwise ll.
        """
        pass

    def NewRoomBoundaryLines(self, sketchPlane, curves, view):
        """
        NewRoomBoundaryLines(self: Document, sketchPlane: SketchPlane, curves: CurveArray, view: View) -> ModelCurveArray
        
            Creates a new boundary line as an Room border.
        
            sketchPlane: The sketch plan
            curves: The geometry curves on which the boundary lines are
            view: The View for the new Room
        """
        pass

    def NewRooms2(self, *__args):
        """
        NewRooms2(self: Document, level: Level) -> ICollection[ElementId]
        
            Creates new rooms in each plan circuit found in the given level in the last 
             phase.
        
        
            level: The level from which the circuits are found.
            Returns: If successful, a set of ElementIds which contains the rooms created should be 
             returned, otherwise ll.
        
        NewRooms2(self: Document, level: Level, phase: Phase) -> ICollection[ElementId]
        
            Creates new rooms in each plan circuit found in the given level in the given 
             phase.
        
        
            level: The level from which the circuits are found.
            phase: The phase on which the room is to exist.
            Returns: If successful, a set of ElementIds which contains the rooms should be returned, 
             otherwise the exception will be thrown.
        
        NewRooms2(self: Document, phase: Phase, count: int) -> ICollection[ElementId]
        
            Creates new unplaced rooms in the given phase.
        
            phase: The phase on which the rooms are to exist.
            count: The number of the rooms to be created.
            Returns: If successful, a set of ElementIds which contains the rooms should be returned, 
             otherwise the exception will be thrown.
        """
        pass

    def NewRoomTag(self, roomId, point, viewId):
        """
        NewRoomTag(self: Document, roomId: LinkElementId, point: UV, viewId: ElementId) -> RoomTag
        
            Creates a new RoomTag referencing a room in the host model or in a Revit link.
        
            roomId: The HostOrLinkElementId of the Room.
            point: A 2D point that defines the tag location on the level of the room.
            viewId: The id of the view where the tag will be shown. If ll and the room in not in a 
             Revit link, the view of the room will be used.
        
            Returns: If successful a RoomTag object will be returned, otherwise ll.
        """
        pass

    def NewSlab(self, profile, level, slopedArrow, slope, isStructural):
        """
        NewSlab(self: Document, profile: CurveArray, level: Level, slopedArrow: Line, slope: float, isStructural: bool) -> Floor
        
            Creates a slab within the project with the given horizontal profile using the 
             default floor style.
        
        
            profile: An array of planar lines and arcs that represent the horizontal profile of the 
             slab.
        
            level: The level on which the slab is to be placed.
            slopedArrow: A line use to control the sloped angle of the slab. It should be in the same 
             face with profile.
        
            slope: The slope.
            isStructural: If set, specifies that the floor is structural in nature.
            Returns: If successful a new floor object within the project, otherwise ll.
        """
        pass

    def NewSlabEdge(self, SlabEdgeType, *__args):
        """
        NewSlabEdge(self: Document, SlabEdgeType: SlabEdgeType, references: ReferenceArray) -> SlabEdge
        
            Creates a slab edge along a reference array.
        
            SlabEdgeType: The type of the slab edge to create
            references: An array of planar lines and arcs that represents the place where you
        want to 
             place the slab edge.
        
            Returns: If successful a new slab edge object within the project, otherwise ll.
        NewSlabEdge(self: Document, SlabEdgeType: SlabEdgeType, reference: Reference) -> SlabEdge
        
            Creates a slab edge along a reference.
        
            SlabEdgeType: The type of the slab edge to create
            reference: A planar line or arc that represents the place where you
        want to place the 
             slab edge.
        
            Returns: If successful a new slab edge object within the project, otherwise ll.
        """
        pass

    def NewSpace(self, *__args):
        """
        NewSpace(self: Document, phase: Phase) -> Space
        
            Creates a new unplaced space on a given phase.
        
            phase: The phase in which the space is to exist.
            Returns: If successful the new space should be returned, otherwise ll.
        NewSpace(self: Document, level: Level, point: UV) -> Space
        
            Creates a new space element on the given level at the given location.
        
            level: The level on which the space is to exist.
            point: A 2D point that dictates the location on that specified level.
            Returns: If successful the new space element is returned, otherwise ll.
        NewSpace(self: Document, level: Level, phase: Phase, point: UV) -> Space
        
            Creates a new space element on the given level, at the given location, and 
             assigned to the given phase.
        
        
            level: The level on which the room is to exist.
            phase: The phase in which the room is to exist.
            point: A 2D point that dictates the location on that specified level.
            Returns: If successful a new Space element within the project, otherwise ll.
        """
        pass

    def NewSpaceBoundaryLines(self, sketchPlane, curves, view):
        """
        NewSpaceBoundaryLines(self: Document, sketchPlane: SketchPlane, curves: CurveArray, view: View) -> ModelCurveArray
        
            Creates a new boundary line as an Space border.
        
            sketchPlane: The sketch plan
            curves: The geometry curves on which the boundary lines are
            view: The View for the new Space
        """
        pass

    def NewSpaces2(self, *__args):
        """
        NewSpaces2(self: Document, level: Level, phase: Phase, view: View) -> ICollection[ElementId]
        
            Creates new spaces on the available plan circuits of a the given level.
        
            level: The level on which the spaces is to exist.
            phase: The phase in which the spaces is to exist.
            view: The view on which the space tags for the spaces are to display.
            Returns: If successful, a set of ElementIds which contains the rooms should be returned, 
             otherwise the exception will be thrown.
        
        NewSpaces2(self: Document, phase: Phase, count: int) -> ICollection[ElementId]
        
            Creates a set of new unplaced spaces on a given phase.
        
            phase: The phase in which the spaces are to exist.
            Returns: If successful, a set of ElementIds of new unplaced spaces are be returned, 
             otherwise ll.
        """
        pass

    def NewSpaceTag(self, space, point, view):
        """
        NewSpaceTag(self: Document, space: Space, point: UV, view: View) -> SpaceTag
        
            Creates a new SpaceTag.
        
            space: The Space which the tag refers.
            point: A 2D point that dictates the location on the level of the space.
            view: The view where the tag will lie.
            Returns: If successful a SpaceTag object will be returned, otherwise ll. 
        Suitable 
             exceptions will be fired if the parameters are invalid.
        """
        pass

    def NewSpotCoordinate(self, view, reference, origin, bend, end, refPt, hasLeader):
        """
        NewSpotCoordinate(self: Document, view: View, reference: Reference, origin: XYZ, bend: XYZ, end: XYZ, refPt: XYZ, hasLeader: bool) -> SpotDimension
        
            Generate a new spot coordinate object within the project.
        
            view: The view in which the spot coordinate is to be visible.
            reference: The reference to which the spot coordinate is to be bound.
            origin: The point which the spot coordinate evaluate.
            bend: The bend point for the spot coordinate.
            end: The end point for the spot coordinate.
            refPt: The actual point on the reference which the spot coordinate evaluate.
            hasLeader: Indicate if it has leader or not.
            Returns: If successful a new spot dimension object, otherwise ll.
        """
        pass

    def NewSpotElevation(self, view, reference, origin, bend, end, refPt, hasLeader):
        """
        NewSpotElevation(self: Document, view: View, reference: Reference, origin: XYZ, bend: XYZ, end: XYZ, refPt: XYZ, hasLeader: bool) -> SpotDimension
        
            Generate a new spot elevation object within the project.
        
            view: The view in which the spot elevation is to be visible.
            reference: The reference to which the spot elevation is to be bound.
            origin: The point which the spot elevation evaluate.
            bend: The bend point for the spot elevation.
            end: The end point for the spot elevation.
            refPt: The actual point on the reference which the spot elevation evaluate.
            hasLeader: Indicate if it has leader or not.
            Returns: If successful a new spot dimension object, otherwise ll.
        """
        pass

    def NewTag(self, dbview, elemToTag, addLeader, tagMode, tagOrientation, pnt):
        """
        NewTag(self: Document, dbview: View, elemToTag: Element, addLeader: bool, tagMode: TagMode, tagOrientation: TagOrientation, pnt: XYZ) -> IndependentTag
        
            Creates a new IndependentTag Element.
        
            dbview: The view in which the tag is to be visible.
            elemToTag: The host object of tag.
            addLeader: Whether there will be a leader.
            tagMode: The mode of the tag. Add by Category, add by Multi-Category, or add by material.
            tagOrientation: The orientation of the tag.
            pnt: If not using a leader, this is the position of the tag head.  If using a 
             leader, then the tag will be placed with the default leader length as close to 
             this input point as possible.
        
            Returns: If successful, an IndependentTag object is returned.
        """
        pass

    def NewTakeoffFitting(self, connector, curve):
        """
        NewTakeoffFitting(self: Document, connector: Connector, curve: MEPCurve) -> FamilyInstance
        
            Add a new family instance of an takeoff fitting into the Autodesk Revit 
             document,
        using one connector and one MEP curve.
        
        
            connector: The connector to be connected to the takeoff.
            curve: The duct or pipe which is the trunk for the takeoff.
            Returns: If creation was successful then an family instance to the new object is 
             returned,
        otherwise an exception with failure information will be thrown.
        """
        pass

    def NewTeeFitting(self, connector1, connector2, connector3):
        """
        NewTeeFitting(self: Document, connector1: Connector, connector2: Connector, connector3: Connector) -> FamilyInstance
        
            Add a new family instance of a tee fitting into the Autodesk Revit document,
        
             using three connectors.
        
        
            connector1: The first connector to be connected to the tee.
            connector2: The second connector to be connected to the tee.
            connector3: The third connector to be connected to the tee. 
        This should be connected to 
             the branch of the tee.
        
            Returns: If creation was successful then an family instance to the new object is 
             returned,
        and the transition fitting will be added at the connectors' end if 
             necessary, 
        otherwise an exception with failure information will be thrown.
        """
        pass

    def NewTransitionFitting(self, connector1, connector2):
        """
        NewTransitionFitting(self: Document, connector1: Connector, connector2: Connector) -> FamilyInstance
        
            Add a new family instance of an transition fitting into the Autodesk Revit 
             document,
        using two connectors.
        
        
            connector1: The first connector to be connected to the transition.
            connector2: The second connector to be connected to the transition.
            Returns: If creation was successful then an family instance to the new object is 
             returned,
        otherwise an exception with failure information will be thrown.
        """
        pass

    def NewUnionFitting(self, connector1, connector2):
        """
        NewUnionFitting(self: Document, connector1: Connector, connector2: Connector) -> FamilyInstance
        
            Add a new family instance of an union fitting into the Autodesk Revit document,
             
        using two connectors.
        
        
            connector1: The first connector to be connected to the union.
            connector2: The second connector to be connected to the union.
            Returns: If creation was successful then an family instance to the new object is 
             returned,
        otherwise an exception with failure information will be thrown.
        """
        pass

    def NewZone(self, level, phase):
        """
        NewZone(self: Document, level: Level, phase: Phase) -> Zone
        
            Creates a new Zone element.
        
            level: The level on which the Zone is to exist.
            phase: The associative phase on which the Zone is to exist.
            Returns: If successful a new Zone element within the project, otherwise ll.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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


class eRefFace(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates the reference face. The Opening will be created at the direction perpendicular to 
    the reference face.
    
    enum eRefFace, values: CenterX (1), CenterY (4), CenterZ (7)
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

    CenterX = None
    CenterY = None
    CenterZ = None
    value__ = None


class FamilyInstanceCreationData(object):
    """
    A class which wraps the arguments of FamilyInstance for batch creation.
    
    FamilyInstanceCreationData(proxy: object)
    FamilyInstanceCreationData(symbol: FamilySymbol, adaptivePoints: IList[XYZ])
    FamilyInstanceCreationData(face: Face, position: Line, symbol: FamilySymbol)
    FamilyInstanceCreationData(face: Face, location: XYZ, referenceDirection: XYZ, symbol: FamilySymbol)
    FamilyInstanceCreationData(location: XYZ, symbol: FamilySymbol, referenceDirection: XYZ, host: Element, structuralType: StructuralType)
    FamilyInstanceCreationData(location: XYZ, symbol: FamilySymbol, host: Element, level: Level, structuralType: StructuralType)
    FamilyInstanceCreationData(location: XYZ, symbol: FamilySymbol, host: Element, structuralType: StructuralType)
    FamilyInstanceCreationData(location: XYZ, symbol: FamilySymbol, level: Level, structuralType: StructuralType)
    FamilyInstanceCreationData(curve: Curve, symbol: FamilySymbol, level: Level, structuralType: StructuralType)
    FamilyInstanceCreationData(location: XYZ, symbol: FamilySymbol, structuralType: StructuralType)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, proxy: object)
        __new__(cls: type, symbol: FamilySymbol, adaptivePoints: IList[XYZ])
        __new__(cls: type, face: Face, position: Line, symbol: FamilySymbol)
        __new__(cls: type, face: Face, location: XYZ, referenceDirection: XYZ, symbol: FamilySymbol)
        __new__(cls: type, location: XYZ, symbol: FamilySymbol, referenceDirection: XYZ, host: Element, structuralType: StructuralType)
        __new__(cls: type, location: XYZ, symbol: FamilySymbol, host: Element, level: Level, structuralType: StructuralType)
        __new__(cls: type, location: XYZ, symbol: FamilySymbol, host: Element, structuralType: StructuralType)
        __new__(cls: type, location: XYZ, symbol: FamilySymbol, level: Level, structuralType: StructuralType)
        __new__(cls: type, curve: Curve, symbol: FamilySymbol, level: Level, structuralType: StructuralType)
        __new__(cls: type, location: XYZ, symbol: FamilySymbol, structuralType: StructuralType)
        """
        pass

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the axis of the FamilyInstance

Get: Axis(self: FamilyInstanceCreationData) -> Line

Set: Axis(self: FamilyInstanceCreationData) = value
"""

    RotateAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the rotate angle of the FamilyInstance

Get: RotateAngle(self: FamilyInstanceCreationData) -> float

Set: RotateAngle(self: FamilyInstanceCreationData) = value
"""



class FamilyItemFactory(ItemFactoryBase, IDisposable):
    """
    The Family Item Factory object is used to create new instances of elements within the
    Autodesk Revit Family.
    """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def NewAngularDimension(self, view, arc, firstRef, secondRef, dimensionType=None):
        """
        NewAngularDimension(self: FamilyItemFactory, view: View, arc: Arc, firstRef: Reference, secondRef: Reference) -> Dimension
        
            Creates a new angular dimension object using the default dimension type.
        
            view: The view in which the dimension is to be visible.
            arc: The extension arc of the dimension.
            firstRef: The first geometric reference to which the dimension is to be bound.
        The 
             reference must be perpendicular to the extension arc.
        
            secondRef: The second geometric reference to which the dimension is to be bound.
        The 
             reference must be perpendicular to the extension arc.
        
            Returns: If creation was successful the new angular dimension is returned, 
        otherwise 
             an exception with failure information will be thrown.
        
        NewAngularDimension(self: FamilyItemFactory, view: View, arc: Arc, firstRef: Reference, secondRef: Reference, dimensionType: DimensionType) -> Dimension
        
            Creates a new angular dimension object using the specified dimension type.
        
            view: The view in which the dimension is to be visible.
            arc: The extension arc of the dimension.
            firstRef: The first geometric reference to which the dimension is to be bound.
        The 
             reference must be perpendicular to the extension arc.
        
            secondRef: The second geometric reference to which the dimension is to be bound.
        The 
             reference must be perpendicular to the extension arc.
        
            dimensionType: The dimension style to be used for the dimension.
            Returns: If creation was successful the new angular dimension is returned, 
        otherwise 
             an exception with failure information will be thrown.
        """
        pass

    def NewArcLengthDimension(self, view, arc, arcRef, firstRef, secondRef, dimensionType=None):
        """
        NewArcLengthDimension(self: FamilyItemFactory, view: View, arc: Arc, arcRef: Reference, firstRef: Reference, secondRef: Reference) -> Dimension
        
            Creates a new arc length dimension object using the default dimension type.
        
            view: The view in which the dimension is to be visible.
            arc: The extension arc of the dimension.
            arcRef: Geometric reference of the arc to which the dimension is to be bound.
        This 
             reference must be parallel to the extension arc.
        
            firstRef: The first geometric reference to which the dimension is to be bound. 
        This 
             reference must intersect the arcRef reference.
        
            secondRef: The second geometric reference to which the dimension is to be bound. 
        This 
             reference must intersect the arcRef reference.
        
            Returns: If creation was successful the new arc length dimension is returned, 
        
             otherwise an exception with failure information will be thrown.
        
        NewArcLengthDimension(self: FamilyItemFactory, view: View, arc: Arc, arcRef: Reference, firstRef: Reference, secondRef: Reference, dimensionType: DimensionType) -> Dimension
        
            Creates a new arc length dimension object using the specified dimension type.
        
            view: The view in which the dimension is to be visible.
            arc: The extension arc of the dimension.
            arcRef: Geometric reference of the arc to which the dimension is to be bound.
        This 
             reference must be parallel to the extension arc.
        
            firstRef: The first geometric reference to which the dimension is to be bound.
        This 
             reference must intersect the arcRef reference.
        
            secondRef: The second geometric reference to which the dimension is to be bound.
        This 
             reference must intersect the arcRef reference.
        
            dimensionType: The dimension style to be used for the dimension.
            Returns: If creation was successful the new arc length dimension is returned, 
        
             otherwise an exception with failure information will be thrown.
        """
        pass

    def NewBlend(self, isSolid, topProfile, baseProfile, sketchPlane):
        """
        NewBlend(self: FamilyItemFactory, isSolid: bool, topProfile: CurveArray, baseProfile: CurveArray, sketchPlane: SketchPlane) -> Blend
        
            Add a new Blend instance into the Autodesk Revit family document.
        
            isSolid: Indicates if the Blend is Solid or Void.
            topProfile: The top blend section. It should consist of only one curve loop.
        The input 
             profile must be in one plane.
        
            baseProfile: The base blend section. It should consist of only one curve loop.
        The input 
             profile must be in one plane.
        
            sketchPlane: The sketch plane for the base profile. Use this to associate the 
        base of the 
             blend to geometry from another element. Optional, it can be ll if you want 
             Revit
        to derive a new sketch plane from the geometry of the base profile.
        
            Returns: If creation was successful the new blend is returned, 
        otherwise an exception 
             with failure information will be thrown.
        """
        pass

    def NewControl(self, controlShape, view, origin):
        """
        NewControl(self: FamilyItemFactory, controlShape: ControlShape, view: View, origin: XYZ) -> Control
        
            Add a new control into the Autodesk Revit family document.
        
            controlShape: The shape of the control.
            view: The view in which the control is to be visible. It
        must be a FloorPlan view or 
             a CeilingPlan view.
        
            origin: The origin of the control.
            Returns: If successful, the newly created control is returned, otherwise an
        exception 
             with error information will be thrown.
        """
        pass

    def NewCurveByPoints(self, points):
        """
        NewCurveByPoints(self: FamilyItemFactory, points: ReferencePointArray) -> CurveByPoints
        
            Create a 3d curve through two or more points in an Autodesk
        Revit family 
             document.
        
        
            points: Two or more PointElements. The curve will interpolate
        these points.
            Returns: The newly created curve.
        """
        pass

    def NewDiameterDimension(self, view, arcRef, origin):
        """
        NewDiameterDimension(self: FamilyItemFactory, view: View, arcRef: Reference, origin: XYZ) -> Dimension
        
            Creates a new diameter dimension object using the default dimension type.
        
            view: The view in which the dimension is to be visible.
            arcRef: Geometric reference of the arc to which the dimension is to be bound.
            origin: The point where the witness line of the diameter dimension will lie.
            Returns: If creation was successful the new diameter dimension is returned, 
        otherwise 
             an exception with failure information will be thrown.
        """
        pass

    def NewExtrusion(self, isSolid, profile, sketchPlane, end):
        """
        NewExtrusion(self: FamilyItemFactory, isSolid: bool, profile: CurveArrArray, sketchPlane: SketchPlane, end: float) -> Extrusion
        
            Add a new Extrusion instance into the Autodesk Revit family document.
        
            isSolid: Indicates if the Extrusion is Solid or Void.
            profile: The profile of the newly created Extrusion. This may contain more 
        than one 
             curve loop. Each loop must be a fully closed curve loop and the loops may not 
        
             intersect. All input curves must lie in the same plane.
        The loop can be a 
             unbound circle or ellipse,  but its geometry will be split in two in 
        order to 
             satisfy requirements for sketches used in extrusions.
        
            sketchPlane: The sketch plane for the extrusion.  The direction of extrusion
        is determined 
             by the normal for the sketch plane.  To extrude in the other direction set 
        
             the end value to negative.
        
            end: The length of the extrusion.
            Returns: If creation was successful the new Extrusion is returned, 
        otherwise an 
             exception with failure information will be thrown.
        """
        pass

    def NewExtrusionForm(self, isSolid, profile, direction):
        """
        NewExtrusionForm(self: FamilyItemFactory, isSolid: bool, profile: ReferenceArray, direction: XYZ) -> Form
        
            Create new Form element by Extrude operation, and add it into the Autodesk 
             Revit family document.
        
        
            isSolid: Indicates if the Form is Solid or Void.
            profile: The profile of extrusion. It should consist of only one curve loop.
            direction: The direction of extrusion, with its length the length of the extrusion. The 
             direction must be perpendicular to the plane determined by profile. The length 
             of vector must be non-zero.
        
            Returns: If creation was successful new form is returned.
        """
        pass

    def NewFormByCap(self, isSolid, profile):
        """
        NewFormByCap(self: FamilyItemFactory, isSolid: bool, profile: ReferenceArray) -> Form
        
            Create new Form element by cap operation (to create a single-surface form), and 
             add it into the Autodesk Revit family document.
        
        
            isSolid: Indicates if the Form is Solid or Void.
            profile: The profile of the newly created cap. It should consist of only one curve loop.
            Returns: If creation was successful new form is returned.
        """
        pass

    def NewFormByThickenSingleSurface(self, isSolid, singleSurfaceForm, thickenDir):
        """
        NewFormByThickenSingleSurface(self: FamilyItemFactory, isSolid: bool, singleSurfaceForm: Form, thickenDir: XYZ) -> Form
        
            Create a new Form element by thickening a single-surface form, and add it into 
             the Autodesk Revit family document.
        
        
            isSolid: Indicates if the Form is Solid or Void.
            singleSurfaceForm: The single-surface form element. It can have one top/bottom face or one side 
             face.
        
            thickenDir: The offset of capped solid.
            Returns: This function will modify the input singleSurfaceForm and return the same 
             element.
        """
        pass

    def NewLinearDimension(self, view, line, references, dimensionType=None):
        """
        NewLinearDimension(self: FamilyItemFactory, view: View, line: Line, references: ReferenceArray) -> Dimension
        
            Generate a new linear dimension object using the default dimension type.
        
            view: The view in which the dimension is to be visible.
            line: The extension line of the dimension.
            references: An array of geometric references to which the dimension is to be bound.
        You 
             must supply at least two references, and all references supplied must be 
             parallel to each other 
        and perpendicular to the extension line.
        
            Returns: If creation was successful the new linear dimension is returned, 
        otherwise an 
             exception with failure information will be thrown.
        
        NewLinearDimension(self: FamilyItemFactory, view: View, line: Line, references: ReferenceArray, dimensionType: DimensionType) -> Dimension
        
            Creates a new linear dimension object using the specified dimension type.
        
            view: The view in which the dimension is to be visible.
            line: The extension line of the dimension.
            references: An array of geometric references to which the dimension is to be bound.
        You 
             must supply at least two references, and all references supplied must be 
             parallel to each other 
        and perpendicular to the extension line.
        
            dimensionType: The dimension style to be used for the dimension.
            Returns: If creation was successful the new linear dimension is returned, 
        otherwise an 
             exception with failure information will be thrown.
        """
        pass

    def NewLoftForm(self, isSolid, profiles):
        """
        NewLoftForm(self: FamilyItemFactory, isSolid: bool, profiles: ReferenceArrayArray) -> Form
        
            Create new Form element by Loft operation, and add it into the Autodesk Revit 
             family document.
        
        
            isSolid: Indicates if the Form is Solid or Void.
            profiles: The profile set of the newly created loft. Each profile should consist of only 
             one curve loop.
        
            Returns: If creation was successful form is are returned.
        """
        pass

    def NewModelText(self, text, modelTextType, sketchPlane, position, horizontalAlign, depth):
        """
        NewModelText(self: FamilyItemFactory, text: str, modelTextType: ModelTextType, sketchPlane: SketchPlane, position: XYZ, horizontalAlign: HorizontalAlign, depth: float) -> ModelText
        
            Create a model text in the Autodesk Revit family document.
        
            text: The text to be displayed.
            modelTextType: The type of model text. If this parameter is ll, the default type will be used.
            sketchPlane: The sketch plane of the model text. The direction of model text is determined 
             by the normal of the sketch plane.
        To extrude in the other direction set the 
             depth value to negative.
        
            position: The position of the model text. The position must lie in the sketch plane.
            horizontalAlign: The horizontal alignment.
            depth: The depth of the model text.
            Returns: If successful, the newly created model text is returned, otherwise an
        
             exception with error information will be thrown.
        """
        pass

    def NewOpening(self, host, profile):
        """
        NewOpening(self: FamilyItemFactory, host: Element, profile: CurveArray) -> Opening
        
            Create an opening to cut the wall or ceiling.
        
            host: Host elements that new opening would lie in. The host can only be a wall or a 
             ceiling.
        
            profile: The profile of the newly created opening. This may contain more 
        than one 
             curve loop. Each loop must be a fully closed curve loop and the loops may not 
        
             intersect. The profiles will be projected into the host plane.
        
            Returns: If successful, the newly created opening is returned, otherwise an
        exception 
             with error information will be thrown.
        """
        pass

    def NewRadialDimension(self, view, arcRef, origin, dimensionType=None):
        """
        NewRadialDimension(self: FamilyItemFactory, view: View, arcRef: Reference, origin: XYZ) -> Dimension
        
            Creates a new radial dimension object using the default dimension type.
        
            view: The view in which the dimension is to be visible.
            arcRef: Geometric reference of the arc to which the dimension is to be bound.
            origin: The point where the witness line of the radial dimension will lie.
            Returns: If creation was successful the new arc length dimension is returned, 
        
             otherwise an exception with failure information will be thrown.
        
        NewRadialDimension(self: FamilyItemFactory, view: View, arcRef: Reference, origin: XYZ, dimensionType: DimensionType) -> Dimension
        
            Generate a new radial dimension object using a specified dimension type.
        
            view: The view in which the dimension is to be visible.
            arcRef: Geometric reference of the arc to which the dimension is to be bound.
            origin: The point where the witness line of the radial dimension will lie.
            dimensionType: The dimension style to be used for the dimension.
            Returns: If creation was successful the new arc length dimension is returned, 
        
             otherwise an exception with failure information will be thrown.
        """
        pass

    def NewReferencePoint(self, A_0):
        """
        NewReferencePoint(self: FamilyItemFactory, A_0: XYZ) -> ReferencePoint
        
            Create a reference point at a given location in an Autodesk
        Revit family 
             document.
        
            Returns: The newly created ReferencePoint.
        NewReferencePoint(self: FamilyItemFactory, A_0: Transform) -> ReferencePoint
        
            Create a reference point at a given location and with a given
        coordinate 
             system in an Autodesk Revit family document.
        
            Returns: The newly created ReferencePoint.
        NewReferencePoint(self: FamilyItemFactory, A_0: PointElementReference) -> ReferencePoint
        
            Create a reference point on an existing reference in an Autodesk
        Revit family 
             document.
        
            Returns: The newly created ReferencePoint.
        """
        pass

    def NewRevolution(self, isSolid, profile, sketchPlane, axis, startAngle, endAngle):
        """
        NewRevolution(self: FamilyItemFactory, isSolid: bool, profile: CurveArrArray, sketchPlane: SketchPlane, axis: Line, startAngle: float, endAngle: float) -> Revolution
        
            Add a new Revolution instance into the Autodesk Revit family document.
        
            isSolid: Indicates if the Revolution is Solid or Void.
            profile: The profile of the newly created revolution. This may contain
        more than one 
             curve loop. Each loop must be a fully closed curve loop and the loops 
        must 
             not intersect. All loops must lie in the same plane.
        The loop can be a unbound 
             circle or ellipse,  but its geometry will be split in two in 
        order to satisfy 
             requirements for sketches used in extrusions.
        
            sketchPlane: The sketch plane for the revolution.  The direction of revolution
        is 
             determined by the normal for the sketch plane.
        
            axis: The axis of revolution. This axis must lie in the same plane as the curve loops.
            startAngle: The start angle of Revolution in radians.
            endAngle: The end angle of Revolution in radians.
            Returns: If creation was successful the new revolution is returned, 
        otherwise an 
             exception with failure information will be thrown.
        """
        pass

    def NewRevolveForms(self, isSolid, profile, axis, startAngle, endAngle):
        """
        NewRevolveForms(self: FamilyItemFactory, isSolid: bool, profile: ReferenceArray, axis: Reference, startAngle: float, endAngle: float) -> FormArray
        
            Create new Form elements by revolve operation, and add them into the Autodesk 
             Revit family document.
        
        
            isSolid: Indicates if the Form is Solid or Void.
            profile: The profile of the newly created revolution. It should consist of only one 
             curve loop.
        The profile must be in the same plane as the axis.
        
            axis: The axis of revolution. The axis is a line that must lie in the same plane as 
             the curves in the profile.
        
            startAngle: The start angle of Revolution in radians.
            endAngle: The end angle of Revolution in radians.
            Returns: If creation was successful new forms are returned.
        """
        pass

    def NewSweep(self, isSolid, path, *__args):
        """
        NewSweep(self: FamilyItemFactory, isSolid: bool, path: CurveArray, pathPlane: SketchPlane, profile: SweepProfile, profileLocationCurveIndex: int, profilePlaneLocation: ProfilePlaneLocation) -> Sweep
        
            Adds a new sweep form to the family document, using a path of curve elements.
        
            isSolid: Indicates if the Sweep is Solid or Void.
            path: The path of the sweep. The path should be 2D, where all input curves lie in one 
             plane, and the curves are not 
        required to reference existing geometry.
        
            pathPlane: The sketch plane for the path. Use this when you want to create 
        a 2D path 
             that resides on an existing planar face. Optional, can be ll for 3D paths or 
        
             for 2D paths where the path should not reference an existing face.
        
            profile: The profile of the newly created Sweep. This may contain
        more than one curve 
             loop or a profile family. The profile must lie in the XY plane, and it will be 
             
        transformed to the profile plane automatically. Each loop must be a fully 
             closed curve loop and the loops 
        must not intersect.
        The loop can be a 
             unbound circle or ellipse,  but its geometry will be split in two in 
        order to 
             satisfy requirements for sketches used in extrusions.
        
            profileLocationCurveIndex: The index of the path curves. The curve upon which the profile
        plane will be 
             determined.
        
            profilePlaneLocation: The location on the profileLocationCurve where the profile
        plane will be 
             determined.
        
            Returns: If creation was successful the new Sweep is returned, 
        otherwise an exception 
             with failure information will be thrown.
        
        NewSweep(self: FamilyItemFactory, isSolid: bool, path: ReferenceArray, profile: SweepProfile, profileLocationCurveIndex: int, profilePlaneLocation: ProfilePlaneLocation) -> Sweep
        
            Adds a new sweep form into the family document, using an array of selected 
             references as a 3D path.
        
        
            isSolid: Indicates if the Sweep is Solid or Void.
            path: The path of the sweep. The path should be reference of curve or edge obtained 
             from existing geometry.
        
            profile: The profile to create the new Sweep. The profile must lie in the XY plane, and 
             it will be 
        transformed to the profile plane automatically. This may contain 
             more than one curve loop or a profile family. 
        Each loop must be a fully 
             closed curve loop and the loops must not intersect.
        The loop can be a unbound 
             circle or ellipse,  but its geometry will be split in two in 
        order to satisfy 
             requirements for sketches used in extrusions.
        
            profileLocationCurveIndex: The index of the path curves. The curve upon which the profile
        plane will be 
             determined.
        
            profilePlaneLocation: The location on the profileLocationCurve where the profile
        plane will be 
             determined.
        
            Returns: If creation was successful the new Sweep is returned, 
        otherwise an exception 
             with failure information will be thrown.
        """
        pass

    def NewSweptBlend(self, isSolid, path, *__args):
        """
        NewSweptBlend(self: FamilyItemFactory, isSolid: bool, path: Curve, pathPlane: SketchPlane, bottomProfile: SweepProfile, topProfile: SweepProfile) -> SweptBlend
        
            Add a new swept blend into the family document, using a curve as the path.
        
            isSolid: Indicates if the swept blend is Solid or Void.
            path: The path of the swept blend. The path should be a single curve.
        Or the path 
             can be a single sketched curve, and the curve is not required to reference 
             existing geometry.
        
            pathPlane: The sketch plane for the path. Use this when you want to create 
        a 2D path 
             that resides on an existing planar face. Optional, can be ll for a path curve 
             obtained from geometry or 
        for 2D paths where the path should not reference an 
             existing edge.
        
            bottomProfile: The bottom profile of the newly created Swept blend. It should consist of only 
             one curve loop.
        The profile must lie in the XY plane, and it will be 
             transformed to the profile plane automatically.
        
            topProfile: The top profile of the newly created Swept blend. It should consist of only one 
             curve loop.
        The profile must lie in the XY plane, and it will be transformed 
             to the profile plane automatically.
        
            Returns: If creation was successful the new Swept blend is returned, 
        otherwise an 
             exception with failure information will be thrown.
        
        NewSweptBlend(self: FamilyItemFactory, isSolid: bool, path: Reference, bottomProfile: SweepProfile, topProfile: SweepProfile) -> SweptBlend
        
            Adds a new swept blend into the family document, using a selected reference as 
             the path.
        
        
            isSolid: Indicates if the swept blend is Solid or Void.
            path: The path of the swept blend. The path might be a reference of single curve or 
             edge obtained from existing geometry.
        Or the path can be a single sketched 
             curve, and the curve is not required to reference existing geometry.
        
            bottomProfile: The bottom profile of the newly created Swept blend. It should consist of only 
             one curve loop.
        the input profile must be in one plane.
        
            topProfile: The top profile of the newly created Swept blend. It should consist of only one 
             curve loop.
        The profile must lie in the XY plane, and it will be transformed 
             to the profile plane automatically.
        
            Returns: If creation was successful the new Swept blend is returned, 
        otherwise an 
             exception with failure information will be thrown.
        """
        pass

    def NewSweptBlendForm(self, isSolid, path, profiles):
        """
        NewSweptBlendForm(self: FamilyItemFactory, isSolid: bool, path: ReferenceArray, profiles: ReferenceArrayArray) -> Form
        
            Create new Form element by swept blend operation, and add it into the Autodesk 
             Revit family document.
        
        
            isSolid: Indicates if the Form is Solid or Void.
            path: The path of the swept blend. The path should be 2D, where all input curves lie 
             in one plane. If there's more than one profile, the path should be a single 
             curve. 
        It's required to reference existing geometry.
        
            profiles: The profile set of the newly created swept blend. Each profile should consist 
             of only one curve loop.
        Each profile must be in a plane that intersects with 
             the path and is perpendicular to the path at the point of intersection.
        
            Returns: If creation was successful new form is returned.
        """
        pass

    def NewSymbolicCurve(self, curve, sketchPlane):
        """
        NewSymbolicCurve(self: FamilyItemFactory, curve: Curve, sketchPlane: SketchPlane) -> SymbolicCurve
        
            Create a symbolic curve in an Autodesk Revit family document.
        
            curve: The geometry curve of the newly created symbolic curve.
            sketchPlane: The sketch plane for the symbolic curve.
            Returns: The newly created symbolic curve.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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


