class HtmlHistory(object,IDisposable):
 """ Manages the list of documents and Web sites the user has visited within the current session. """
 def Back(self,numberBack):
  """
  Back(self: HtmlHistory,numberBack: int)

   Navigates backward in the navigation stack by the specified number of entries.

  

   numberBack: The number of entries to navigate backward in the navigation stack. This number must be a 

    positive integer.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: HtmlHistory)

   Releases all resources used by the System.Windows.Forms.HtmlHistory.
  """
  pass
 def Forward(self,numberForward):
  """
  Forward(self: HtmlHistory,numberForward: int)

   Navigates forward in the navigation stack by the specified number of entries.

  

   numberForward: The number of entries to navigate forward in the navigation stack. This number must be a 

    positive integer.
  """
  pass
 def Go(self,*__args):
  """
  Go(self: HtmlHistory,relativePosition: int)

   Navigates to the specified relative position in the browser's history.

  

   relativePosition: The entry in the navigation stack you want to display.

  Go(self: HtmlHistory,urlString: str)

   Navigates to the specified Uniform Resource Locator (URL).

  

   urlString: The URL you want to display. This may be a relative or virtual URL (for example,page.html,

    path/page.html,or /path/to/page.html),in which case the current Web page's URL is used as a 

    base.

  

  Go(self: HtmlHistory,url: Uri)

   Navigates to the specified Uniform Resource Locator (URL).

  

   url: The URL as a System.Uri object.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 DomHistory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unmanaged interface wrapped by this class.



Get: DomHistory(self: HtmlHistory) -> object



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size of the history stack.



Get: Length(self: HtmlHistory) -> int



"""


