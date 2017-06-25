# encoding: utf-8
# module Autodesk.Revit.DB.PointClouds calls itself PointClouds
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CloudPoint(object):
    """
    Represents a point obtained from a Point cloud.
    
    CloudPoint(x: Single, y: Single, z: Single, color: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, x, y, z, color):
        """
        __new__[CloudPoint]() -> CloudPoint
        
        __new__(cls: type, x: Single, y: Single, z: Single, color: int)
        """
        pass

    Color = None
    X = None
    Y = None
    Z = None


class IPointCloudAccess:
    """
    An interface that provides functionality for working with an individual
       Point Cloud.
    """
    def CreatePointSetIterator(self, rFilter, *__args):
        """
        CreatePointSetIterator(self: IPointCloudAccess, rFilter: PointCloudFilter, viewId: ElementId) -> IPointSetIterator
        
            Implement this method to return an iterator for iterating over blocks of this 
             point cloud.
        
        
            rFilter: The filter used to process cloud points and determine which ones lie with the 
             target volume.
        
            viewId: The view id for the current view passed as auxiliary information to allow the
         
               engine to optimize retrieval of points.  If viewId == InvalidElementId, the
         
               query is not for a view display operation.
        
            Returns: The newly created iterator.
        CreatePointSetIterator(self: IPointCloudAccess, rFilter: PointCloudFilter, density: float, viewId: ElementId) -> IPointSetIterator
        
            Implement this method to return an iterator for iterating over blocks of this 
             point cloud.
        
        
            rFilter: The filter used to process cloud points and determine which ones lie with the 
             target volume.
        
            density: Desired number of points per unit area. Area is computed in native units of the 
             point cloud.
           Another iterator, created with the same density and a more 
             restrictive
           filter, should return a subset of the points returned by this 
             iterator.
        
            viewId: The view id for the current view passed as auxiliary information to allow the
         
               engine to optimize retrieval of points.  If viewId == InvalidElementId, the
         
               query is not for a view display operation.
        
            Returns: The newly created iterator.
        """
        pass

    def Free(self):
        """
        Free(self: IPointCloudAccess)
            Completes the lifetime of the object providing this interface.
        """
        pass

    def GetColorEncoding(self):
        """
        GetColorEncoding(self: IPointCloudAccess) -> PointCloudColorEncoding
        
            Returns the encoding used by points in this point cloud.
            Returns: The encoding.
        """
        pass

    def GetExtent(self):
        """
        GetExtent(self: IPointCloudAccess) -> Outline
        
            Implement this method to returns an object that contains the bounding box of 
             the entire
           point cloud, aligned to the point cloud coordinate system.
        
            Returns: The bounding box of the point cloud.
        """
        pass

    def GetName(self):
        """
        GetName(self: IPointCloudAccess) -> str
        
            Implement this method to return the name of the point cloud that will be used 
             when Revit needs to
           refer to the point cloud type, e.g. in the Manage Links 
             dialog or in the
           Type Properties dialog.
        
            Returns: The name of the point cloud for Revit's user interface.
        """
        pass

    def GetOffset(self):
        """
        GetOffset(self: IPointCloudAccess) -> XYZ
        
            Implement this method to return the offset stored in the point cloud.
            Returns: The offset vector of this point cloud's coordinate system.
        """
        pass

    def GetUnitsToFeetConversionFactor(self):
        """
        GetUnitsToFeetConversionFactor(self: IPointCloudAccess) -> float
        
            Implement this method to return the conversion factor from the units of the 
             point cloud to feet.
        
            Returns: The multiplication factor to convert coordinates of points in this cloud to 
             feet.
        """
        pass

    def ReadPoints(self, rFilter, viewId, buffer, nBufferSize):
        """
        ReadPoints(self: IPointCloudAccess, rFilter: PointCloudFilter, viewId: ElementId, buffer: IntPtr, nBufferSize: int) -> int
        
            Implement this method so that on successive invocations it will return distinct 
             subsets of
           points which meet the criterion.
        
        
            rFilter: The filter used to process cloud points and determine which ones lie with the 
             target volume.
        
            viewId: The view id for the current view passed as auxiliary information to allow the
         
               engine to optimize retrieval of points.  If viewId == InvalidElementId, the
         
               query is not for a view display operation.
        
            buffer: Memory buffer into which the points should be written. The buffer was allocated
             
           by Revit and it is guaranteed to be valid for the duration of the call.
        
            nBufferSize: The maximum number of CloudPoint objects that may be copied into the buffer.
            Returns: The actual number of CloudPoint objects placed in the buffer (can be less than 
             the
           length of the buffer).  If there are no points available that match the 
             filter criteria, return 0.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IPointCloudEngine:
    """ An interface that controls the behavior of the link from Revit to a custom Point Cloud Engine. """
    def CreatePointCloudAccess(self, identifier):
        """
        CreatePointCloudAccess(self: IPointCloudEngine, identifier: str) -> IPointCloudAccess
        
            Implement this method to construct the IPointCloudAccess interface for the 
             point cloud designated by
           the identifier.  This method is called once 
             during the creation of a PointCloudType.
        
        
            identifier: An identifier unique to the point cloud.  This will be a file name if the
           
             engine was registered as file-based, or an arbitrary identifier if the engine 
             is not file-based.
        
            Returns: The object that can be used to create iterators and interrogate the
           point 
             cloud for its features.
        """
        pass

    def Free(self):
        """
        Free(self: IPointCloudEngine)
            Revit will call this method when done using the engine.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IPointSetIterator:
    """ An interface that Revit will call when iterating through sets of points on the engine. """
    def Free(self):
        """
        Free(self: IPointSetIterator)
            Use this method to discard any resources consumed by the iterator.  Revit will 
             call it when done using the iterator.
        """
        pass

    def ReadPoints(self, buffer, bufferSize):
        """
        ReadPoints(self: IPointSetIterator, buffer: IntPtr, bufferSize: int) -> int
        
            Implement this method to fill the provided buffer with points up to the number 
             of maximum points for
           which the buffer was allocated.
        
        
            buffer: Memory buffer into which the points should be written. The buffer was allocated
             
           by Revit and it is guaranteed to be valid for the duration of the call.
        
            bufferSize: The maximum number of CloudPoint objects that may be copied into the buffer.
            Returns: The actual number of CloudPoint objects placed in the buffer (can be less than 
             the
           length of the buffer).  If there are no more points available, return 
             0.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PointCloudColorEncoding(Enum, IComparable, IFormattable, IConvertible):
    """
    The color encodings supported by Revit point clouds.
    
    enum PointCloudColorEncoding, values: ABGR (1), ARGB (0)
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

    ABGR = None
    ARGB = None
    value__ = None


class PointCloudColorSettings(object, IDisposable):
    """
    The color settings which are applied to a PointCloudInstance element, or one of its scans.
    
    PointCloudColorSettings(other: PointCloudColorSettings)
    PointCloudColorSettings(color1: Color, color2: Color)
    PointCloudColorSettings(mode: PointCloudColorMode)
    PointCloudColorSettings()
    """
    def Assign(self, other):
        """
        Assign(self: PointCloudColorSettings, other: PointCloudColorSettings)
            Assigns values of the source settings to this object.
        
            other: The source settings.
        """
        pass

    def Dispose(self):
        """ Dispose(self: PointCloudColorSettings) """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: PointCloudColorSettings, other: PointCloudColorSettings) -> bool
        
            Check if the contents of two settings are equal.
        
            other: The settings to be compared.
            Returns: True for equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PointCloudColorSettings, disposing: bool) """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: PointCloudColorSettings)
        __new__(cls: type, color1: Color, color2: Color)
        __new__(cls: type, mode: PointCloudColorMode)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Color1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color 1

Get: Color1(self: PointCloudColorSettings) -> Color

"""

    Color2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color 2

Get: Color2(self: PointCloudColorSettings) -> Color

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PointCloudColorSettings) -> bool

"""



class PointCloudEngineRegistry(object):
    """ This class supports registration of custom Point Cloud Engines in a Revit session. """
    @staticmethod
    def GetSupportedEngines():
        """
        GetSupportedEngines() -> IList[str]
        
            Returns a list of the identifiers supported by point cloud engines registered 
             to Revit.
        
            Returns: The list of identifiers.
        """
        pass

    @staticmethod
    def IsEngineFileBased(identifier):
        """
        IsEngineFileBased(identifier: str) -> bool
        
            Identifies if a given engine is file-based.
        
            identifier: The engine identifier.
            Returns: True if the engine is file-based, false otherwise.
        """
        pass

    @staticmethod
    def RegisterPointCloudEngine(identifier, engine, isFileBased):
        """
        RegisterPointCloudEngine(identifier: str, engine: IPointCloudEngine, isFileBased: bool)
            Registers a new point cloud engine and associates it to a particular file 
             extension.
        
        
            identifier: A string that distinguishes the engine being registered.  If isFileBased is 
             true,
           this should be the file extension (e.g. "pcg").  If isFileBased is 
             false, this
           identifier is used only by API calls and should be unique.
        
            engine: The point cloud engine that governs point clouds matching the input identifier.
            isFileBased: Indicates to Revit if a single Point Cloud corresponds to a single file on disk.
        """
        pass

    @staticmethod
    def UnregisterPointCloudEngine(identifier):
        """
        UnregisterPointCloudEngine(identifier: str)
            Unregisters the point cloud engine associated to a particular identifier.
        
            identifier: The identifier of the engine to be unregistered.
        """
        pass

    __all__ = [
        'GetSupportedEngines',
        'IsEngineFileBased',
        'RegisterPointCloudEngine',
        'UnregisterPointCloudEngine',
    ]


class PointCloudFilter(object, IDisposable):
    """ A class used to describe the criteria an application desires when obtaining members of a point cloud. """
    def Clone(self):
        """
        Clone(self: PointCloudFilter) -> PointCloudFilter
        
            Returns a copy of the filter. The engine is permitted to copy the filter 
             multiple times e.g. to parallelize filtering.
        
            Returns: A copy of the original filter.
        """
        pass

    def Dispose(self):
        """ Dispose(self: PointCloudFilter) """
        pass

    def PrepareForCell(self, min, max, numTests):
        """
        PrepareForCell(self: PointCloudFilter, min: XYZ, max: XYZ, numTests: int)
            Informs the filter that a series of points within a given cell is about to be 
             checked.
        
        
            min: The lower corner of the cell.
            max: The upper corner of the cell.
            numTests: The engine's estimate of the number of TestPoint() calls it is going to make 
             for this cell.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PointCloudFilter, disposing: bool) """
        pass

    def TestCell(self, min, max):
        """
        TestCell(self: PointCloudFilter, min: XYZ, max: XYZ) -> int
        
            Checks whether a given cell, i.e. a box aligned with the XYZ axes, is inside, 
             outside
           or on the border of the volume of interest.
        
        
            min: The lower corner of the cell.
            max: The upper corner of the cell.
            Returns: -1 -- The cell is entirely rejected.   0 -- The cell partially belongs to the 
             volume of interest.  Use PrepareForCell() and TestPoint() to
           evaluate 
             individual points. 1 -- The cell is fully accepted.
        """
        pass

    def TestPoint(self, point):
        """
        TestPoint(self: PointCloudFilter, point: CloudPoint) -> bool
        
            Checks if a point is inside the volume of interest.
        
            point: The point to be tested.
            Returns: If true, the point is accepted, if false, the point is not accepted.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PointCloudFilter) -> bool

"""



class PointCloudFilterFactory(object):
    """ A factory class for creating point cloud filters. """
    @staticmethod
    def CreateMultiPlaneFilter(planes, exactPlaneCount=None):
        """
        CreateMultiPlaneFilter(planes: IList[Plane], exactPlaneCount: int) -> PointCloudFilter
        CreateMultiPlaneFilter(planes: IList[Plane]) -> PointCloudFilter
        """
        pass

    __all__ = [
        'CreateMultiPlaneFilter',
    ]


class PointCloudFilterUtils(object):
    """ Utilities specific to point cloud filters. """
    @staticmethod
    def GetFilteredOutline(filter, box):
        """
        GetFilteredOutline(filter: PointCloudFilter, box: Outline) -> Outline
        
            Computes outline of a part of a box that satisfies given PointCloudFilter.
        
            filter: Point cloud filter.
            box: A box aligned with coordinate axes.
            Returns: The bounding box of the set of all points within the original box that satisfy 
             the filter.
           Not every point within the resulting outline satisfies the 
             filter, but any point that is contained
           in the original box and satisfies 
             the filter is guaranteed to be within the resulting outline.
        """
        pass

    __all__ = [
        'GetFilteredOutline',
    ]


class PointCloudOverrides(object, IDisposable):
    """
    Graphic overrides that are stored by a view to be applied to a PointCloudInstance element, or a scan within the element.
    
    PointCloudOverrides()
    """
    @staticmethod
    def ArePointCloudOverrideSettingsValid(tag, settings):
        """
        ArePointCloudOverrideSettingsValid(tag: str, settings: PointCloudOverrideSettings) -> bool
        
            Checks if PointCloudOverrideSettings are valid
        
            tag: The tag identifying the particular scan/region within the PointCloudInstance 
             element.
           Tags can be obtained from PointCloudInstance via method 
             getScans/getRegions.
        
            settings: Override settings to be checked.
        """
        pass

    def Assign(self, other):
        """
        Assign(self: PointCloudOverrides, other: PointCloudOverrides)
            Assigns values of the source overrides to this object.
        
            other: The source overrides.
        """
        pass

    def Dispose(self):
        """ Dispose(self: PointCloudOverrides) """
        pass

    def GetPointCloudOverrideSettings(self, elementId, scanTag=None, doc=None):
        """
        GetPointCloudOverrideSettings(self: PointCloudOverrides, elementId: ElementId) -> PointCloudOverrideSettings
        
            Gets override settings assigned to the whole PointCloudInstance element.
        
            elementId: Id of the overridden element.
            Returns: The override settings assigned to the element, if present, or a default 
             override settings if nothing was found.
        
        GetPointCloudOverrideSettings(self: PointCloudOverrides, elementId: ElementId, scanTag: str, doc: Document) -> PointCloudOverrideSettings
        
            Gets override settings assigned to a particular scan within a 
             PointCloudInstance element.
        
        
            elementId: Id of the overridden element.
            scanTag: The tag identifying the particular scan within the PointCloudInstance element.
        
                Tags can be obtained from PointCloudInstance via method getScans.
        
            doc: Document containing the overridden element.
            Returns: The override settings assigned to the scan, if present, or a default override 
             settings if nothing was found.
        """
        pass

    def GetPointCloudRegionOverrideSettings(self, elementId, regionTag=None, doc=None):
        """
        GetPointCloudRegionOverrideSettings(self: PointCloudOverrides, elementId: ElementId) -> PointCloudOverrideSettings
        
            Gets region override settings assigned to the whole PointCloudInstance element.
        
            elementId: Id of the overridden element.
            Returns: The override settings assigned to the element, if present, or a default 
             override settings if nothing was found.
        
        GetPointCloudRegionOverrideSettings(self: PointCloudOverrides, elementId: ElementId, regionTag: str, doc: Document) -> PointCloudOverrideSettings
        
            Gets override settings assigned to a particular region within a 
             PointCloudInstance element.
        
        
            elementId: Id of the overridden element.
            regionTag: The tag identifying the particular region within the PointCloudInstance 
             element.
           Tags can be obtained from PointCloudInstance via method 
             getRegions.
        
            doc: Document containing the overridden element.
            Returns: The override settings assigned to the region, if present, or a default override 
             settings if nothing was found.
        """
        pass

    def GetPointCloudScanOverrideSettings(self, elementId, scanTag=None, doc=None):
        """
        GetPointCloudScanOverrideSettings(self: PointCloudOverrides, elementId: ElementId) -> PointCloudOverrideSettings
        
            Gets scan override settings assigned to the whole PointCloudInstance element.
        
            elementId: Id of the overridden element.
            Returns: The override settings assigned to the element, if present, or a default 
             override settings if nothing was found.
        
        GetPointCloudScanOverrideSettings(self: PointCloudOverrides, elementId: ElementId, scanTag: str, doc: Document) -> PointCloudOverrideSettings
        
            Gets override settings assigned to a particular scan within a 
             PointCloudInstance element.
        
        
            elementId: Id of the overridden element.
            scanTag: The tag identifying the particular scan within the PointCloudInstance element.
        
                Tags can be obtained from PointCloudInstance via method getScans.
        
            doc: Document containing the overridden element.
            Returns: The override settings assigned to the scan, if present, or a default override 
             settings if nothing was found.
        """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: PointCloudOverrides, other: PointCloudOverrides) -> bool
        
            Check if the contents of two overrides are equal.
        
            other: The overrides to be compared.
            Returns: True for equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PointCloudOverrides, disposing: bool) """
        pass

    def SetPointCloudOverrideSettings(self, elementId, newSettings, scanTag=None, doc=None):
        """
        SetPointCloudOverrideSettings(self: PointCloudOverrides, elementId: ElementId, newSettings: PointCloudOverrideSettings)
            Assigns override settings to the whole PointCloudInstance element.
        
            elementId: Id of the element to be overridden.
            newSettings: Override settings to be assigned.
        SetPointCloudOverrideSettings(self: PointCloudOverrides, elementId: ElementId, newSettings: PointCloudOverrideSettings, scanTag: str, doc: Document)
            Assigns override settings to a particular scan within a PointCloudInstance 
             element.
        
        
            elementId: Id of the element to be overridden.
            newSettings: Override settings to be assigned.
            scanTag: The tag identifying the particular scan within the PointCloudInstance element.
        
                Tags can be obtained from PointCloudInstance via method getScans.
        
            doc: Document containing the element to be overridden.
        """
        pass

    def SetPointCloudRegionOverrideSettings(self, elementId, newSettings, regionTag=None, doc=None):
        """
        SetPointCloudRegionOverrideSettings(self: PointCloudOverrides, elementId: ElementId, newSettings: PointCloudOverrideSettings)
            Assigns region override settings to the whole PointCloudInstance element.
        
            elementId: Id of the element to be overridden.
            newSettings: Override settings to be assigned.
        SetPointCloudRegionOverrideSettings(self: PointCloudOverrides, elementId: ElementId, newSettings: PointCloudOverrideSettings, regionTag: str, doc: Document)
            Assigns override settings to a particular region within a PointCloudInstance 
             element.
        
        
            elementId: Id of the element to be overridden.
            newSettings: Override settings to be assigned.
            regionTag: The tag identifying the particular region within the PointCloudInstance 
             element.
           Tags can be obtained from PointCloudInstance via method 
             getRegions.
        
            doc: Document containing the element to be overridden.
        """
        pass

    def SetPointCloudScanOverrideSettings(self, elementId, newSettings, scanTag=None, doc=None):
        """
        SetPointCloudScanOverrideSettings(self: PointCloudOverrides, elementId: ElementId, newSettings: PointCloudOverrideSettings)
            Assigns scan override settings to the whole PointCloudInstance element.
        
            elementId: Id of the element to be overridden.
            newSettings: Override settings to be assigned.
        SetPointCloudScanOverrideSettings(self: PointCloudOverrides, elementId: ElementId, newSettings: PointCloudOverrideSettings, scanTag: str, doc: Document)
            Assigns scan override settings to a particular scan within a PointCloudInstance 
             element.
        
        
            elementId: Id of the element to be overridden.
            newSettings: Override settings to be assigned.
            scanTag: The tag identifying the particular scan within the PointCloudInstance element.
        
                Tags can be obtained from PointCloudInstance via method getScans.
        
            doc: Document containing the element to be overridden.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PointCloudOverrides) -> bool

"""



class PointCloudOverrideSettings(object, IDisposable):
    """
    The graphic override settings for one PointCloudInstance element or one of its scans.
    
    PointCloudOverrideSettings(other: PointCloudOverrideSettings)
    PointCloudOverrideSettings()
    """
    def Assign(self, other):
        """
        Assign(self: PointCloudOverrideSettings, other: PointCloudOverrideSettings)
            Assigns values of the source settings to this object.
        
            other: The source settings.
        """
        pass

    def Dispose(self):
        """ Dispose(self: PointCloudOverrideSettings) """
        pass

    def GetModeOverride(self, mode):
        """
        GetModeOverride(self: PointCloudOverrideSettings, mode: PointCloudColorMode) -> PointCloudColorSettings
        
            Lookup color settings for the given color mode.
        
            mode: Color mode for which to lookup the color settings.
            Returns: Color settings stored for the given color mode or default color settings if 
             nothing is stored for the given color mode.
        """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: PointCloudOverrideSettings, other: PointCloudOverrideSettings) -> bool
        
            Checks if the contents of two settings are equal.
        
            other: The settings to be compared.
            Returns: True for equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PointCloudOverrideSettings, disposing: bool) """
        pass

    def SetModeOverride(self, mode, colorSettings):
        """
        SetModeOverride(self: PointCloudOverrideSettings, mode: PointCloudColorMode, colorSettings: PointCloudColorSettings)
            Sets color settings for the given color mode.
        
            mode: Color mode for which color settings are set.
            colorSettings: Color settings to be set for the given color mode.
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

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type, other: PointCloudOverrideSettings)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ColorMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current color mode for the PointCloudInstance element or its scan.

Get: ColorMode(self: PointCloudOverrideSettings) -> PointCloudColorMode

Set: ColorMode(self: PointCloudOverrideSettings) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PointCloudOverrideSettings) -> bool

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Visibility flag for point cloud scans.

Get: Visible(self: PointCloudOverrideSettings) -> bool

Set: Visible(self: PointCloudOverrideSettings) = value
"""



class PointCollection(object, IEnumerable[CloudPoint], IEnumerable, IDisposable):
    """ A class that represents a set of points created and returned by Revit in response to a query. """
    def Dispose(self):
        """ Dispose(self: PointCollection) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PointCollection) -> IEnumerator[CloudPoint]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def GetPointBufferPointer(self):
        """
        GetPointBufferPointer(self: PointCollection) -> IntPtr
        
            Returns an unsafe pointer to the buffer in which this collection stores the 
             points.
        
            Returns: The pointer to the collection's storage.
        """
        pass

    def GetPointIterator(self):
        """
        GetPointIterator(self: PointCollection) -> PointIterator
        
            Creates and returns an iterator for the points contained in this collection.
            Returns: New iterator created, make sure to call 'free' on it when finished using it.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PointCollection, disposing: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CloudPoint](enumerable: IEnumerable[CloudPoint], value: CloudPoint) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of points in this collection.

Get: Count(self: PointCollection) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PointCollection) -> bool

"""



class PointIterator(object, IEnumerator[CloudPoint], IDisposable, IEnumerator):
    """ A class used to iterate individual points in a PointCollection. """
    def Dispose(self):
        """ Dispose(self: PointIterator) """
        pass

    def Free(self):
        """
        Free(self: PointIterator)
            Completes lifetime of the iterator.  Call it when done using the iterator.
        """
        pass

    def IsDone(self):
        """
        IsDone(self: PointIterator) -> bool
        
            Identifies if the iteration has reached the end of the collection.
            Returns: True if the iteration has reached the end, false otherwise.
        """
        pass

    def MoveNext(self):
        """
        MoveNext(self: PointIterator) -> bool
        
            Increments the iterator to the next point in the collection.
            Returns: True if there is another available point in this iterator.
           False if the 
             iterator has completed all available points.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PointIterator, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: PointIterator)
            Resets the iterator to the beginning of the collection.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CloudPoint](enumerator: IEnumerator[CloudPoint], value: CloudPoint) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: PointIterator) -> CloudPoint

"""

    CurrentObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentObject(self: PointIterator) -> object

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PointIterator) -> bool

"""



