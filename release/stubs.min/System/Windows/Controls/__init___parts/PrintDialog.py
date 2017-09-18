class PrintDialog(object):
 """
 Invokes a standard Microsoft Windows print dialog box that configures a System.Printing.PrintTicket and System.Printing.PrintQueue according to user input and then prints a document.

 

 PrintDialog()
 """
 def PrintDocument(self,documentPaginator,description):
  """
  PrintDocument(self: PrintDialog,documentPaginator: DocumentPaginator,description: str)

   Prints a System.Windows.Documents.DocumentPaginator object to the System.Printing.PrintQueue 

    that is currently selected.

  

  

   documentPaginator: The System.Windows.Documents.DocumentPaginator object to print.

   description: A description of the job that is to be printed. This text appears in the user interface (UI) of 

    the printer.
  """
  pass
 def PrintVisual(self,visual,description):
  """
  PrintVisual(self: PrintDialog,visual: Visual,description: str)

   Prints a visual (non-text) object,which is derived from the System.Windows.Media.Visual class,

    to the System.Printing.PrintQueue that is currently selected.

  

  

   visual: The System.Windows.Media.Visual to print.

   description: A description of the job that is to be printed. This text appears in the user interface (UI) of 

    the printer.
  """
  pass
 def ShowDialog(self):
  """
  ShowDialog(self: PrintDialog) -> Nullable[bool]

  

   Invokes the System.Windows.Controls.PrintDialog as a modal dialog box.

   Returns: true if a user clicks Print; false if a user clicks Cancel; or null if a user closes the dialog 

    box without clicking Print or Cancel.
  """
  pass
 CurrentPageEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CurrentPageEnabled(self: PrintDialog) -> bool



Set: CurrentPageEnabled(self: PrintDialog)=value

"""

 MaxPage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the highest page number that is allowed in page ranges.



Get: MaxPage(self: PrintDialog) -> UInt32



Set: MaxPage(self: PrintDialog)=value

"""

 MinPage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the lowest page number that is allowed in page ranges.



Get: MinPage(self: PrintDialog) -> UInt32



Set: MinPage(self: PrintDialog)=value

"""

 PageRange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the range of pages to print when System.Windows.Controls.PrintDialog.PageRangeSelection is set to System.Windows.Controls.PageRangeSelection.UserPages.



Get: PageRange(self: PrintDialog) -> PageRange



Set: PageRange(self: PrintDialog)=value

"""

 PageRangeSelection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Controls.PageRangeSelection for this instance of System.Windows.Controls.PrintDialog.



Get: PageRangeSelection(self: PrintDialog) -> PageRangeSelection



Set: PageRangeSelection(self: PrintDialog)=value

"""

 PrintableAreaHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the height of the printable area of the page.



Get: PrintableAreaHeight(self: PrintDialog) -> float



"""

 PrintableAreaWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width of the printable area of the page.



Get: PrintableAreaWidth(self: PrintDialog) -> float



"""

 PrintQueue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Printing.PrintQueue that represents the printer that is selected.



Get: PrintQueue(self: PrintDialog) -> PrintQueue



Set: PrintQueue(self: PrintDialog)=value

"""

 PrintTicket=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Printing.PrintTicket that is used by the System.Windows.Controls.PrintDialog when the user clicks Print for the current print job.



Get: PrintTicket(self: PrintDialog) -> PrintTicket



Set: PrintTicket(self: PrintDialog)=value

"""

 SelectedPagesEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SelectedPagesEnabled(self: PrintDialog) -> bool



Set: SelectedPagesEnabled(self: PrintDialog)=value

"""

 UserPageRangeEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether users of the Print dialog box have the option to specify ranges of pages to print.



Get: UserPageRangeEnabled(self: PrintDialog) -> bool



Set: UserPageRangeEnabled(self: PrintDialog)=value

"""


