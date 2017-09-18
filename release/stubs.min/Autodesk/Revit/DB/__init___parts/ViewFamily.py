class ViewFamily(Enum,IComparable,IFormattable,IConvertible):
 """
 An enumerated type that corresponds to the type of a Revit view.
 
 enum ViewFamily,values: AreaPlan (110),CeilingPlan (111),CostReport (106),Detail (113),Drafting (108),Elevation (114),FloorPlan (109),GraphicalColumnSchedule (119),ImageView (104),Invalid (101),Legend (117),LoadsReport (115),PanelSchedule (118),PressureLossReport (116),Schedule (105),Section (112),Sheet (107),StructuralPlan (120),ThreeDimensional (102),Walkthrough (103)
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
 CostReport=None
 Detail=None
 Drafting=None
 Elevation=None
 FloorPlan=None
 GraphicalColumnSchedule=None
 ImageView=None
 Invalid=None
 Legend=None
 LoadsReport=None
 PanelSchedule=None
 PressureLossReport=None
 Schedule=None
 Section=None
 Sheet=None
 StructuralPlan=None
 ThreeDimensional=None
 value__=None
 Walkthrough=None

