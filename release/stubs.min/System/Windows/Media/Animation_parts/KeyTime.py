class KeyTime(object,IEquatable[KeyTime]):
 """ During the relative course of an animation,a System.Windows.Media.Animation.KeyTime instance specifies the precise timing when a particular key frame should take place. """
 def Equals(self,*__args):
  """
  Equals(self: KeyTime,value: KeyTime) -> bool

  

   Indicates whether this instance is equal to the specified System.Windows.Media.Animation.KeyTime.

  

   value: The object to compare with this instance.

   Returns: true if value is equal to this instance; otherwise,false.

  Equals(keyTime1: KeyTime,keyTime2: KeyTime) -> bool

  

   Indicates whether the two specified System.Windows.Media.Animation.KeyTime structures are equal.

  

   keyTime1: The first value to compare.

   keyTime2: The second value to compare.

   Returns: true if the values of keyTime1 and keyTime2 are equal; otherwise false.

  Equals(self: KeyTime,value: object) -> bool

  

   Indicates whether this instance equals the specified object.

  

   value: The object to compare with this instance.

   Returns: true if value is a System.Windows.Media.Animation.KeyTime that represents the same length of 

    time as this instance; otherwise false.
  """
  pass
 @staticmethod
 def FromPercent(percent):
  """
  FromPercent(percent: float) -> KeyTime

  

   Creates a new System.Windows.Media.Animation.KeyTime instance,with the 

    System.Windows.Media.Animation.KeyTimeType property initialized to the value of the specified 

    parameter.

  

  

   percent: The value of the new System.Windows.Media.Animation.KeyTime.

   Returns: A new System.Windows.Media.Animation.KeyTime instance,initialized to the value of percent.
  """
  pass
 @staticmethod
 def FromTimeSpan(timeSpan):
  """
  FromTimeSpan(timeSpan: TimeSpan) -> KeyTime

  

   Creates a new System.Windows.Media.Animation.KeyTime instance,with the 

    System.Windows.Media.Animation.KeyTimeType property initialized to the value of the specified 

    parameter.

  

  

   timeSpan: The value of the new System.Windows.Media.Animation.KeyTime.

   Returns: A new System.Windows.Media.Animation.KeyTime instance,initialized to the value of timeSpan.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: KeyTime) -> int

  

   Returns an integer hash code representing this instance.

   Returns: An integer hash code.
  """
  pass
 def ToString(self):
  """
  ToString(self: KeyTime) -> str

  

   Returns a string representing this System.Windows.Media.Animation.KeyTime instance.

   Returns: A string representation of this instance.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Percent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time when the key frame ends expressed as a percentage of the total duration of the animation.



Get: Percent(self: KeyTime) -> float



"""

 TimeSpan=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time when the key frame ends expressed as a time relative to the beginning of the animation.



Get: TimeSpan(self: KeyTime) -> TimeSpan



"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Media.Animation.KeyTime.Type value this instance represents.



Get: Type(self: KeyTime) -> KeyTimeType



"""


 Paced=None
 Uniform=None

