class PrintControllerWithStatusDialog(PrintController):
 """
 Controls how a document is printed from a Windows Forms application.

 

 PrintControllerWithStatusDialog(underlyingController: PrintController)

 PrintControllerWithStatusDialog(underlyingController: PrintController,dialogTitle: str)
 """
 def OnEndPage(self,document,e):
  """
  OnEndPage(self: PrintControllerWithStatusDialog,document: PrintDocument,e: PrintPageEventArgs)

   Completes the control sequence that determines when and how to print a page of a document.

  

   document: A System.Drawing.Printing.PrintDocument that represents the document currently being printed.

   e: A System.Drawing.Printing.PrintPageEventArgs that contains the event data.
  """
  pass
 def OnEndPrint(self,document,e):
  """
  OnEndPrint(self: PrintControllerWithStatusDialog,document: PrintDocument,e: PrintEventArgs)

   Completes the control sequence that determines when and how to print a document.

  

   document: A System.Drawing.Printing.PrintDocument that represents the document currently being printed.

   e: A System.Drawing.Printing.PrintPageEventArgs that contains the event data.
  """
  pass
 def OnStartPage(self,document,e):
  """
  OnStartPage(self: PrintControllerWithStatusDialog,document: PrintDocument,e: PrintPageEventArgs) -> Graphics

  

   Begins the control sequence that determines when and how to print a page of a document.

  

   document: A System.Drawing.Printing.PrintDocument that represents the document currently being printed.

   e: A System.Drawing.Printing.PrintPageEventArgs that contains the event data.

   Returns: A System.Drawing.Graphics object that represents a page from a 

    System.Drawing.Printing.PrintDocument.
  """
  pass
 def OnStartPrint(self,document,e):
  """
  OnStartPrint(self: PrintControllerWithStatusDialog,document: PrintDocument,e: PrintEventArgs)

   Begins the control sequence that determines when and how to print a document.

  

   document: A System.Drawing.Printing.PrintDocument that represents the document currently being printed.

   e: A System.Drawing.Printing.PrintEventArgs that contains the event data.
  """
  pass
 @staticmethod
 def __new__(self,underlyingController,dialogTitle=None):
  """
  __new__(cls: type,underlyingController: PrintController)

  __new__(cls: type,underlyingController: PrintController,dialogTitle: str)
  """
  pass
 IsPreview=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating this System.Windows.Forms.PrintControllerWithStatusDialog is used for print preview.



Get: IsPreview(self: PrintControllerWithStatusDialog) -> bool



"""


