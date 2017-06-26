class Panel(FamilyInstance,IDisposable):
 """ This object represents a curtain panel. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def FindHostPanel(self):
  """
  FindHostPanel(self: Panel) -> ElementId
  
   Finds the id of the host panel (i.e.,wall)
  associated with this panel. If a 
    host panel is present,then
  it is displayed instead of the curtain panel.
  
   Returns: Element id of the host panel associated with this panel.
  Otherwise,
    InvalidElementId is returned
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetRefGridLines(self,uGridLineId,vGridLineId):
  """
  GetRefGridLines(self: Panel,uGridLineId: ElementId,vGridLineId: ElementId) -> (ElementId,ElementId)
  
   This method is used to get the reference gridlines.
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
 Lockable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is used to know whether a panel can be locked.

Get: Lockable(self: Panel) -> bool

"""

 PanelType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Panel style of this Panel.

Get: PanelType(self: Panel) -> PanelType

Set: PanelType(self: Panel)=value
"""

 Transform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is used to find the transform of a curtain panel within project.

Get: Transform(self: Panel) -> Transform

"""


