class Interval(object,ISerializable,IEquatable[Interval],IComparable[Interval],IComparable,IEpsilonComparable[Interval]):
 """
 Interval(t0: float,t1: float)
 Interval(other: Interval)
 """
 def CompareTo(self,other):
  """ CompareTo(self: Interval,other: Interval) -> int """
  pass
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Interval,other: Interval,epsilon: float) -> bool """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Interval,other: Interval) -> bool
  Equals(self: Interval,obj: object) -> bool
  """
  pass
 @staticmethod
 def FromIntersection(a,b):
  """ FromIntersection(a: Interval,b: Interval) -> Interval """
  pass
 @staticmethod
 def FromUnion(a,b):
  """ FromUnion(a: Interval,b: Interval) -> Interval """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Interval) -> int """
  pass
 def Grow(self,value):
  """ Grow(self: Interval,value: float) """
  pass
 def IncludesInterval(self,interval,strict=None):
  """
  IncludesInterval(self: Interval,interval: Interval,strict: bool) -> bool
  IncludesInterval(self: Interval,interval: Interval) -> bool
  """
  pass
 def IncludesParameter(self,t,strict=None):
  """
  IncludesParameter(self: Interval,t: float,strict: bool) -> bool
  IncludesParameter(self: Interval,t: float) -> bool
  """
  pass
 def MakeIncreasing(self):
  """ MakeIncreasing(self: Interval) """
  pass
 def NormalizedIntervalAt(self,intervalParameter):
  """ NormalizedIntervalAt(self: Interval,intervalParameter: Interval) -> Interval """
  pass
 def NormalizedParameterAt(self,intervalParameter):
  """ NormalizedParameterAt(self: Interval,intervalParameter: float) -> float """
  pass
 def ParameterAt(self,normalizedParameter):
  """ ParameterAt(self: Interval,normalizedParameter: float) -> float """
  pass
 def ParameterIntervalAt(self,normalizedInterval):
  """ ParameterIntervalAt(self: Interval,normalizedInterval: Interval) -> Interval """
  pass
 def Reverse(self):
  """ Reverse(self: Interval) """
  pass
 def Swap(self):
  """ Swap(self: Interval) """
  pass
 def ToString(self):
  """ ToString(self: Interval) -> str """
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
  """ __radd__(number: float,interval: Interval) -> Interval """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rsub__(self,*args):
  """ __rsub__(number: float,interval: Interval) -> Interval """
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
 """Get: IsDecreasing(self: Interval) -> bool

"""

 IsIncreasing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsIncreasing(self: Interval) -> bool

"""

 IsSingleton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSingleton(self: Interval) -> bool

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: Interval) -> bool

"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Length(self: Interval) -> float

"""

 Max=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Max(self: Interval) -> float

"""

 Mid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Mid(self: Interval) -> float

"""

 Min=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Min(self: Interval) -> float

"""

 T0=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: T0(self: Interval) -> float

Set: T0(self: Interval)=value
"""

 T1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: T1(self: Interval) -> float

Set: T1(self: Interval)=value
"""


 Unset=None

