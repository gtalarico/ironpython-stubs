# encoding: utf-8
# module Rhino.Render calls itself Render
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CachedTextureCoordinates(CommonObject):
    # no doc
    def Add(self, item):
        """ Add(self: CachedTextureCoordinates, item: Point3d) """
        pass

    def Clear(self):
        """ Clear(self: CachedTextureCoordinates) """
        pass

    def Contains(self, item):
        """ Contains(self: CachedTextureCoordinates, item: Point3d) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: CachedTextureCoordinates, array: Array[Point3d], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CachedTextureCoordinates) -> IEnumerator[Point3d] """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: CachedTextureCoordinates, item: Point3d) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: CachedTextureCoordinates, index: int, item: Point3d) """
        pass

    def Remove(self, item):
        """ Remove(self: CachedTextureCoordinates, item: Point3d) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: CachedTextureCoordinates, index: int) """
        pass

    def TryGetAt(self, index, u, v, w):
        """ TryGetAt(self: CachedTextureCoordinates, index: int) -> (bool, float, float, float) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: ICollection[Point3d], item: Point3d) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CachedTextureCoordinates) -> int

"""

    Dim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dim(self: CachedTextureCoordinates) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: CachedTextureCoordinates) -> bool

"""

    MappingId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MappingId(self: CachedTextureCoordinates) -> Guid

"""



class MappingTag(object):
    """ MappingTag() """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: MappingTag) -> Guid

Set: Id(self: MappingTag) = value
"""

    MappingCRC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MappingCRC(self: MappingTag) -> UInt32

Set: MappingCRC(self: MappingTag) = value
"""

    MappingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MappingType(self: MappingTag) -> TextureMappingType

Set: MappingType(self: MappingTag) = value
"""

    MeshTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MeshTransform(self: MappingTag) -> Transform

Set: MeshTransform(self: MappingTag) = value
"""



class RenderSettings(object):
    """ RenderSettings() """
    def Dispose(self):
        """ Dispose(self: RenderSettings) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    AmbientLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AmbientLight(self: RenderSettings) -> Color

Set: AmbientLight(self: RenderSettings) = value
"""

    AntialiasLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AntialiasLevel(self: RenderSettings) -> int

Set: AntialiasLevel(self: RenderSettings) = value
"""

    BackgroundColorBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColorBottom(self: RenderSettings) -> Color

Set: BackgroundColorBottom(self: RenderSettings) = value
"""

    BackgroundColorTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColorTop(self: RenderSettings) -> Color

Set: BackgroundColorTop(self: RenderSettings) = value
"""

    BackgroundStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundStyle(self: RenderSettings) -> BackgroundStyle

Set: BackgroundStyle(self: RenderSettings) = value
"""

    DepthCue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepthCue(self: RenderSettings) -> bool

Set: DepthCue(self: RenderSettings) = value
"""

    FlatShade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlatShade(self: RenderSettings) -> bool

Set: FlatShade(self: RenderSettings) = value
"""

    ImageSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImageSize(self: RenderSettings) -> Size

Set: ImageSize(self: RenderSettings) = value
"""

    RenderAnnotations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderAnnotations(self: RenderSettings) -> bool

Set: RenderAnnotations(self: RenderSettings) = value
"""

    RenderBackfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderBackfaces(self: RenderSettings) -> bool

Set: RenderBackfaces(self: RenderSettings) = value
"""

    RenderCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderCurves(self: RenderSettings) -> bool

Set: RenderCurves(self: RenderSettings) = value
"""

    RenderIsoparams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderIsoparams(self: RenderSettings) -> bool

Set: RenderIsoparams(self: RenderSettings) = value
"""

    RenderMeshEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderMeshEdges(self: RenderSettings) -> bool

Set: RenderMeshEdges(self: RenderSettings) = value
"""

    RenderPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderPoints(self: RenderSettings) -> bool

Set: RenderPoints(self: RenderSettings) = value
"""

    ShadowmapLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowmapLevel(self: RenderSettings) -> int

Set: ShadowmapLevel(self: RenderSettings) = value
"""

    UseHiddenLights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseHiddenLights(self: RenderSettings) -> bool

Set: UseHiddenLights(self: RenderSettings) = value
"""

    UseViewportSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseViewportSize(self: RenderSettings) -> bool

Set: UseViewportSize(self: RenderSettings) = value
"""



class TextureMapping(CommonObject):
    # no doc
    @staticmethod
    def CreateBoxMapping(plane, dx, dy, dz, capped):
        """ CreateBoxMapping(plane: Plane, dx: Interval, dy: Interval, dz: Interval, capped: bool) -> TextureMapping """
        pass

    @staticmethod
    def CreateCylinderMapping(cylinder, capped):
        """ CreateCylinderMapping(cylinder: Cylinder, capped: bool) -> TextureMapping """
        pass

    @staticmethod
    def CreatePlaneMapping(plane, dx, dy, dz):
        """ CreatePlaneMapping(plane: Plane, dx: Interval, dy: Interval, dz: Interval) -> TextureMapping """
        pass

    @staticmethod
    def CreateSphereMapping(sphere):
        """ CreateSphereMapping(sphere: Sphere) -> TextureMapping """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def TryGetMappingBox(self, plane, dx, dy, dz):
        """ TryGetMappingBox(self: TextureMapping) -> (bool, Plane, Interval, Interval, Interval) """
        pass

    def TryGetMappingCylinder(self, cylinder):
        """ TryGetMappingCylinder(self: TextureMapping) -> (bool, Cylinder) """
        pass

    def TryGetMappingPlane(self, plane, dx, dy, dz):
        """ TryGetMappingPlane(self: TextureMapping) -> (bool, Plane, Interval, Interval, Interval) """
        pass

    def TryGetMappingSphere(self, sphere):
        """ TryGetMappingSphere(self: TextureMapping) -> (bool, Sphere) """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: TextureMapping) -> Guid

"""

    MappingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MappingType(self: TextureMapping) -> TextureMappingType

"""

    NormalTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalTransform(self: TextureMapping) -> Transform

Set: NormalTransform(self: TextureMapping) = value
"""

    PrimativeTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimativeTransform(self: TextureMapping) -> Transform

Set: PrimativeTransform(self: TextureMapping) = value
"""

    UvwTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UvwTransform(self: TextureMapping) -> Transform

Set: UvwTransform(self: TextureMapping) = value
"""



class TextureMappingType(Enum):
    """ enum TextureMappingType, values: BoxMapping (5), BrepMappingPrimitive (8), CylinderMapping (3), MeshMappingPrimitive (6), None (0), PlaneMapping (2), SphereMapping (4), SurfaceMappingPrimitive (7), SurfaceParameters (1) """
    BoxMapping = None
    BrepMappingPrimitive = None
    CylinderMapping = None
    MeshMappingPrimitive = None
    None = None
    PlaneMapping = None
    SphereMapping = None
    SurfaceMappingPrimitive = None
    SurfaceParameters = None
    value__ = None


