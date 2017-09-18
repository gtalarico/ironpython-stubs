class RepeatBehavior(object,IFormattable):
 """
 Describes how a System.Windows.Media.Animation.Timeline repeats its simple duration.

 

 RepeatBehavior(count: float)

 RepeatBehavior(duration: TimeSpan)
 """
 def Equals(self,*__args):
  """
  Equals(repeatBehavior1: RepeatBehavior,repeatBehavior2: RepeatBehavior) -> bool

  

   Indicates whether the two specified System.Windows.Media.Animation.RepeatBehavior structures are 

    equal.

  

  

   repeatBehavior1: The first value to compare.

   repeatBehavior2: The second value to compare.

   Returns: true if both the type and repeat behavior of repeatBehavior1 are equal to that of 

    repeatBehavior2; otherwise,false.

  

  Equals(self: RepeatBehavior,repeatBehavior: RepeatBehavior) -> bool

  

   Returns a value that indicates whether this instance is equal to the specified 

    System.Windows.Media.Animation.RepeatBehavior.

  

  

   repeatBehavior: The value to compare to this instance.

   Returns: true if both the type and repeat behavior of repeatBehavior are equal to this instance; 

    otherwise,false.

  

  Equals(self: RepeatBehavior,value: object) -> bool

  

   Indicates whether this instance is equal to the specified object.

  

   value: The object to compare with this instance.

   Returns: true if value is a System.Windows.Media.Animation.RepeatBehavior that represents the same repeat 

    behavior as this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: RepeatBehavior) -> int

  

   Returns the hash code of this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def ToString(self,formatProvider=None):
  """
  ToString(self: RepeatBehavior,formatProvider: IFormatProvider) -> str

  

   Returns a string representation of this System.Windows.Media.Animation.RepeatBehavior instance 

    with the specified format.

  

  

   formatProvider: The format used to construct the return value.

   Returns: A string representation of this instance.

  ToString(self: RepeatBehavior) -> str

  

   Returns a string representation of this System.Windows.Media.Animation.RepeatBehavior instance.

   Returns: A string representation of this instance.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,count: float)

  __new__(cls: type,duration: TimeSpan)

  __new__[RepeatBehavior]() -> RepeatBehavior
  """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of times a System.Windows.Media.Animation.Timeline should repeat.



Get: Count(self: RepeatBehavior) -> float



"""

 Duration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total length of time a System.Windows.Media.Animation.Timeline should play.



Get: Duration(self: RepeatBehavior) -> TimeSpan



"""

 HasCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the repeat behavior has a specified iteration count.



Get: HasCount(self: RepeatBehavior) -> bool



"""

 HasDuration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the repeat behavior has a specified repeat duration.



Get: HasDuration(self: RepeatBehavior) -> bool



"""


 Forever=None

