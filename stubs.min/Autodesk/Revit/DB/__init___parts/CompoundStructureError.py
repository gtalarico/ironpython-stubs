class CompoundStructureError(Enum,IComparable,IFormattable,IConvertible):
 """
 When CompoundStructure::isValid() returns false,it uses these values to indicate precise nature of defect.
 
 enum CompoundStructureError,values: BadShellOrder (0),BadShellsStructure (5),CoreTooThin (1),DeckCantBoundAbove (12),DeckCantBoundBelow (13),ExtensibleRegionsNotContiguousAlongBottom (17),ExtensibleRegionsNotContiguousAlongTop (16),InvalidMaterialId (15),InvalidProfileId (18),MembraneTooThick (3),NonmembraneTooThin (4),ThinOuterLayer (6),VarThickLayerCantBeZero (14),VerticalUnusedLayer (7),VerticalWrongOrderCoreExterior (9),VerticalWrongOrderCoreInterior (10),VerticalWrongOrderLayer (8),VerticalWrongOrderMembrane (11)
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
 BadShellOrder=None
 BadShellsStructure=None
 CoreTooThin=None
 DeckCantBoundAbove=None
 DeckCantBoundBelow=None
 ExtensibleRegionsNotContiguousAlongBottom=None
 ExtensibleRegionsNotContiguousAlongTop=None
 InvalidMaterialId=None
 InvalidProfileId=None
 MembraneTooThick=None
 NonmembraneTooThin=None
 ThinOuterLayer=None
 value__=None
 VarThickLayerCantBeZero=None
 VerticalUnusedLayer=None
 VerticalWrongOrderCoreExterior=None
 VerticalWrongOrderCoreInterior=None
 VerticalWrongOrderLayer=None
 VerticalWrongOrderMembrane=None

