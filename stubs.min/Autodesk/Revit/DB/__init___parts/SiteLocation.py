class SiteLocation(ElementType, IDisposable):
    """ Contains the geographical location information for the project's site. """
    def ConvertFromProjectTime(self, projectTime):
        """
        ConvertFromProjectTime(self: SiteLocation, projectTime: DateTime) -> DateTime
        
            Converts project time to UTC time.
        
            projectTime: The project time.
        """
        pass

    def ConvertToProjectTime(self, inputTime):
        """
        ConvertToProjectTime(self: SiteLocation, inputTime: DateTime) -> DateTime
        
            Converts local time or UTC time to project time.
        
            inputTime: The input local time or UTC time.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
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

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Elevation of the site location.

Get: Elevation(self: SiteLocation) -> float

"""

    Latitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The latitude of the site location.

Get: Latitude(self: SiteLocation) -> float

Set: Latitude(self: SiteLocation) = value
"""

    Longitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The longitude of the site location.

Get: Longitude(self: SiteLocation) -> float

Set: Longitude(self: SiteLocation) = value
"""

    PlaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The place name of the site.

Get: PlaceName(self: SiteLocation) -> str

Set: PlaceName(self: SiteLocation) = value
"""

    TimeZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time-zone that contains the site

Get: TimeZone(self: SiteLocation) -> float

Set: TimeZone(self: SiteLocation) = value
"""

    WeatherStationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the weather station at the site location.

Get: WeatherStationName(self: SiteLocation) -> str

"""


