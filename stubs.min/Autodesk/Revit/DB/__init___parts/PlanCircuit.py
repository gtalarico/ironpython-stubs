class PlanCircuit(APIObject,IDisposable):
 """ An object that represents an enclosed area in a plan view within the Autodesk Revit project. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def GetPointInside(self):
  """
  GetPointInside(self: PlanCircuit) -> UV
  
   Returns a point inside the circuit.
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
 Area=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The enclosed area of the circuit.

Get: Area(self: PlanCircuit) -> float

"""

 IsRoomLocated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Reports whether there is a room located in this circuit.

Get: IsRoomLocated(self: PlanCircuit) -> bool

"""

 SideNum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of sides in the circuit.

Get: SideNum(self: PlanCircuit) -> int

"""


