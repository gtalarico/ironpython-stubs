class NumberSystem(Element,IDisposable):
 """ An annotation that consists of a series of numeric tags attached to and describing a host element. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetReferencePick(self):
  """
  GetReferencePick(self: NumberSystem) -> Reference

  

   Gets the reference curve.

   Returns: The pick of reference curve.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetReferencePick(self,referencePick):
  """
  SetReferencePick(self: NumberSystem,referencePick: Reference)

   Sets the reference pick.

  

   referencePick: The pick to set.
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
 JustifyOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset to the justification curve.



Get: JustifyOffset(self: NumberSystem) -> float



Set: JustifyOffset(self: NumberSystem)=value

"""

 JustifyOption=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number justify option of number system.



Get: JustifyOption(self: NumberSystem) -> NumberSystemJustifyOption



Set: JustifyOption(self: NumberSystem)=value

"""

 NumberDisplayRule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The display rule of the number system.



Get: NumberDisplayRule(self: NumberSystem) -> NumberSystemDisplayRule



Set: NumberDisplayRule(self: NumberSystem)=value

"""

 NumberedElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The LinkElementId of the numbered host element.



Get: NumberedElementId(self: NumberSystem) -> LinkElementId



"""

 NumberOrientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number orientation of number system.



Get: NumberOrientation(self: NumberSystem) -> TagOrientation



Set: NumberOrientation(self: NumberSystem)=value

"""

 ReferenceOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset to the reference curve.



Get: ReferenceOffset(self: NumberSystem) -> float



Set: ReferenceOffset(self: NumberSystem)=value

"""


