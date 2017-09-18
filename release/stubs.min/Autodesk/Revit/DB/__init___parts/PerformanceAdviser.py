class PerformanceAdviser(object,IDisposable):
 """ The tool to report performance problems in a given document. """
 def AddRule(self,id,rule):
  """
  AddRule(self: PerformanceAdviser,id: PerformanceAdviserRuleId,rule: IPerformanceAdviserRule)

   Adds a performance adviser rule to the list of rules.

  

   id: An id of the rule to be added to the list of rules.

   rule: The rule to be added
  """
  pass
 def DeleteRule(self,id):
  """
  DeleteRule(self: PerformanceAdviser,id: PerformanceAdviserRuleId)

   Deletes a performance adviser rule from the list of rules.

  

   id: An id of the rule to be deleted from the list of rules.
  """
  pass
 def Dispose(self):
  """ Dispose(self: PerformanceAdviser) """
  pass
 def ExecuteAllRules(self,document):
  """
  ExecuteAllRules(self: PerformanceAdviser,document: Document) -> IList[FailureMessage]

  

   Executes all rules in the list on a given document.

  

   document: Document on which the rules will be executed.

   Returns: Failure messages explaining performance problems detected in the document.
  """
  pass
 def ExecuteRules(self,document,rules):
  """
  ExecuteRules(self: PerformanceAdviser,document: Document,rules: IList[PerformanceAdviserRuleId]) -> IList[FailureMessage]

  ExecuteRules(self: PerformanceAdviser,document: Document,rules: IList[int]) -> IList[FailureMessage]
  """
  pass
 def GetAllRuleIds(self):
  """
  GetAllRuleIds(self: PerformanceAdviser) -> IList[PerformanceAdviserRuleId]

  

   Retrieves an enumeration of rule Ids.

   Returns: A collection of rule Ids
  """
  pass
 def GetElementFilterFromRule(self,*__args):
  """
  GetElementFilterFromRule(self: PerformanceAdviser,id: PerformanceAdviserRuleId,document: Document) -> ElementFilter

  

   Retrieves a filter to restrict elements to be checked.

  

   id: The rule id to get information for.

   document: Document for which performance problems are being checked.

   Returns: The filter to restrict elements to be checked.

  GetElementFilterFromRule(self: PerformanceAdviser,index: int,document: Document) -> ElementFilter

  

   Retrieves a filter to restrict elements to be checked.

  

   index: The rule index to get information for.

   document: Document for which performance problems are being checked.

   Returns: The filter to restrict elements to be checked.
  """
  pass
 def GetNumberOfRules(self):
  """
  GetNumberOfRules(self: PerformanceAdviser) -> int

  

   Retrieves number of performance adviser rules in the list.

   Returns: Number of performance adviser rules in the list.
  """
  pass
 @staticmethod
 def GetPerformanceAdviser():
  """
  GetPerformanceAdviser() -> PerformanceAdviser

  

   Returns the only instance of PerformanceAdviser in the Application.

   Returns: The only instance of PerformanceAdviser in the Application.
  """
  pass
 def GetRuleDescription(self,*__args):
  """
  GetRuleDescription(self: PerformanceAdviser,id: PerformanceAdviserRuleId) -> str

  

   Retrieves the description of the rule.

  

   id: The rule id to get information for.

   Returns: The description of the rule.

  GetRuleDescription(self: PerformanceAdviser,index: int) -> str

  

   Retrieves the description of the rule.

  

   index: The rule index to get information for.

   Returns: The description of the rule.
  """
  pass
 def GetRuleId(self,index):
  """
  GetRuleId(self: PerformanceAdviser,index: int) -> PerformanceAdviserRuleId

  

   Retrieves an id of a rule for a given index in the list.

  

   index: The index to retrieve the rule id for.

   Returns: The rule id.
  """
  pass
 def GetRuleName(self,*__args):
  """
  GetRuleName(self: PerformanceAdviser,id: PerformanceAdviserRuleId) -> str

  

   Retrieves the name of the rule.

  

   id: The rule id to get information for.

   Returns: The name of the rule.

  GetRuleName(self: PerformanceAdviser,index: int) -> str

  

   Retrieves the name of the rule.

  

   index: The rule index to get information for.

   Returns: The name of the rule.
  """
  pass
 def IsRuleEnabled(self,*__args):
  """
  IsRuleEnabled(self: PerformanceAdviser,index: int) -> bool

  

   Retrieves an enabled/disabled status for the given rule.

  

   index: The rule index to retrieve enabled/disabled status for.

   Returns: True if rule is disabled,false otherwise.

  IsRuleEnabled(self: PerformanceAdviser,id: PerformanceAdviserRuleId) -> bool

  

   Retrieves an enabled/disabled status for the given rule.

  

   id: The rule id to retrieve enabled/disabled status for.

   Returns: True if rule is disabled,false otherwise.
  """
  pass
 def PostWarning(self,message):
  """
  PostWarning(self: PerformanceAdviser,message: FailureMessage)

   Reports a problem detected during execution of a rule.

  

   message: Warning describing the problem detected by a rule.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: PerformanceAdviser,disposing: bool) """
  pass
 def SetRuleEnabled(self,*__args):
  """
  SetRuleEnabled(self: PerformanceAdviser,index: int,enabled: bool)

   Retrieves an enabled/disabled status for the given rule.

  

   index: The rule index to set enabled/disabled status for.

   enabled: True enables the rule,false disables.

  SetRuleEnabled(self: PerformanceAdviser,id: PerformanceAdviserRuleId,enabled: bool)

   Retrieves an enabled/disabled status for the given rule.

  

   id: The rule id to set enabled/disabled status for.

   enabled: True enables the rule,false disables.
  """
  pass
 def WillRuleCheckElements(self,*__args):
  """
  WillRuleCheckElements(self: PerformanceAdviser,id: PerformanceAdviserRuleId) -> bool

  

   Reports if rule needs to be executed on individual elements.

  

   id: The rule id to get information for.

   Returns: True if rule needs to be executed on individual elements.

  WillRuleCheckElements(self: PerformanceAdviser,index: int) -> bool

  

   Reports if rule needs to be executed on individual elements.

  

   index: The rule index to get information for.

   Returns: True if rule needs to be executed on individual elements.
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



Get: IsValidObject(self: PerformanceAdviser) -> bool



"""


