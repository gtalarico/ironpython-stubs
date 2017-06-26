class City(APIObject, IDisposable):
    """ An object that contains geographical location information for a known city. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
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

    Latitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Latitude of the city

Get: Latitude(self: City) -> float

"""

    Longitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Longitude of the city

Get: Longitude(self: City) -> float

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the city

Get: Name(self: City) -> str

"""

    TimeZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time-zone in which the city resides

Get: TimeZone(self: City) -> float

"""

    WeatherStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An identifier for the nearest weather station

Get: WeatherStation(self: City) -> str

"""


