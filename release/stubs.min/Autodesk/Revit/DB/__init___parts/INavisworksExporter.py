class INavisworksExporter(IExternalServer):
 """ The interface used to implement a Navisworks exporter. """
 def Export(self,document,folder,name,options):
  """
  Export(self: INavisworksExporter,document: Document,folder: str,name: str,options: NavisworksExportOptions)

   The method that Revit will invoke to perform an export to Navisworks.

  

   document: The document to export.

   folder: The folder path.

   name: The file name.

   options: The export options.
  """
  pass
 def ValidateExportOptions(self,document,folder,name,options,exceptionMessage):
  """
  ValidateExportOptions(self: INavisworksExporter,document: Document,folder: str,name: str,options: NavisworksExportOptions) -> (bool,str)

  

   Determines if the inputs are valid,and returns an error message if not.

  

   document: The document to export.

   folder: The folder path.

   name: The file name.

   options: The export options.

   Returns: True if the options are valid,false otherwise.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
