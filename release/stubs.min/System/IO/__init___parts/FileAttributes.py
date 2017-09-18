class FileAttributes(Enum,IComparable,IFormattable,IConvertible):
 """
 Provides attributes for files and directories.

 

 enum (flags) FileAttributes,values: Archive (32),Compressed (2048),Device (64),Directory (16),Encrypted (16384),Hidden (2),IntegrityStream (32768),Normal (128),NoScrubData (131072),NotContentIndexed (8192),Offline (4096),ReadOnly (1),ReparsePoint (1024),SparseFile (512),System (4),Temporary (256)
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
 Archive=None
 Compressed=None
 Device=None
 Directory=None
 Encrypted=None
 Hidden=None
 IntegrityStream=None
 Normal=None
 NoScrubData=None
 NotContentIndexed=None
 Offline=None
 ReadOnly=None
 ReparsePoint=None
 SparseFile=None
 System=None
 Temporary=None
 value__=None

