class Clock(DispatcherObject):
    """ Maintains run-time timing state for a System.Windows.Media.Animation.Timeline. """
    def DiscontinuousTimeMovement(self, *args): #cannot find CLR method
        """
        DiscontinuousTimeMovement(self: Clock)
            When implemented in a derived class, will be invoked whenever a clock repeats, skips, or seeks.
        """
        pass

    def GetCanSlip(self, *args): #cannot find CLR method
        """
        GetCanSlip(self: Clock) -> bool
        
            Returns whether the System.Windows.Media.Animation.Clock has its own external time source, which may require synchronization with the timing system.
            Returns: Returns true if the System.Windows.Media.Animation.Clock has its own external source for time, which may require synchronization with the timing system; otherwise, false.
        """
        pass

    def GetCurrentTimeCore(self, *args): #cannot find CLR method
        """
        GetCurrentTimeCore(self: Clock) -> TimeSpan
        
            Gets this clock's current time within its current iteration.
            Returns: The current time of this clock if it is active or filling; otherwise, System.TimeSpan.Zero.
        """
        pass

    def SpeedChanged(self, *args): #cannot find CLR method
        """
        SpeedChanged(self: Clock)
            When implemented in a derived class, will be invoked whenever a clock begins, skips, pauses, resumes, or when the clock's System.Windows.Media.Animation.ClockController.SpeedRatio is modified.
        """
        pass

    def Stopped(self, *args): #cannot find CLR method
        """
        Stopped(self: Clock)
            When implemented in a derived class, will be invoked whenever a clock is stopped using the System.Windows.Media.Animation.ClockController.Stop method.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, timeline: Timeline) """
        pass

    Controller = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Windows.Media.Animation.ClockController that can be used to start, pause, resume, seek, skip, stop, or remove this System.Windows.Media.Animation.Clock.

Get: Controller(self: Clock) -> ClockController

"""

    CurrentGlobalSpeed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rate at which the clock's time is currently progressing, compared to real-world time.

Get: CurrentGlobalSpeed(self: Clock) -> Nullable[float]

"""

    CurrentGlobalTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current global time, as established by the WPF timing system.

"""

    CurrentIteration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the current iteration of this clock.

Get: CurrentIteration(self: Clock) -> Nullable[int]

"""

    CurrentProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current progress of this System.Windows.Media.Animation.Clock within its current iteration.

Get: CurrentProgress(self: Clock) -> Nullable[float]

"""

    CurrentState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the clock is currently System.Windows.Media.Animation.ClockState.Active, System.Windows.Media.Animation.ClockState.Filling, or System.Windows.Media.Animation.ClockState.Stopped.

Get: CurrentState(self: Clock) -> ClockState

"""

    CurrentTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets this clock's current time within its current iteration.

Get: CurrentTime(self: Clock) -> Nullable[TimeSpan]

"""

    HasControllableRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Media.Animation.Clock is part of a controllable clock tree.

Get: HasControllableRoot(self: Clock) -> bool

"""

    IsPaused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Windows.Media.Animation.Clock, or any of its parents, is paused.

Get: IsPaused(self: Clock) -> bool

"""

    NaturalDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the natural duration of this clock's System.Windows.Media.Animation.Clock.Timeline.

Get: NaturalDuration(self: Clock) -> Duration

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the clock that is the parent of this clock.

Get: Parent(self: Clock) -> Clock

"""

    Timeline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.Animation.Clock.Timeline from which this System.Windows.Media.Animation.Clock was created.

Get: Timeline(self: Clock) -> Timeline

"""


    Completed = None
    CurrentGlobalSpeedInvalidated = None
    CurrentStateInvalidated = None
    CurrentTimeInvalidated = None
    RemoveRequested = None

