class ClockGroup(Clock):
    """ An assemblage of System.Windows.Media.Animation.Clock types with behavior based off of a System.Windows.Media.Animation.TimelineGroup. """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, timelineGroup: TimelineGroup) """
        pass

    Children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the children collection of this System.Windows.Media.Animation.ClockGroup.

Get: Children(self: ClockGroup) -> ClockCollection

"""

    CurrentGlobalTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current global time, as established by the WPF timing system.

"""

    Timeline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.Animation.TimelineGroup object that dictates the behavior of this System.Windows.Media.Animation.ClockGroup instance.

Get: Timeline(self: ClockGroup) -> TimelineGroup

"""


