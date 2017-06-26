class Domain(Enum,IComparable,IFormattable,IConvertible):
 """
 Enumeration of connector domain types
 
 enum Domain,values: DomainCableTrayConduit (4),DomainElectrical (2),DomainHvac (1),DomainPiping (3),DomainUndefined (0)
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
 DomainCableTrayConduit=None
 DomainElectrical=None
 DomainHvac=None
 DomainPiping=None
 DomainUndefined=None
 value__=None

