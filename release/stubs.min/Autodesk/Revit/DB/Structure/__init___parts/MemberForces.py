class MemberForces(object,IDisposable):
 """
 An object that represents a member forces on analytical model element.

 

 MemberForces(start: bool,force: XYZ,moment: XYZ)
 """
 def Dispose(self):
  """ Dispose(self: MemberForces) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: MemberForces,disposing: bool) """
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
 def __new__(self,start,force,moment):
  """ __new__(cls: type,start: bool,force: XYZ,moment: XYZ) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Force=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The translational forces at relative point position of the element.



Get: Force(self: MemberForces) -> XYZ



Set: Force(self: MemberForces)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: MemberForces) -> bool



"""

 Moment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rotational forces at relative point position of the element.



Get: Moment(self: MemberForces) -> XYZ



Set: Moment(self: MemberForces)=value

"""

 Start=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Member Forces position on analytical model stick element. True for start,false for end.



Get: Start(self: MemberForces) -> bool



Set: Start(self: MemberForces)=value

"""


