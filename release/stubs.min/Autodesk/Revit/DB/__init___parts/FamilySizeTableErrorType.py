class FamilySizeTableErrorType(Enum,IComparable,IFormattable,IConvertible):
 """
 The set of errors that can be returned when importing a FamilySizeTable from a CSV file.

 

 enum FamilySizeTableErrorType,values: CannotOpenFile (1),CannotParseColumnHeader (4),CannotReadFile (2),FileNotFound (0),IncorrectNumberOfColumns (5),InvalidHeaderSeparator (3),Undefined (-1)
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
 CannotOpenFile=None
 CannotParseColumnHeader=None
 CannotReadFile=None
 FileNotFound=None
 IncorrectNumberOfColumns=None
 InvalidHeaderSeparator=None
 Undefined=None
 value__=None

