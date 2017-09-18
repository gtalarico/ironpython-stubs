class StringComparison(Enum,IComparable,IFormattable,IConvertible):
 """
 Specifies the culture,case,and sort rules to be used by certain overloads of the System.String.Compare(System.String,System.String) and System.String.Equals(System.Object) methods.

 

 enum StringComparison,values: CurrentCulture (0),CurrentCultureIgnoreCase (1),InvariantCulture (2),InvariantCultureIgnoreCase (3),Ordinal (4),OrdinalIgnoreCase (5)
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
 CurrentCulture=None
 CurrentCultureIgnoreCase=None
 InvariantCulture=None
 InvariantCultureIgnoreCase=None
 Ordinal=None
 OrdinalIgnoreCase=None
 value__=None

