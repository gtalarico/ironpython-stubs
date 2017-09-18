class RevitLinkLoadResultType(Enum,IComparable,IFormattable,IConvertible):
 """
 Enum listing the possible results after loading a linked model.

 

 enum RevitLinkLoadResultType,values: ExternalServerMissing (9),LinkExists (10),LinkLoaded (1),LinkMayBeUpgraded (8),LinkNotFound (2),LinkNotLoadedOtherError (7),LinkNotOpenable (3),LinkOpenAsHost (4),SameCentralModelAsHost (6),SameModelAsHost (5),Uninitialized (0)
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
 ExternalServerMissing=None
 LinkExists=None
 LinkLoaded=None
 LinkMayBeUpgraded=None
 LinkNotFound=None
 LinkNotLoadedOtherError=None
 LinkNotOpenable=None
 LinkOpenAsHost=None
 SameCentralModelAsHost=None
 SameModelAsHost=None
 Uninitialized=None
 value__=None

