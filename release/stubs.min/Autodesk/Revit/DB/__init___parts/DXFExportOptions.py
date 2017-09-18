class DXFExportOptions(ACADExportOptions,IDisposable):
 """
 The export options used by exporting DXF format file.

 

 DXFExportOptions(option: DXFExportOptions)

 DXFExportOptions()
 """
 def Dispose(self):
  """ Dispose(self: BaseExportOptions,A_0: bool) """
  pass
 @staticmethod
 def GetPredefinedOptions(document,setup):
  """
  GetPredefinedOptions(document: Document,setup: str) -> DXFExportOptions

  

   Returns an instance DXFExportOptions containing settings from a predefined 

    export setup.

  

  

   document: A Revit project document to retrieve the setup from.

   setup: The name of a predefined export setup from the specified document.

   Returns: An instance of predefined DXFExportOptions,or ll if the name was not found.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BaseExportOptions,disposing: bool) """
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
 def __new__(self,option=None):
  """
  __new__(cls: type,option: DXFExportOptions)

  __new__(cls: type)
  """
  pass
