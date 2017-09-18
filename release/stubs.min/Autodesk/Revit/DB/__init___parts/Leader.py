class Leader(APIObject,IDisposable):
 """ A leader object that can be attached to annotation elements such as text notes. """
 def Dispose(self):
  """ Dispose(self: Leader,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Leader,disposing: bool)ReleaseUnmanagedResources(self: APIObject) """
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
 Anchor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Anchor point of the Leader



Get: Anchor(self: Leader) -> XYZ



"""

 Elbow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Elbow point of the Leader.



Get: Elbow(self: Leader) -> XYZ



Set: Elbow(self: Leader)=value

"""

 End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """End point of the Leader.



Get: End(self: Leader) -> XYZ



Set: End(self: Leader)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: Leader) -> bool



"""

 LeaderShape=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Geometric style of the leader



Get: LeaderShape(self: Leader) -> LeaderShape



"""


