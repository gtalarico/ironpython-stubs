class Duration(object):
 """
 Represents the duration of time that a System.Windows.Media.Animation.Timeline is active.
 
 Duration(timeSpan: TimeSpan)
 """
 def Add(self,duration):
  """
  Add(self: Duration,duration: Duration) -> Duration
  
   Adds the value of the specified instance of System.Windows.Duration to the 
    value of the current instance.
  
  
   duration: An instance of System.Windows.Duration that represents the value of the current 
    instance plus duration.
  
   Returns: If both instances of System.Windows.Duration have values,an instance of 
    System.Windows.Duration that represents the combined values. Otherwise this 
    method returns null.
  """
  pass
 @staticmethod
 def Compare(t1,t2):
  """
  Compare(t1: Duration,t2: Duration) -> int
  
   Compares one System.Windows.Duration value to another.
  
   t1: The first instance of System.Windows.Duration to compare.
   t2: The second instance of System.Windows.Duration to compare.
   Returns: If t1 is less than t2,a negative value that represents the difference. If t1 
    is equal to t2,zero. If t1 is greater than t2,a positive value that 
    represents the difference.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(t1: Duration,t2: Duration) -> bool
  
   Determines whether two instances of System.Windows.Duration are equal.
  
   t1: First instance of System.Windows.Duration to compare.
   t2: Second instance of System.Windows.Duration to compare.
   Returns: true if t1 is equal to t2; otherwise,false.
  Equals(self: Duration,duration: Duration) -> bool
  
   Determines whether a specified System.Windows.Duration is equal to this 
    instance of System.Windows.Duration.
  
  
   duration: Instance of System.Windows.Duration to check for equality.
   Returns: true if duration is equal to the current instance of System.Windows.Duration; 
    otherwise,false.
  
  Equals(self: Duration,value: object) -> bool
  
   Determines whether a specified object is equal to an instance of 
    System.Windows.Duration.
  
  
   value: Object to check for equality.
   Returns: true if value is equal to the current instance of Duration; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Duration) -> int
  
   Gets a hash code for this instance.
   Returns: A signed 32-bit integer hash code.
  """
  pass
 @staticmethod
 def Plus(duration):
  """
  Plus(duration: Duration) -> Duration
  
   Returns the specified instance of System.Windows.Duration.
  
   duration: The instance of System.Windows.Duration to get.
   Returns: An instance of System.Windows.Duration.
  """
  pass
 def Subtract(self,duration):
  """
  Subtract(self: Duration,duration: Duration) -> Duration
  
   Subtracts the value of the specified instance of System.Windows.Duration from 
    this instance.
  
  
   duration: The instance of System.Windows.Duration to subtract from the current instance.
   Returns: A new instance of System.Windows.Duration whose value is the result of this 
    instance minus the value of duration.
  """
  pass
 def ToString(self):
  """
  ToString(self: Duration) -> str
  
   Converts an instance of System.Windows.Duration to a System.String 
    representation.
  
   Returns: A System.String representation of this instance of System.Windows.Duration.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 @staticmethod
 def __new__(self,timeSpan):
  """
  __new__[Duration]() -> Duration
  
  __new__(cls: type,timeSpan: TimeSpan)
  """
  pass
 def __ne__(self,*args):
  pass
 def __pos__(self,*args):
  """
  __pos__(duration: Duration) -> Duration
  
   Returns the specified instance of System.Windows.Duration.
  
   duration: The instance of System.Windows.Duration to get.
   Returns: An instance of System.Windows.Duration.
  """
  pass
 def __radd__(self,*args):
  """
  __radd__(t1: Duration,t2: Duration) -> Duration
  
   Adds two instances of System.Windows.Duration together.
  
   t1: The first instance of System.Windows.Duration to add.
   t2: The second instance of System.Windows.Duration to add.
   Returns: If both instances of System.Windows.Duration have System.TimeSpan values,this 
    method returns the sum of those two values. If either value is set to 
    System.Windows.Duration.Automatic,the method returns 
    System.Windows.Duration.Automatic. If either value is set to 
    System.Windows.Duration.Forever,the method returns 
    System.Windows.Duration.Forever.If either t1 or t2 has no value,this method 
    returns null.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(t1: Duration,t2: Duration) -> Duration
  
   Subtracts the value of one instance of System.Windows.Duration from another.
  
   t1: The first instance of System.Windows.Duration.
   t2: The instance of System.Windows.Duration to subtract.
   Returns: If both instances of System.Windows.Duration have values,an instance of 
    System.Windows.Duration that represents the value of t1 minus t2. If t1 has a 
    value of System.Windows.Duration.Forever and t2 has a value of 
    System.Windows.Duration.TimeSpan,this method returns 
    System.Windows.Duration.Forever. Otherwise this method returns null.
  """
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 HasTimeSpan=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates if this System.Windows.Duration represents a System.TimeSpan value.

Get: HasTimeSpan(self: Duration) -> bool

"""

 TimeSpan=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.TimeSpan value that this System.Windows.Duration represents.

Get: TimeSpan(self: Duration) -> TimeSpan

"""


 Automatic=None
 Forever=None

