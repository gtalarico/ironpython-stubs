class MEPSystemClassification(Enum,IComparable,IFormattable,IConvertible):
 """
 This enumeration is used to classify MEP connectors and systems
    and drives certain behavior for a particular system type
 
 enum MEPSystemClassification,values: CableTrayConduit (32),Communication (14),CondensateDrain (15),Controls (13),DataCircuit (5),DomesticColdWater (20),DomesticHotWater (19),ExhaustAir (3),FireAlarm (11),FireProtectDry (24),FireProtectOther (26),FireProtectPreaction (25),FireProtectWet (23),Fitting (28),Global (29),NurseCall (12),OtherAir (4),OtherPipe (22),PowerBalanced (30),PowerCircuit (6),PowerUnBalanced (31),Recirculation (21),ReturnAir (2),ReturnHydronic (8),Sanitary (16),Security (10),Storm (18),SupplyAir (1),SupplyHydronic (7),SwitchTopology (27),Telephone (9),UndefinedSystemClassification (0),Vent (17)
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
 CableTrayConduit=None
 Communication=None
 CondensateDrain=None
 Controls=None
 DataCircuit=None
 DomesticColdWater=None
 DomesticHotWater=None
 ExhaustAir=None
 FireAlarm=None
 FireProtectDry=None
 FireProtectOther=None
 FireProtectPreaction=None
 FireProtectWet=None
 Fitting=None
 Global=None
 NurseCall=None
 OtherAir=None
 OtherPipe=None
 PowerBalanced=None
 PowerCircuit=None
 PowerUnBalanced=None
 Recirculation=None
 ReturnAir=None
 ReturnHydronic=None
 Sanitary=None
 Security=None
 Storm=None
 SupplyAir=None
 SupplyHydronic=None
 SwitchTopology=None
 Telephone=None
 UndefinedSystemClassification=None
 value__=None
 Vent=None

