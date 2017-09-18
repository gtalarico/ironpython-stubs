class ExportDWGSettings(Element,IDisposable):
 """ This element contains DWG/DXF export settings which are saved in a Revit document. """
 @staticmethod
 def Create(document,name,options=None):
  """
  Create(document: Document,name: str) -> ExportDWGSettings

  

   Create a DWG export settings with default values.

  

   document: Document where created settings is saved.

   name: The name specified to this settings.

   Returns: The new DWG export settings instance.

  Create(document: Document,name: str,options: DWGExportOptions) -> ExportDWGSettings

  

   Create a DWG export settings with default values.

  

   document: Document where created settings is saved.

   name: The name specified to this settings.

   options: Initialize settings by using values in DWGExportOptions.

   Returns: The new DWG export settings instance.

  Create(document: Document,name: str,options: DXFExportOptions) -> ExportDWGSettings

  

   Create a DWG export settings with default values.

  

   document: Document where created settings is saved.

   name: The name specified to this settings.

   options: Initialize settings by using values in DXFExportOptions.

   Returns: The new DWG export settings instance.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetDWGExportOptions(self):
  """
  GetDWGExportOptions(self: ExportDWGSettings) -> DWGExportOptions

  

   Gets the options stored in the these settings.

   Returns: The options.
  """
  pass
 def GetDXFExportOptions(self):
  """
  GetDXFExportOptions(self: ExportDWGSettings) -> DXFExportOptions

  

   Gets the options stored in the these settings.

   Returns: The options
  """
  pass
 @staticmethod
 def ListNames(aDoc):
  """
  ListNames(aDoc: Document) -> IList[str]

  

   Returns a list of names of dwg/dxf export settings.

  

   aDoc: A Revit document to retrieve names from.

   Returns: An array of strings representing names of predefined setups.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetDWGExportOptions(self,options):
  """
  SetDWGExportOptions(self: ExportDWGSettings,options: DWGExportOptions)

   Sets the options stored in these settings.

  

   options: The options.
  """
  pass
 def SetDXFExportOptions(self,options):
  """
  SetDXFExportOptions(self: ExportDWGSettings,options: DXFExportOptions)

   Sets the options stored in these settings.

  

   options: The options.
  """
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
