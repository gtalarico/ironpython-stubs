class EnergyAnalysisOpening(Element,IDisposable):
 """ Analytical opening. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAnalyticalSurface(self):
  """
  GetAnalyticalSurface(self: EnergyAnalysisOpening) -> EnergyAnalysisSurface

  

   Gets the associative analytical parent surface element.

   Returns: The associative analytical parent surface element.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetPolyloop(self):
  """
  GetPolyloop(self: EnergyAnalysisOpening) -> Polyloop

  

   Gets the planar polygon describing the opening geometry.
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
 CADLinkUniqueId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unique id of the originating CAD object's link (linked document) associated with this opening.



Get: CADLinkUniqueId(self: EnergyAnalysisOpening) -> str



"""

 CADObjectUniqueId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unique id of the originating CAD object (model element) associated with this opening.



Get: CADObjectUniqueId(self: EnergyAnalysisOpening) -> str



"""

 Corner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The lower-left coordinate for the analytical rectangular geometry viewed from outside.



Get: Corner(self: EnergyAnalysisOpening) -> XYZ



"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The height of the analytical rectangular geometry.



Get: Height(self: EnergyAnalysisOpening) -> float



"""

 OpeningId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unique identifier for the opening.



Get: OpeningId(self: EnergyAnalysisOpening) -> str



"""

 OpeningName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unique name identifier for the opening.



Get: OpeningName(self: EnergyAnalysisOpening) -> str



"""

 OpeningType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The analytical opening type.



Get: OpeningType(self: EnergyAnalysisOpening) -> EnergyAnalysisOpeningType



"""

 OriginatingElementDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description for the originating Revit element.



Get: OriginatingElementDescription(self: EnergyAnalysisOpening) -> str



"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The gbXML opening type attribute.



Get: Type(self: EnergyAnalysisOpening) -> gbXMLOpeningType



"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The width of the analytical rectangular geometry.



Get: Width(self: EnergyAnalysisOpening) -> float



"""


