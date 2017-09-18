class ExtrusionRoof(RoofBase,IDisposable):
 """ Represents some kinds of Extrusion Roofs. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetProfile(self):
  """
  GetProfile(self: ExtrusionRoof) -> ModelCurveArray

  

   Retrieve the Profile of ExtrusionRoof.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 CurtainGrids=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve all the CurtainGrid objects of a curtain Roof.



Get: CurtainGrids(self: ExtrusionRoof) -> CurtainGridSet



"""


