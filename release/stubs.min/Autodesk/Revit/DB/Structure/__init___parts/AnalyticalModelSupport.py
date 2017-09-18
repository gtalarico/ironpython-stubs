class AnalyticalModelSupport(object,IDisposable):
 """ Represents one support for an Element,in the realm of the Analytical Model. """
 def Dispose(self):
  """ Dispose(self: AnalyticalModelSupport) """
  pass
 def GetCurve(self):
  """
  GetCurve(self: AnalyticalModelSupport) -> Curve

  

   Retrieves the curve providing support.

   Returns: Represents the curve providing support,if the Support Type is Curve Support.
  """
  pass
 def GetFace(self):
  """
  GetFace(self: AnalyticalModelSupport) -> Face

  

   Retrieves surface providing support,

   Returns: Surface representing the surface providing support,if the Support Type is 

    Surface Support.
  """
  pass
 def GetPoint(self):
  """
  GetPoint(self: AnalyticalModelSupport) -> XYZ

  

   Retrieves the point providing support.

   Returns: Represents the point providing support,if the Support Type is Point Support.
  """
  pass
 def GetPriority(self):
  """
  GetPriority(self: AnalyticalModelSupport) -> AnalyticalSupportPriority

  

   Retrieves the priority of the support provided.

   Returns: Indicates the support priority,as determined by Analytical Support Checking
  """
  pass
 def GetSupportingElement(self):
  """
  GetSupportingElement(self: AnalyticalModelSupport) -> ElementId

  

   Retrieves the actual Element Id providing support.

   Returns: Represents Element that provides support.
  """
  pass
 def GetSupportType(self):
  """
  GetSupportType(self: AnalyticalModelSupport) -> AnalyticalSupportType

  

   Gets the type of support provided.

   Returns: Indicates type of support provided.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: AnalyticalModelSupport,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: AnalyticalModelSupport) -> bool



"""


