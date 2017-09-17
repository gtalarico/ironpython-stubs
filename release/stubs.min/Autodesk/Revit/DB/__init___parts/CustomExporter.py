class CustomExporter(object,IDisposable):
 """
 A class that allows exporting 3D views via an export context.
 
 CustomExporter(document: Document,context: IExportContext)
 """
 def Dispose(self):
  """ Dispose(self: CustomExporter) """
  pass
 def Export(self,*__args):
  """
  Export(self: CustomExporter,view: View3D)
   Exports one 3-D view
  
   view: An instance of the 3-D view to export
  Export(self: CustomExporter,viewIds: IList[ElementId])
  """
  pass
 @staticmethod
 def IsRenderingSupported():
  """
  IsRenderingSupported() -> bool
  
   Checks if 3D view rendering is currently supported in the running instance of 
    Revit.
  
   Returns: Returns True if rendering is currently supported,False otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: CustomExporter,disposing: bool) """
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
 @staticmethod
 def __new__(self,document,context):
  """ __new__(cls: type,document: Document,context: IExportContext) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IncludeGeometricObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This flag sets the exporter to either include or exclude
   output of geometric objects such as faces and curves
   when the model is being processed by the export context.

Get: IncludeGeometricObjects(self: CustomExporter) -> bool

Set: IncludeGeometricObjects(self: CustomExporter)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: CustomExporter) -> bool

"""

 ShouldStopOnError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This flag instructs the exporting process to either stop or continue
   in case an error occurs during any of the exporting methods.

Get: ShouldStopOnError(self: CustomExporter) -> bool

Set: ShouldStopOnError(self: CustomExporter)=value
"""


