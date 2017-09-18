# encoding: utf-8
# module Rhino.Render calls itself Render
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CachedTextureCoordinates(CommonObject, IDisposable, ISerializable, IList[Point3d], ICollection[Point3d], IEnumerable[Point3d], IEnumerable):
    """ Used for cached texture coordinates """
    def Add(self, item):
        """
        Add(self: CachedTextureCoordinates, item: Point3d)
            IList implementation, this list is always read-only so calling this
                    will cause a 
             NotSupportedException to be thrown.
        """
        pass

    def Clear(self):
        """
        Clear(self: CachedTextureCoordinates)
            IList implementation, this list is always read-only so calling this
                    will cause a 
             NotSupportedException to be thrown.
        """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: CachedTextureCoordinates, item: Point3d) -> bool
        
            Determines whether this collection contains a specific value.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """
        CopyTo(self: CachedTextureCoordinates, array: Array[Point3d], arrayIndex: int)
            Copies the elements of the this collection to an System.Array,
                    starting at a 
             particular System.Array index.
        
        
            array: The one-dimensional System.Array that is the destination of the
                    elements copied 
             from this collection. The System.Array must have
                    zero-based indexing.
        
            arrayIndex: The zero-based index in array at which copying begins.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: CachedTextureCoordinates) -> IEnumerator[Point3d]
        
            Returns an enumerator that iterates through this collection.
            Returns: A enumerator that can be used to iterate through this collection.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: CachedTextureCoordinates, item: Point3d) -> int
        
            Determines the index of a specific point in this collection.
        
            item: The point (UV or UVW) to locate in this collection.
            Returns: The index of item if found in the list; otherwise, -1.
        """
        pass

    def Insert(self, index, item):
        """
        Insert(self: CachedTextureCoordinates, index: int, item: Point3d)
            IList implementation, this list is always read-only so calling this
                    will cause a 
             NotSupportedException to be thrown.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: CommonObject)
            Is called when a non-const operation first occurs.
        """
        pass

    def Remove(self, item):
        """
        Remove(self: CachedTextureCoordinates, item: Point3d) -> bool
        
            IList implementation, this list is always read-only so calling this
                    will cause a 
             NotSupportedException to be thrown.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: CachedTextureCoordinates, index: int)
            IList implementation, this list is always read-only so calling this
                    will cause a 
             NotSupportedException to be thrown.
        """
        pass

    def TryGetAt(self, index, u, v, w):
        """
        TryGetAt(self: CachedTextureCoordinates, index: int) -> (bool, float, float, float)
        
            Use this method to iterate the cached texture coordinate array.
        
            index: Index for the vertex to fetch.
            Returns: Returns true if index is valid; otherwise returns false.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[Point3d], item: Point3d) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
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
    """Number of cached coordinates.

Get: Count(self: CachedTextureCoordinates) -> int

"""

    Dim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Coordinate dimension: 2 = UV, 3 = UVW

Get: Dim(self: CachedTextureCoordinates) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This collection is always read-only

Get: IsReadOnly(self: CachedTextureCoordinates) -> bool

"""

    MappingId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The texture mapping Id.

Get: MappingId(self: CachedTextureCoordinates) -> Guid

"""



class ContentUndoBlocker(object, IDisposable):
    """ ContentUndoBlocker() """
    def Dispose(self):
        """ Dispose(self: ContentUndoBlocker) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class CreatePreviewEventArgs(EventArgs):
    """ Used in RenderPlugIn virtual CreatePreview function """
    Cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get set by Rhino if the preview generation should be canceled for this

Get: Cancel(self: CreatePreviewEventArgs) -> bool

"""

    Environment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The environment that the previewed object is rendered in.

Get: Environment(self: CreatePreviewEventArgs) -> RenderEnvironment

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unique Id for this scene.

Get: Id(self: CreatePreviewEventArgs) -> int

"""

    Lights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lights(self: CreatePreviewEventArgs) -> List[Light]

"""

    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Objects(self: CreatePreviewEventArgs) -> List[SceneObject]

"""

    PreviewContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The content being previewed.

Get: PreviewContent(self: CreatePreviewEventArgs) -> RenderContent

"""

    PreviewImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Initially null.  If this image is set, then this image will be used for
            the preview.  If never set, the default internal simulation preview will
            be used.

Get: PreviewImage(self: CreatePreviewEventArgs) -> Bitmap

Set: PreviewImage(self: CreatePreviewEventArgs) = value
"""

    PreviewImageSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pixel size of the image that is being requested for the preview scene

Get: PreviewImageSize(self: CreatePreviewEventArgs) -> Size

"""

    Quality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Quality of the preview image that is being requested for the preview scene

Get: Quality(self: CreatePreviewEventArgs) -> PreviewSceneQuality

"""

    Reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reason the preview is getting generated

Get: Reason(self: CreatePreviewEventArgs) -> CreatePreviewReason

"""

    Viewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Viewport(self: CreatePreviewEventArgs) -> ViewportInfo

"""


    SceneObject = None


class CreatePreviewReason(Enum, IComparable, IFormattable, IConvertible):
    """
    Reason the content preview is being generated
    
    enum CreatePreviewReason, values: ContentChanged (0), Other (99), RefreshDisplay (2), ViewChanged (1)
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

    ContentChanged = None
    Other = None
    RefreshDisplay = None
    value__ = None
    ViewChanged = None


class CreateTexture2dPreviewEventArgs(EventArgs):
    # no doc
    PreviewImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Initially null.  If this image is set, then this image will be used for
            the preview.  If never set, the default internal simulation preview will
            be used.

Get: PreviewImage(self: CreateTexture2dPreviewEventArgs) -> Bitmap

Set: PreviewImage(self: CreateTexture2dPreviewEventArgs) = value
"""

    PreviewImageSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pixel size of the image that is being requested for the preview scene

Get: PreviewImageSize(self: CreateTexture2dPreviewEventArgs) -> Size

"""



class CustomRenderMeshProvider(object):
    """
    You must call CustomRenderMeshProvider.RegisterProviders() from your
                plug-ins OnLoad override for each assembly containing a custom mesh
                provider.  Only publicly exported classes derived from
                CustomRenderMeshProvider with a public constructor that has no parameters
                will get registered.
    """
    @staticmethod
    def AllObjectsChanged():
        """
        AllObjectsChanged()
            Call this method if your render meshes change.
        """
        pass

    def BoundingBox(self, vp, obj, requestingPlugIn, preview):
        """
        BoundingBox(self: CustomRenderMeshProvider, vp: ViewportInfo, obj: RhinoObject, requestingPlugIn: Guid, preview: bool) -> BoundingBox
        
            Returns a bounding box for the custom render meshes for the given object.
        
            vp: The viewport being rendered.
            obj: The Rhino object of interest.
            requestingPlugIn: UUID of the RDK plug-in requesting the meshes.
            preview: Type of mesh to build.
            Returns: A bounding box value.
        """
        pass

    def BuildCustomMeshes(self, vp, objMeshes, requestingPlugIn, meshType):
        """
        BuildCustomMeshes(self: CustomRenderMeshProvider, vp: ViewportInfo, objMeshes: RenderPrimitiveList, requestingPlugIn: Guid, meshType: bool) -> bool
        
            Build custom render mesh(es).
        
            vp: The viewport being rendered.
            objMeshes: The meshes class to populate with custom meshes.
            requestingPlugIn: UUID of the RDK plug-in requesting the meshes.
            meshType: Type of mesh to build.
            Returns: true if operation was successful.
        """
        pass

    @staticmethod
    def ObjectChanged(obj):
        """ ObjectChanged(obj: RhinoObject) """
        pass

    @staticmethod
    def RegisterProviders(assembly, pluginId):
        """
        RegisterProviders(assembly: Assembly, pluginId: Guid)
            Call this method once from your plug-ins OnLoad override for each
                    assembly 
             containing a custom mesh provider.  Only publicly exported
                    classes derived from 
             CustomRenderMeshProvider with a public constructor
                    that has no parameters will get 
             registered.
        
        
            assembly: Assembly to search for valid CustomRenderMeshProvider derived classes.
            pluginId: The plug-in that owns the custom mesh providers.
        """
        pass

    def WillBuildCustomMeshes(self, vp, obj, requestingPlugIn, preview):
        """
        WillBuildCustomMeshes(self: CustomRenderMeshProvider, vp: ViewportInfo, obj: RhinoObject, requestingPlugIn: Guid, preview: bool) -> bool
        
            Determines if custom render meshes will be built for a particular object.
        
            vp: The viewport being rendered.
            obj: The Rhino object of interest.
            requestingPlugIn: UUID of the RDK plug-in requesting the meshes.
            preview: Type of mesh to build.
            Returns: true if custom meshes will be built.
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the provider for UI display.

Get: Name(self: CustomRenderMeshProvider) -> str

"""



class Decal(object, IDisposable):
    """ Represents a decal, or a picture that can be moved on an object. """
    def ConstPointer(self):
        """ ConstPointer(self: Decal) -> IntPtr """
        pass

    @staticmethod
    def Create(createParams):
        """ Create(createParams: DecalCreateParams) -> Decal """
        pass

    def Dispose(self, isDisposing=None):
        """ Dispose(self: Decal, isDisposing: bool)Dispose(self: Decal) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: Decal) -> IntPtr """
        pass

    def TryGetColor(self, point, normal, colInOut, uvOut):
        """
        TryGetColor(self: Decal, point: Point3d, normal: Vector3d, colInOut: Color4f, uvOut: Point2d) -> (bool, Color4f, Point2d)
        
            Blend color with the decal color at a given point.
        
            point: The point in space or, if the decal is uv-mapped, the uv-coordinate of that point.
            normal: The face normal of the given point.
            colInOut: The color to blend the decal color to.
            uvOut: the UV on the texture that the color point was read from.
            Returns: true if the given point hits the decal, else false.
        """
        pass

    def UVBounds(self, minUOut, minVOut, maxUOut, maxVOut):
        """
        UVBounds(self: Decal, minUOut: float, minVOut: float, maxUOut: float, maxVOut: float) -> (float, float, float, float)
        
            The UV bounds of the decal. Only used when mapping is UV.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DecalMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the mapping of the decal.

Get: DecalMapping(self: Decal) -> DecalMapping

"""

    DecalProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the decal's projection. Used only when mapping is planar.

Get: DecalProjection(self: Decal) -> DecalProjection

"""

    EndLatitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stop latitude of the decal's sweep. Only used when mapping is cylindrical or spherical.

Get: EndLatitude(self: Decal) -> float

"""

    EndLongitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stop longitude of the decal's sweep. Only used when mapping is spherical.

Get: EndLongitude(self: Decal) -> float

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the decal. Only used when mapping is cylindrical.

Get: Height(self: Decal) -> float

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the decal ID associated with this decal.

Get: Id(self: Decal) -> int

"""

    MapToInside = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Used only when mapping is cylindrical or spherical.

Get: MapToInside(self: Decal) -> bool

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the origin of the decal in world space.

Get: Origin(self: Decal) -> Point3d

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the radius of the decal. Only used when mapping is cylindrical or spherical.

Get: Radius(self: Decal) -> float

"""

    StartLatitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the start latitude of the decal's sweep. Only used when mapping is cylindrical or spherical.

Get: StartLatitude(self: Decal) -> float

"""

    StartLongitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the start longitude of the decal's sweep. Only used when mapping is spherical.

Get: StartLongitude(self: Decal) -> float

"""

    TextureInstanceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the texture ID for this decal.

Get: TextureInstanceId(self: Decal) -> Guid

"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the decal's transparency in the range 0 to 1.

Get: Transparency(self: Decal) -> float

"""

    VectorAcross = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the vector across. For cylindrical and spherical mapping, the vector is unitized.

Get: VectorAcross(self: Decal) -> Vector3d

"""

    VectorUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For cylindrical and spherical mapping, the vector is unitized.

Get: VectorUp(self: Decal) -> Vector3d

"""



class DecalMapping(Enum, IComparable, IFormattable, IConvertible):
    """ enum DecalMapping, values: Cylindrical (1), Planar (0), Spherical (2), UV (3) """
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

    Cylindrical = None
    Planar = None
    Spherical = None
    UV = None
    value__ = None


class DecalProjection(Enum, IComparable, IFormattable, IConvertible):
    """ enum DecalProjection, values: Backward (1), Both (2), Forward (0) """
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

    Backward = None
    Both = None
    Forward = None
    value__ = None


class Decals(object, IEnumerable[Decal], IEnumerable):
    """ Represents all the decals of an object. """
    def Add(self, decal):
        """
        Add(self: Decals, decal: Decal) -> UInt32
        
            Add a new Decal to the decals list, use Decal.Create to create
                    a new decal instance 
             to add.
        """
        pass

    def Clear(self):
        """ Clear(self: Decals) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Decals) -> IEnumerator[Decal] """
        pass

    def Remove(self, decal):
        """ Remove(self: Decals, decal: Decal) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Decal](enumerable: IEnumerable[Decal], value: Decal) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class GroundPlane(object):
    """
    Represents an infinite plane for implementation by renderers.
                See Rhino.PlugIns.RenderPlugIn.SupportsFeature(Rhino.PlugIns.RenderPlugIn.RenderFeature)SupportsFeature.
    """
    Altitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Height above world XY plane in model units.

Get: Altitude(self: GroundPlane) -> float

Set: Altitude(self: GroundPlane) = value
"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Document this groundplane is associated with.

Get: Document(self: GroundPlane) -> RhinoDoc

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether the document ground plane is enabled.

Get: Enabled(self: GroundPlane) -> bool

Set: Enabled(self: GroundPlane) = value
"""

    MaterialInstanceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of material in material table for this ground plane.

Get: MaterialInstanceId(self: GroundPlane) -> Guid

Set: MaterialInstanceId(self: GroundPlane) = value
"""

    TextureOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Texture mapping offset in world units.

Get: TextureOffset(self: GroundPlane) -> Vector2d

Set: TextureOffset(self: GroundPlane) = value
"""

    TextureRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Texture mapping rotation around world origin + offset in degrees.

Get: TextureRotation(self: GroundPlane) -> float

Set: TextureRotation(self: GroundPlane) = value
"""

    TextureSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Texture mapping single UV span size in world units.

Get: TextureSize(self: GroundPlane) -> Vector2d

Set: TextureSize(self: GroundPlane) = value
"""


    Changed = None


class ImageFile(object):
    """ Controls interaction with RDK render image files """
    Deleted = None
    Loaded = None
    Saved = None
    __all__ = [
        'Deleted',
        'Loaded',
        'Saved',
    ]


class ImageFileEvent(Enum, IComparable, IFormattable, IConvertible):
    """ enum ImageFileEvent, values: Deleted (2), Loaded (1), Saved (0) """
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

    Deleted = None
    Loaded = None
    Saved = None
    value__ = None


class ImageFileEventArgs(EventArgs):
    # no doc
    EllapsedTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EllapsedTime(self: ImageFileEventArgs) -> int

"""

    Event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Event(self: ImageFileEventArgs) -> ImageFileEvent

"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: ImageFileEventArgs) -> str

"""

    RenderEngine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderEngine(self: ImageFileEventArgs) -> str

"""

    RenderEngineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderEngineId(self: ImageFileEventArgs) -> Guid

"""

    SessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionId(self: ImageFileEventArgs) -> Guid

"""



class MappingTag(object):
    """
    Holds texture mapping information.
    
    MappingTag()
    """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a map globally unique identifier.

Get: Id(self: MappingTag) -> Guid

Set: Id(self: MappingTag) = value
"""

    MappingCRC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the cyclic redundancy check on the mapping.
            See also Rhino.RhinoMath.CRC32(System.UInt32,System.Byte[]).

Get: MappingCRC(self: MappingTag) -> UInt32

Set: MappingCRC(self: MappingTag) = value
"""

    MappingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a texture mapping type: linear, cylinder, etc...

Get: MappingType(self: MappingTag) -> TextureMappingType

Set: MappingType(self: MappingTag) = value
"""

    MeshTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a 4x4 matrix tranform.

Get: MeshTransform(self: MappingTag) -> Transform

Set: MeshTransform(self: MappingTag) = value
"""



class NamedValue(object):
    """ NamedValue(name: str, value: object) """
    @staticmethod # known case of __new__
    def __new__(self, name, value):
        """ __new__(cls: type, name: str, value: object) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: NamedValue) -> str

Set: Name(self: NamedValue) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: NamedValue) -> object

Set: Value(self: NamedValue) = value
"""



class PreviewSceneQuality(Enum, IComparable, IFormattable, IConvertible):
    """
    Quality levels when creating preview images
    
    enum PreviewSceneQuality, values: RealtimeQuick (-1), RefineFirstPass (1), RefineSecondPass (2), RefineThirdPass (3)
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

    RealtimeQuick = None
    RefineFirstPass = None
    RefineSecondPass = None
    RefineThirdPass = None
    value__ = None


class RenderContent(object, IDisposable):
    # no doc
    def AddAutomaticUserInterfaceSection(self, caption, id):
        """
        AddAutomaticUserInterfaceSection(self: RenderContent, caption: str, id: int) -> bool
        
            Add a new automatic user interface section, Field values which include
                    prompts will 
             be automatically added to this section.
        
        
            caption: Expandable tab caption.
            id: Tab id which may be used later on to reference this tab.
            Returns: Returns true if the automatic tab section was added otherwise; returns
                    false on 
             error.
        """
        pass

    def AddChild(self, renderContent):
        """ AddChild(self: RenderContent, renderContent: RenderContent) -> bool """
        pass

    @staticmethod
    def AddPersistentRenderContent(renderContent):
        """
        AddPersistentRenderContent(renderContent: RenderContent) -> bool
        
            Add a material, environment or texture to the internal RDK document lists as
                    top 
             level content.  The content must have been returned from
                    RenderContent::MakeCopy, 
             NewContentFromType or a similar function that returns
                    a non-document content.
        
        
            renderContent: The render content.
            Returns: true on success.
        """
        pass

    def AddUserInterfaceSection(self, classType, caption, createExpanded, createVisible):
        """
        AddUserInterfaceSection(self: RenderContent, classType: Type, caption: str, createExpanded: bool, createVisible: bool) -> UserInterfaceSection
        
            Add a new .NET control to an content expandable tab section, the height
                    of the 
             createExpanded tabs client area will be the initial height of the
                    specified 
             control.
        
        
            classType: The control class to create and embed as a child window in the
                    expandable tab 
             client area.  This class type must be derived from
                    IWin32Window or this method will 
             throw an ArgumentException.  Implement
                    the IUserInterfaceSection interface in your 
             classType to get
                    UserInterfaceSection notification.
        
            caption: Expandable tab caption.
            createExpanded: If this value is true then the new expandable tab section will
                    initially be 
             expanded, if it is false it will be collapsed.
        
            createVisible: If this value is true then the new expandable tab section will
                    initially be 
             visible, if it is false it will be hidden.
        
            Returns: Returns the UserInterfaceSection object used to manage the new 
                    user control object.
        """
        pass

    def BindParameterToField(self, parameterName, *__args):
        """ BindParameterToField(self: RenderContent, parameterName: str, field: Field, setEvent: ChangeContexts)BindParameterToField(self: RenderContent, parameterName: str, childSlotName: str, field: Field, setEvent: ChangeContexts) """
        pass

    def ChangeChild(self, oldContent, newContent):
        """ ChangeChild(self: RenderContent, oldContent: RenderContent, newContent: RenderContent) -> bool """
        pass

    def ChildSlotAmount(self, childSlotName):
        """
        ChildSlotAmount(self: RenderContent, childSlotName: str) -> float
        
            Gets the amount property for the texture in the specified child slot.  Values are typically from 
             0.0 - 100.0
        
        
            childSlotName: Child slot name for the child
        """
        pass

    def ChildSlotNameFromParamName(self, paramName):
        """
        ChildSlotNameFromParamName(self: RenderContent, paramName: str) -> str
        
            A "child slot" is the specific "slot" that a child (usually a texture) occupies.
                     
             This is generally the "use" of the child - in other words, the thing the child
                     
             operates on.  Some examples are "color", "transparency".
        
        
            paramName: The name of a parameter field. Since child textures will usually correspond with some
                  
               parameter (they generally either replace or modify a parameter over UV space) these functions 
             are used to
                    specify which parameter corresponded with child slot.  If there is no 
             correspondence, return the empty
                    string.
        
            Returns: The default behavior for these functions is to return the input string.
                     
             Sub-classes may (in the future) override these functions to provide different mappings.
        """
        pass

    def ChildSlotOn(self, childSlotName):
        """
        ChildSlotOn(self: RenderContent, childSlotName: str) -> bool
        
            Gets the on-ness property for the texture in the specified child slot.
        
            childSlotName: Child slot name for the child
        """
        pass

    @staticmethod
    def Create(type, *__args):
        """
        Create(type: Guid, parent: RenderContent, childSlotName: str, flags: ShowContentChooserFlags, doc: RhinoDoc) -> RenderContent
        Create(type: Type, parent: RenderContent, childSlotName: str, flags: ShowContentChooserFlags, doc: RhinoDoc) -> RenderContent
        Create(type: Guid, flags: ShowContentChooserFlags, doc: RhinoDoc) -> RenderContent
        Create(type: Type, flags: ShowContentChooserFlags, doc: RhinoDoc) -> RenderContent
        """
        pass

    def DeleteAllChildren(self, changeContexts):
        """ DeleteAllChildren(self: RenderContent, changeContexts: ChangeContexts) """
        pass

    def DeleteChild(self, childSlotName, changeContexts):
        """ DeleteChild(self: RenderContent, childSlotName: str, changeContexts: ChangeContexts) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: RenderContent) """
        pass

    def FindChild(self, childSlotName):
        """ FindChild(self: RenderContent, childSlotName: str) -> RenderContent """
        pass

    @staticmethod
    def FromId(document, id):
        """
        FromId(document: RhinoDoc, id: Guid) -> RenderContent
        
            Search for a content object based on its Id
        
            document: The Rhino document containing the content.
            id: Id of the content instance to search for.
            Returns: Returns the content object with the specified Id if it is found
                    otherwise it 
             returns null.
        """
        pass

    def GetChildSlotParameter(self, parameterName, childSlotName):
        """
        GetChildSlotParameter(self: RenderContent, parameterName: str, childSlotName: str) -> object
        
            Extra requirements are a way of specifying extra functionality on parameters in the automatic 
             UI.
                    Implement this function to specify additional functionality for automatic UI 
             sections or the texture summary.
                    See IAutoUIExtraRequirements.h in the C++ RDK for 
             string definitions for the parameter names.
        
        
            parameterName: The parameter or field internal name to which this query applies
            childSlotName: The extra requirement parameter, as listed in IAutoUIExtraRequirements.h in the C++ RDK
            Returns: Call the base class if you do not support the extra requirement parameter.
                    Current 
             supported return values are (int, bool, float, double, string, Guid, Color, Vector3d, Point3d, 
             DateTime)
        """
        pass

    def GetParameter(self, parameterName):
        """
        GetParameter(self: RenderContent, parameterName: str) -> object
        
            Query the content instance for the value of a given named parameter.
                    If you do not 
             support this parameter, call the base class.
        
        
            parameterName: Name of the parameter
        """
        pass

    def Icon(self, size):
        """
        Icon(self: RenderContent, size: Size) -> Bitmap
        
            Icon to display in the content browser, this bitmap needs to be valid for
                    the life 
             of this content object, the content object that returns the bitmap
                    is responsible 
             for disposing of the bitmap.
        
        
            size: Requested icon size
            Returns: Return Icon to display in the content browser.
        """
        pass

    def IsFactoryProductAcceptableAsChild(self, kindId, factoryKind, childSlotName):
        """
        IsFactoryProductAcceptableAsChild(self: RenderContent, kindId: Guid, factoryKind: str, childSlotName: str) -> bool
        
            Override this method to restrict the type of acceptable child content.
                    The default 
             implementation of this method just returns true.
        
            Returns: Return true only if content with the specified kindId can be  accepted
                    as a child 
             in the specified child slot.
        """
        pass

    @staticmethod
    def LoadFromFile(filename):
        """
        LoadFromFile(filename: str) -> RenderContent
        
            Loads content from a library file.  Does not add the content to the persistent content list.
           
                      Use AddPersistantContent to add it to the list.
        
        
            filename: full path to the file to be loaded.
            Returns: The loaded content or null if an error occurred.
        """
        pass

    def ModifyRenderContentStyles(self, *args): #cannot find CLR method
        """ ModifyRenderContentStyles(self: RenderContent, stylesToAdd: RenderContentStyles, stylesToRemove: RenderContentStyles) """
        pass

    def OnAddUserInterfaceSections(self, *args): #cannot find CLR method
        """
        OnAddUserInterfaceSections(self: RenderContent)
            Override to provide UI sections to display in the editor.
        """
        pass

    def OnGetDefaultsInteractive(self, *args): #cannot find CLR method
        """
        OnGetDefaultsInteractive(self: RenderContent, parentWindowHandle: IntPtr) -> bool
        
            Override this method to prompt user for information necessary to
                    create a new 
             content object.  For example, if you are created a
                    textured material you may prompt 
             the user for a bitmap file name
                    prior to creating the textured material.
        
            Returns: If true is returned the content is created otherwise the creation
                    is aborted.
        """
        pass

    def OpenInEditor(self):
        """
        OpenInEditor(self: RenderContent) -> bool
        
            Call this method to open the content in the relevant thumbnail editor
                    and select it 
             for editing by the user. The content must be in the
                    document or the call will fail.
        
            Returns: Returns true on success or false on error.
        """
        pass

    def OpenInModalEditor(self):
        """
        OpenInModalEditor(self: RenderContent) -> bool
        
            Call this method to open the content in the a modal version of the editor.
                    The 
             content must be in the document or the call will fail.
        
            Returns: Returns true on success or false on error.
        """
        pass

    def ParamNameFromChildSlotName(self, childSlotName):
        """
        ParamNameFromChildSlotName(self: RenderContent, childSlotName: str) -> str
        
            A "child slot" is the specific "slot" that a child (usually a texture) occupies.
                    
             This is generally the "use" of the child - in other words, the thing the child
                    
             operates on.  Some examples are "color", "transparency".
        
        
            childSlotName: The named of the child slot to receive the parameter name for.
            Returns: The default behaviour for these functions is to return the input string.  Sub-classes may (in 
             the future) override these functions to provide different mappings.
        """
        pass

    @staticmethod
    def RegisterContent(*__args):
        """
        RegisterContent(assembly: Assembly, pluginId: Guid) -> Array[Type]
        
            Call RegisterContent in your plug-in's OnLoad function in order to register all of the
                 
                custom RenderContent classes in your assembly.
        
        
            assembly: Assembly where custom content is defined, this may be a plug-in assembly
                    or another 
             assembly referenced by the plug-in.
        
            pluginId: Parent plug-in for this assembly.
            Returns: array of render content types registered on success. null on error.
        RegisterContent(plugin: PlugIn) -> Array[Type]
        
            Call RegisterContent in your plug-in's OnLoad function in order to register all of the
                 
                custom RenderContent classes in your assembly.
        
            Returns: array of render content types registered on success. null on error.
        """
        pass

    def SetChild(self, renderContent, childSlotName, changeContexts):
        """ SetChild(self: RenderContent, renderContent: RenderContent, childSlotName: str, changeContexts: ChangeContexts) -> bool """
        pass

    def SetChildSlotAmount(self, childSlotName, amount, cc):
        """ SetChildSlotAmount(self: RenderContent, childSlotName: str, amount: float, cc: ChangeContexts) """
        pass

    def SetChildSlotOn(self, childSlotName, bOn, cc):
        """ SetChildSlotOn(self: RenderContent, childSlotName: str, bOn: bool, cc: ChangeContexts) """
        pass

    def SetChildSlotParameter(self, parameterName, childSlotName, value, sc):
        """ SetChildSlotParameter(self: RenderContent, parameterName: str, childSlotName: str, value: object, sc: ExtraRequirementsSetContexts) -> bool """
        pass

    def SetParameter(self, parameterName, value, changeContexts):
        """ SetParameter(self: RenderContent, parameterName: str, value: object, changeContexts: ChangeContexts) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ChildSlotName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChildSlotName(self: RenderContent) -> str

Set: ChildSlotName(self: RenderContent) = value
"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the document this content belongs to or null if the content has not
            yet been added to a document.  This will be null when content is
            generated for browsers or preview generation.

Get: Document(self: RenderContent) -> RhinoDoc

"""

    Fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rhino.Render.Fields FieldDictionary which provides access to setting
            and retrieving field values.

Get: Fields(self: RenderContent) -> FieldDictionary

"""

    FilesToEmbed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string array of full paths to files used by the content that may be
            embedded in .3dm files and library files (.rmtl, .renv, .rtex). The
            default implementation returns an empty string list. Override this to
            return the file name or file names used by your content. This is
            typically used by textures that reference files containing the texture
            imagery.

Get: FilesToEmbed(self: RenderContent) -> IEnumerable[str]

"""

    Hidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if the content has the hidden flag set.

Get: Hidden(self: RenderContent) -> bool

Set: Hidden(self: RenderContent) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Instance identifier for this content.

Get: Id(self: RenderContent) -> Guid

Set: Id(self: RenderContent) = value
"""

    IsLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set this property to true prior to adding content to the document to
            lock the content browser editing UI methods.  Setting this to true will
            keep the browser from allowing things like deleting, renaming or
            changing content.  This is useful for custom child content that you
            want to be editable but persistent.  Setting this after adding content
            to the document will cause an exception to be thrown.

Get: IsLocked(self: RenderContent) -> bool

Set: IsLocked(self: RenderContent) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Instance name for this content.

Get: Name(self: RenderContent) -> str

Set: Name(self: RenderContent) = value
"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Notes for this content.

Get: Notes(self: RenderContent) -> str

Set: Notes(self: RenderContent) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the top content in this parent/child chain.

Get: Parent(self: RenderContent) -> RenderContent

"""

    TopLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this content has no parent, false if it is the child of another content.

Get: TopLevel(self: RenderContent) -> bool

"""

    TopLevelParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the top content in this parent/child chain.

Get: TopLevelParent(self: RenderContent) -> RenderContent

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description for your content type.  ie.  "Procedural checker pattern"

Get: TypeDescription(self: RenderContent) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name for your content type.  ie. "My .net Texture"

Get: TypeName(self: RenderContent) -> str

"""


    ChangeContexts = None
    ContentAdded = None
    ContentChanged = None
    ContentDeleting = None
    ContentFieldChanged = None
    ContentRenamed = None
    ContentReplaced = None
    ContentReplacing = None
    ContentUpdatePreview = None
    ExtraRequirementsSetContexts = None
    MatchDataResult = None
    ShowContentChooserFlags = None


class RenderContentEventArgs(EventArgs):
    # no doc
    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Content(self: RenderContentEventArgs) -> RenderContent

"""



class RenderContentChangedEventArgs(RenderContentEventArgs):
    # no doc
    ChangeContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChangeContext(self: RenderContentChangedEventArgs) -> ChangeContexts

"""



class RenderContentFieldChangedEventArgs(RenderContentChangedEventArgs):
    # no doc
    FieldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldName(self: RenderContentFieldChangedEventArgs) -> str

"""



class RenderContentKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines constant values for all render content kinds, such as material,
                environment or texture.
    
    enum (flags) RenderContentKind, values: Environment (2), Material (1), None (0), Texture (4)
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

    Environment = None
    Material = None
    None = None
    Texture = None
    value__ = None


class RenderContentSerializer(object):
    """
    Used to import and export custom render content types such as
                materials, environments and textures.  You must override
                RenderPlugIn.RenderContentSerializers() and return an array of
                derived RenderContentSerializer class types to add to the content
                browsers.
    """
    def Read(self, pathToFile):
        """
        Read(self: RenderContentSerializer, pathToFile: str) -> RenderContent
        
            Called to when importing a file, file should be parsed and converted to
                    a valid 
             RenderContent object.
        
        
            pathToFile: Full path of the file to load.
            Returns: Returns a valid RenderContent object such as RenderMaterial if the file
                    was 
             successfully parsed otherwise returns null.
        """
        pass

    def Write(self, pathToFile, renderContent, previewArgs):
        """
        Write(self: RenderContentSerializer, pathToFile: str, renderContent: RenderContent, previewArgs: CreatePreviewEventArgs) -> bool
        
            Called to save a custom RenderContent object as an external file.
        
            pathToFile: Full path of file to write
            renderContent: Render content to save
            previewArgs: Parameters used to generate a preview image which may be embedded in
                    the exported 
             file.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, fileExtension: str, contentKind: RenderContentKind, canRead: bool, canWrite: bool) """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true then the file type can be imported and will be included in the
            file open box when importing the specified render content type.

Get: CanRead(self: RenderContentSerializer) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true then the file type can be exported and will be included in the
            file save box when exporting the specified render content type.

Get: CanWrite(self: RenderContentSerializer) -> bool

"""

    ContentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of content created when importing or exporting this file type.

Get: ContentType(self: RenderContentSerializer) -> RenderContentKind

"""

    EnglishDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """English string describing this plug-in

Get: EnglishDescription(self: RenderContentSerializer) -> str

"""

    FileExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File extension associated with this serialize object

Get: FileExtension(self: RenderContentSerializer) -> str

"""

    LocalDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Localized plug-in description

Get: LocalDescription(self: RenderContentSerializer) -> str

"""



class RenderContentStyles(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) RenderContentStyles, values: Adjustment (128), Fields (256), GraphDisplay (32), LocalTextureMapping (16), ModalEditing (512), None (0), PreviewCache (4), ProgressivePreview (8), QuickPreview (2), SharedUI (64), TextureSummary (1) """
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

    Adjustment = None
    Fields = None
    GraphDisplay = None
    LocalTextureMapping = None
    ModalEditing = None
    None = None
    PreviewCache = None
    ProgressivePreview = None
    QuickPreview = None
    SharedUI = None
    TextureSummary = None
    value__ = None


class RenderEndEventArgs(EventArgs):
    """
    Contains information about why OnRenderEnd was called
    
    RenderEndEventArgs()
    """

class RenderEnvironment(RenderContent, IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: RenderContent, disposing: bool) """
        pass

    def ModifyRenderContentStyles(self, *args): #cannot find CLR method
        """ ModifyRenderContentStyles(self: RenderContent, stylesToAdd: RenderContentStyles, stylesToRemove: RenderContentStyles) """
        pass

    @staticmethod
    def NewBasicEnvironment(environment):
        """
        NewBasicEnvironment(environment: SimulatedEnvironment) -> RenderEnvironment
        
            Constructs a new Rhino.Render.RenderEnvironment from a Rhino.Render.SimulatedEnvironment.
        
            environment: The environment to create the basic environment from.
            Returns: A new basic environment.
        """
        pass

    def OnAddUserInterfaceSections(self, *args): #cannot find CLR method
        """
        OnAddUserInterfaceSections(self: RenderContent)
            Override to provide UI sections to display in the editor.
        """
        pass

    def OnGetDefaultsInteractive(self, *args): #cannot find CLR method
        """
        OnGetDefaultsInteractive(self: RenderContent, parentWindowHandle: IntPtr) -> bool
        
            Override this method to prompt user for information necessary to
                    create a new 
             content object.  For example, if you are created a
                    textured material you may prompt 
             the user for a bitmap file name
                    prior to creating the textured material.
        
            Returns: If true is returned the content is created otherwise the creation
                    is aborted.
        """
        pass

    def SimulateEnvironment(self, simualation, isForDataOnly):
        """ SimulateEnvironment(self: RenderEnvironment, simualation: SimulatedEnvironment, isForDataOnly: bool) -> SimulatedEnvironment """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class RenderEnvironmentTable(object, IEnumerable[RenderEnvironment], IEnumerable, IRhinoTable[RenderEnvironment]):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: RenderEnvironmentTable) -> IEnumerator[RenderEnvironment] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[RenderEnvironment](enumerable: IEnumerable[RenderEnvironment], value: RenderEnvironment) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: RenderEnvironmentTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: RenderEnvironmentTable) -> RhinoDoc

"""



class RenderMaterial(RenderContent, IDisposable):
    # no doc
    @staticmethod
    def CreateBasicMaterial(material):
        """
        CreateBasicMaterial(material: Material) -> RenderMaterial
        
            Constructs a new basic material from a Rhino.DocObjects.MaterialMaterial.
        
            material: (optional)The material to create the basic material from.
            Returns: A new basic material.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RenderContent, disposing: bool) """
        pass

    def ModifyRenderContentStyles(self, *args): #cannot find CLR method
        """ ModifyRenderContentStyles(self: RenderContent, stylesToAdd: RenderContentStyles, stylesToRemove: RenderContentStyles) """
        pass

    def OnAddUserInterfaceSections(self, *args): #cannot find CLR method
        """
        OnAddUserInterfaceSections(self: RenderContent)
            Override to provide UI sections to display in the editor.
        """
        pass

    def OnGetDefaultsInteractive(self, *args): #cannot find CLR method
        """
        OnGetDefaultsInteractive(self: RenderContent, parentWindowHandle: IntPtr) -> bool
        
            Override this method to prompt user for information necessary to
                    create a new 
             content object.  For example, if you are created a
                    textured material you may prompt 
             the user for a bitmap file name
                    prior to creating the textured material.
        
            Returns: If true is returned the content is created otherwise the creation
                    is aborted.
        """
        pass

    def SimulateMaterial(self, simulation, isForDataOnly):
        """
        SimulateMaterial(self: RenderMaterial, simulation: Material, isForDataOnly: bool) -> Material
        
            Override this function to provide a Rhino.DocObjects.Material definition for this material
             
                    to be used by other rendering engines including the display.
        
        
            simulation: Set the properties of the input basic material to provide the simulation for this material.
            isForDataOnly: Called when only asking for a hash - don't write any textures to the disk - just provide the 
             filenames they will get.
        """
        pass

    def TextureChildSlotName(self, slot):
        """ TextureChildSlotName(self: RenderMaterial, slot: StandardChildSlots) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultPreviewBackgroundType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set or get the default scene background for the image that appears in
            preview panes

Get: DefaultPreviewBackgroundType(self: RenderMaterial) -> PreviewBackgroundType

Set: DefaultPreviewBackgroundType(self: RenderMaterial) = value
"""

    DefaultPreviewGeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set or get the default geometry that appears in preview panes

Get: DefaultPreviewGeometryType(self: RenderMaterial) -> PreviewGeometryType

Set: DefaultPreviewGeometryType(self: RenderMaterial) = value
"""

    DefaultPreviewSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default preview geometry size

Get: DefaultPreviewSize(self: RenderMaterial) -> float

Set: DefaultPreviewSize(self: RenderMaterial) = value
"""


    BasicMaterialParameterNames = None
    PreviewBackgroundType = None
    PreviewGeometryType = None
    StandardChildSlots = None


class RenderMaterialTable(object, IEnumerable[RenderMaterial], IEnumerable, IRhinoTable[RenderMaterial]):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: RenderMaterialTable) -> IEnumerator[RenderMaterial] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[RenderMaterial](enumerable: IEnumerable[RenderMaterial], value: RenderMaterial) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: RenderMaterialTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: RenderMaterialTable) -> RhinoDoc

"""



class RenderPanels(object):
    """ This class is used to extend the standard Render user interface """
    @staticmethod
    def FromRenderSessionId(plugIn, panelType, renderSessionId):
        """
        FromRenderSessionId(plugIn: PlugIn, panelType: Type, renderSessionId: Guid) -> object
        
            Get the instance of a render panel associated with a specific render
                    session, this 
             is useful when it is necessary to update a control from a
                    
             Rhino.Render.RenderPipeline
        
        
            plugIn: The plug-in that registered the custom user interface
            panelType: The type of panel to return
            renderSessionId: The Rhino.Render.RenderPipeline.RenderSessionId of a specific render
                    session.
            Returns: Returns the custom panel object if found; otherwise null is returned.
        """
        pass

    def RegisterPanel(self, plugin, renderPanelType, panelType, caption, alwaysShow, initialShow):
        """
        RegisterPanel(self: RenderPanels, plugin: PlugIn, renderPanelType: RenderPanelType, panelType: Type, caption: str, alwaysShow: bool, initialShow: bool)
            Register custom render user interface with Rhino.  This should only be
                    done in 
             Rhino.PlugIns.RenderPlugIn.RegisterRenderPanels(Rhino.Render.RenderPanels).  Panels
                    
             registered after Rhino.PlugIns.RenderPlugIn.RegisterRenderPanels(Rhino.Render.RenderPanels) is 
             called
                    will be ignored.
        
        
            plugin: The plug-in providing the custom user interface
            renderPanelType: See Rhino.Render.RenderPanelType for supported user interface types.
            panelType: The type of object to be created and added to the render container.
            caption: The caption for the custom user interface.
            alwaysShow: If true the custom user interface will always be visible, if false then
                    it may be 
             hidden or shown as requested by the user.
        
            initialShow: Initial visibility state of the custom user interface control.
        """
        pass


class RenderPanelType(Enum, IComparable, IFormattable, IConvertible):
    """
    Contains the custom user interfaces that may be provided
    
    enum RenderPanelType, values: RenderWindow (0)
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

    RenderWindow = None
    value__ = None


class RenderPipeline(object, IDisposable):
    """
    Provides facilities to a render plug-in for integrating with the standard
                Rhino render window. Also adds helper functions for processing a render
                scene. This is the suggested class to use when integrating a renderer with
                Rhino and maintaining a "standard" user interface that users will expect.
    """
    def AddLightToScene(self, *args): #cannot find CLR method
        """ AddLightToScene(self: RenderPipeline, light: LightObject) -> bool """
        pass

    def AddRenderMeshToScene(self, *args): #cannot find CLR method
        """ AddRenderMeshToScene(self: RenderPipeline, obj: RhinoObject, material: Material, mesh: Mesh) -> bool """
        pass

    def CloseWindow(self):
        """
        CloseWindow(self: RenderPipeline) -> bool
        
            Closes the render window associated with this render instance.
            Returns: Return true if successful or false if not.
        """
        pass

    def CommandResult(self):
        """ CommandResult(self: RenderPipeline) -> Result """
        pass

    def ContinueModal(self, *args): #cannot find CLR method
        """
        ContinueModal(self: RenderPipeline) -> bool
        
            Frequently called during a rendering by the frame work in order to
                    determine if the 
             rendering should continue.
        
            Returns: Returns true if the rendering should continue.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RenderPipeline) """
        pass

    def GetRenderWindow(self):
        """ GetRenderWindow(self: RenderPipeline) -> RenderWindow """
        pass

    def IgnoreRhinoObject(self, *args): #cannot find CLR method
        """ IgnoreRhinoObject(self: RenderPipeline, obj: RhinoObject) -> bool """
        pass

    def NeedToProcessGeometryTable(self, *args): #cannot find CLR method
        """ NeedToProcessGeometryTable(self: RenderPipeline) -> bool """
        pass

    def NeedToProcessLightTable(self, *args): #cannot find CLR method
        """ NeedToProcessLightTable(self: RenderPipeline) -> bool """
        pass

    def OnRenderBegin(self, *args): #cannot find CLR method
        """
        OnRenderBegin(self: RenderPipeline) -> bool
        
            Called by the framework when it is time to start rendering, the render window will be created at 
             this point and it is safe to start
        """
        pass

    def OnRenderEnd(self, *args): #cannot find CLR method
        """
        OnRenderEnd(self: RenderPipeline, e: RenderEndEventArgs)
            Called by the framework when the user closes the render window or clicks
                    on the 
             stop button in the render window.
        """
        pass

    def OnRenderWindowBegin(self, *args): #cannot find CLR method
        """ OnRenderWindowBegin(self: RenderPipeline, view: RhinoView, rectangle: Rectangle) -> bool """
        pass

    def Render(self):
        """
        Render(self: RenderPipeline) -> RenderReturnCode
        
            Call this function to render the scene normally. The function returns when rendering is complete 
             (or cancelled).
        
            Returns: A code that explains how rendering completed.
        """
        pass

    def RenderEnterModalLoop(self, *args): #cannot find CLR method
        """ RenderEnterModalLoop(self: RenderPipeline) -> bool """
        pass

    def RenderExitModalLoop(self, *args): #cannot find CLR method
        """ RenderExitModalLoop(self: RenderPipeline) -> bool """
        pass

    def RenderPreCreateWindow(self, *args): #cannot find CLR method
        """ RenderPreCreateWindow(self: RenderPipeline) -> bool """
        pass

    def RenderSceneWithNoMeshes(self, *args): #cannot find CLR method
        """ RenderSceneWithNoMeshes(self: RenderPipeline) -> bool """
        pass

    @staticmethod
    def RenderSize():
        """
        RenderSize() -> Size
        
            Gets the render size as specified in the ON_3dmRenderSettings. Will automatically return the 
             correct size based on the ActiveView or custom settings.
        
            Returns: The render size.
        """
        pass

    def RenderWindow(self, view, rect, inWindow):
        """
        RenderWindow(self: RenderPipeline, view: RhinoView, rect: Rectangle, inWindow: bool) -> RenderReturnCode
        
            Call this function to render the scene in a view window. The function returns when rendering is 
             complete (or cancelled).
        
        
            view: the view that the user selected a rectangle in.
            rect: rectangle that the user selected.
            inWindow: true to render directly into the view window.
            Returns: A code that explains how rendering completed.
        """
        pass

    def SaveImage(self, fileName):
        """
        SaveImage(self: RenderPipeline, fileName: str) -> bool
        
            Saves the rendered image to a file.
        
            fileName: the full path to the file name to save to. If null or empty a file
                    dialog will be 
             displayed prompting the user for a save file name.
        
            Returns: Returns true if a file was written or false if a file dialog was
                    canceled or the 
             file was not written.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, doc: RhinoDoc, mode: RunMode, plugin: PlugIn, sizeRendering: Size, caption: str, channels: StandardChannels, reuseRenderWindow: bool, clearLastRendering: bool) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ConfirmationSeconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets the number of seconds that need to elapse during rendering before the user is asked if the rendered image should be saved.

Set: ConfirmationSeconds(self: RenderPipeline) = value
"""

    PlugIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlugIn(self: RenderPipeline) -> PlugIn

"""

    RenderSessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Id associated with this render session, this is useful when
            looking up Rhino.Render.RenderPanels.

Get: RenderSessionId(self: RenderPipeline) -> Guid

"""


    RenderReturnCode = None


class RenderPrimitive(object, IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: RenderPrimitive) """
        pass

    def Mesh(self):
        """
        Mesh(self: RenderPrimitive) -> Mesh
        
            Returns the mesh associated with the object, this will mesh primitives
                    and always 
             return a mesh.
        """
        pass

    def TryGetBox(self, box):
        """
        TryGetBox(self: RenderPrimitive) -> (bool, Box)
        
            Call this method to get a Rhino.Geometry.Box primitive for this mesh.  If this
                    
             meshes Rhino.Render.RenderPrimitive.PrimitiveType is not a Rhino.Render.RenderPrimitiveType.Box
        
                         then the box parameter is set to Rhino.Geometry.Box.Empty.
        
            Returns: Returns true if Rhino.Render.RenderPrimitive.PrimitiveType is 
             Rhino.Render.RenderPrimitiveType.Box and
                    the box parameter was initialized 
             otherwise returns false.
        """
        pass

    def TryGetCone(self, cone, truncation):
        """
        TryGetCone(self: RenderPrimitive) -> (bool, Cone, Plane)
        
            Call this method to get a Rhino.Geometry.Cone primitive for this mesh.  If this
                    
             meshes Rhino.Render.RenderPrimitive.PrimitiveType is not a Rhino.Render.RenderPrimitiveType.Cone
             
                    then the cone parameter is set to Rhino.Geometry.Cone.Unset and the truncation
            
                     parameter is set to Rhino.Geometry.Plane.Unset.
        
            Returns: Returns true if Rhino.Render.RenderPrimitive.PrimitiveType is 
             Rhino.Render.RenderPrimitiveType.Cone and
                    the cone and truncation parameters were 
             initialized otherwise returns false.
        """
        pass

    def TryGetPlane(self, plane):
        """
        TryGetPlane(self: RenderPrimitive) -> (bool, PlaneSurface)
        
            Call this method to get a Rhino.Geometry.Plane primitive for this mesh.  If this
                    
             meshes Rhino.Render.RenderPrimitive.PrimitiveType is not a 
             Rhino.Render.RenderPrimitiveType.Plane
                    then the plane parameter is set to null.
        
            Returns: Returns true if Rhino.Render.RenderPrimitive.PrimitiveType is 
             Rhino.Render.RenderPrimitiveType.Plane and
                    the plane parameter was initialized 
             otherwise returns false.
        """
        pass

    def TryGetSphere(self, sphere):
        """
        TryGetSphere(self: RenderPrimitive) -> (bool, Sphere)
        
            Call this method to get a sphere primitive for this mesh.  If this
                    meshes 
             Rhino.Render.RenderPrimitive.PrimitiveType is not a Rhino.Render.RenderPrimitiveType.Sphere
            
                     then the sphere parameter is set to Rhino.Geometry.Sphere.Unset.
        
            Returns: Returns true if Rhino.Render.RenderPrimitive.PrimitiveType is 
             Rhino.Render.RenderPrimitiveType.Sphere and
                    the sphere parameter was initialized 
             otherwise returns false.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bounding box for this primitive.

Get: BoundingBox(self: RenderPrimitive) -> BoundingBox

"""

    HasRenderMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property will be true if this mesh has a Rhino.Render.RenderPrimitive.RenderMaterial associated with
            it or false if there is a Rhino.Render.RenderPrimitive.Material.

Get: HasRenderMaterial(self: RenderPrimitive) -> bool

"""

    InstanceTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Instance reference transform or Identity if not an instance reference.

Get: InstanceTransform(self: RenderPrimitive) -> Transform

"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Rhino.Render.RenderPrimitive.Materialassociated with this mesh or null if the
            Rhino.Render.RenderPrimitive property has a value.

Get: Material(self: RenderPrimitive) -> Material

"""

    PrimitiveType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Call this before extracting meshes if you support render primitives to
            get the Rhino.Render.RenderPrimitiveType of this mesh then call the
            associated Rhino.Render.RenderPrimitive.TryGetSphere(Rhino.Geometry.Sphere@), Rhino.Render.RenderPrimitive.TryGetPlane(Rhino.Geometry.PlaneSurface@), Rhino.Render.RenderPrimitive.TryGetCone(Rhino.Geometry.Cone@,Rhino.Geometry.Plane@), or
            Rhino.Render.RenderPrimitive.TryGetBox(Rhino.Geometry.Box@) method.  Calling the Rhino.Render.RenderPrimitive.Mesh property
            will mesh the primitive and return a mesh always.

Get: PrimitiveType(self: RenderPrimitive) -> RenderPrimitiveType

"""

    RenderMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Rhino.Render.RenderPrimitive.RenderMaterial associated with this mesh or null if there is not one.

Get: RenderMaterial(self: RenderPrimitive) -> RenderMaterial

"""

    RhinoObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Rhino object associated with this render primitive.

Get: RhinoObject(self: RenderPrimitive) -> RhinoObject

"""



class RenderPrimitiveList(object, IDisposable):
    # no doc
    def Add(self, *__args):
        """
        Add(self: RenderPrimitiveList, plane: PlaneSurface, material: RenderMaterial)
            Add primitive plane and material.
        
            plane: Plane to add.
            material: Material to add, may be null if not needed.
        Add(self: RenderPrimitiveList, box: Box, material: RenderMaterial)
            Add primitive box and material.
        
            box: Box to add.
            material: Material to add, may be null if not needed.
        Add(self: RenderPrimitiveList, cone: Cone, truncation: Plane, material: RenderMaterial)
            Add primitive cone and material.
        
            cone: Cone to add.
            truncation: The plane used to cut the cone (the non-apex end is kept). Should be
                    equal to 
             cone.plane if not truncated.
        
            material: Material to add, may be null if not needed.
        Add(self: RenderPrimitiveList, mesh: Mesh, material: RenderMaterial)
            Add mesh and material.
        
            mesh: Mesh to add.
            material: Material to add, may be null if not needed.
        Add(self: RenderPrimitiveList, sphere: Sphere, material: RenderMaterial)
            Add primitive sphere and material.
        
            sphere: Sphere to add.
            material: Material to add, may be null if not needed.
        """
        pass

    def Clear(self):
        """
        Clear(self: RenderPrimitiveList)
            Remove all primitives from this list
        """
        pass

    def ConvertMeshesToTriangles(self):
        """
        ConvertMeshesToTriangles(self: RenderPrimitiveList)
            Convert mesh quad faces to triangle faces.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RenderPrimitiveList) """
        pass

    def Material(self, index):
        """
        Material(self: RenderPrimitiveList, index: int) -> RenderMaterial
        
            Call this method to get the render material associated with the mesh at
                    the 
             specified index.  Will return null if there is no
                    material associated with the 
             requested mesh.
        
        
            index: The zero based index of the item in the list.  Valid values are greater
                    than or 
             equal to 0 and less than Count.
        
            Returns: If there is a render material associated at the requested index then
                    the material 
             is returned otherwise null is returned.
        """
        pass

    def Mesh(self, index):
        """
        Mesh(self: RenderPrimitiveList, index: int) -> Mesh
        
            Get the mesh for the primitive at the specified index. If the item at
                    this index is 
             a primitive type other than a mesh then it mesh
                    representation is returned.
        
        
            index: The zero based index of the item in the list.  Valid values are greater
                    than or 
             equal to 0 and less than Count.
        
            Returns: Returns the mesh for the primitive at the specified index. If the item
                    at this 
             index is a primitive type other than a mesh then it mesh
                    representation is 
             returned.
        """
        pass

    def PrimitiveType(self, index):
        """
        PrimitiveType(self: RenderPrimitiveList, index: int) -> RenderPrimitiveType
        
            Type of primitive object at this index.
        
            index: The zero based index of the item in the list.  Valid values are greater
                    than or 
             equal to 0 and less than Count.
        
            Returns: Primitive type of the item at this index.
        """
        pass

    def ToMaterialArray(self):
        """
        ToMaterialArray(self: RenderPrimitiveList) -> Array[RenderMaterial]
        
            Call this method to see if there are any RenderMaterials associated
                    with the 
             meshes.  Each primitive can optionally have a RenderMaterial
                    associated with it, if 
             the RenderMaterial is null then check for a
                    RhinoObject.RenderMaterial.
        
            Returns: Return an array that of the same size as the ToMeshArray() containing
                    the 
             RenderMaterial associated with the mesh, may contain null entries
                    if there is no 
             RenderMaterial associated with the custom mesh.
        """
        pass

    def ToMeshArray(self):
        """
        ToMeshArray(self: RenderPrimitiveList) -> Array[Mesh]
        
            Call this method to get a array of meshes, all primitives will get
                    meshed and the 
             meshes will get included in the returned array.
        
            Returns: Return an array of meshes from this list, this will convert all
                    primitives to 
             meshes.
        """
        pass

    def TryGetBox(self, index, box):
        """
        TryGetBox(self: RenderPrimitiveList, index: int) -> (bool, Box)
        
            Call this method to get a box at the specified index.
        
            index: The zero based index of the item in the list.  Valid values are greater
                    than or 
             equal to 0 and less than Count.
        
            Returns: Return true if the index is in range and the primitive at the requested
                    index is a 
             box otherwise returns false.
        """
        pass

    def TryGetCone(self, index, cone, truncation):
        """
        TryGetCone(self: RenderPrimitiveList, index: int) -> (bool, Cone, Plane)
        
            Call this method to get a box at the specified index.
        
            index: The zero based index of the item in the list.  Valid values are greater
                    than or 
             equal to 0 and less than Count.
        
            Returns: Return true if the index is in range and the primitive at the requested
                    index is a 
             box otherwise returns false.
        """
        pass

    def TryGetPlane(self, index, plane):
        """
        TryGetPlane(self: RenderPrimitiveList, index: int) -> (bool, PlaneSurface)
        
            Call this method to get a box at the specified index.
        
            index: The zero based index of the item in the list.  Valid values are greater
                    than or 
             equal to 0 and less than Count.
        
            Returns: Return true if the index is in range and the primitive at the requested
                    index is a 
             plane otherwise returns false.
        """
        pass

    def TryGetSphere(self, index, sphere):
        """
        TryGetSphere(self: RenderPrimitiveList, index: int) -> (bool, Sphere)
        
            Call this method to get a box at the specified index.
        
            index: The zero based index of the item in the list.  Valid values are greater
                    than or 
             equal to 0 and less than Count.
        
            Returns: Return true if the index is in range and the primitive at the requested
                    index is a 
             box otherwise returns false.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of meshes in this list

Get: Count(self: RenderPrimitiveList) -> int

"""

    RhinoObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Rhino object associated with this list

Get: RhinoObject(self: RenderPrimitiveList) -> RhinoObject

"""

    UseObjectsMappingChannels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the texture mapping will be taken from the Rhino
            object otherwise; the texture mapping will use the texture coordinates
            on the mesh only.

Get: UseObjectsMappingChannels(self: RenderPrimitiveList) -> bool

Set: UseObjectsMappingChannels(self: RenderPrimitiveList) = value
"""



class RenderPrimitiveType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RenderPrimitiveType, values: Box (4), Cone (5), Mesh (1), None (0), Plane (3), Sphere (2) """
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

    Box = None
    Cone = None
    Mesh = None
    None = None
    Plane = None
    Sphere = None
    value__ = None


class RenderPropertyChangedEvent(EventArgs):
    """ Used by Rhino.Render object property value has changed events. """
    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional argument which may specify the property being modified.

Get: Context(self: RenderPropertyChangedEvent) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The document triggering the event.

Get: Document(self: RenderPropertyChangedEvent) -> RhinoDoc

"""



class RenderSettings(object, IDisposable):
    """
    Contains settings used in rendering.
    
    RenderSettings()
    """
    def Dispose(self):
        """
        Dispose(self: RenderSettings)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AmbientLight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ambient light color used in rendering.

Get: AmbientLight(self: RenderSettings) -> Color

Set: AmbientLight(self: RenderSettings) = value
"""

    AntialiasLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """0=none, 1=normal, 2=best.

Get: AntialiasLevel(self: RenderSettings) -> int

Set: AntialiasLevel(self: RenderSettings) = value
"""

    BackgroundColorBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the background bottom color used in rendering.

Get: BackgroundColorBottom(self: RenderSettings) -> Color

Set: BackgroundColorBottom(self: RenderSettings) = value
"""

    BackgroundColorTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the background top color used in rendering.
            Sets also the background color if a solid background color is set.

Get: BackgroundColorTop(self: RenderSettings) -> Color

Set: BackgroundColorTop(self: RenderSettings) = value
"""

    BackgroundStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How the viewport's backgroun should be filled.

Get: BackgroundStyle(self: RenderSettings) -> BackgroundStyle

Set: BackgroundStyle(self: RenderSettings) = value
"""

    DepthCue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to render using depth cues.
            These are clues to help the perception of position and orientation of objects in the image.

Get: DepthCue(self: RenderSettings) -> bool

Set: DepthCue(self: RenderSettings) = value
"""

    FlatShade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to render using flat shading.

Get: FlatShade(self: RenderSettings) -> bool

Set: FlatShade(self: RenderSettings) = value
"""

    ImageDpi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of dots/inch (dots=pixels) to use when printing and saving
            bitmaps. The default is 72.0 dots/inch.

Get: ImageDpi(self: RenderSettings) -> float

Set: ImageDpi(self: RenderSettings) = value
"""

    ImageSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating the size of the rendering result if
            UseViewportSize is set to false.  If UseViewportSize is set to true,
            then this value is ignored.

Get: ImageSize(self: RenderSettings) -> Size

Set: ImageSize(self: RenderSettings) = value
"""

    ImageUnitSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """unit system to use when converting image pixel size and dpi information
            into a print size.  Default = inches

Get: ImageUnitSystem(self: RenderSettings) -> UnitSystem

Set: ImageUnitSystem(self: RenderSettings) = value
"""

    RenderAnnotations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to instruct the rendering engine to show annotations,
            such as linear dimensions or angular dimensions.

Get: RenderAnnotations(self: RenderSettings) -> bool

Set: RenderAnnotations(self: RenderSettings) = value
"""

    RenderBackfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to render back faces.

Get: RenderBackfaces(self: RenderSettings) -> bool

Set: RenderBackfaces(self: RenderSettings) = value
"""

    RenderCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to instruct the rendering engine to show curves.

Get: RenderCurves(self: RenderSettings) -> bool

Set: RenderCurves(self: RenderSettings) = value
"""

    RenderIsoparams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to instruct the rendering engine to show isocurves.

Get: RenderIsoparams(self: RenderSettings) -> bool

Set: RenderIsoparams(self: RenderSettings) = value
"""

    RenderMeshEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to instruct the rendering engine to show mesh edges.

Get: RenderMeshEdges(self: RenderSettings) -> bool

Set: RenderMeshEdges(self: RenderSettings) = value
"""

    RenderPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to instruct the rendering engine to show points.

Get: RenderPoints(self: RenderSettings) -> bool

Set: RenderPoints(self: RenderSettings) = value
"""

    ShadowmapLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """0=none, 1=normal, 2=best.

Get: ShadowmapLevel(self: RenderSettings) -> int

Set: ShadowmapLevel(self: RenderSettings) = value
"""

    UseHiddenLights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to render using lights that are on layers that are off.

Get: UseHiddenLights(self: RenderSettings) -> bool

Set: UseHiddenLights(self: RenderSettings) = value
"""

    UseViewportSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to use the resolution of the
            viewport being rendered or ImageSize when rendering

Get: UseViewportSize(self: RenderSettings) -> bool

Set: UseViewportSize(self: RenderSettings) = value
"""



class RenderTabs(object):
    # no doc
    @staticmethod
    def FromRenderSessionId(plugIn, tabType, renderSessionId):
        """
        FromRenderSessionId(plugIn: PlugIn, tabType: Type, renderSessionId: Guid) -> object
        
            Get the instance of a render tab associated with a specific render
                    session, this is 
             useful when it is necessary to update a control from a
                    Rhino.Render.RenderPipeline
        
        
            plugIn: The plug-in that registered the custom user interface
            tabType: The type of tab to return
            renderSessionId: The Rhino.Render.RenderPipeline.RenderSessionId of a specific render
                    session.
            Returns: Returns the custom tab object if found; otherwise null is returned.
        """
        pass

    def RegisterTab(self, plugin, tabType, caption, icon):
        """
        RegisterTab(self: RenderTabs, plugin: PlugIn, tabType: Type, caption: str, icon: Icon)
            Register custom render user interface with Rhino.  This should only be
                    done in 
             Rhino.PlugIns.RenderPlugIn.RegisterRenderPanels(Rhino.Render.RenderPanels).  Panels
                    
             registered after Rhino.PlugIns.RenderPlugIn.RegisterRenderPanels(Rhino.Render.RenderPanels) is 
             called
                    will be ignored.
        
        
            plugin: The plug-in providing the custom user interface
            tabType: The type of object to be created and added to the render container.
            caption: The caption for the custom user interface.
        """
        pass

    @staticmethod
    def SessionIdFromTab(tab):
        """
        SessionIdFromTab(tab: object) -> Guid
        
            Get the session Id that created the specified tab object.
        """
        pass


class RenderTexture(RenderContent, IDisposable):
    # no doc
    def CreateEvaluator(self):
        """
        CreateEvaluator(self: RenderTexture) -> TextureEvaluator
        
            Constructs a texture evaluator. This is an independent lightweight object
                    capable 
             of evaluating texture color throughout uvw space. May be called
                    from within a 
             rendering shade pipeline.
        
            Returns: A texture evaluator instance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RenderContent, disposing: bool) """
        pass

    def GetDisplayInViewport(self):
        """ GetDisplayInViewport(self: RenderTexture) -> bool """
        pass

    def GetEnvironmentMappingMode(self):
        """ GetEnvironmentMappingMode(self: RenderTexture) -> TextureEnvironmentMappingMode """
        pass

    @staticmethod
    def GetEnvironmentMappingProjection(mode, reflectionVector, u, v):
        """ GetEnvironmentMappingProjection(mode: TextureEnvironmentMappingMode, reflectionVector: Vector3d) -> (bool, Single, Single) """
        pass

    def GetInternalEnvironmentMappingMode(self):
        """ GetInternalEnvironmentMappingMode(self: RenderTexture) -> TextureEnvironmentMappingMode """
        pass

    def GetMappingChannel(self):
        """ GetMappingChannel(self: RenderTexture) -> int """
        pass

    def GetOffset(self):
        """
        GetOffset(self: RenderTexture) -> Vector3d
        
            Get offset value across UVW space. If the projection type is WCS or
                    other type 
             specified in model units, then this is the offset in meters.
        """
        pass

    def GetOffsetLocked(self):
        """ GetOffsetLocked(self: RenderTexture) -> bool """
        pass

    def GetPreviewIn3D(self):
        """ GetPreviewIn3D(self: RenderTexture) -> bool """
        pass

    def GetPreviewLocalMapping(self):
        """ GetPreviewLocalMapping(self: RenderTexture) -> bool """
        pass

    def GetProjectionMode(self):
        """ GetProjectionMode(self: RenderTexture) -> TextureProjectionMode """
        pass

    def GetRepeat(self):
        """
        GetRepeat(self: RenderTexture) -> Vector3d
        
            Get repeat value across UVW space. If the projection type is WCS or
                    other type 
             specified in model units, then this is the repeat across 1
                    meter of the model.
        """
        pass

    def GetRepeatLocked(self):
        """ GetRepeatLocked(self: RenderTexture) -> bool """
        pass

    def GetRotation(self):
        """ GetRotation(self: RenderTexture) -> Vector3d """
        pass

    @staticmethod
    def GetWcsBoxMapping(worldXyz, normal):
        """ GetWcsBoxMapping(worldXyz: Point3d, normal: Vector3d) -> Point3d """
        pass

    def GetWrapType(self):
        """ GetWrapType(self: RenderTexture) -> TextureWrapType """
        pass

    def IsHdrCapable(self):
        """ IsHdrCapable(self: RenderTexture) -> bool """
        pass

    def ModifyRenderContentStyles(self, *args): #cannot find CLR method
        """ ModifyRenderContentStyles(self: RenderContent, stylesToAdd: RenderContentStyles, stylesToRemove: RenderContentStyles) """
        pass

    @staticmethod
    def NewBitmapTexture(texture):
        """
        NewBitmapTexture(texture: SimulatedTexture) -> RenderTexture
        
            Constructs a new basic texture from a SimulatedTexture.
        
            texture: The texture to create the basic texture from.
            Returns: A new render texture.
        """
        pass

    def OnAddUserInterfaceSections(self, *args): #cannot find CLR method
        """
        OnAddUserInterfaceSections(self: RenderContent)
            Override to provide UI sections to display in the editor.
        """
        pass

    def OnGetDefaultsInteractive(self, *args): #cannot find CLR method
        """
        OnGetDefaultsInteractive(self: RenderContent, parentWindowHandle: IntPtr) -> bool
        
            Override this method to prompt user for information necessary to
                    create a new 
             content object.  For example, if you are created a
                    textured material you may prompt 
             the user for a bitmap file name
                    prior to creating the textured material.
        
            Returns: If true is returned the content is created otherwise the creation
                    is aborted.
        """
        pass

    def SetDisplayInViewport(self, value, changeContext):
        """ SetDisplayInViewport(self: RenderTexture, value: bool, changeContext: ChangeContexts) """
        pass

    def SetEnvironmentMappingMode(self, value, changeContext):
        """ SetEnvironmentMappingMode(self: RenderTexture, value: TextureEnvironmentMappingMode, changeContext: ChangeContexts) """
        pass

    def SetMappingChannel(self, value, changeContext):
        """ SetMappingChannel(self: RenderTexture, value: int, changeContext: ChangeContexts) """
        pass

    def SetOffset(self, value, changeContext):
        """ SetOffset(self: RenderTexture, value: Vector3d, changeContext: ChangeContexts) """
        pass

    def SetOffsetLocked(self, value, changeContext):
        """ SetOffsetLocked(self: RenderTexture, value: bool, changeContext: ChangeContexts) """
        pass

    def SetPreviewIn3D(self, value, changeContext):
        """ SetPreviewIn3D(self: RenderTexture, value: bool, changeContext: ChangeContexts) """
        pass

    def SetPreviewLocalMapping(self, value, changeContext):
        """ SetPreviewLocalMapping(self: RenderTexture, value: bool, changeContext: ChangeContexts) """
        pass

    def SetProjectionMode(self, value, changeContext):
        """ SetProjectionMode(self: RenderTexture, value: TextureProjectionMode, changeContext: ChangeContexts) """
        pass

    def SetRepeat(self, value, changeContext):
        """ SetRepeat(self: RenderTexture, value: Vector3d, changeContext: ChangeContexts) """
        pass

    def SetRepeatLocked(self, value, changeContext):
        """ SetRepeatLocked(self: RenderTexture, value: bool, changeContext: ChangeContexts) """
        pass

    def SetRotation(self, value, changeContext):
        """ SetRotation(self: RenderTexture, value: Vector3d, changeContext: ChangeContexts) """
        pass

    def SetWrapType(self, value, changeContext):
        """ SetWrapType(self: RenderTexture, value: TextureWrapType, changeContext: ChangeContexts) """
        pass

    def SimulateTexture(self, simulation, isForDataOnly):
        """ SimulateTexture(self: RenderTexture, simulation: SimulatedTexture, isForDataOnly: bool) -> SimulatedTexture """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    LocalMappingTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the transformation that can be applied to the UVW vector to convert it
            from normalized texture space into locally mapped space (ie - with repeat,
            offset and rotation applied.)

Get: LocalMappingTransform(self: RenderTexture) -> Transform

"""



class RenderTextureTable(object, IEnumerable[RenderTexture], IEnumerable, IRhinoTable[RenderTexture]):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: RenderTextureTable) -> IEnumerator[RenderTexture] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[RenderTexture](enumerable: IEnumerable[RenderTexture], value: RenderTexture) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: RenderTextureTable) -> int

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: RenderTextureTable) -> RhinoDoc

"""



class RenderWindow(object):
    # no doc
    def AddChannel(self, channel):
        """ AddChannel(self: RenderWindow, channel: StandardChannels) -> bool """
        pass

    def AddWireframeChannel(self, doc, viewport, size, region):
        """
        AddWireframeChannel(self: RenderWindow, doc: RhinoDoc, viewport: ViewportInfo, size: Size, region: Rectangle) -> bool
        
            A wireframe channel will not be added if none of the document properties settings
                    
             indicate that one is needed. In other words, Rhino will not generate an empty wireframe channel
        
                         just for the fun of it.
        
        
            doc: The document to display
            viewport: The view to display
            size: The size of the image without clipping (ie - if you have a region, it was the
                    size 
             of the image before you cut the region out.
        
            region: The area of the rendering you want to display.  This should match the size
                    of the 
             render window itself (ie - the one set using SetSize)
        
            Returns: Returns true if the wireframe channel was successfully added.
        """
        pass

    @staticmethod
    def ChannelId(ch):
        """ ChannelId(ch: StandardChannels) -> Guid """
        pass

    @staticmethod
    def FromSessionId(sessionId):
        """ FromSessionId(sessionId: Guid) -> RenderWindow """
        pass

    def Invalidate(self):
        """
        Invalidate(self: RenderWindow)
            Invalidate the entire view window so that the pixels get painted.
        """
        pass

    def InvalidateArea(self, rect):
        """ InvalidateArea(self: RenderWindow, rect: Rectangle) """
        pass

    def OpenChannel(self, id):
        """ OpenChannel(self: RenderWindow, id: StandardChannels) -> Channel """
        pass

    def SetProgress(self, text, progress):
        """
        SetProgress(self: RenderWindow, text: str, progress: Single)
            Accepts a rendering progress value to inform the user of the rendering advances.
        
            text: The progress text.
            progress: A progress value in the domain [0.0f; 1.0f].
        """
        pass

    def SetRGBAChannelColors(self, *__args):
        """
        SetRGBAChannelColors(self: RenderWindow, rectangle: Rectangle, colors: Array[Color4f])
            Call this method to open the RenderWindow.StandardChannels.RGBA channel and set a block of color 
             values
        
        
            rectangle: rectangle.X is the horizontal pixel position of the left edge. No validation is done on this 
             value.
                      The caller is responsible for ensuring that it is within the frame buffer.
             
                    rectangle.Y is the vertical pixel position of the top edge. No validation is done 
             on this value.
                      The caller is responsible for ensuring that it is within the frame 
             buffer.
                    rectangle.Width is the width of the rectangle in pixels. No validation is 
             done on this value.
                    rectangle.Height is the height of the rectangle in pixels. No 
             validation is done on this value.
        
            colors: Array of Color4f values used to set the RenderWindow.StandardChannels.RGBA
        SetRGBAChannelColors(self: RenderWindow, size: Size, colors: Array[Color4f])
            Call this method to open the RenderWindow.StandardChannels.RGBA channel and set a block of color 
             values
        
        
            size: Size of the area to set. No validation is done on this value
            colors: Array of Color4f values used to set the RenderWindow.StandardChannels.RGBA
        """
        pass

    def SetSize(self, size):
        """ SetSize(self: RenderWindow, size: Size) """
        pass

    def Size(self):
        """ Size(self: RenderWindow) -> Size """
        pass

    SessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionId(self: RenderWindow) -> Guid

"""


    Channel = None
    Cloned = None
    StandardChannels = None


class RenderWindowClonedEventArgs(EventArgs):
    # no doc
    NewRenderWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewRenderWindow(self: RenderWindowClonedEventArgs) -> RenderWindow

"""

    NewSessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewSessionId(self: RenderWindowClonedEventArgs) -> Guid

"""

    OldRenderWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldRenderWindow(self: RenderWindowClonedEventArgs) -> RenderWindow

"""

    OldSessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldSessionId(self: RenderWindowClonedEventArgs) -> Guid

"""



class SimulatedEnvironment(object, IDisposable):
    """ SimulatedEnvironment() """
    def ConstPointer(self):
        """ ConstPointer(self: SimulatedEnvironment) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimulatedEnvironment) """
        pass

    @staticmethod
    def ProjectionFromString(projection):
        """ ProjectionFromString(projection: str) -> BackgroundProjections """
        pass

    @staticmethod
    def StringFromProjection(projection):
        """ StringFromProjection(projection: BackgroundProjections) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: SimulatedEnvironment) -> Color

Set: BackgroundColor(self: SimulatedEnvironment) = value
"""

    BackgroundImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundImage(self: SimulatedEnvironment) -> SimulatedTexture

Set: BackgroundImage(self: SimulatedEnvironment) = value
"""

    BackgroundProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundProjection(self: SimulatedEnvironment) -> BackgroundProjections

Set: BackgroundProjection(self: SimulatedEnvironment) = value
"""


    BackgroundProjections = None


class SimulatedTexture(object, IDisposable):
    """ SimulatedTexture() """
    def ConstPointer(self):
        """ ConstPointer(self: SimulatedTexture) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimulatedTexture) """
        pass

    def MetersToUnits(self, units):
        """ MetersToUnits(self: SimulatedTexture, units: float) -> float """
        pass

    def Texture(self):
        """ Texture(self: SimulatedTexture) -> Texture """
        pass

    def UnitsToMeters(self, units):
        """ UnitsToMeters(self: SimulatedTexture, units: float) -> float """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filename(self: SimulatedTexture) -> str

Set: Filename(self: SimulatedTexture) = value
"""

    Filtered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filtered(self: SimulatedTexture) -> bool

Set: Filtered(self: SimulatedTexture) = value
"""

    HasTransparentColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasTransparentColor(self: SimulatedTexture) -> bool

Set: HasTransparentColor(self: SimulatedTexture) = value
"""

    LocalMappingTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalMappingTransform(self: SimulatedTexture) -> Transform

"""

    MappingChannel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MappingChannel(self: SimulatedTexture) -> int

Set: MappingChannel(self: SimulatedTexture) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: SimulatedTexture) -> Vector2d

Set: Offset(self: SimulatedTexture) = value
"""

    OriginalFilename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalFilename(self: SimulatedTexture) -> str

"""

    ProjectionMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionMode(self: SimulatedTexture) -> ProjectionModes

Set: ProjectionMode(self: SimulatedTexture) = value
"""

    Repeat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Repeat(self: SimulatedTexture) -> Vector2d

Set: Repeat(self: SimulatedTexture) = value
"""

    Repeating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Repeating(self: SimulatedTexture) -> bool

Set: Repeating(self: SimulatedTexture) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: SimulatedTexture) -> float

Set: Rotation(self: SimulatedTexture) = value
"""

    TransparentColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransparentColor(self: SimulatedTexture) -> Color4f

Set: TransparentColor(self: SimulatedTexture) = value
"""

    TransparentColorSensitivity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransparentColorSensitivity(self: SimulatedTexture) -> float

Set: TransparentColorSensitivity(self: SimulatedTexture) = value
"""


    ProjectionModes = None


class Sun(object, IDisposable):
    """
    Represents the Sun on a little portion of Earth.
    
    Sun()
    """
    def Dispose(self):
        """ Dispose(self: Sun) """
        pass

    def GetDateTime(self, kind):
        """ GetDateTime(self: Sun, kind: DateTimeKind) -> DateTime """
        pass

    def SetPosition(self, *__args):
        """
        SetPosition(self: Sun, when: DateTime, latitudeDegrees: float, longitudeDegrees: float)
            Sets position of the sun based on physical location and time.
        
            when: A datetime instance.
                    If the date System.DateTime.KindKind is 
             System.DateTimeKind.LocalDateTimeKind.Local,
                    or 
             System.DateTimeKind.UnspecifiedDateTimeKind.Unspecified, the date is considered local.
        
            latitudeDegrees: The latitude, in degrees, of the location on Earth.
            longitudeDegrees: The longitude, in degrees, of the location on Earth.
        SetPosition(self: Sun, azimuthDegrees: float, altitudeDegrees: float)
            Sets position of the Sun based on azimuth and altitude values.
        
            azimuthDegrees: The azimut sun angle in degrees.
            altitudeDegrees: The altitude sun angle in degrees.
        """
        pass

    def ShowDialog(self):
        """
        ShowDialog(self: Sun)
            Show the tabbed sun dialog.
        """
        pass

    @staticmethod
    def SunDirection(latitude, longitude, when):
        """ SunDirection(latitude: float, longitude: float, when: DateTime) -> Vector3d """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Altitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Altitude(self: Sun) -> float

"""

    Azimuth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Azimuth(self: Sun) -> float

"""

    DaylightSaving = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Daylight savings time

Get: DaylightSaving(self: Sun) -> bool

Set: DaylightSaving(self: Sun) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Turn to sun on/off in this document.

Get: Enabled(self: Sun) -> bool

Set: Enabled(self: Sun) = value
"""

    Latitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Latitude(self: Sun) -> float

"""

    Longitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Longitude(self: Sun) -> float

"""

    ManualControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set angles directly or use place/date/time

Get: ManualControl(self: Sun) -> bool

Set: ManualControl(self: Sun) = value
"""

    North = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Angle in degrees on world X-Y plane that should be considered north in the model. Angle is
            measured starting at X-Axis and travels counterclockwise. Y-Axis would be a north angle of 90
            degrees.

Get: North(self: Sun) -> float

Set: North(self: Sun) = value
"""

    SkylightOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Turn skylight on or off

Get: SkylightOn(self: Sun) -> bool

Set: SkylightOn(self: Sun) = value
"""

    TimeZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Measured in hours += UTC

Get: TimeZone(self: Sun) -> float

Set: TimeZone(self: Sun) = value
"""

    Vector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vector(self: Sun) -> Vector3d

"""


    Changed = None


class TextureEnvironmentMappingMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum TextureEnvironmentMappingMode, values: Automatic (0), Box (3), Cube (6), EnvironmentMap (2), Hemispherical (9), HorizontalCrossCube (8), LightProbe (5), Spherical (1), VerticalCrossCube (7) """
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

    Automatic = None
    Box = None
    Cube = None
    EnvironmentMap = None
    Hemispherical = None
    HorizontalCrossCube = None
    LightProbe = None
    Spherical = None
    value__ = None
    VerticalCrossCube = None


class TextureEvaluator(object, IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: TextureEvaluator) """
        pass

    def GetColor(self, uvw, duvwdx, duvwdy):
        """ GetColor(self: TextureEvaluator, uvw: Point3d, duvwdx: Vector3d, duvwdy: Vector3d) -> Color4f """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class TextureMapping(CommonObject, IDisposable, ISerializable):
    """ Represents a texture mapping. """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    @staticmethod
    def CreateBoxMapping(plane, dx, dy, dz, capped):
        """
        CreateBoxMapping(plane: Plane, dx: Interval, dy: Interval, dz: Interval, capped: bool) -> TextureMapping
        
            Create a box projection texture mapping.
        
            plane: The sides of the box the box are parallel to the plane's coordinate
                    planes.  The 
             dx, dy, dz intervals determine the location of the sides.
        
            dx: Determines the location of the front and back planes. The vector
                    plane.xaxis is 
             perpendicular to these planes and they pass through
                    plane.PointAt(dx[0],0,0) and 
             plane.PointAt(dx[1],0,0), respectivly.
        
            dy: Determines the location of the left and right planes. The vector
                    plane.yaxis is 
             perpendicular to these planes and they pass through
                    plane.PointAt(0,dy[0],0) and 
             plane.PointAt(0,dy[1],0), respectivly.
        
            dz: Determines the location of the top and bottom planes. The vector
                    plane.zaxis is 
             perpendicular to these planes and they pass through
                    plane.PointAt(0,0,dz[0]) and 
             plane.PointAt(0,0,dz[1]), respectivly.
        
            capped: If true, the box is treated as a finite capped box.
            Returns: TextureMapping instance if input is valid
        """
        pass

    @staticmethod
    def CreateCylinderMapping(cylinder, capped):
        """
        CreateCylinderMapping(cylinder: Cylinder, capped: bool) -> TextureMapping
        
            Create a cylindrical projection texture mapping.
        
            cylinder: cylinder in world space used to define a cylindrical coordinate system.
                    The angular 
             parameter maps (0,2pi) to texture "u" (0,1), The height
                    parameter maps 
             (height[0],height[1]) to texture "v" (0,1), and the
                    radial parameter maps (0,r) to 
             texture "w" (0,1).
        
            capped: If true, the cylinder is treated as a finite capped cylinder
            Returns: TextureMapping instance if input is valid
        """
        pass

    @staticmethod
    def CreatePlaneMapping(plane, dx, dy, dz):
        """
        CreatePlaneMapping(plane: Plane, dx: Interval, dy: Interval, dz: Interval) -> TextureMapping
        
            Create a planar projection texture mapping
        
            plane: A plane to use for mapping.
            dx: portion of the plane's x axis that is mapped to [0,1] (can be a decreasing interval)
            dy: portion of the plane's y axis that is mapped to [0,1] (can be a decreasing interval)
            dz: portion of the plane's z axis that is mapped to [0,1] (can be a decreasing interval)
            Returns: TextureMapping instance if input is valid
        """
        pass

    @staticmethod
    def CreateSphereMapping(sphere):
        """
        CreateSphereMapping(sphere: Sphere) -> TextureMapping
        
            Create a spherical projection texture mapping.
        
            sphere: sphere in world space used to define a spherical coordinate system.
                    The longitude 
             parameter maps (0,2pi) to texture "u" (0,1).
                    The latitude paramter maps 
             (-pi/2,+pi/2) to texture "v" (0,1).
                    The radial parameter maps (0,r) to texture "w" 
             (0,1).
        
            Returns: TextureMapping instance if input is valid
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject, disposing: bool)
            For derived class implementers.
                    This method is called with argument true when class 
             user calls Dispose(), while with argument false when
                    the Garbage Collector invokes 
             the finalizer, or Finalize() method.You must reclaim all used unmanaged resources in both cases, 
             and can use this chance to call Dispose on disposable fields if the argument is true.Also, you 
             must call the base virtual method within your overriding method.
        
        
            disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 
             finalizer.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: CommonObject)
            Is called when a non-const operation first occurs.
        """
        pass

    def TryGetMappingBox(self, plane, dx, dy, dz):
        """
        TryGetMappingBox(self: TextureMapping) -> (bool, Plane, Interval, Interval, Interval)
        
            Get a box projection from the texture mapping.
            Returns: Returns true if a valid box is returned.
        """
        pass

    def TryGetMappingCylinder(self, cylinder):
        """
        TryGetMappingCylinder(self: TextureMapping) -> (bool, Cylinder)
        
            Get a cylindrical projection parameters from this texture mapping.
            Returns: Returns true if a valid cylinder is returned.
        """
        pass

    def TryGetMappingPlane(self, plane, dx, dy, dz):
        """
        TryGetMappingPlane(self: TextureMapping) -> (bool, Plane, Interval, Interval, Interval)
        
            Get plane mapping parameters from this texture mapping.
            Returns: Return true if valid plane mapping parameters were returned.
        """
        pass

    def TryGetMappingSphere(self, sphere):
        """
        TryGetMappingSphere(self: TextureMapping) -> (bool, Sphere)
        
            Get a spherical projection parameters from this texture mapping.
            Returns: Returns true if a valid sphere is returned.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique Id for this texture mapping object.

Get: Id(self: TextureMapping) -> Guid

"""

    MappingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Texture mapping type associated with this Mapping object.

Get: MappingType(self: TextureMapping) -> TextureMappingType

"""

    NormalTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For primitive based mappings, these transformations are used to map
            the world coordinate (x,y,z) point P and  surface normal N before it is
            projected to the normalized mapping primitive. The surface normal
            transformation, m_Nxyz, is always calculated from m_Pxyz.  It is a
            runtime setting that is not saved in 3dm files. If m_type is
            srfp_mapping, then m_Pxyz and m_Nxyz are ignored.

Get: NormalTransform(self: TextureMapping) -> Transform

Set: NormalTransform(self: TextureMapping) = value
"""

    PrimativeTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For primitive based mappings, these transformations are used to map
            the world coordinate (x,y,z) point P and  surface normal N before it is
            projected to the normalized mapping primitive. The surface normal
            transformation, m_Nxyz, is always calculated from m_Pxyz.  It is a
            runtime setting that is not saved in 3dm files. If m_type is
            srfp_mapping, then m_Pxyz and m_Nxyz are ignored.

Get: PrimativeTransform(self: TextureMapping) -> Transform

Set: PrimativeTransform(self: TextureMapping) = value
"""

    UvwTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Transform applied to mapping coordinate (u,v,w) to convert it into a
            texture coordinate.

Get: UvwTransform(self: TextureMapping) -> Transform

Set: UvwTransform(self: TextureMapping) = value
"""



class TextureMappingType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated constants for mapping types such as planar, cylindrical or spherical.
    
    enum TextureMappingType, values: BoxMapping (5), BrepMappingPrimitive (8), CylinderMapping (3), MeshMappingPrimitive (6), None (0), PlaneMapping (2), SphereMapping (4), SurfaceMappingPrimitive (7), SurfaceParameters (1)
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


class TextureProjectionMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum TextureProjectionMode, values: EnvironmentMap (3), MappingChannel (0), Screen (5), View (1), Wcs (2), WcsBox (4) """
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

    EnvironmentMap = None
    MappingChannel = None
    Screen = None
    value__ = None
    View = None
    Wcs = None
    WcsBox = None


class TextureWrapType(Enum, IComparable, IFormattable, IConvertible):
    """ enum TextureWrapType, values: Clamped (0), Repeating (1) """
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

    Clamped = None
    Repeating = None
    value__ = None


class TwoColorRenderTexture(RenderTexture, IDisposable):
    # no doc
    def AddAdditionalUISections(self, *args): #cannot find CLR method
        """ AddAdditionalUISections(self: TwoColorRenderTexture) """
        pass

    def Dispose(self):
        """ Dispose(self: RenderContent, disposing: bool) """
        pass

    def ModifyRenderContentStyles(self, *args): #cannot find CLR method
        """ ModifyRenderContentStyles(self: RenderContent, stylesToAdd: RenderContentStyles, stylesToRemove: RenderContentStyles) """
        pass

    def OnAddUserInterfaceSections(self, *args): #cannot find CLR method
        """ OnAddUserInterfaceSections(self: TwoColorRenderTexture) """
        pass

    def OnGetDefaultsInteractive(self, *args): #cannot find CLR method
        """
        OnGetDefaultsInteractive(self: RenderContent, parentWindowHandle: IntPtr) -> bool
        
            Override this method to prompt user for information necessary to
                    create a new 
             content object.  For example, if you are created a
                    textured material you may prompt 
             the user for a bitmap file name
                    prior to creating the textured material.
        
            Returns: If true is returned the content is created otherwise the creation
                    is aborted.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Color1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color1(self: TwoColorRenderTexture) -> Color4f

Set: Color1(self: TwoColorRenderTexture) = value
"""

    Color2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color2(self: TwoColorRenderTexture) -> Color4f

Set: Color2(self: TwoColorRenderTexture) = value
"""

    SuperSample = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuperSample(self: TwoColorRenderTexture) -> bool

Set: SuperSample(self: TwoColorRenderTexture) = value
"""

    SwapColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SwapColors(self: TwoColorRenderTexture) -> bool

Set: SwapColors(self: TwoColorRenderTexture) = value
"""

    Texture1Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Texture1Amount(self: TwoColorRenderTexture) -> float

Set: Texture1Amount(self: TwoColorRenderTexture) = value
"""

    Texture1On = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Texture1On(self: TwoColorRenderTexture) -> bool

Set: Texture1On(self: TwoColorRenderTexture) = value
"""

    Texture2Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Texture2Amount(self: TwoColorRenderTexture) -> float

Set: Texture2Amount(self: TwoColorRenderTexture) = value
"""

    Texture2On = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Texture2On(self: TwoColorRenderTexture) -> bool

Set: Texture2On(self: TwoColorRenderTexture) = value
"""



class Utilities(object):
    # no doc
    @staticmethod
    def SetDefaultRenderPlugIn(pluginId):
        """
        SetDefaultRenderPlugIn(pluginId: Guid) -> bool
        
            Set default render application
        
            pluginId: ID of render plug-in
            Returns: True if plug-in found and loaded successfully.  False if pluginId is
                     invalid or 
             was unable to load plug-in
        """
        pass

    __all__ = [
        'SetDefaultRenderPlugIn',
    ]


# variables with complex values

