class PlanTopology(APIObject,IDisposable):
 """ An object that represents a Plan Topology within the Autodesk Revit project. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def GetRoomIds(self):
  """
  GetRoomIds(self: PlanTopology) -> ICollection[ElementId]
  
   Retrieves room ElementIds of the PlanTopology in the last phase.
   Returns: The PlanTopology Room ElementIds of the last phase.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
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
 Circuits=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Circuits of the PlanTopology.

Get: Circuits(self: PlanTopology) -> PlanCircuitSet

"""

 Level=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Level of the PlanTopology.

Get: Level(self: PlanTopology) -> Level

"""

 Phase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The phase of the PlanTopology.

Get: Phase(self: PlanTopology) -> Phase

"""


