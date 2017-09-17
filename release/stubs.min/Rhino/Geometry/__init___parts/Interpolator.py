class Interpolator(RhinoList[float],IList[float],ICollection[float],IEnumerable[float],IEnumerable,IList,ICollection):
 """
 Interpolator()
 Interpolator(initialCapacity: int)
 Interpolator(list: RhinoList[float])
 Interpolator(collection: IEnumerable[float])
 Interpolator(amount: int,defaultValue: float)
 """
 def InterpolateCatmullRom(self,t):
  """ InterpolateCatmullRom(self: Interpolator,t: float) -> float """
  pass
 def InterpolateCosine(self,t):
  """ InterpolateCosine(self: Interpolator,t: float) -> float """
  pass
 def InterpolateCubic(self,t):
  """ InterpolateCubic(self: Interpolator,t: float) -> float """
  pass
 def InterpolateLinear(self,t):
  """ InterpolateLinear(self: Interpolator,t: float) -> float """
  pass
 def InterpolateNearestNeighbour(self,t):
  """ InterpolateNearestNeighbour(self: Interpolator,t: float) -> float """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,initialCapacity: int)
  __new__(cls: type,list: RhinoList[float])
  __new__(cls: type,collection: IEnumerable[float])
  __new__(cls: type,amount: int,defaultValue: float)
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Cyclical=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Cyclical(self: Interpolator) -> bool

Set: Cyclical(self: Interpolator)=value
"""


