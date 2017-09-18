class IPerformanceAdviserRule:
 """ Base class to derive specific performance adviser rules from. """
 def ExecuteElementCheck(self,document,element):
  """
  ExecuteElementCheck(self: IPerformanceAdviserRule,document: Document,element: Element)

   Invoked by performance advisor for each element to be checked.

  

   document: Document for which performance problems are being checked.

   element: The Element being checked for performance problems.
  """
  pass
 def FinalizeCheck(self,document):
  """
  FinalizeCheck(self: IPerformanceAdviserRule,document: Document)

   Invoked by performance advisor once in the end of the check.

  

   document: Document for which performance problems are being checked.
  """
  pass
 def GetDescription(self):
  """
  GetDescription(self: IPerformanceAdviserRule) -> str

  

   Retrieves the description of the rule.

   Returns: The description of the rule.
  """
  pass
 def GetElementFilter(self,document):
  """
  GetElementFilter(self: IPerformanceAdviserRule,document: Document) -> ElementFilter

  

   Retrieves a filter to restrict elements to be checked.

  

   document: Document for which performance problems are being checked.

   Returns: The filter to restrict elements to be checked.
  """
  pass
 def GetName(self):
  """
  GetName(self: IPerformanceAdviserRule) -> str

  

   Retrieves the name of the rule.

   Returns: The name of the rule.
  """
  pass
 def InitCheck(self,document):
  """
  InitCheck(self: IPerformanceAdviserRule,document: Document)

   Invoked by performance advisor once in the beginning of the check. If rule 

    checks document as a whole,

     the check can be performed in this method.

  

  

   document: Document for which performance problems are being checked.
  """
  pass
 def WillCheckElements(self):
  """
  WillCheckElements(self: IPerformanceAdviserRule) -> bool

  

   Reports if rule needs to be executed on individual elements.

   Returns: True if rule needs to be executed on individual elements.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
