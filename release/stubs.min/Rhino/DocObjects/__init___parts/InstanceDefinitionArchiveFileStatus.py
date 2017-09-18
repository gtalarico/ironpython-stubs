class InstanceDefinitionArchiveFileStatus(Enum,IComparable,IFormattable,IConvertible):
 """
 The archive file of a linked instance definition can have the following possible states.

    Use InstanceObject.ArchiveFileStatus to query a instance definition's archive file status.

 

 enum InstanceDefinitionArchiveFileStatus,values: LinkedFileIsDifferent (3),LinkedFileIsNewer (1),LinkedFileIsOlder (2),LinkedFileIsUpToDate (0),LinkedFileNotFound (-1),LinkedFileNotReadable (-2),NotALinkedInstanceDefinition (-3)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 LinkedFileIsDifferent=None
 LinkedFileIsNewer=None
 LinkedFileIsOlder=None
 LinkedFileIsUpToDate=None
 LinkedFileNotFound=None
 LinkedFileNotReadable=None
 NotALinkedInstanceDefinition=None
 value__=None

