class MediaClock(Clock):
 """ Maintains the timing state for media through a System.Windows.Media.MediaTimeline. """
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,media: MediaTimeline) """
  pass
 CurrentGlobalTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current global time,as established by the WPF timing system.

"""

 Timeline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Media.MediaTimeline that describes the controlling behavior of the clock.

Get: Timeline(self: MediaClock) -> MediaTimeline

"""


