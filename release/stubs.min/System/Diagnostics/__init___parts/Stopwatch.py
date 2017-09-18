class Stopwatch(object):
 """
 Provides a set of methods and properties that you can use to accurately measure elapsed time.

 

 Stopwatch()
 """
 @staticmethod
 def GetTimestamp():
  """
  GetTimestamp() -> Int64

  

   Gets the current number of ticks in the timer mechanism.

   Returns: A long integer representing the tick counter value of the underlying timer mechanism.
  """
  pass
 def Reset(self):
  """
  Reset(self: Stopwatch)

   Stops time interval measurement and resets the elapsed time to zero.
  """
  pass
 def Restart(self):
  """
  Restart(self: Stopwatch)

   Stops time interval measurement,resets the elapsed time to zero,and starts measuring elapsed 

    time.
  """
  pass
 def Start(self):
  """
  Start(self: Stopwatch)

   Starts,or resumes,measuring elapsed time for an interval.
  """
  pass
 @staticmethod
 def StartNew():
  """
  StartNew() -> Stopwatch

  

   Initializes a new System.Diagnostics.Stopwatch instance,sets the elapsed time property to zero,

    and starts measuring elapsed time.

  

   Returns: A System.Diagnostics.Stopwatch that has just begun measuring elapsed time.
  """
  pass
 def Stop(self):
  """
  Stop(self: Stopwatch)

   Stops measuring elapsed time for an interval.
  """
  pass
 Elapsed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total elapsed time measured by the current instance.



Get: Elapsed(self: Stopwatch) -> TimeSpan



"""

 ElapsedMilliseconds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total elapsed time measured by the current instance,in milliseconds.



Get: ElapsedMilliseconds(self: Stopwatch) -> Int64



"""

 ElapsedTicks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total elapsed time measured by the current instance,in timer ticks.



Get: ElapsedTicks(self: Stopwatch) -> Int64



"""

 IsRunning=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Diagnostics.Stopwatch timer is running.



Get: IsRunning(self: Stopwatch) -> bool



"""


 Frequency=None
 IsHighResolution=True

