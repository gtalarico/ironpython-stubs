class DocumentPaginator(object):
 """ Provides an abstract base class that supports creation of multiple-page elements from a single document. """
 def CancelAsync(self,userState):
  """
  CancelAsync(self: DocumentPaginator,userState: object)
   Cancels a previous 
    erload:System.Windows.Documents.DocumentPaginator.GetPageAsync or 
    erload:System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberAsync 
    operation.
  
  
   userState: The original userState passed to 
    erload:System.Windows.Documents.DocumentPaginator.GetPageAsync,
    erload:System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberAsync,or 
    erload:System.Windows.Documents.DocumentPaginator.ComputePageCountAsync that 
    identifies the asynchronous task to cancel.
  """
  pass
 def ComputePageCount(self):
  """
  ComputePageCount(self: DocumentPaginator)
   Forces a pagination of the content,updates 
    System.Windows.Documents.DocumentPaginator.PageCount with the new total,and 
    sets System.Windows.Documents.DocumentPaginator.IsPageCountValid to true.
  """
  pass
 def ComputePageCountAsync(self,userState=None):
  """
  ComputePageCountAsync(self: DocumentPaginator,userState: object)
   Asynchronously,forces a pagination of the content,updates 
    System.Windows.Documents.DocumentPaginator.PageCount with the new total,sets 
    System.Windows.Documents.DocumentPaginator.IsPageCountValid to true.
  
  
   userState: A unique identifier for the asynchronous task.
  ComputePageCountAsync(self: DocumentPaginator)
   Asynchronously,forces a pagination of the content,updates 
    System.Windows.Documents.DocumentPaginator.PageCount with the new total,and 
    sets System.Windows.Documents.DocumentPaginator.IsPageCountValid to true.
  """
  pass
 def GetPage(self,pageNumber):
  """
  GetPage(self: DocumentPaginator,pageNumber: int) -> DocumentPage
  
   When overridden in a derived class,gets the 
    System.Windows.Documents.DocumentPage for the specified page number.
  
  
   pageNumber: The zero-based page number of the document page that is needed.
   Returns: The System.Windows.Documents.DocumentPage for the specified pageNumber,or 
    System.Windows.Documents.DocumentPage.Missing if the page does not exist.
  """
  pass
 def GetPageAsync(self,pageNumber,userState=None):
  """
  GetPageAsync(self: DocumentPaginator,pageNumber: int,userState: object)
   Asynchronously returns (through the 
    System.Windows.Documents.DocumentPaginator.GetPageCompleted event) the 
    System.Windows.Documents.DocumentPage for the specified page number and assigns 
    the specified ID to the asynchronous task.
  
  
   pageNumber: The zero-based page number of the System.Windows.Documents.DocumentPage to get.
   userState: A unique identifier for the asynchronous task.
  GetPageAsync(self: DocumentPaginator,pageNumber: int)
   Asynchronously returns (through the 
    System.Windows.Documents.DocumentPaginator.GetPageCompleted event) the 
    System.Windows.Documents.DocumentPage for the specified page number.
  
  
   pageNumber: The zero-based page number of the document page that is needed.
  """
  pass
 def OnComputePageCountCompleted(self,*args):
  """
  OnComputePageCountCompleted(self: DocumentPaginator,e: AsyncCompletedEventArgs)
   Raises the System.Windows.Documents.DocumentPaginator.ComputePageCountCompleted 
    event.
  
  
   e: An System.ComponentModel.AsyncCompletedEventArgs that contains the event data.
  """
  pass
 def OnGetPageCompleted(self,*args):
  """
  OnGetPageCompleted(self: DocumentPaginator,e: GetPageCompletedEventArgs)
   Raises the System.Windows.Documents.DocumentPaginator.GetPageCompleted event.
  
   e: A System.Windows.Documents.GetPageCompletedEventArgs that contains the event 
    data.
  """
  pass
 def OnPagesChanged(self,*args):
  """
  OnPagesChanged(self: DocumentPaginator,e: PagesChangedEventArgs)
   Raises the System.Windows.Documents.DocumentPaginator.PagesChanged event.
  
   e: A System.Windows.Documents.PagesChangedEventArgs that contains the event data.
  """
  pass
 IsPageCountValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a value indicating whether System.Windows.Documents.DocumentPaginator.PageCount is the total number of pages.

Get: IsPageCountValid(self: DocumentPaginator) -> bool

"""

 PageCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a count of the number of pages currently formatted

Get: PageCount(self: DocumentPaginator) -> int

"""

 PageSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets or sets the suggested width and height of each page.

Get: PageSize(self: DocumentPaginator) -> Size

Set: PageSize(self: DocumentPaginator)=value
"""

 Source=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,returns the element being paginated.

Get: Source(self: DocumentPaginator) -> IDocumentPaginatorSource

"""


 ComputePageCountCompleted=None
 GetPageCompleted=None
 PagesChanged=None

