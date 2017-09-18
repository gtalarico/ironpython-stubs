class UIView(object,IDisposable):
 """ A class containing data about view windows in the Revit user interface. """
 def Close(self):
  """
  Close(self: UIView)

   Closes the view.
  """
  pass
 def Dispose(self):
  """ Dispose(self: UIView) """
  pass
 def GetWindowRectangle(self):
  """
  GetWindowRectangle(self: UIView) -> Rectangle

  

   Gets the rectangle containing the coordinates of the view's drawing area.

   Returns: The rectangle of the view window.
  """
  pass
 def GetZoomCorners(self):
  """
  GetZoomCorners(self: UIView) -> IList[XYZ]

  

   Gets the corners of the view's rectangle.

     The two points that define the 

    corners of the view's rectangle in model coordinates.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: UIView,disposing: bool) """
  pass
 def Zoom(self,zoomFactor):
  """
  Zoom(self: UIView,zoomFactor: float)

   Zoom the view.

  

   zoomFactor: Factor by which to zoom in or out. Values greater than 1 zooms in,less than 1 

    zooms out.
  """
  pass
 def ZoomAndCenterRectangle(self,viewCorner1,viewCorner2):
  """
  ZoomAndCenterRectangle(self: UIView,viewCorner1: XYZ,viewCorner2: XYZ)

   Zoom and center the view to a specified rectangle.

  

   viewCorner1: A corner of the desired view rectangle in model coordinates.

   viewCorner2: The opposite corner of the desired view rectangle in model coordinates.
  """
  pass
 def ZoomSheetSize(self):
  """
  ZoomSheetSize(self: UIView)

   Zoom to the sheet size.
  """
  pass
 def ZoomToFit(self):
  """
  ZoomToFit(self: UIView)

   Zoom the view to fit its contents.
  """
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



Get: IsValidObject(self: UIView) -> bool



"""

 ViewId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the View associated with a UIView.



Get: ViewId(self: UIView) -> ElementId



"""



# variables with complex values

