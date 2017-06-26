class RoutingPreferenceManager(object,IDisposable):
 """ Manages default pipe segments,fittings,and selection criteria for a given MEPCurveType """
 def AddRule(self,groupType,rule,index=None):
  """
  AddRule(self: RoutingPreferenceManager,groupType: RoutingPreferenceRuleGroupType,rule: RoutingPreferenceRule)
   Adds a new routing preference rule to the rule group.
  
   groupType: The routing preference group in which the rule should be added.
   rule: The new rule to be added.
  AddRule(self: RoutingPreferenceManager,groupType: RoutingPreferenceRuleGroupType,rule: RoutingPreferenceRule,index: int)
   Adds a new routing preference rule to the specified position in the rule group.
  
   groupType: The routing preference group type in which the rule should be added.
   rule: The new rule to be added.
   index: The zero-based index position where the new rule will be added.
  """
  pass
 def Dispose(self):
  """ Dispose(self: RoutingPreferenceManager) """
  pass
 def GetMEPPartId(self,groupType,conditions):
  """
  GetMEPPartId(self: RoutingPreferenceManager,groupType: RoutingPreferenceRuleGroupType,conditions: RoutingConditions) -> ElementId
  
   Gets a fitting or segment id of given routing preference group that meets the 
    specified routing conditions.
  
  
   groupType: The routing preference group
   conditions: A set of routing conditions
   Returns: The Id of the fitting or segment that met the given routing conditions.
  """
  pass
 def GetNumberOfRules(self,eGroupType):
  """
  GetNumberOfRules(self: RoutingPreferenceManager,eGroupType: RoutingPreferenceRuleGroupType) -> int
  
   The number of RoutingPreference rules in a group.
  """
  pass
 def GetRule(self,groupType,index):
  """
  GetRule(self: RoutingPreferenceManager,groupType: RoutingPreferenceRuleGroupType,index: int) -> RoutingPreferenceRule
  
   Gets the specified rule.
  
   groupType: The routing preference group type from which the rule should be returned.
   index: The zero-based index where the rule should be returned.
   Returns: The rule at the specified group and zero-based index position.
  """
  pass
 def GetSharedSizes(self,size,shape):
  """
  GetSharedSizes(self: RoutingPreferenceManager,size: float,shape: ConnectorProfileType) -> IList[ElementId]
  
   Gets a list of all segments of a given profile shape that define a given size.
  
   size: The size to search for.
   shape: The profile shape of segment object.
   Returns: A list of all segments that define a given size.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RoutingPreferenceManager,disposing: bool) """
  pass
 def RemoveRule(self,groupType,index):
  """
  RemoveRule(self: RoutingPreferenceManager,groupType: RoutingPreferenceRuleGroupType,index: int)
   Removes an existing routing preference rule.
     Thrown if the index is out of 
    bounds.
  
  
   groupType: The routing preference group type in which the rule should be removed.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RoutingPreferenceManager) -> bool

"""

 OwnerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the MEPCurveType that owns the RoutingPreferenceManager

Get: OwnerId(self: RoutingPreferenceManager) -> ElementId

"""

 PreferredJunctionType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The preferred junction type.

Get: PreferredJunctionType(self: RoutingPreferenceManager) -> PreferredJunctionType

Set: PreferredJunctionType(self: RoutingPreferenceManager)=value
"""


