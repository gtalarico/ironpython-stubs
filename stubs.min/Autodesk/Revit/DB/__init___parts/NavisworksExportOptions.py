class NavisworksExportOptions(object,IDisposable):
 """
 Options which controls the Navisworks export.
 
 NavisworksExportOptions()
 """
 def Dispose(self):
  """ Dispose(self: NavisworksExportOptions) """
  pass
 def GetSelectedElementIds(self):
  """
  GetSelectedElementIds(self: NavisworksExportOptions) -> ICollection[ElementId]
  
   Returns the element ids of the elements to export. Empty by default.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: NavisworksExportOptions,disposing: bool) """
  pass
 def SetSelectedElementIds(self,ids):
  """ SetSelectedElementIds(self: NavisworksExportOptions,ids: ICollection[ElementId]) """
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
 ConvertElementProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to convert element properties,false otherwise.
   Default value is false.

Get: ConvertElementProperties(self: NavisworksExportOptions) -> bool

Set: ConvertElementProperties(self: NavisworksExportOptions)=value
"""

 Coordinates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Options which specifies the coordinates of Navisworks Exporter.
   Default value is Shared.

Get: Coordinates(self: NavisworksExportOptions) -> NavisworksCoordinates

Set: Coordinates(self: NavisworksExportOptions)=value
"""

 DivideFileIntoLevels=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to divide file into levels,false otherwise.
   Default value is true.

Get: DivideFileIntoLevels(self: NavisworksExportOptions) -> bool

Set: DivideFileIntoLevels(self: NavisworksExportOptions)=value
"""

 ExportElementIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to export Revit element ids,false to skip these values.
   Default value is true.

Get: ExportElementIds(self: NavisworksExportOptions) -> bool

Set: ExportElementIds(self: NavisworksExportOptions)=value
"""

 ExportLinks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to export Revit links found in the main model,false to skip links.
   Default value is false.

Get: ExportLinks(self: NavisworksExportOptions) -> bool

Set: ExportLinks(self: NavisworksExportOptions)=value
"""

 ExportParts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to export Revit part elements,false to export the original parent elements.
   Default value is false.

Get: ExportParts(self: NavisworksExportOptions) -> bool

Set: ExportParts(self: NavisworksExportOptions)=value
"""

 ExportRoomAsAttribute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to export data for each room converts into a single shared room attribute,false otherwise.
   Default value is true.

Get: ExportRoomAsAttribute(self: NavisworksExportOptions) -> bool

Set: ExportRoomAsAttribute(self: NavisworksExportOptions)=value
"""

 ExportRoomGeometry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to export Revit room geometry,false otherwise.
   Default value is true.

Get: ExportRoomGeometry(self: NavisworksExportOptions) -> bool

Set: ExportRoomGeometry(self: NavisworksExportOptions)=value
"""

 ExportScope=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Options which specifies the export scope of Navisworks Exporter.
   Default value is Model.

Get: ExportScope(self: NavisworksExportOptions) -> NavisworksExportScope

Set: ExportScope(self: NavisworksExportOptions)=value
"""

 ExportUrls=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to export URL parameters,false otherwise.
   Default value is true.

Get: ExportUrls(self: NavisworksExportOptions) -> bool

Set: ExportUrls(self: NavisworksExportOptions)=value
"""

 FindMissingMaterials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the file exporter looks for a match for the materials missing from the export,false otherwise.
   Default value is true.

Get: FindMissingMaterials(self: NavisworksExportOptions) -> bool

Set: FindMissingMaterials(self: NavisworksExportOptions)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: NavisworksExportOptions) -> bool

"""

 Parameters=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Options which specifies the parameter conversion of Navisworks Exporter.
   Default value is All.

Get: Parameters(self: NavisworksExportOptions) -> NavisworksParameters

Set: Parameters(self: NavisworksExportOptions)=value
"""

 ViewId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element id of the view to export. InvalidElementId by default. Used only when ExportScope=View.

Get: ViewId(self: NavisworksExportOptions) -> ElementId

Set: ViewId(self: NavisworksExportOptions)=value
"""


