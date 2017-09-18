class ElementPhaseStatusFilter(ElementSlowFilter,IDisposable):
 """
 A filter used to match elements that have a given phase status on a given phase.

 

 ElementPhaseStatusFilter(phaseId: ElementId,phaseStatuses: ICollection[ElementOnPhaseStatus],inverted: bool)

 ElementPhaseStatusFilter(phaseId: ElementId,phaseStatuses: ICollection[ElementOnPhaseStatus])

 ElementPhaseStatusFilter(phaseId: ElementId,phaseStatus: ElementOnPhaseStatus,inverted: bool)

 ElementPhaseStatusFilter(phaseId: ElementId,phaseStatus: ElementOnPhaseStatus)
 """
 def Dispose(self):
  """ Dispose(self: ElementFilter,A_0: bool) """
  pass
 def GetPhaseStatuses(self):
  """
  GetPhaseStatuses(self: ElementPhaseStatusFilter) -> ICollection[ElementOnPhaseStatus]

  

   Returns the phase statuses assigned to this filter.

   Returns: The phase statuses.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ElementFilter,disposing: bool) """
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
 def __new__(self,phaseId,*__args):
  """
  __new__(cls: type,phaseId: ElementId,phaseStatuses: ICollection[ElementOnPhaseStatus],inverted: bool)

  __new__(cls: type,phaseId: ElementId,phaseStatuses: ICollection[ElementOnPhaseStatus])

  __new__(cls: type,phaseId: ElementId,phaseStatus: ElementOnPhaseStatus,inverted: bool)

  __new__(cls: type,phaseId: ElementId,phaseStatus: ElementOnPhaseStatus)
  """
  pass
 PhaseId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The phase id.



Get: PhaseId(self: ElementPhaseStatusFilter) -> ElementId



"""


