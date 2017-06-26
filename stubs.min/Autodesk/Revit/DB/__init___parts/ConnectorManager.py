class ConnectorManager(object,IDisposable):
 """ Provides access to the Connector Manager """
 def Dispose(self):
  """ Dispose(self: ConnectorManager) """
  pass
 def Lookup(self,index):
  """
  Lookup(self: ConnectorManager,index: int) -> Connector
  
   Lookup the connector using the unique index value that identify this connector.
  
   index: The unique index value.
   Returns: Returns the connector or null if a connector for the provided unique index 
    value doesn't exist.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ConnectorManager,disposing: bool) """
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
 Connectors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Return all the Connectors of the Connector Manager.

Get: Connectors(self: ConnectorManager) -> ConnectorSet

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ConnectorManager) -> bool

"""

 Owner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is used to retrieve the owner of the Connector Manager.

Get: Owner(self: ConnectorManager) -> Element

"""

 UnusedConnectors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Return all the unused Connectors of the Connector Manager.

Get: UnusedConnectors(self: ConnectorManager) -> ConnectorSet

"""


