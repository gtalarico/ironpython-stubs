class String(object):
 """
 Represents text as a series of Unicode characters.
 
 str(value: Char*)
 str(value: Char*,startIndex: int,length: int)
 str(value: SByte*)
 str(value: SByte*,startIndex: int,length: int)
 str(value: SByte*,startIndex: int,length: int,enc: Encoding)
 str(value: Array[Char],startIndex: int,length: int)
 str(value: Array[Char])
 str(c: Char,count: int)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return String()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def capitalize(self,*args):
  """ capitalize(self: str) -> str """
  pass
 def center(self,*args):
  """
  center(self: str,width: int) -> str
  center(self: str,width: int,fillchar: Char) -> str
  """
  pass
 def count(self,*args):
  """
  count(self: str,sub: str) -> int
  count(self: str,sub: str,start: int) -> int
  count(self: str,ssub: str,start: int,end: int) -> int
  """
  pass
 def decode(self,*args):
  """
  decode(s: str) -> str
  decode(s: str,encoding: object,errors: str) -> str
  """
  pass
 def encode(self,*args):
  """ encode(s: str,encoding: object,errors: str) -> str """
  pass
 def endswith(self,*args):
  """
  endswith(self: str,suffix: object) -> bool
  endswith(self: str,suffix: object,start: int) -> bool
  endswith(self: str,suffix: object,start: int,end: int) -> bool
  endswith(self: str,suffix: str) -> bool
  endswith(self: str,suffix: str,start: int) -> bool
  endswith(self: str,suffix: str,start: int,end: int) -> bool
  """
  pass
 def expandtabs(self,*args):
  """
  expandtabs(self: str) -> str
  expandtabs(self: str,tabsize: int) -> str
  """
  pass
 def find(self,*args):
  """
  find(self: str,sub: str) -> int
  find(self: str,sub: str,start: int) -> int
  find(self: str,sub: str,start: long) -> int
  find(self: str,sub: str,start: int,end: int) -> int
  find(self: str,sub: str,start: long,end: long) -> int
  find(self: str,sub: str,start: object,end: object) -> int
  """
  pass
 def format(self,*args):
  """
  format(format_string: str,*args: Array[object]) -> str
  format(format_string�: str,**kwargs�: dict,*args�: Array[object]) -> str
  """
  pass
 def index(self,*args):
  """
  index(self: str,sub: str) -> int
  index(self: str,sub: str,start: int) -> int
  index(self: str,sub: str,start: int,end: int) -> int
  index(self: str,sub: str,start: object,end: object) -> int
  """
  pass
 def isalnum(self,*args):
  """ isalnum(self: str) -> bool """
  pass
 def isalpha(self,*args):
  """ isalpha(self: str) -> bool """
  pass
 def isdecimal(self,*args):
  """ isdecimal(self: str) -> bool """
  pass
 def isdigit(self,*args):
  """ isdigit(self: str) -> bool """
  pass
 def islower(self,*args):
  """ islower(self: str) -> bool """
  pass
 def isnumeric(self,*args):
  """ isnumeric(self: str) -> bool """
  pass
 def isspace(self,*args):
  """ isspace(self: str) -> bool """
  pass
 def istitle(self,*args):
  """ istitle(self: str) -> bool """
  pass
 def isunicode(self,*args):
  """ isunicode(self: str) -> bool """
  pass
 def isupper(self,*args):
  """ isupper(self: str) -> bool """
  pass
 def join(self,*args):
  """
  join(self: str,sequence: object) -> str
  join(self: str,sequence: list) -> str
  """
  pass
 def ljust(self,*args):
  """
  ljust(self: str,width: int) -> str
  ljust(self: str,width: int,fillchar: Char) -> str
  """
  pass
 def lower(self,*args):
  """ lower(self: str) -> str """
  pass
 def lstrip(self,*args):
  """
  lstrip(self: str) -> str
  lstrip(self: str,chars: str) -> str
  """
  pass
 def partition(self,*args):
  """ partition(self: str,sep: str) -> tuple (of str) """
  pass
 def replace(self,*args):
  """ replace(self: str,old: str,new: str,count: int) -> str """
  pass
 def rfind(self,*args):
  """
  rfind(self: str,sub: str) -> int
  rfind(self: str,sub: str,start: int) -> int
  rfind(self: str,sub: str,start: long) -> int
  rfind(self: str,sub: str,start: int,end: int) -> int
  rfind(self: str,sub: str,start: long,end: long) -> int
  rfind(self: str,sub: str,start: object,end: object) -> int
  """
  pass
 def rindex(self,*args):
  """
  rindex(self: str,sub: str) -> int
  rindex(self: str,sub: str,start: int) -> int
  rindex(self: str,sub: str,start: int,end: int) -> int
  rindex(self: str,sub: str,start: object,end: object) -> int
  """
  pass
 def rjust(self,*args):
  """
  rjust(self: str,width: int) -> str
  rjust(self: str,width: int,fillchar: Char) -> str
  """
  pass
 def rpartition(self,*args):
  """ rpartition(self: str,sep: str) -> tuple (of str) """
  pass
 def rsplit(self,*args):
  """
  rsplit(self: str) -> list
  rsplit(self: str,sep: str) -> list
  rsplit(self: str,sep: str,maxsplit: int) -> list
  """
  pass
 def rstrip(self,*args):
  """
  rstrip(self: str) -> str
  rstrip(self: str,chars: str) -> str
  """
  pass
 def split(self,*args):
  """
  split(self: str) -> list
  split(self: str,sep: str) -> list
  split(self: str,sep: str,maxsplit: int) -> list
  """
  pass
 def splitlines(self,*args):
  """
  splitlines(self: str) -> list
  splitlines(self: str,keepends: bool) -> list
  """
  pass
 def startswith(self,*args):
  """
  startswith(self: str,prefix: object) -> bool
  startswith(self: str,prefix: object,start: int) -> bool
  startswith(self: str,prefix: object,start: int,end: int) -> bool
  startswith(self: str,prefix: str) -> bool
  startswith(self: str,prefix: str,start: int) -> bool
  startswith(self: str,prefix: str,start: int,end: int) -> bool
  """
  pass
 def strip(self,*args):
  """
  strip(self: str) -> str
  strip(self: str,chars: str) -> str
  """
  pass
 def swapcase(self,*args):
  """ swapcase(self: str) -> str """
  pass
 def title(self,*args):
  """ title(self: str) -> str """
  pass
 def translate(self,*args):
  """
  translate(self: str,table: dict) -> str
  translate(self: str,table: str) -> str
  translate(self: str,table: str,deletechars: str) -> str
  """
  pass
 def upper(self,*args):
  """ upper(self: str) -> str """
  pass
 def zfill(self,*args):
  """ zfill(self: str,width: int) -> str """
  pass
 def _formatter_field_name_split(self,*args):
  """ _formatter_field_name_split(self: str) -> tuple """
  pass
 def _formatter_parser(self,*args):
  """ _formatter_parser(self: str) -> IEnumerable[tuple] """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(s: str,item: str) -> bool
  __contains__(s: str,item: Char) -> bool
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
  pass
 def __getnewargs__(self,*args):
  """ __getnewargs__(self: str) -> object """
  pass
 def __getslice__(self,*args):
  """ __getslice__(self: str,x: int,y: int) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __mod__(self,*args):
  """ x.__mod__(y) <==> x%y """
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type) -> object
  __new__(cls: type,object: object) -> object
  __new__(cls: type,object: str) -> object
  __new__(cls: type,object: ExtensibleString) -> object
  __new__(cls: type,object: Char) -> object
  __new__(cls: type,object: long) -> object
  __new__(cls: type,object: Extensible[long]) -> object
  __new__(cls: type,object: int) -> object
  __new__(cls: type,object: bool) -> object
  __new__(cls: type,object: float) -> object
  __new__(cls: type,object: Extensible[float]) -> object
  __new__(cls: type,object: Single) -> object
  __new__(cls: type,string: object,encoding: str,errors: str) -> object
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(self: str,other: str) -> str
  __radd__(self: Char,other: str) -> str
  """
  pass
 def __rmod__(self,*args):
  """ __rmod__(other: object,self: str) -> object """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(other: int,self: str) -> str
  __rmul__(count: Index,self: str) -> object
  __rmul__(count: object,self: str) -> object
  """
  pass
