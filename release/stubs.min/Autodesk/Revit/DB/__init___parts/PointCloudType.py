class PointCloudType(ElementType,IDisposable):
 """
 Represents a type of point cloud loaded into a Revit document.  Each PointCloudType maps to

    a single file or identifier (depending upon the type of Point Cloud Engine which governs it).
 """
 @staticmethod
 def Create(document,engineIdentifier,typeIdentifier):
  """
  Create(document: Document,engineIdentifier: str,typeIdentifier: str) -> PointCloudType

  

   Creates a new point cloud type for a given point cloud engine.

  

   document: The document in which to create the point cloud.

   engineIdentifier: The string identifying the engine to be invoked.

     It should be the file 

    extension or engine identifier registered by the third party.

  

   typeIdentifier: The file name or the identification string for a non-file based engine.

   Returns: The newly created PointCloudType object to be used to create instances of

     

    this point cloud.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetPath(self):
  """
  GetPath(self: PointCloudType) -> ModelPath

  

   Gets the path of the link source from which the points are loaded.

   Returns: Returns the file path for a file based point cloud or null for the non-file 

    based point cloud.
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
 ColorEncoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color encoding used by points extracted from instances of this point cloud.



Get: ColorEncoding(self: PointCloudType) -> PointCloudColorEncoding



"""

 EngineIdentifier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The identifier of the engine responsible for handling of the point cloud.



Get: EngineIdentifier(self: PointCloudType) -> str



"""

 FoundStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Shows whether the Point Cloud external file could be found.



Get: FoundStatus(self: PointCloudType) -> PointCloudFoundStatus



"""

 Offset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the offset stored in the point cloud.



Get: Offset(self: PointCloudType) -> XYZ



"""

 Scale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The multiplier applied to the points in all instances of this point cloud.



Get: Scale(self: PointCloudType) -> float



Set: Scale(self: PointCloudType)=value

"""


