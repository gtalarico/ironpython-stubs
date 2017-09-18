class ViewType(Enum,IComparable,IFormattable,IConvertible):
 """
 An enumerated type listing available view types.

 

 enum ViewType,values: AreaPlan (116),CeilingPlan (2),ColumnSchedule (122),CostReport (119),Detail (118),DraftingView (10),DrawingSheet (6),Elevation (3),EngineeringPlan (115),FloorPlan (1),Internal (214),Legend (11),LoadsReport (120),PanelSchedule (123),PresureLossReport (121),ProjectBrowser (7),Rendering (125),Report (8),Schedule (5),Section (117),SystemBrowser (12),ThreeD (4),Undefined (0),Walkthrough (124)
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
 AreaPlan=None
 CeilingPlan=None
 ColumnSchedule=None
 CostReport=None
 Detail=None
 DraftingView=None
 DrawingSheet=None
 Elevation=None
 EngineeringPlan=None
 FloorPlan=None
 Internal=None
 Legend=None
 LoadsReport=None
 PanelSchedule=None
 PresureLossReport=None
 ProjectBrowser=None
 Rendering=None
 Report=None
 Schedule=None
 Section=None
 SystemBrowser=None
 ThreeD=None
 Undefined=None
 value__=None
 Walkthrough=None

