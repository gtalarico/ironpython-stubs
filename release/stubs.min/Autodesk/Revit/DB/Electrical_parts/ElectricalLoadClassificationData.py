class ElectricalLoadClassificationData(Enum,IComparable,IFormattable,IConvertible):
 """
 This enum is used by the ElectricalLoadClassification class as additional data whenever
    data members changed.  It is used as the additional data when the atom corresponding to each
    data member is touched.
 
 enum ElectricalLoadClassificationData,values: ActualElecLoadNameLabel (8),DemandFactor (2),LoadSummaryDemandFactorLabel (3),Name (0),PanelConnectedCurrentLabel (6),PanelConnectedLabel (4),PanelEstimatedCurrentLabel (7),PanelEstimatedLabel (5),SpaceLoadClass (1)
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
 ActualElecLoadNameLabel=None
 DemandFactor=None
 LoadSummaryDemandFactorLabel=None
 Name=None
 PanelConnectedCurrentLabel=None
 PanelConnectedLabel=None
 PanelEstimatedCurrentLabel=None
 PanelEstimatedLabel=None
 SpaceLoadClass=None
 value__=None

