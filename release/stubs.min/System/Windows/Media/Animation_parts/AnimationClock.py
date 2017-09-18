class AnimationClock(Clock):
 """ Maintains the run-time state of an System.Windows.Media.Animation.AnimationTimeline and processes its output values. """
 def GetCurrentValue(self,defaultOriginValue,defaultDestinationValue):
  """
  GetCurrentValue(self: AnimationClock,defaultOriginValue: object,defaultDestinationValue: object) -> object

  

   Gets the current output value of the System.Windows.Media.Animation.AnimationClock.

  

   defaultOriginValue: The origin value provided to the clock if its animation does not have its own start value. If 

    this clock is the first in a composition chain it will be the base value of the property being 

    animated; otherwise it will be the value returned by the previous clock in the chain

  

   defaultDestinationValue: The destination value provided to the clock if its animation does not have its own destination 

    value. If this clock is the first in a composition chain it will be the base value of the 

    property being animated; otherwise it will be the value returned by the previous clock in the 

    chain

  

   Returns: The current value of this System.Windows.Media.Animation.AnimationClock.
  """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,animation: AnimationTimeline) """
  pass
 CurrentGlobalTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current global time,as established by the WPF timing system.



"""

 Timeline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Media.Animation.AnimationTimeline that describes this clock's behavior.



Get: Timeline(self: AnimationClock) -> AnimationTimeline



"""


