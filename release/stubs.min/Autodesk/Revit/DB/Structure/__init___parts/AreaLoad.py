class AreaLoad(LoadBase,IDisposable):
 """ An object that represents a force applied across an area. """
 @staticmethod
 def Create(aDoc,*__args):
  """
  Create(aDoc: Document,host: AnalyticalModelSurface,forceVector: XYZ,symbol: AreaLoadType) -> AreaLoad

  

   Creates a new hosted area load within the project.

  

   aDoc: Document to which new area load will be added.

   host: The analytical surface host element (Analytical Floor,Analytical Foundation 

    Slab or Analytical Wall) for the area Load.

  

   forceVector: The force vector applied to the 1st reference point of the area load.

   symbol: The symbol of the AreaLoad. Set ll to use default type.

   Returns: If successful,returns an object of the newly created AreaLoad. ll is returned 

    if the operation fails.

  

  Create(aDoc: Document,loops: IList[CurveLoop],forceVector: XYZ,symbol: AreaLoadType) -> AreaLoad

  Create(aDoc: Document,loops: IList[CurveLoop],forceVectors: IList[XYZ],refPointCurveIndexes: IList[int],refPointCurveSelectors: IList[int],symbol: AreaLoadType) -> AreaLoad
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetLoops(self):
  """
  GetLoops(self: AreaLoad) -> IList[CurveLoop]

  

   Returns curve loops that define geometry of the area load.
  """
  pass
 def GetRefPoint(self,index):
  """
  GetRefPoint(self: AreaLoad,index: int) -> XYZ

  

   Returns the physical location of the reference point.

  

   index: The index of the point to return.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetLoops(self,doc,newLoops):
  """ SetLoops(self: AreaLoad,doc: Document,newLoops: IList[CurveLoop]) -> bool """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Area=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns area of the area load.



Get: Area(self: AreaLoad) -> float



"""

 ForceVector1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The force vector applied to the 1st reference point of the area load,oriented according to OrientTo setting.



Get: ForceVector1(self: AreaLoad) -> XYZ



Set: ForceVector1(self: AreaLoad)=value

"""

 ForceVector2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The force vector applied to the 2nd reference point of the area load,oriented according to OrientTo setting.



Get: ForceVector2(self: AreaLoad) -> XYZ



Set: ForceVector2(self: AreaLoad)=value

"""

 ForceVector3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The force vector applied to the 3rd reference point of the area load,oriented according to OrientTo setting.



Get: ForceVector3(self: AreaLoad) -> XYZ



Set: ForceVector3(self: AreaLoad)=value

"""

 IsProjected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the load is projected.



Get: IsProjected(self: AreaLoad) -> bool



Set: IsProjected(self: AreaLoad)=value

"""

 NumRefPoints=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the total number of reference points for the area load.



Get: NumRefPoints(self: AreaLoad) -> int



"""


