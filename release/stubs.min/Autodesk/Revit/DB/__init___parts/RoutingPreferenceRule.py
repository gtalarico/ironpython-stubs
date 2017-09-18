class RoutingPreferenceRule(object,IDisposable):
 """
 A class representing a rule set in MEP routing preferences.

 

 RoutingPreferenceRule(MEPPartId: ElementId,description: str)
 """
 def AddCriterion(self,myCriterion):
  """
  AddCriterion(self: RoutingPreferenceRule,myCriterion: RoutingCriterionBase)

   Adds a new routing criterion.

  

   myCriterion: The criterion to add.
  """
  pass
 def Dispose(self):
  """ Dispose(self: RoutingPreferenceRule) """
  pass
 def GetCriterion(self,index):
  """
  GetCriterion(self: RoutingPreferenceRule,index: int) -> RoutingCriterionBase

  

   Gets the specified criteria.

   Returns: The criterion at the specified zero-based index position.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RoutingPreferenceRule,disposing: bool) """
  pass
 def RemoveCriteron(self,index):
  """
  RemoveCriteron(self: RoutingPreferenceRule,index: int)

   Removes an existing criterion.

  

   index: The index position of removed routing preference rule in the group.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,MEPPartId,description):
  """ __new__(cls: type,MEPPartId: ElementId,description: str) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description of the routing preference rule.



Get: Description(self: RoutingPreferenceRule) -> str



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: RoutingPreferenceRule) -> bool



"""

 MEPPartId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The referenced MEPPart (segment or fitting) type in this rule. It may be InvalidElementId if no MEPPart will be allowed when the conditions satisfy the criteria in this rule.



Get: MEPPartId(self: RoutingPreferenceRule) -> ElementId



"""

 NumberOfCriteria=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of routing criteria.



Get: NumberOfCriteria(self: RoutingPreferenceRule) -> int



"""

 RoutingPreferenceManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the routing preference manager that owns this rule.



Get: RoutingPreferenceManager(self: RoutingPreferenceRule) -> RoutingPreferenceManager



"""


