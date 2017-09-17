class TextNoteOptions(object,IDisposable):
 """
 Options to use when creating a new text note element.
 
 TextNoteOptions(typeId: ElementId)
 TextNoteOptions()
 """
 def Dispose(self):
  """ Dispose(self: TextNoteOptions) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TextNoteOptions,disposing: bool) """
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
 def __new__(self,typeId=None):
  """
  __new__(cls: type,typeId: ElementId)
  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 HorizontalAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Horizontal alignment of the text.

Get: HorizontalAlignment(self: TextNoteOptions) -> HorizontalTextAlignment

Set: HorizontalAlignment(self: TextNoteOptions)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: TextNoteOptions) -> bool

"""

 KeepRotatedTextReadable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Flag controling whether a rotate text is to stay oriented to be always readable.

Get: KeepRotatedTextReadable(self: TextNoteOptions) -> bool

Set: KeepRotatedTextReadable(self: TextNoteOptions)=value
"""

 Rotation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Base line angle of a text note,in radians.

Get: Rotation(self: TextNoteOptions) -> float

Set: Rotation(self: TextNoteOptions)=value
"""

 TypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of a text type that defines the style of a text note.

Get: TypeId(self: TextNoteOptions) -> ElementId

Set: TypeId(self: TextNoteOptions)=value
"""


