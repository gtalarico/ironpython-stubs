class ClockController(DispatcherObject):
 """ Interactively controls a System.Windows.Media.Animation.Clock. """
 def Begin(self):
  """
  Begin(self: ClockController)

   Sets the target System.Windows.Media.Animation.ClockController.Clock to begin at the next tick.
  """
  pass
 def Pause(self):
  """
  Pause(self: ClockController)

   Stops the target System.Windows.Media.Animation.Clock from progressing.
  """
  pass
 def Remove(self):
  """
  Remove(self: ClockController)

   Removes the System.Windows.Media.Animation.Clock associated with this 

    System.Windows.Media.Animation.ClockController from the properties it animates. The clock and 

    its child clocks will no longer affect these properties.
  """
  pass
 def Resume(self):
  """
  Resume(self: ClockController)

   Enables a System.Windows.Media.Animation.Clock that was previously paused to resume progressing.
  """
  pass
 def Seek(self,offset,origin):
  """
  Seek(self: ClockController,offset: TimeSpan,origin: TimeSeekOrigin)

   Seeks the target System.Windows.Media.Animation.ClockController.Clock by the specified amount 

    when the next tick occurs. If the target clock is stopped,seeking makes it active again.

  

  

   offset: The seek offset,measured in the target clock's time. This offset is relative to the clock's 

    System.Windows.Media.Animation.TimeSeekOrigin.BeginTime or 

    System.Windows.Media.Animation.TimeSeekOrigin.Duration,depending on the value of origin.

  

   origin: A value that indicates whether the specified offset is relative to the target clock's 

    System.Windows.Media.Animation.TimeSeekOrigin.BeginTime or 

    System.Windows.Media.Animation.TimeSeekOrigin.Duration.
  """
  pass
 def SeekAlignedToLastTick(self,offset,origin):
  """
  SeekAlignedToLastTick(self: ClockController,offset: TimeSpan,origin: TimeSeekOrigin)

   Seeks the target System.Windows.Media.Animation.Clock by the specified amount immediately. If 

    the target clock is stopped,seeking makes it active again.

  

  

   offset: The seek offset,measured in the target clock's time. This offset is relative to the clock's 

    System.Windows.Media.Animation.TimeSeekOrigin.BeginTime or 

    System.Windows.Media.Animation.TimeSeekOrigin.Duration,depending on the value of origin.

  

   origin: A value that indicates whether the specified offset is relative to the target clock's 

    System.Windows.Media.Animation.TimeSeekOrigin.BeginTime or 

    System.Windows.Media.Animation.TimeSeekOrigin.Duration.
  """
  pass
 def SkipToFill(self):
  """
  SkipToFill(self: ClockController)

   Advances the current time of the target System.Windows.Media.Animation.Clock to the end of its 

    active period.
  """
  pass
 def Stop(self):
  """
  Stop(self: ClockController)

   Stops the target System.Windows.Media.Animation.Clock.
  """
  pass
 Clock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Media.Animation.Clock controlled by this System.Windows.Media.Animation.ClockController.



Get: Clock(self: ClockController) -> Clock



"""

 SpeedRatio=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the interactive speed of the target System.Windows.Media.Animation.Clock.



Get: SpeedRatio(self: ClockController) -> float



Set: SpeedRatio(self: ClockController)=value

"""


