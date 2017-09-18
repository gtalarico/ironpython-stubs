class DWGExportOptions(ACADExportOptions,IDisposable):
 """
 The export options used by exporting DWG format file.

 

 DWGExportOptions(option: DWGExportOptions)

 DWGExportOptions()
 """
 def Dispose(self):
  """ Dispose(self: BaseExportOptions,A_0: bool) """
  pass
 @staticmethod
 def GetPredefinedOptions(document,setup):
  """
  GetPredefinedOptions(document: Document,setup: str) -> DWGExportOptions

  

   Returns an instance DWGExportOptions containing settings from a predefined 

    export setup.

  

  

   document: A Revit project document to retrieve the setup from.

   setup: The name of a predefined export setup from the specified document.

   Returns: An instance of predefined DWGExportOptions,or ll if the name was not found.
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
  __new__(cls: type,option: DWGExportOptions)

  __new__(cls: type)
  """
  pass
 MergedViews=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether to merge all views in one file (via XRefs).

   Default value is false for mergedViews.



Get: MergedViews(self: DWGExportOptions) -> bool



Set: MergedViews(self: DWGExportOptions)=value

"""


