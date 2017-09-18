class PrintManager(APIObject,IDisposable):
 """ The PrintManager object is used to configure the global print settings. """
 def Apply(self):
  """
  Apply(self: PrintManager)
   Apply the local print settings to global for all documents.
  """
  pass
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def SelectNewPrintDriver(self,strPrinterName):
  """
  SelectNewPrintDriver(self: PrintManager,strPrinterName: str)
   Select a new printer.
  
   strPrinterName: The name string of new printer.
  """
  pass
 def SubmitPrint(self,view=None):
  """
  SubmitPrint(self: PrintManager) -> bool
  
   Print the views and sheets defined in the current local PrintManager settings.
   Returns: True if successful,otherwise False.
  SubmitPrint(self: PrintManager,view: View) -> bool
  
   Print a view with the current PrintManager settings.
  
   view: The User-assigned view.
   Returns: True if successful,otherwise False.
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
 Collate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether to collate of the current print.

Get: Collate(self: PrintManager) -> bool

Set: Collate(self: PrintManager)=value
"""

 CombinedFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether to combine multiple selected views/sheets into a single file.

Get: CombinedFile(self: PrintManager) -> bool

Set: CombinedFile(self: PrintManager)=value
"""

 CopyNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The copy number.

Get: CopyNumber(self: PrintManager) -> int

Set: CopyNumber(self: PrintManager)=value
"""

 IsVirtual=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The virtual type in Autodesk Revit.

Get: IsVirtual(self: PrintManager) -> VirtualPrinterType

"""

 PaperSizes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all print sizes of current printer.

Get: PaperSizes(self: PrintManager) -> PaperSizeSet

"""

 PaperSources=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all print sources of current printer.

Get: PaperSources(self: PrintManager) -> PaperSourceSet

"""

 PrinterName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the current printer.

Get: PrinterName(self: PrintManager) -> str

"""

 PrintOrderReverse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether to reverse the print order of the current print.

Get: PrintOrderReverse(self: PrintManager) -> bool

Set: PrintOrderReverse(self: PrintManager)=value
"""

 PrintRange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The print range.

Get: PrintRange(self: PrintManager) -> PrintRange

Set: PrintRange(self: PrintManager)=value
"""

 PrintSetup=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The PrintSetup which manages the print settings of current document.

Get: PrintSetup(self: PrintManager) -> PrintSetup

"""

 PrintToFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether to print to file.

Get: PrintToFile(self: PrintManager) -> bool

Set: PrintToFile(self: PrintManager)=value
"""

 PrintToFileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The file name when printing to file.

Get: PrintToFileName(self: PrintManager) -> str

Set: PrintToFileName(self: PrintManager)=value
"""

 ViewSheetSetting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ViewSheetSetting which manages the view/sheet set information of current document,and you can change the default view/sheet
set for current project.

Get: ViewSheetSetting(self: PrintManager) -> ViewSheetSetting

"""


