class WebBrowserSiteBase(object,IOleControlSite,IOleClientSite,IOleInPlaceSite,ISimpleFrameSite,IPropertyNotifySink,IDisposable):
 """ Implements the interfaces of an ActiveX site for use as a base class by the System.Windows.Forms.WebBrowser.WebBrowserSite class. """
 def Dispose(self):
  """
  Dispose(self: WebBrowserSiteBase)

   Releases all resources used by the System.Windows.Forms.WebBrowserSiteBase.
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
