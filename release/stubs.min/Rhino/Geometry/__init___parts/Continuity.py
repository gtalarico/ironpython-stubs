class Continuity(Enum,IComparable,IFormattable,IConvertible):
 """
 Provides enumerated values for continuity along geometry,

    such as continuous first derivative or continuous unit tangent and curvature.

 

 enum Continuity,values: C0_continuous (1),C0_locus_continuous (6),C1_continuous (2),C1_locus_continuous (7),C2_continuous (3),C2_locus_continuous (8),Cinfinity_continuous (11),G1_continuous (4),G1_locus_continuous (9),G2_continuous (5),G2_locus_continuous (10),None (0)
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
 C0_continuous=None
 C0_locus_continuous=None
 C1_continuous=None
 C1_locus_continuous=None
 C2_continuous=None
 C2_locus_continuous=None
 Cinfinity_continuous=None
 G1_continuous=None
 G1_locus_continuous=None
 G2_continuous=None
 G2_locus_continuous=None
 None=None
 value__=None

