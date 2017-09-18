# encoding: utf-8
# module Grasshopper.Getters calls itself Getters
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_ArcGetter(object):
    # no doc
    @staticmethod
    def GetArc():
        """ GetArc() -> GH_Arc """
        pass

    @staticmethod
    def GetArcs():
        """ GetArcs() -> List[GH_Arc] """
        pass


class GH_BoxGetter(object):
    # no doc
    @staticmethod
    def GetBox():
        """ GetBox() -> GH_Box """
        pass

    @staticmethod
    def GetBoxes():
        """ GetBoxes() -> List[GH_Box] """
        pass


class GH_BrepGetter(object):
    # no doc
    @staticmethod
    def GetBrep():
        """ GetBrep() -> GH_Brep """
        pass

    @staticmethod
    def GetBreps():
        """ GetBreps() -> List[GH_Brep] """
        pass


class GH_CircleGetter(object):
    # no doc
    @staticmethod
    def GetCircle():
        """ GetCircle() -> GH_Circle """
        pass

    @staticmethod
    def GetCircles():
        """ GetCircles() -> List[GH_Circle] """
        pass


class GH_CurveGetter(object):
    # no doc
    @staticmethod
    def GetCurve():
        """ GetCurve() -> GH_Curve """
        pass

    @staticmethod
    def GetCurves():
        """ GetCurves() -> List[GH_Curve] """
        pass


class GH_GeometryGetter(object):
    # no doc
    @staticmethod
    def GetGeometries():
        """ GetGeometries() -> List[IGH_GeometricGoo] """
        pass

    @staticmethod
    def GetGeometry():
        """ GetGeometry() -> IGH_GeometricGoo """
        pass


class GH_LineGetter(object):
    # no doc
    @staticmethod
    def GetLine():
        """ GetLine() -> GH_Line """
        pass

    @staticmethod
    def GetLines():
        """ GetLines() -> List[GH_Line] """
        pass


class GH_MeshGetter(object):
    # no doc
    @staticmethod
    def GetMesh():
        """ GetMesh() -> GH_Mesh """
        pass

    @staticmethod
    def GetMeshes():
        """ GetMeshes() -> List[GH_Mesh] """
        pass


class GH_PlaneGetter(object):
    # no doc
    @staticmethod
    def GetPlane():
        """ GetPlane() -> GH_Plane """
        pass

    @staticmethod
    def GetPlanes():
        """ GetPlanes() -> List[GH_Plane] """
        pass


class GH_PointGetter(object):
    """ GH_PointGetter() """
    def DefaultRefType(self):
        """ DefaultRefType(self: GH_PointGetter) -> GH_PointRefType """
        pass

    @staticmethod
    def GetPoint(*__args):
        """
        GetPoint(self: GH_PointGetter, base: Point3d) -> GH_Point
        GetPoint(self: GH_PointGetter) -> GH_Point
        GetPoint(prompt: str, base_point: Point3d, out_point: Point3d) -> (GH_GetterResult, Point3d)
        """
        pass

    def GetPoints(self):
        """ GetPoints(self: GH_PointGetter) -> List[GH_Point] """
        pass

    def RecreateSetup(self, pt):
        """ RecreateSetup(self: GH_PointGetter, pt: GH_Point) """
        pass

    AcceptPreselected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AcceptPreselected(self: GH_PointGetter) -> bool

Set: AcceptPreselected(self: GH_PointGetter) = value
"""

    PointRefType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointRefType(self: GH_PointGetter) -> GH_PointRefType

Set: PointRefType(self: GH_PointGetter) = value
"""



class GH_RectangleGetter(object):
    # no doc
    @staticmethod
    def GetRectangle():
        """ GetRectangle() -> GH_Rectangle """
        pass

    @staticmethod
    def GetRectangles():
        """ GetRectangles() -> List[GH_Rectangle] """
        pass


class GH_SurfaceGetter(object):
    # no doc
    @staticmethod
    def GetSurface():
        """ GetSurface() -> GH_Surface """
        pass

    @staticmethod
    def GetSurfaces():
        """ GetSurfaces() -> List[GH_Surface] """
        pass


class GH_TransformGetter(object):
    # no doc

class GH_VectorGetter(object):
    # no doc
    @staticmethod
    def GetVector():
        """ GetVector() -> GH_Vector """
        pass

    @staticmethod
    def GetVectors():
        """ GetVectors() -> List[GH_Vector] """
        pass


