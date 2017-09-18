class MEPModel(APIObject,IDisposable):
 """ Supports all MEP models that are persistent within the Autodesk Revit project """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
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
 AssignedElectricalSystems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves the electrical systems this electrical panel currently is assigned to.



Get: AssignedElectricalSystems(self: MEPModel) -> ElectricalSystemSet



"""

 ConnectorManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves the Connector Manager from this MEPModel.



Get: ConnectorManager(self: MEPModel) -> ConnectorManager



"""

 ElectricalSystems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves the electrical systems that are currently created using this MEPModel.



Get: ElectricalSystems(self: MEPModel) -> ElectricalSystemSet



"""


