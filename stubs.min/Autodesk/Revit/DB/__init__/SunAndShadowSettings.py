class SunAndShadowSettings(Element, IDisposable):
    """ The SunAndShadowSettings class represents the sun control. """
    @staticmethod
    def CalculateTimeZone(latitude, longitude):
        """
        CalculateTimeZone(latitude: float, longitude: float) -> float
        
            Use Revit's utilities to calculate the time zone for a given longitude and 
             latitude.
        
        
            latitude: The latitude.
            longitude: The longitude.
            Returns: The time zone, in hours, ranging from +12 hours to -12 hours with 0 being GMT.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def FitToModel(self):
        """
        FitToModel(self: SunAndShadowSettings)
            Adjust SunAndShadowSettings to fit around the current model geometry.
        """
        pass

    @staticmethod
    def GetActiveSunAndShadowSettings(aDocument):
        """
        GetActiveSunAndShadowSettings(aDocument: Document) -> Element
        
            Returns the current SunAndShadowSettings element assigned to the active view 
             for the
           supplied document.
        
        
            aDocument: The document.
            Returns: The active SunAndShadowSettings element for the supplied document.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetFrameAltitude(self, frame):
        """
        GetFrameAltitude(self: SunAndShadowSettings, frame: float) -> float
        
            Identifies the altitude of the sun (angle in radians) for a specific frame.
        
            frame: Frame for which time is requested
            Returns: Altitude angle (radians)
        """
        pass

    def GetFrameAzimuth(self, frame):
        """
        GetFrameAzimuth(self: SunAndShadowSettings, frame: float) -> float
        
            Identifies the azimuth of the sun (angle in radians) for a specific frame.
        
            frame: Frame for which time is requested
            Returns: Azimuth angle (radians).  This is measured counterclockwise from the X axis 
             (East direction).  Note that this
           is a different frame of reference than is 
             used by Revit for the Lighting Study Azimuth value.
        """
        pass

    def GetFrameTime(self, frame):
        """
        GetFrameTime(self: SunAndShadowSettings, frame: float) -> DateTime
        
            Identifies the date and time of the SunAndShadowSettings element for a given 
             frame.
        
        
            frame: Frame for which time is requested
            Returns: The date and time.  The value will be in Coordinated Universal Time (UTC).
        """
        pass

    def GetMatchingPreset(self):
        """
        GetMatchingPreset(self: SunAndShadowSettings) -> str
        
            Finds the name of the 'per-document' SunAndShadowSettings that matches the 
             properties
           of this per-view element.
        
            Returns: Name of the per-document SunAndShadowSettings that matches the view specific 
             element.
        """
        pass

    def GetSunrise(self, date):
        """
        GetSunrise(self: SunAndShadowSettings, date: DateTime) -> DateTime
        
            Identifies the sunrise time for the SunAndShadowSettings element at its current 
             location
           and indicated date.
        
        
            date: The date for which to determine sunrise time.
            Returns: The date and time.  The value will be in Coordinated Universal Time (UTC).
        """
        pass

    def GetSunset(self, date):
        """
        GetSunset(self: SunAndShadowSettings, date: DateTime) -> DateTime
        
            Identifies the sunset time for the SunAndShadowSettings element at its current 
             location
           and indicated date.
        
        
            date: The date for which to determine sunset time.
            Returns: The date and time.  The value will be in Coordinated Universal Time (UTC).
        """
        pass

    def IsAfterStartDateAndTime(self, time):
        """
        IsAfterStartDateAndTime(self: SunAndShadowSettings, time: DateTime) -> bool
        
            Checks whether the end date and time is valid.
        
            time: Date and time value
            Returns: True if the date and time is valid, false otherwise.
        """
        pass

    def IsBeforeEndDateAndTime(self, time):
        """
        IsBeforeEndDateAndTime(self: SunAndShadowSettings, time: DateTime) -> bool
        
            Checks whether the start date and time is valid.
        
            time: Date and time value
            Returns: True if the date and time is valid, false otherwise.
        """
        pass

    def IsFrameValid(self, frame):
        """
        IsFrameValid(self: SunAndShadowSettings, frame: float) -> bool
        
            Checks whether the frame is valid for the supplied SunAndShadowSettings.
        
            frame: Frame value
            Returns: True if the frame is valid for the SunAndShadowSettings, false otherwise.
        """
        pass

    def IsGroundPlaneLevelValid(self, levelId):
        """
        IsGroundPlaneLevelValid(self: SunAndShadowSettings, levelId: ElementId) -> bool
        
            Checks whether the element represents a valid Ground Plane level.
        
            levelId: Level element id.
            Returns: True if the element is a valid Ground Plane Level, false otherwise.
        """
        pass

    def IsTimeIntervalValid(self, interval):
        """
        IsTimeIntervalValid(self: SunAndShadowSettings, interval: SunStudyTimeInterval) -> bool
        
            Checks whether the time interval is valid for the SunAndShadowType.
        
            interval: Time interval value.
            Returns: True if the time interval is valid for the current SunAndShadowType, false 
             otherwise.
        """
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

    ActiveFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the active animation frame for a single-day or multi-day study,
   starting at 1.0 for the first frame and incrementing in intervals of 1.0.

Get: ActiveFrame(self: SunAndShadowSettings) -> float

Set: ActiveFrame(self: SunAndShadowSettings) = value
"""

    ActiveFrameTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the date and time of the SunAndShadowSettings element for the active frame.

Get: ActiveFrameTime(self: SunAndShadowSettings) -> DateTime

"""

    Altitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Altitude setting (angle in radians). This is only relevant when dealing with a SunAndShadowSettings
   element that uses lighting mode.

Get: Altitude(self: SunAndShadowSettings) -> float

Set: Altitude(self: SunAndShadowSettings) = value
"""

    Azimuth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Azimuth setting (angle in radians). This is only relevant when dealing with a SunAndShadowSettings
   element that uses lighting mode.

Get: Azimuth(self: SunAndShadowSettings) -> float

Set: Azimuth(self: SunAndShadowSettings) = value
"""

    EndDateAndTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the end date and time.

Get: EndDateAndTime(self: SunAndShadowSettings) -> DateTime

Set: EndDateAndTime(self: SunAndShadowSettings) = value
"""

    GroundPlaneHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the ground plane height.

Get: GroundPlaneHeight(self: SunAndShadowSettings) -> float

"""

    GroundPlaneLevelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the element id of the Ground Plane level for the SunAndShadowSettings element.

Get: GroundPlaneLevelId(self: SunAndShadowSettings) -> ElementId

Set: GroundPlaneLevelId(self: SunAndShadowSettings) = value
"""

    Latitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the current latitude used by the SunAndShadowSettings element.

Get: Latitude(self: SunAndShadowSettings) -> float

"""

    Longitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the current longitude used by the SunAndShadowSettings element.

Get: Longitude(self: SunAndShadowSettings) -> float

"""

    NumberOfFrames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the total number of animation frames for a single-day or multi-day study.

Get: NumberOfFrames(self: SunAndShadowSettings) -> float

"""

    ProjectLocationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the ProjectLocation element used by the SunAndShadowSettings element.

Get: ProjectLocationId(self: SunAndShadowSettings) -> ElementId

"""

    ProjectLocationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the name of the project location used by the SunAndShadowSettings element.

Get: ProjectLocationName(self: SunAndShadowSettings) -> str

"""

    RelativeToView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies whether the SunAndShadowSettings element is relative to the view
   direction. This is only relevant for lighting mode.

Get: RelativeToView(self: SunAndShadowSettings) -> bool

Set: RelativeToView(self: SunAndShadowSettings) = value
"""

    SharesSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies whether settings are shared globally.

Get: SharesSettings(self: SunAndShadowSettings) -> bool

Set: SharesSettings(self: SunAndShadowSettings) = value
"""

    StartDateAndTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the start or current date and time.

Get: StartDateAndTime(self: SunAndShadowSettings) -> DateTime

Set: StartDateAndTime(self: SunAndShadowSettings) = value
"""

    SunAndShadowType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the type of the SunAndShadowSettings element.

Get: SunAndShadowType(self: SunAndShadowSettings) -> SunAndShadowType

Set: SunAndShadowType(self: SunAndShadowSettings) = value
"""

    SunriseToSunset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies whether the current single day sun study is set to run from
   sunrise to sunset.

Get: SunriseToSunset(self: SunAndShadowSettings) -> bool

Set: SunriseToSunset(self: SunAndShadowSettings) = value
"""

    TimeInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the time interval between animation frames.

Get: TimeInterval(self: SunAndShadowSettings) -> SunStudyTimeInterval

Set: TimeInterval(self: SunAndShadowSettings) = value
"""

    TimeZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the time zone.

Get: TimeZone(self: SunAndShadowSettings) -> float

"""

    UsesDST = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies whether the SunAndShadowSettings element is using daylight savings time.

Get: UsesDST(self: SunAndShadowSettings) -> bool

"""

    UsesGroundPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies whether the SunAndShadowSettings element uses a ground plane.

Get: UsesGroundPlane(self: SunAndShadowSettings) -> bool

Set: UsesGroundPlane(self: SunAndShadowSettings) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Visibility in current view for a per-view SunAndShadowSettings element.

Get: Visible(self: SunAndShadowSettings) -> bool

Set: Visible(self: SunAndShadowSettings) = value
"""


