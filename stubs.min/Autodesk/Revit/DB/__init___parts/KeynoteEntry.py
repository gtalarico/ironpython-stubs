class KeynoteEntry(KeyBasedTreeEntry,IDisposable):
 """
 Represents an entry in the keynote table,containing the key value,keynote text,and parent key (if applicable).
 
 KeynoteEntry(key: str,text: str)
 KeynoteEntry(key: str,parentKey: str,text: str)
 """
 def Dispose(self):
  """ Dispose(self: KeyBasedTreeEntry,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: KeyBasedTreeEntry,disposing: bool) """
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
 def __new__(self,key,*__args):
  """
  __new__(cls: type,key: str,text: str)
  __new__(cls: type,key: str,parentKey: str,text: str)
  """
  pass
 KeynoteText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The text associated with this KeynoteEntry.

Get: KeynoteText(self: KeynoteEntry) -> str

"""


