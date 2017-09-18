class Interval(object,ISerializable,IEquatable[Interval],IComparable[Interval],IComparable,IEpsilonComparable[Interval]):
 """
 Represents an interval in one-dimensional space,

    that is defined as two extrema or bounds.

 

 Interval(t0: float,t1: float)

 Interval(other: Interval)
 """
 def CompareTo(self,other):
  """
  CompareTo(self: Interval,other: Interval) -> int

  

   Compares this Rhino.Geometry.Interval with another interval.

      The lower bound has 

    first evaluation priority.

  

  

   other: The other Rhino.Geometry.Interval to compare with.

   Returns: 0: if this is identical to other-1: if this[0] < other[0]+1: if this[0] > other[0]-1: if this[0] 

    == other[0] and this[1] < other[1]+1: if this[0] == other[0] and this[1] > other[1].
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Interval,other: Interval,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Interval,other: Interval) -> bool

  

   Determines whether the specified Rhino.Geometry.Interval is equal to the current 

    Rhino.Geometry.Interval,

     comparing by value.

  

  

   other: The other interval to compare with.

   Returns: true if obj is an Rhino.Geometry.Interval and has the same bounds; false otherwise.

  Equals(self: Interval,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to the current Rhino.Geometry.Interval,

  

       comparing by value.

  

  

   obj: The other object to compare with.

   Returns: true if obj is an Rhino.Geometry.Interval and has the same bounds; false otherwise.
  """
  pass
 @staticmethod
 def FromIntersection(a,b):
  """
  FromIntersection(a: Interval,b: Interval) -> Interval

  

   Returns a new Interval that is the Intersection of the two input Intervals.

  

   a: The first input interval.

   b: The second input interval.

   Returns: If the intersection is not empty,then 

     intersection=[max(a.Min(),b.Min()),

    min(a.Max(),b.Max())]

     The interval [ON.UnsetValue,ON.UnsetValue] is considered to 

    be

     the empty set interval.  The result of any intersection involving an

       

     empty set interval or disjoint intervals is the empty set interval.
  """
  pass
 @staticmethod
 def FromUnion(a,b):
  """
  FromUnion(a: Interval,b: Interval) -> Interval

  

   Returns a new Interval which contains both inputs.

  

   a: The first input interval.

   b: The second input interval.

   Returns: The union of an empty set and an increasing interval is the increasing interval.

     

    The union of two empty sets is empty.The union of an empty set an a non-empty interval is the 

    non-empty interval.The union of two non-empty intervals is [min(a.Min(),b.Min()),

    max(a.Max(),b.Max())]
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Interval) -> int

  

   Computes the hash code for this Rhino.Geometry.Interval object.

   Returns: A hash value that might be equal for two different Rhino.Geometry.Interval values.
  """
  pass
 def Grow(self,value):
  """
  Grow(self: Interval,value: float)

   Grows the Rhino.Geometry.Interval to include the given number.

  

   value: Number to include in this interval.
  """
  pass
 def IncludesInterval(self,interval,strict=None):
  """
  IncludesInterval(self: Interval,interval: Interval,strict: bool) -> bool

  

   Tests another interval for Interval inclusion.

  

   interval: Interval to test.

   strict: If true,the other interval must be fully on the inside of the Interval.

   Returns: true if the other interval is contained within the limits of this Interval; otherwise false.

  IncludesInterval(self: Interval,interval: Interval) -> bool

  

   Tests another interval for Interval inclusion.

  

   interval: Interval to test.

   Returns: true if the other interval is contained within or is coincident with the limits of this 

    Interval; otherwise false.
  """
  pass
 def IncludesParameter(self,t,strict=None):
  """
  IncludesParameter(self: Interval,t: float,strict: bool) -> bool

  

   Tests a parameter for Interval inclusion.

  

   t: Parameter to test.

   strict: If true,the parameter must be fully on the inside of the Interval.

   Returns: true if t is contained within the limits of this Interval.

  IncludesParameter(self: Interval,t: float) -> bool

  

   Tests a parameter for Interval inclusion.

  

   t: Parameter to test.

   Returns: true if t is contained within or is coincident with the limits of this Interval.
  """
  pass
 def MakeIncreasing(self):
  """
  MakeIncreasing(self: Interval)

   Ensures this Rhino.Geometry.Interval is either singleton or increasing.
  """
  pass
 def NormalizedIntervalAt(self,intervalParameter):
  """
  NormalizedIntervalAt(self: Interval,intervalParameter: Interval) -> Interval

  

   Converts interval value,or pair of values,to normalized parameter.

   Returns: Normalized parameter x so that min*(1.0-x) + max*x=intervalParameter.
  """
  pass
 def NormalizedParameterAt(self,intervalParameter):
  """
  NormalizedParameterAt(self: Interval,intervalParameter: float) -> float

  

   Converts interval value,or pair of values,to normalized parameter.

   Returns: Normalized parameter x so that min*(1.0-x) + max*x=intervalParameter.
  """
  pass
 def ParameterAt(self,normalizedParameter):
  """
  ParameterAt(self: Interval,normalizedParameter: float) -> float

  

   Converts normalized parameter to interval value,or pair of values.

   Returns: Interval parameter min*(1.0-normalizedParameter) + max*normalizedParameter.
  """
  pass
 def ParameterIntervalAt(self,normalizedInterval):
  """
  ParameterIntervalAt(self: Interval,normalizedInterval: Interval) -> Interval

  

   Converts normalized parameter to interval value,or pair of values.

   Returns: Interval parameter min*(1.0-normalizedParameter) + max*normalized_paramete.
  """
  pass
 def Reverse(self):
  """
  Reverse(self: Interval)

   Changes interval to [-T1,-T0].
  """
  pass
 def Swap(self):
  """
  Swap(self: Interval)

   Exchanges T0 and T1.
  """
  pass
 def ToString(self):
  """
  ToString(self: Interval) -> str

  

   Returns a string representation of this Rhino.Geometry.Interval.

   Returns: A string with T0,T1.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Interval]() -> Interval

  

  __new__(cls: type,t0: float,t1: float)

  __new__(cls: type,other: Interval)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(number: float,interval: Interval) -> Interval

  

   Shifts an interval by a specific amount (addition).

  

   number: The shifting value.

   interval: The interval to be used as a base.

   Returns: A new interval where T0 and T1 are summed with number.
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(number: float,interval: Interval) -> Interval

  

   Shifts an interval by a specific amount (subtraction).

  

   number: The shifting value to subtract from (minuend).

   interval: The interval to be subtracted from (subtrahend).

   Returns: A new interval with [number-T0,number-T1].
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 IsDecreasing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns true if T[0] > T[1].



Get: IsDecreasing(self: Interval) -> bool



"""

 IsIncreasing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns true if T0 < T1.



Get: IsIncreasing(self: Interval) -> bool



"""

 IsSingleton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns true if T0 == T1 != ON.UnsetValue.



Get: IsSingleton(self: Interval) -> bool



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this Interval is valid. 

   Valid intervals must contain valid numbers.



Get: IsValid(self: Interval) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the signed length of the numeric range. 

   If the interval is decreasing,a negative length will be returned.



Get: Length(self: Interval) -> float



"""

 Max=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the larger of T0 and T1.



Get: Max(self: Interval) -> float



"""

 Mid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the average of T0 and T1.



Get: Mid(self: Interval) -> float



"""

 Min=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the smaller of T0 and T1.



Get: Min(self: Interval) -> float



"""

 T0=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the lower bound of the Interval.



Get: T0(self: Interval) -> float



Set: T0(self: Interval)=value

"""

 T1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the upper bound of the Interval.



Get: T1(self: Interval) -> float



Set: T1(self: Interval)=value

"""


 Unset=None

