class ComponentRepeaterSlot(Element,IDisposable):
 """ Represents a slot that holds one repeated component in a component repeater. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def IsTypeValidForSlot(self,typeId):
  """
  IsTypeValidForSlot(self: ComponentRepeaterSlot,typeId: ElementId) -> bool
  
   Determines whether instance of given family type can be used in the component 
    repeater slot.
  
  
   typeId: The element id of the type.
   Returns: True if the family type can be used in the component repeater slot.
  """
  pass
 def MakeDefault(self):
  """
  MakeDefault(self: ComponentRepeaterSlot)
   Populates the slot with an instance of the default family type of the component 
    repeater.
  """
  pass
 def MakeEmpty(self):
  """
  MakeEmpty(self: ComponentRepeaterSlot)
   Makes the slot empty by removing the instance currently held by the slot.
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
 FamilyType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the family type of the component in the slot,or invalid id if the slot is empty.

Get: FamilyType(self: ComponentRepeaterSlot) -> ElementId

Set: FamilyType(self: ComponentRepeaterSlot)=value
"""

 IsDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A flag indicating whether the slot currently holds an instance of the default family type of the component repeater.

Get: IsDefault(self: ComponentRepeaterSlot) -> bool

"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A flag indicating whether the slot is currently empty.

Get: IsEmpty(self: ComponentRepeaterSlot) -> bool

"""


