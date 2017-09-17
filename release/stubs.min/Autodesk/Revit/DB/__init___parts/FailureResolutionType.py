class FailureResolutionType(Enum,IComparable,IFormattable,IConvertible):
 """
 Enumeration to classify FailureResolutions by nature of operation they perform on failing Elements.
 
 enum FailureResolutionType,values: CreateElements (2),Default (1),DeleteElements (3),DetachElements (7),FixElements (6),Invalid (0),MoveElements (5),Others (100000),QuitEditMode (8),SaveDocument (11),SetValue (10),ShowElements (12),SkipElements (4),UnlockConstraints (9)
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
 CreateElements=None
 Default=None
 DeleteElements=None
 DetachElements=None
 FixElements=None
 Invalid=None
 MoveElements=None
 Others=None
 QuitEditMode=None
 SaveDocument=None
 SetValue=None
 ShowElements=None
 SkipElements=None
 UnlockConstraints=None
 value__=None

