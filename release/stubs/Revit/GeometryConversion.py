# encoding: utf-8
# module Revit.GeometryConversion calls itself GeometryConversion
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CurveUtils(object):
    # no doc
    @staticmethod
    def CurvesAreSimilar(a, b):
        """
        CurvesAreSimilar(a: Curve, b: Curve) -> bool
        
            This method uses basic checks to compare curves for similarity.
                    It 
             starts by comparing the curves' end points. Curves which have similar
                 
                end points but different directions will not be regarded as similar,
               
                  because directionality is important in Revit for other purposes. 
                
                 Depending on the curve type, other comparisons are then performed.
        
        
            a: The first curve.
            b: The second curve.
            Returns: Returns true if the curves are similar within Tolerance, and 
                    
             false if they are not.
        """
        pass

    @staticmethod
    def GetPlaneFromCurve(c, planarOnly):
        """ GetPlaneFromCurve(c: Curve, planarOnly: bool) -> Plane """
        pass

    @staticmethod
    def IsLineLike(crv):
        """ IsLineLike(crv: Curve) -> bool """
        pass

    @staticmethod
    def PointArraysAreSame(pnts1, pnts2):
        """ PointArraysAreSame(pnts1: ReferencePointArray, pnts2: ReferencePointArray) -> bool """
        pass

    @staticmethod
    def ReferencePointsAreSame(pnt1, pnt2):
        """ ReferencePointsAreSame(pnt1: ReferencePoint, pnt2: ReferencePoint) -> bool """
        pass

    Tolerance = 9.9999999999999995e-07
    __all__ = [
        'CurvesAreSimilar',
        'GetPlaneFromCurve',
        'IsLineLike',
        'PointArraysAreSame',
        'ReferencePointsAreSame',
        'Tolerance',
    ]


class DynamoToRevitBRep(object):
    # no doc
    @staticmethod
    def ToRevitType(*__args):
        """
        ToRevitType(surf: Surface, performHostUnitConversion: bool, materialId: ElementId) -> GeometryObject
        
            this method attempts to construct a BRep from a surface.
        ToRevitType(sol: Solid, performHostUnitConversion: bool, materialId: ElementId) -> GeometryObject
        
            this method attempts to construct a BRep from a closed solid.
        """
        pass

    __all__ = [
        'ToRevitType',
    ]


class GeometryObjectConverter(object):
    # no doc
    @staticmethod
    def Convert(geom, reference, transform):
        """
        Convert(geom: GeometryObject, reference: Reference, transform: CoordinateSystem) -> object
        
            Convert a GeometryObject to an applicable ProtoGeometry type.
            Returns: A Geometry type.  Null if there's no suitable conversion.
        """
        pass

    @staticmethod
    def ConvertToMany(solid, reference, transform):
        """
        ConvertToMany(solid: Solid, reference: Reference, transform: CoordinateSystem) -> IEnumerable[object]
        
            Get the edges and faces from the solid and convert them
        """
        pass

    @staticmethod
    def InternalConvert(geom):
        """ InternalConvert(geom: PolyLine) -> PolyCurve """
        pass

    __all__ = [
        'Convert',
        'ConvertToMany',
        'InternalConvert',
    ]


class GeometryPrimitiveConverter(object):
    # no doc
    @staticmethod
    def GetPerpendicular(*__args):
        """
        GetPerpendicular(vector: Vector) -> Vector
        GetPerpendicular(xyz: XYZ) -> XYZ
        """
        pass

    @staticmethod
    def ToCoordinateSystem(t, convertUnits):
        """ ToCoordinateSystem(t: Transform, convertUnits: bool) -> CoordinateSystem """
        pass

    @staticmethod
    def ToDegrees(degrees):
        """ ToDegrees(degrees: float) -> float """
        pass

    @staticmethod
    def ToDoubleArray(list):
        """ ToDoubleArray(list: Array[float]) -> DoubleArray """
        pass

    @staticmethod
    def ToPlane(plane, convertUnits):
        """
        ToPlane(plane: Plane, convertUnits: bool) -> Plane
        ToPlane(plane: Plane, convertUnits: bool) -> Plane
        """
        pass

    @staticmethod
    def ToPoint(xyz, convertUnits):
        """ ToPoint(xyz: XYZ, convertUnits: bool) -> Point """
        pass

    @staticmethod
    def ToPoints(list, convertUnits):
        """ ToPoints(list: List[XYZ], convertUnits: bool) -> List[Point] """
        pass

    @staticmethod
    def ToProtoType(*__args):
        """
        ToProtoType(uv: UV) -> UV
        ToProtoType(point: Point, convertUnits: bool) -> Point
        ToProtoType(xyz: BoundingBoxXYZ, convertUnits: bool) -> BoundingBox
        """
        pass

    @staticmethod
    def ToRadians(degrees):
        """ ToRadians(degrees: float) -> float """
        pass

    @staticmethod
    def ToRevitBoundingBox(cs, minPoint, maxPoint, convertUnits):
        """ ToRevitBoundingBox(cs: CoordinateSystem, minPoint: Point, maxPoint: Point, convertUnits: bool) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def ToRevitType(*__args):
        """
        ToRevitType(vec: Vector, convertUnits: bool) -> XYZ
        ToRevitType(pt: Point, convertUnits: bool) -> XYZ
        ToRevitType(bb: BoundingBox, convertUnits: bool) -> BoundingBoxXYZ
        """
        pass

    @staticmethod
    def ToTransform(cs, convertUnits):
        """ ToTransform(cs: CoordinateSystem, convertUnits: bool) -> Transform """
        pass

    @staticmethod
    def ToVector(xyz, convertUnits):
        """ ToVector(xyz: XYZ, convertUnits: bool) -> Vector """
        pass

    @staticmethod
    def ToXyz(*__args):
        """
        ToXyz(vec: Vector, convertUnits: bool) -> XYZ
        ToXyz(pt: Point, convertUnits: bool) -> XYZ
        """
        pass

    @staticmethod
    def ToXyzs(list, convertUnits):
        """
        ToXyzs(list: Array[Vector], convertUnits: bool) -> Array[XYZ]
        ToXyzs(list: Array[Point], convertUnits: bool) -> Array[XYZ]
        ToXyzs(list: List[Point], convertUnits: bool) -> List[XYZ]
        """
        pass

    __all__ = [
        'GetPerpendicular',
        'ToCoordinateSystem',
        'ToDegrees',
        'ToDoubleArray',
        'ToPlane',
        'ToPoint',
        'ToPoints',
        'ToProtoType',
        'ToRadians',
        'ToRevitBoundingBox',
        'ToRevitType',
        'ToTransform',
        'ToVector',
        'ToXyz',
        'ToXyzs',
    ]


class NurbsUtils(object):
    # no doc
    @staticmethod
    def ElevateBezierDegree(crv, finalDegree):
        """
        ElevateBezierDegree(crv: NurbsCurve, finalDegree: int) -> NurbsCurve
        
            Elevate the degree of a Bezier curve (represented in NURBS form) to a given 
             degree
                    without changing the shape
        
        
            crv: The curve
            finalDegree: The requested degree
        """
        pass

    __all__ = [
        'ElevateBezierDegree',
    ]


class PolygonContainment(object):
    # no doc
    @staticmethod
    def AdjustDelta(delta, vertex, next_vertex, p):
        """ AdjustDelta(delta: int, vertex: UV, next_vertex: UV, p: UV) -> int """
        pass

    @staticmethod
    def GetQuadrant(vertex, p):
        """
        GetQuadrant(vertex: UV, p: UV) -> int
        
            Determine the quadrant of a polygon vertex 
                    relative to the test 
             point.
        """
        pass

    @staticmethod
    def GetXIntercept(p, q, y):
        """
        GetXIntercept(p: UV, q: UV, y: float) -> float
        
            Determine the X intercept of a polygon edge 
                    with a horizontal 
             line at the Y value of the 
                    test point.
        """
        pass

    @staticmethod
    def PolygonContains(polygon, point):
        """ PolygonContains(polygon: List[UV], point: UV) -> bool """
        pass

    __all__ = [
        'AdjustDelta',
        'GetQuadrant',
        'GetXIntercept',
        'PolygonContains',
    ]


class ProtoToRevitCurve(object):
    # no doc
    @staticmethod
    def ToRevitType(*__args):
        """
        ToRevitType(pcrv: PolyCurve, performHostUnitConversion: bool) -> CurveLoop
        ToRevitType(crv: Curve, performHostUnitConversion: bool) -> Curve
        """
        pass

    __all__ = [
        'ToRevitType',
    ]


class ProtoToRevitMesh(object):
    # no doc
    @staticmethod
    def CreateBoundingBoxMeshForErrors(minPoint, maxPoint, performHostUnitConversion):
        """
        CreateBoundingBoxMeshForErrors(minPoint: Point, maxPoint: Point, performHostUnitConversion: bool) -> IList[GeometryObject]
        
            This is to create a bounding box mesh for geometries which have errors during 
             the tessellating process
        """
        pass

    @staticmethod
    def ToRevitType(*__args):
        """
        ToRevitType(mesh: Mesh, target: TessellatedShapeBuilderTarget, fallback: TessellatedShapeBuilderFallback, MaterialId: ElementId, performHostUnitConversion: bool) -> IList[GeometryObject]
        ToRevitType(solid: Solid, target: TessellatedShapeBuilderTarget, fallback: TessellatedShapeBuilderFallback, MaterialId: ElementId, performHostUnitConversion: bool) -> IList[GeometryObject]
        ToRevitType(srf: Surface, target: TessellatedShapeBuilderTarget, fallback: TessellatedShapeBuilderFallback, MaterialId: ElementId, performHostUnitConversion: bool) -> IList[GeometryObject]
        """
        pass

    __all__ = [
        'CreateBoundingBoxMeshForErrors',
        'ToRevitType',
    ]


class RevitToProtoCurve(object):
    # no doc
    @staticmethod
    def ToProtoType(*__args):
        """
        ToProtoType(geom: PolyLine, performHostUnitConversion: bool) -> PolyCurve
        ToProtoType(revitCurves: CurveArray, performHostUnitConversion: bool) -> PolyCurve
        ToProtoType(revitCurve: Curve, performHostUnitConversion: bool, referenceOverride: Reference) -> Curve
        """
        pass

    __all__ = [
        'ToProtoType',
    ]


class RevitToProtoFace(object):
    # no doc
    @staticmethod
    def ToProtoType(revitFace, performHostUnitConversion, referenceOverride):
        """ ToProtoType(revitFace: Face, performHostUnitConversion: bool, referenceOverride: Reference) -> IEnumerable[Surface] """
        pass

    __all__ = [
        'ToProtoType',
    ]


class RevitToProtoMesh(object):
    # no doc
    @staticmethod
    def ToProtoType(*__args):
        """
        ToProtoType(meshArray: IEnumerable[Mesh], performHostUnitConversion: bool) -> Array[Mesh]
        ToProtoType(mesh: Mesh, performHostUnitConversion: bool) -> Mesh
        """
        pass

    __all__ = [
        'ToProtoType',
    ]


class RevitToProtoSolid(object):
    # no doc
    @staticmethod
    def ToProtoType(solid, performHostUnitConversion):
        """ ToProtoType(solid: Solid, performHostUnitConversion: bool) -> Solid """
        pass

    __all__ = [
        'ToProtoType',
    ]


class SurfaceExtractor(object):
    """
    This class is required to extract the underlying surface representation from a Revit Face.
                All Face types are supported.
    """
    @staticmethod
    def ExtractSurface(face, edgeLoops):
        """
        ExtractSurface(face: HermiteFace, edgeLoops: IEnumerable[PolyCurve]) -> Surface
        ExtractSurface(face: RevolvedFace, edgeLoops: IEnumerable[PolyCurve]) -> Surface
        ExtractSurface(face: RuledFace, edgeLoops: IEnumerable[PolyCurve]) -> Surface
        ExtractSurface(face: PlanarFace, edgeLoops: IEnumerable[PolyCurve]) -> Surface
        ExtractSurface(face: CylindricalFace, edgeLoops: IEnumerable[PolyCurve]) -> Surface
        ExtractSurface(face: ConicalFace, edgeLoops: IEnumerable[PolyCurve]) -> Surface
        """
        pass

    __all__ = [
        'ExtractSurface',
    ]


class UnitConverter(object):
    # no doc
    @staticmethod
    def ConvertToDynamoUnits(geometry):
# Error generating skeleton for function ConvertToDynamoUnits: Method must be called on a Type for which Type.IsGenericParameter is false.

    @staticmethod
    def ConvertToHostUnits(geometry):
# Error generating skeleton for function ConvertToHostUnits: Method must be called on a Type for which Type.IsGenericParameter is false.

    @staticmethod
    def DynamoToHostFactor(unitType):
        """ DynamoToHostFactor(unitType: UnitType) -> float """
        pass

    @staticmethod
    def HostToDynamoFactor(unitType):
        """ HostToDynamoFactor(unitType: UnitType) -> float """
        pass

    @staticmethod
    def InDynamoUnits(geometry):
# Error generating skeleton for function InDynamoUnits: Method must be called on a Type for which Type.IsGenericParameter is false.

    @staticmethod
    def InHostUnits(geometry):
# Error generating skeleton for function InHostUnits: Method must be called on a Type for which Type.IsGenericParameter is false.

    __all__ = [
        'ConvertToDynamoUnits',
        'ConvertToHostUnits',
        'DynamoToHostFactor',
        'HostToDynamoFactor',
        'InDynamoUnits',
        'InHostUnits',
    ]


