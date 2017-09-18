class BrepTrim(CurveProxy,IDisposable,ISerializable):
 """
 Brep trim information is stored in BrepTrim classes. Brep.Trims is an

    array of all the trims in the brep. A BrepTrim is derived from CurveProxy

    so the trim can supply easy to use evaluation tools via the Curve virtual

    member functions.

    Note well that the domains and orientations of the curve m_C2[trim.m_c2i]

    and the trim as a curve may not agree.
 """
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Curve,disposing: bool)

   For derived class implementers.

     This method is called with argument true when class 

    user calls Dispose(),while with argument false when

     the Garbage Collector invokes 

    the finalizer,or Finalize() method.You must reclaim all used unmanaged resources in both cases,

    and can use this chance to call Dispose on disposable fields if the argument is true.Also,you 

    must call the base virtual method within your overriding method.

  

  

   disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 

    finalizer.
  """
  pass
 def GetTolerances(self,toleranceU,toleranceV):
  """
  GetTolerances(self: BrepTrim) -> (float,float)

  

   The values in tolerance[] record the accuracy of the parameter space

      trimming 

    curves.
  """
  pass
 def GetTrimParameter(self,edgeParameter,trimParameter):
  """
  GetTrimParameter(self: BrepTrim,edgeParameter: float) -> (bool,float)

  

   Get corresponding trim parameter at given edge parameter.

   Returns: true on success
  """
  pass
 def IsReversed(self):
  """
  IsReversed(self: BrepTrim) -> bool

  

   Get orientation of trim with respect to it's corresponding edge.

   Returns: true if the 2d trim and 3d edge have opposite orientations
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: Curve)

   For derived classes implementers.

     Defines the necessary implementation to free the 

    instance from being const.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
  """
  pass
 def SetTolerances(self,toleranceU,toleranceV):
  """
  SetTolerances(self: BrepTrim,toleranceU: float,toleranceV: float)

   The values in tolerance[] record the accuracy of the parameter space

      trimming 

    curves.
  """
  pass
 def SetTrimCurve(self,curve2dIndex,subDomain=None):
  """
  SetTrimCurve(self: BrepTrim,curve2dIndex: int,subDomain: Interval) -> bool

  

   Set 2d curve geometry used by a b-rep trim.

  

   curve2dIndex: index of 2d curve in m_C2[] array

   Returns: true if successful

  SetTrimCurve(self: BrepTrim,curve2dIndex: int) -> bool

  

   Set 2d curve geometry used by a b-rep trim.

  

   curve2dIndex: index of 2d curve in m_C2[] array

   Returns: true if successful
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Brep=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Brep that owns this trim.



Get: Brep(self: BrepTrim) -> Brep



"""

 Edge=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Brep edge this trim belongs to. This will be null for singular trims



Get: Edge(self: BrepTrim) -> BrepEdge



"""

 Face=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Brep face this trim belongs to



Get: Face(self: BrepTrim) -> BrepFace



"""

 IsoStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """



Get: IsoStatus(self: BrepTrim) -> IsoStatus



Set: IsoStatus(self: BrepTrim)=value

"""

 Loop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Loop that this trim belongs to



Get: Loop(self: BrepTrim) -> BrepLoop



"""

 TrimIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of this trim in the Brep.Trims collection.



Get: TrimIndex(self: BrepTrim) -> int



"""

 TrimType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Type of trim



Get: TrimType(self: BrepTrim) -> BrepTrimType



Set: TrimType(self: BrepTrim)=value

"""


