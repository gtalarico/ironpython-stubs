class ComInterfaceType(Enum,IComparable,IFormattable,IConvertible):
 """
 Identifies how to expose an interface to COM.

 

 enum ComInterfaceType,values: InterfaceIsDual (0),InterfaceIsIDispatch (2),InterfaceIsIInspectable (3),InterfaceIsIUnknown (1)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 InterfaceIsDual=None
 InterfaceIsIDispatch=None
 InterfaceIsIInspectable=None
 InterfaceIsIUnknown=None
 value__=None

