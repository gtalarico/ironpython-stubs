class IWin32Window:
 """ Defines the contract for Win32 window handles. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the window handle.

Get: Handle(self: IWin32Window) -> IntPtr

"""


