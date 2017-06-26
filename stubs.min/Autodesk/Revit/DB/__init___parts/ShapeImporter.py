class ShapeImporter(object,IDisposable):
 """
 An utility class that supports conversion of geometry stored in an external format into a Revit geometry objects.
 
 ShapeImporter()
 """
 def Convert(self,document,filename):
  """
  Convert(self: ShapeImporter,document: Document,filename: str) -> IList[GeometryObject]
  
   Converts the geometry stored in the external format into a collection of Revit 
    geometry objects.
  
  
   document: The Revit document where the resulting Revit geometry objects will be used. 
    This document may need to be modified
     to store dependent elements such as 
    graphics styles and/or materials.
  
   filename: The full path to the input file.
   Returns: A collection of Revit geometry objects created from the incoming data.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ShapeImporter) """
  pass
 @staticmethod
 def IsServiceAvailable():
  """
  IsServiceAvailable() -> bool
  
   Checks whether the data conversion service is available.
   Returns: True if the data conversion service is available,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ShapeImporter,disposing: bool) """
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
 InputFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The format of the incoming data.

Get: InputFormat(self: ShapeImporter) -> ShapeImporterSourceFormat

Set: InputFormat(self: ShapeImporter)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ShapeImporter) -> bool

"""


