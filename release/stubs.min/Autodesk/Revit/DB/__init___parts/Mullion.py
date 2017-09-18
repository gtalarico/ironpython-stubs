class Mullion(FamilyInstance,IDisposable):
 """ Represents a CurtainGrid within Autodesk Revit. """
 def BreakMullion(self):
  """
  BreakMullion(self: Mullion)

   This method is used to break the current Mullion at ends with its neighboring 

    mullions.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def JoinMullion(self):
  """
  JoinMullion(self: Mullion)

   This method is used to control the join condition the current Mullion with its 

    neighboring mullions.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 LocationCurve=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This method get the curve location of the current Mullion.



Get: LocationCurve(self: Mullion) -> Curve



"""

 Lock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get - to get whether the Mullion line is locked.

   Set - Lock/unlock the Mullion.



Get: Lock(self: Mullion) -> bool



Set: Lock(self: Mullion)=value

"""

 Lockable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get - to get whether the Mullion can be lock or unlock.



Get: Lockable(self: Mullion) -> bool



"""

 MullionType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The MullionType style of this Mullion. 

Get - to access type of mullion

Set - change type of mullion. If the mullion is locked,InvalidOperationException exception will be thrown.



Get: MullionType(self: Mullion) -> MullionType



Set: MullionType(self: Mullion)=value

"""


