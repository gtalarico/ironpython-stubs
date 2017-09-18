class PolyCurve(Curve,IDisposable,ISerializable):
 """
 Represents a curve that is the result of joining several (possibly different)

    types of curves.

 

 PolyCurve()
 """
 def Append(self,*__args):
  """
  Append(self: PolyCurve,curve: Curve) -> bool

  

   Appends and matches the start of the curve to the end of polycurve. 

     This function 

    will fail if the PolyCurve is closed or if SegmentCount > 0 and the new segment is closed.

  

  

   curve: Segment to append.

   Returns: true on success,false on failure.

  Append(self: PolyCurve,arc: Arc) -> bool

  

   Appends and matches the start of the arc to the end of polycurve. 

     This function 

    will fail if the polycurve is closed or if SegmentCount > 0 and the arc is closed.

  

  

   arc: Arc segment to append.

   Returns: true on success,false on failure.

  Append(self: PolyCurve,line: Line) -> bool

  

   Appends and matches the start of the line to the end of polycurve. 

     This function 

    will fail if the polycurve is closed.

  

  

   line: Line segment to append.

   Returns: true on success,false on failure.
  """
  pass
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
 def Duplicate(self):
  """
  Duplicate(self: PolyCurve) -> GeometryBase

  

   Duplicates this polycurve.

     When not overridden in a derived class,this calls 

    Rhino.Geometry.PolyCurve.DuplicatePolyCurve.

  

   Returns: An exact duplicate of this curve.
  """
  pass
 def DuplicatePolyCurve(self):
  """
  DuplicatePolyCurve(self: PolyCurve) -> PolyCurve

  

   Duplicates this polycurve.

     This is the same as Rhino.Geometry.PolyCurve.Duplicate.

   Returns: An exact duplicate of this curve.
  """
  pass
 def Explode(self):
  """
  Explode(self: PolyCurve) -> Array[Curve]

  

   Explodes this PolyCurve into a list of Curve segments. This will not explode nested polycurves. 


    
     Call Rhino.Geometry.PolyCurve.RemoveNesting first if you need all individual 

    segments.

  

   Returns: An array of polycurve segments.
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
 def PolyCurveParameter(self,segmentIndex,segmentCurveParameter):
  """
  PolyCurveParameter(self: PolyCurve,segmentIndex: int,segmentCurveParameter: float) -> float

  

   Converts a segment curve parameter to a polycurve parameter.

  

   segmentIndex: Index of segment.

   segmentCurveParameter: Parameter on segment.

   Returns: Polycurve evaluation parameter or UnsetValue if the polycurve curve parameter could not be 

    computed.
  """
  pass
 def RemoveNesting(self):
  """
  RemoveNesting(self: PolyCurve) -> bool

  

   Explodes nested polycurve segments and reconstructs this curve from the shattered remains. 

   

      The result will have not have any PolyCurves as segments but it will have identical 

     

       locus and parameterization.

  

   Returns: true if any nested PolyCurve was found and absorbed,false if no PolyCurve segments could be 

    found.
  """
  pass
 def SegmentCurve(self,index):
  """
  SegmentCurve(self: PolyCurve,index: int) -> Curve

  

   Gets the segment curve at the given index.

  

   index: Index of segment to retrieve.

   Returns: The segment at the given index or null on failure.
  """
  pass
 def SegmentCurveParameter(self,polycurveParameter):
  """
  SegmentCurveParameter(self: PolyCurve,polycurveParameter: float) -> float

  

   Converts a polycurve parameter to a segment curve parameter.

  

   polycurveParameter: Parameter on PolyCurve to convert.

   Returns: Segment curve evaluation parameter or UnsetValue if the 

     segment curve parameter 

    could not be computed.
  """
  pass
 def SegmentDomain(self,segmentIndex):
  """
  SegmentDomain(self: PolyCurve,segmentIndex: int) -> Interval

  

   Returns the polycurve subdomain assigned to a segment curve.

  

   segmentIndex: Index of segment.

   Returns: The polycurve subdomain assigned to a segment curve. 

     Returns Interval.Unset if 

    segment_index < 0 or segment_index >= Count().
  """
  pass
 def SegmentIndex(self,polycurveParameter):
  """
  SegmentIndex(self: PolyCurve,polycurveParameter: float) -> int

  

   Finds the segment used for evaluation at polycurve_parameter.

  

   polycurveParameter: Parameter on polycurve for segment lookup.

   Returns: Index of the segment used for evaluation at polycurve_parameter. 

     If 

    polycurve_parameter < Domain.Min(),then 0 is returned. 

     If polycurve_parameter > 

    Domain.Max(),then Count()-1 is returned.
  """
  pass
 def SegmentIndexes(self,subdomain,segmentIndex0,segmentIndex1):
  """
  SegmentIndexes(self: PolyCurve,subdomain: Interval) -> (int,int,int)

  

   Finds the segments that overlap the Polycurve sub domain.

  

   subdomain: Domain on this PolyCurve.

   Returns: Number of segments that overlap the subdomain.
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
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)

  __new__(cls: type)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 HasGap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This is a quick way to see if the curve has gaps between the sub curve segments.



Get: HasGap(self: PolyCurve) -> bool



"""

 IsNested=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not a PolyCurve contains nested PolyCurves.



Get: IsNested(self: PolyCurve) -> bool



"""

 SegmentCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of segments that make up this Polycurve.



Get: SegmentCount(self: PolyCurve) -> int



"""


