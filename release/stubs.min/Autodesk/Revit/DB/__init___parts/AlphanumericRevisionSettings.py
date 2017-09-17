class AlphanumericRevisionSettings(object,IDisposable):
 """
 Contains settings that apply to Revisions with the Alphanumeric RevisionNumberType.
 
 AlphanumericRevisionSettings(sequence: IList[str],prefix: str,suffix: str)
 AlphanumericRevisionSettings()
 AlphanumericRevisionSettings(other: AlphanumericRevisionSettings)
 """
 def Dispose(self):
  """ Dispose(self: AlphanumericRevisionSettings) """
  pass
 def GetSequence(self):
  """
  GetSequence(self: AlphanumericRevisionSettings) -> IList[str]
  
   Gets a list containing the strings to be used as the numbering sequence for
     
    revisions with the Alphanumeric RevisionNumberType.
  """
  pass
 def IsEqual(self,other):
  """
  IsEqual(self: AlphanumericRevisionSettings,other: AlphanumericRevisionSettings) -> bool
  
   Determines whether a specified AlphanumericRevisionSettings is the same as 
    'this'.
  
  
   other: The AlphanumericRevisionSettings object to be compared with 'this'.
   Returns: True,if two AlphanumericRevisionSettings are the same.
  """
  pass
 def IsValid(self):
  """
  IsValid(self: AlphanumericRevisionSettings) -> bool
  
   Determines whether the AlphanumericRevisionSettings object is in a valid state.
   Returns: True if the settings are valid.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: AlphanumericRevisionSettings,disposing: bool) """
  pass
 def SetSequence(self,sequence):
  """ SetSequence(self: AlphanumericRevisionSettings,sequence: IList[str]) """
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
  __new__(cls: type,sequence: IList[str],prefix: str,suffix: str)
  __new__(cls: type)
  __new__(cls: type,other: AlphanumericRevisionSettings)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AlphanumericRevisionSettings) -> bool

"""

 Prefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The prefix string that will be prepended to the number of each revision with Alphanumeric RevisionNumberingType.

Get: Prefix(self: AlphanumericRevisionSettings) -> str

Set: Prefix(self: AlphanumericRevisionSettings)=value
"""

 Suffix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The suffix string that will be appended to the number of each revision with Alphanumeric RevisionNumberingType.

Get: Suffix(self: AlphanumericRevisionSettings) -> str

Set: Suffix(self: AlphanumericRevisionSettings)=value
"""


