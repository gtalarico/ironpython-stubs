class gbXMLConditionType(Enum,IComparable,IFormattable,IConvertible):
 """
 This enumeration corresponds to the conditionType attribute in gbXML.

    The enumerated attribute identifies the type of heating,cooling,

    or ventilation the space has.

 

 enum gbXMLConditionType,values: Cooled (1),Heated (0),HeatedAndCooled (2),NaturallyVentedOnly (5),NoConditionType (-1),NoOfConditionTypes (6),Unconditioned (3),Vented (4)
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
 Cooled=None
 Heated=None
 HeatedAndCooled=None
 NaturallyVentedOnly=None
 NoConditionType=None
 NoOfConditionTypes=None
 Unconditioned=None
 value__=None
 Vented=None

