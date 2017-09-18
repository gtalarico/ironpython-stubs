class ListType(Enum,IComparable,IFormattable,IConvertible):
 """
 An enumerated type indicating the style of list item

    for paragraphs that are part of ordered or unordered lists

    in FormattedText.

 

 enum ListType,values: ArabicNumbers (3),Bullet (2),LowerCaseLetters (4),Mixed (0),None (1),UpperCaseLetters (5)
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
 ArabicNumbers=None
 Bullet=None
 LowerCaseLetters=None
 Mixed=None
 None=None
 UpperCaseLetters=None
 value__=None

