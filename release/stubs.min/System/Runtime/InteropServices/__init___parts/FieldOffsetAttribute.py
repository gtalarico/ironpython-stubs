class FieldOffsetAttribute:
 """
 Indicates the physical position of fields within the unmanaged representation of a class or structure.
 
 FieldOffsetAttribute(offset: int)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return FieldOffsetAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,offset):
  """ __new__(cls: type,offset: int) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the offset from the beginning of the structure to the beginning of the field.

Get: Value(self: FieldOffsetAttribute) -> int

"""


