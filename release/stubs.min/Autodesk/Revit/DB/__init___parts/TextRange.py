class TextRange(object,IDisposable):
 """
 An object that is used to identify a range of characters in a

    Autodesk.Revit.DB.FormattedText.

 

 TextRange(start: int,length: int)

 TextRange()

 TextRange(other: TextRange)
 """
 def Dispose(self):
  """ Dispose(self: TextRange) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TextRange,disposing: bool) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,start: int,length: int)

  __new__(cls: type)

  __new__(cls: type,other: TextRange)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of the first character after the end of the range



Get: End(self: TextRange) -> int



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: TextRange) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The length of the range.



Get: Length(self: TextRange) -> int



Set: Length(self: TextRange)=value

"""

 Start=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The start index of a range within the Autodesk.Revit.DB.FormattedText.



Get: Start(self: TextRange) -> int



Set: Start(self: TextRange)=value

"""


