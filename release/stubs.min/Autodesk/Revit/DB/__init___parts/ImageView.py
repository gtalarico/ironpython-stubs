class ImageView(ViewDrafting,IDisposable):
 """ Class for ImageView views """
 @staticmethod
 def Create(document,imageFileName):
  """
  Create(document: Document,imageFileName: str) -> ImageView
  
   Create an ImageView containing an image imported from disk.
  
   document: The document in which to create the view.
   imageFileName: The full path to the image file.
   Returns: The newly created view.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: View,view: View) -> BoundingBoxXYZ """
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
 ImageInstanceId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the image in the view.

Get: ImageInstanceId(self: ImageView) -> ElementId

"""


