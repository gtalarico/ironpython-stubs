class BaseImportOptions(object,IDisposable):
 """ A base class containing import options used during import of several formats. """
 def Dispose(self):
  """ Dispose(self: BaseImportOptions) """
  pass
 def GetLayerSelection(self):
  """
  GetLayerSelection(self: BaseImportOptions) -> ICollection[str]
  
   Get all set layers name which user want to import into Revit.
   Returns: The layers' name.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BaseImportOptions,disposing: bool) """
  pass
 def SetLayerSelection(self,layerSelection):
  """ SetLayerSelection(self: BaseImportOptions,layerSelection: ICollection[str]) """
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
 AutoCorrectAlmostVHLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Correct almost-vertical lines and almost-horizontal lines for import model
   if option is set to true,the almost-vertical lines would be vertical lines and almost-horizontal lines would be horizontal lines.

Get: AutoCorrectAlmostVHLines(self: BaseImportOptions) -> bool

Set: AutoCorrectAlmostVHLines(self: BaseImportOptions)=value
"""

 ColorMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Color mode for the import.
   Three modes are supported. Black and White,Preserve Colors,and Invert Colors.

Get: ColorMode(self: BaseImportOptions) -> ImportColorMode

Set: ColorMode(self: BaseImportOptions)=value
"""

 CustomScale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Scaling the import.
   If this is defined and a valid value (> 0.0),it takes preference over units.

Get: CustomScale(self: BaseImportOptions) -> float

Set: CustomScale(self: BaseImportOptions)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: BaseImportOptions) -> bool

"""

 OrientToView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Place the import at the same orientation as the view that was passed into the import method.
   This option can only be used when not importing into a single view.(i.e. ThisViewOnly is set to false)

Get: OrientToView(self: BaseImportOptions) -> bool

Set: OrientToView(self: BaseImportOptions)=value
"""

 Placement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Where to place the import.
   Set this option to place the view at the origin or the center,or a shared coordinates.

Get: Placement(self: BaseImportOptions) -> ImportPlacement

Set: Placement(self: BaseImportOptions)=value
"""

 ReferencePoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The 3D point in the document where the imported instance will be inserted.
   If not explicitly set,the instance will be inserted at the document origin.

Get: ReferencePoint(self: BaseImportOptions) -> XYZ

Set: ReferencePoint(self: BaseImportOptions)=value
"""

 ThisViewOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Imports drawings into the view that was passed into the import method.
   This option is not available in 3D views.

Get: ThisViewOnly(self: BaseImportOptions) -> bool

Set: ThisViewOnly(self: BaseImportOptions)=value
"""

 Unit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unit of measure for imported geometry.

Get: Unit(self: BaseImportOptions) -> ImportUnit

Set: Unit(self: BaseImportOptions)=value
"""

 VisibleLayersOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Only import the visible layers.

Get: VisibleLayersOnly(self: BaseImportOptions) -> bool

Set: VisibleLayersOnly(self: BaseImportOptions)=value
"""


