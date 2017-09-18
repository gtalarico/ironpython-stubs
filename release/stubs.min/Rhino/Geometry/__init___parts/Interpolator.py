class Interpolator(RhinoList[float],IList[float],ICollection[float],IEnumerable[float],IEnumerable,IList,ICollection):
 """
 Exposes a set of standard numeric interpolation algorithms.

 

 Interpolator()

 Interpolator(initialCapacity: int)

 Interpolator(list: RhinoList[float])

 Interpolator(collection: IEnumerable[float])

 Interpolator(amount: int,defaultValue: float)
 """
 def InterpolateCatmullRom(self,t):
  """
  InterpolateCatmullRom(self: Interpolator,t: float) -> float

  

   Sample the list of numbers with Catmull-Rom interpolation.

  

   t: Parameter to sample at. The integer portion of the parameter 

     indicates the index 

    of the left-hand value. If this Interpolator is cyclical,

     parameters will be 

    wrapped.

  

   Returns: The sampled value at t.
  """
  pass
 def InterpolateCosine(self,t):
  """
  InterpolateCosine(self: Interpolator,t: float) -> float

  

   Sample the list of numbers with cosine interpolation.

  

   t: Parameter to sample at. The integer portion of the parameter 

     indicates the index 

    of the left-hand value. If this Interpolator is cyclical,

     parameters will be 

    wrapped.

  

   Returns: The sampled value at t.
  """
  pass
 def InterpolateCubic(self,t):
  """
  InterpolateCubic(self: Interpolator,t: float) -> float

  

   Sample the list of numbers with cubic interpolation.

  

   t: Parameter to sample at. The integer portion of the parameter 

     indicates the index 

    of the left-hand value. If this Interpolator is cyclical,

     parameters will be 

    wrapped.

  

   Returns: The sampled value at t.
  """
  pass
 def InterpolateLinear(self,t):
  """
  InterpolateLinear(self: Interpolator,t: float) -> float

  

   Sample the list of numbers with linear interpolation.

  

   t: Parameter to sample at. The integer portion of the parameter 

     indicates the index 

    of the left-hand value. If this Interpolator is cyclical,

     parameters will be 

    wrapped.

  

   Returns: The sampled value at t.
  """
  pass
 def InterpolateNearestNeighbour(self,t):
  """
  InterpolateNearestNeighbour(self: Interpolator,t: float) -> float

  

   Sample the list of numbers with Nearest Neighbour interpolation.

  

   t: Parameter to sample at. The integer portion of the parameter 

     indicates the index 

    of the left-hand value. If this Interpolator is cyclical,

     parameters will be 

    wrapped.

  

   Returns: The sampled value at t.
  """
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
 """Gets or sets a value indicating whether or not the values inside this Interpolator 

   are to be treated as cyclical (i.e. circular).



Get: Cyclical(self: Interpolator) -> bool



Set: Cyclical(self: Interpolator)=value

"""


