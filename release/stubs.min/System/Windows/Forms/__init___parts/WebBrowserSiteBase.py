class WebBrowserSiteBase(object,IOleControlSite,IOleClientSite,IOleInPlaceSite,ISimpleFrameSite,IPropertyNotifySink,IDisposable):
 """ Implements the interfaces of an ActiveX site for use as a base class by the System.Windows.Forms.WebBrowser.WebBrowserSite class. """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return WebBrowserSiteBase()

 def Dispose(self):
  """
  Dispose(self: WebBrowserSiteBase)
   Releases all resources used by the System.Windows.Forms.WebBrowserSiteBase.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
