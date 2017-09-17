class ElectricalDemandFactorDefinition(Element,IDisposable):
 """
 The ElectricalDemandFactorDef class represents a serialized version of an instance of
    demand factor definition.  It has a name,rule type,and values for the rules that are serialized.
 
 ElectricalDemandFactorDefinition()
 """
 def AddValue(self,dfValue):
  """
  AddValue(self: ElectricalDemandFactorDefinition,dfValue: ElectricalDemandFactorValue)
   Adds a value to the value set for this demand factor definition
  
   dfValue: Value to add to the set
  """
  pass
 def ClearValues(self):
  """
  ClearValues(self: ElectricalDemandFactorDefinition)
   Clears all the values stored for this demand factor definition.
  """
  pass
 @staticmethod
 def Create(ADoc,strName):
  """
  Create(ADoc: Document,strName: str) -> ElectricalDemandFactorDefinition
  
   Creates a new instance of a demand factor definition.
  
   ADoc: The document where the element will be created and added.
   strName: The name of the electrical demand factor definition to be created.
   Returns: The newly created demand factor definition element.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetApplicableDemandFactor(self,numberOrLoad):
  """
  GetApplicableDemandFactor(self: ElectricalDemandFactorDefinition,numberOrLoad: float) -> float
  
   This method will return the applicable demand factor for the specified number
   
      of devices or load.
  
  
   numberOrLoad: The number of devices or load for which the demand factor should be looked up.
   Returns: The applicable demand factor.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetValues(self):
  """
  GetValues(self: ElectricalDemandFactorDefinition) -> ICollection[ElectricalDemandFactorValue]
  
   Provides access to the value set stored with this demand factor definition
  """
  pass
 def GetValuesCount(self):
  """
  GetValuesCount(self: ElectricalDemandFactorDefinition) -> int
  
   Returns the number of values in the set.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveValue(self,dfValue):
  """
  RemoveValue(self: ElectricalDemandFactorDefinition,dfValue: ElectricalDemandFactorValue)
   Removes a value to the value set for this demand factor definition
  
   dfValue: Value to remove from the set
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetValues(self,values):
  """ SetValues(self: ElectricalDemandFactorDefinition,values: ICollection[ElectricalDemandFactorValue]) """
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
 AdditionalLoad=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Additional load to be included during demand load calculation.

Get: AdditionalLoad(self: ElectricalDemandFactorDefinition) -> float

Set: AdditionalLoad(self: ElectricalDemandFactorDefinition)=value
"""

 IncludeAdditionalLoad=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Should the additional load (if set) be included in demand load calculations.

Get: IncludeAdditionalLoad(self: ElectricalDemandFactorDefinition) -> bool

Set: IncludeAdditionalLoad(self: ElectricalDemandFactorDefinition)=value
"""

 RuleType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rule type for this demand factor definition.

Get: RuleType(self: ElectricalDemandFactorDefinition) -> ElectricalDemandFactorRule

Set: RuleType(self: ElectricalDemandFactorDefinition)=value
"""


