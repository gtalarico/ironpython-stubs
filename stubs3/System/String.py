# encoding: utf-8
# module System.String calls itself str
# from (built-in)
# by generator 1.145
"""
str(value: Char*)
str(value: Char*, startIndex: int, length: int)
str(value: SByte*)
str(value: SByte*, startIndex: int, length: int)
str(value: SByte*, startIndex: int, length: int, enc: Encoding)
str(value: Array[Char], startIndex: int, length: int)
str(value: Array[Char])
str(c: Char, count: int)
"""
# no imports

# functions

def capitalize(self): # real signature unknown; restored from __doc__
    """ capitalize(self: str) -> str """
    return ""

def center(self, width, fillchar): # real signature unknown; restored from __doc__
    """
    center(self: str, width: int, fillchar: Char) -> str
    center(self: str, width: int) -> str
    """
    return ""

def count(self, ssub, start, end): # real signature unknown; restored from __doc__
    """
    count(self: str, ssub: str, start: int, end: int) -> int
    count(self: str, sub: str, start: int) -> int
    count(self: str, sub: str) -> int
    """
    return 0

def decode(s, encoding, errors): # real signature unknown; restored from __doc__
    """
    decode(s: str, encoding: object, errors: str) -> str
    decode(s: str) -> str
    """
    return ""

def encode(s, encoding, errors): # real signature unknown; restored from __doc__
    """ encode(s: str, encoding: object, errors: str) -> str """
    return ""

def endswith(self, suffix, start, end): # real signature unknown; restored from __doc__
    """
    endswith(self: str, suffix: object, start: int, end: int) -> bool
    endswith(self: str, suffix: object, start: int) -> bool
    endswith(self: str, suffix: object) -> bool
    """
    return False

def expandtabs(self, tabsize): # real signature unknown; restored from __doc__
    """
    expandtabs(self: str, tabsize: int) -> str
    expandtabs(self: str) -> str
    """
    return ""

def find(self, sub, start, end): # real signature unknown; restored from __doc__
    """
    find(self: str, sub: str, start: int, end: int) -> int
    find(self: str, sub: str, start: long, end: long) -> int
    find(self: str, sub: str, start: object, end: object) -> int
    find(self: str, sub: str) -> int
    find(self: str, sub: str, start: int) -> int
    find(self: str, sub: str, start: long) -> int
    """
    return 0

def format(format_string, **kwargs, *args, p_object=None): # real signature unknown; restored from __doc__
    """
    format(format_string: str, **kwargs: dict, *args: Array[object]) -> str
    format(format_string: str, *args: Array[object]) -> str
    """
    return ""

def index(self, sub, start, end): # real signature unknown; restored from __doc__
    """
    index(self: str, sub: str, start: int, end: int) -> int
    index(self: str, sub: str, start: object, end: object) -> int
    index(self: str, sub: str) -> int
    index(self: str, sub: str, start: int) -> int
    """
    return 0

def isalnum(self): # real signature unknown; restored from __doc__
    """ isalnum(self: str) -> bool """
    return False

def isalpha(self): # real signature unknown; restored from __doc__
    """ isalpha(self: str) -> bool """
    return False

def isdecimal(self): # real signature unknown; restored from __doc__
    """ isdecimal(self: str) -> bool """
    return False

def isdigit(self): # real signature unknown; restored from __doc__
    """ isdigit(self: str) -> bool """
    return False

def islower(self): # real signature unknown; restored from __doc__
    """ islower(self: str) -> bool """
    return False

def isnumeric(self): # real signature unknown; restored from __doc__
    """ isnumeric(self: str) -> bool """
    return False

def isspace(self): # real signature unknown; restored from __doc__
    """ isspace(self: str) -> bool """
    return False

def istitle(self): # real signature unknown; restored from __doc__
    """ istitle(self: str) -> bool """
    return False

def isunicode(self): # real signature unknown; restored from __doc__
    """ isunicode(self: str) -> bool """
    return False

def isupper(self): # real signature unknown; restored from __doc__
    """ isupper(self: str) -> bool """
    return False

def join(self, sequence): # real signature unknown; restored from __doc__
    """
    join(self: str, sequence: list) -> str
    join(self: str, sequence: object) -> str
    """
    return ""

def ljust(self, width, fillchar): # real signature unknown; restored from __doc__
    """
    ljust(self: str, width: int, fillchar: Char) -> str
    ljust(self: str, width: int) -> str
    """
    return ""

def lower(self): # real signature unknown; restored from __doc__
    """ lower(self: str) -> str """
    return ""

def lstrip(self, chars): # real signature unknown; restored from __doc__
    """
    lstrip(self: str, chars: str) -> str
    lstrip(self: str) -> str
    """
    return ""

def partition(self, sep): # real signature unknown; restored from __doc__
    """ partition(self: str, sep: str) -> tuple (of str) """
    return ()

def replace(self, old, new_, maxsplit): # real signature unknown; restored from __doc__
    """ replace(self: str, old: object, new_: object, maxsplit: int) -> str """
    return ""

def rfind(self, sub, start, end): # real signature unknown; restored from __doc__
    """
    rfind(self: str, sub: str, start: int, end: int) -> int
    rfind(self: str, sub: str, start: long, end: long) -> int
    rfind(self: str, sub: str, start: object, end: object) -> int
    rfind(self: str, sub: str) -> int
    rfind(self: str, sub: str, start: int) -> int
    rfind(self: str, sub: str, start: long) -> int
    """
    return 0

def rindex(self, sub, start, end): # real signature unknown; restored from __doc__
    """
    rindex(self: str, sub: str, start: int, end: int) -> int
    rindex(self: str, sub: str, start: object, end: object) -> int
    rindex(self: str, sub: str) -> int
    rindex(self: str, sub: str, start: int) -> int
    """
    return 0

def rjust(self, width, fillchar): # real signature unknown; restored from __doc__
    """
    rjust(self: str, width: int, fillchar: Char) -> str
    rjust(self: str, width: int) -> str
    """
    return ""

def rpartition(self, sep): # real signature unknown; restored from __doc__
    """ rpartition(self: str, sep: str) -> tuple (of str) """
    return ()

def rsplit(self, sep, maxsplit): # real signature unknown; restored from __doc__
    """
    rsplit(self: str, sep: str, maxsplit: int) -> list
    rsplit(self: str, sep: str) -> list
    rsplit(self: str) -> list
    """
    return []

def rstrip(self, chars): # real signature unknown; restored from __doc__
    """
    rstrip(self: str, chars: str) -> str
    rstrip(self: str) -> str
    """
    return ""

def split(self, sep, maxsplit): # real signature unknown; restored from __doc__
    """
    split(self: str, sep: str, maxsplit: int) -> list
    split(self: str, sep: str) -> list
    split(self: str) -> list
    """
    return []

def splitlines(self, keepends): # real signature unknown; restored from __doc__
    """
    splitlines(self: str, keepends: bool) -> list
    splitlines(self: str) -> list
    """
    return []

def startswith(self, prefix, start, end): # real signature unknown; restored from __doc__
    """
    startswith(self: str, prefix: object, start: int, end: int) -> bool
    startswith(self: str, prefix: object, start: int) -> bool
    startswith(self: str, prefix: object) -> bool
    """
    return False

def strip(self, chars): # real signature unknown; restored from __doc__
    """
    strip(self: str, chars: str) -> str
    strip(self: str) -> str
    """
    return ""

def swapcase(self): # real signature unknown; restored from __doc__
    """ swapcase(self: str) -> str """
    return ""

def title(self): # real signature unknown; restored from __doc__
    """ title(self: str) -> str """
    return ""

def translate(self, table, deletechars): # real signature unknown; restored from __doc__
    """
    translate(self: str, table: str, deletechars: str) -> str
    translate(self: str, table: str) -> str
    translate(self: str, table: dict) -> str
    """
    return ""

def upper(self): # real signature unknown; restored from __doc__
    """ upper(self: str) -> str """
    return ""

def zfill(self, width): # real signature unknown; restored from __doc__
    """ zfill(self: str, width: int) -> str """
    return ""

def _formatter_field_name_split(self): # real signature unknown; restored from __doc__
    """ _formatter_field_name_split(self: str) -> tuple """
    return ()

def _formatter_parser(self): # real signature unknown; restored from __doc__
    """ _formatter_parser(self: str) -> IEnumerable[tuple] """
    pass

def __add__(y): # real signature unknown; restored from __doc__
    """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
    pass

def __contains__(s, item): # real signature unknown; restored from __doc__
    """
    __contains__(s: str, item: Char) -> bool
    __contains__(s: str, item: str) -> bool
    """
    return False

def __eq__(y): # real signature unknown; restored from __doc__
    """ x.__eq__(y) <==> x==y """
    pass

def __format__(self, formatSpec): # real signature unknown; restored from __doc__
    """ __format__(self: str, formatSpec: str) -> str """
    return ""

def __getitem__(y): # real signature unknown; restored from __doc__
    """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
    pass

def __getnewargs__(self): # real signature unknown; restored from __doc__
    """ __getnewargs__(self: str) -> object """
    return object()

def __getslice__(self, x, y): # real signature unknown; restored from __doc__
    """ __getslice__(self: str, x: int, y: int) -> str """
    return ""

def __ge__(x, y): # real signature unknown; restored from __doc__
    """ __ge__(x: str, y: str) -> bool """
    return False

def __gt__(y): # real signature unknown; restored from __doc__
    """ x.__gt__(y) <==> x>y """
    pass

def __len__(): # real signature unknown; restored from __doc__
    """ x.__len__() <==> len(x) """
    pass

def __le__(x, y): # real signature unknown; restored from __doc__
    """ __le__(x: str, y: str) -> bool """
    return False

def __lt__(y): # real signature unknown; restored from __doc__
    """ x.__lt__(y) <==> x<y """
    pass

def __mod__(y): # real signature unknown; restored from __doc__
    """ x.__mod__(y) <==> x%y """
    pass

def __mul__(y): # real signature unknown; restored from __doc__
    """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
    pass

@staticmethod # known case of __new__
def __new__(cls, p_object): # real signature unknown; restored from __doc__
    """
    __new__(cls: type, object: float) -> object
    __new__(cls: type, object: bool) -> object
    __new__(cls: type, object: int) -> object
    __new__(cls: type, string: object, encoding: str, errors: str) -> object
    __new__(cls: type, object: Single) -> object
    __new__(cls: type, object: Extensible[float]) -> object
    __new__(cls: type, object: Extensible[long]) -> object
    __new__(cls: type, object: str) -> object
    __new__(cls: type, object: object) -> object
    __new__(cls: type) -> object
    __new__(cls: type, object: long) -> object
    __new__(cls: type, object: Char) -> object
    __new__(cls: type, object: ExtensibleString) -> object
    """
    return object()

def __ne__(a, b): # real signature unknown; restored from __doc__
    """ __ne__(a: str, b: str) -> bool """
    return False

def __radd__(self, other): # real signature unknown; restored from __doc__
    """
    __radd__(self: Char, other: str) -> str
    __radd__(self: str, other: str) -> str
    """
    return ""

def __repr__(self): # real signature unknown; restored from __doc__
    """ __repr__(self: str) -> str """
    return ""

def __rmod__(other, self): # real signature unknown; restored from __doc__
    """ __rmod__(other: object, self: str) -> object """
    return object()

def __rmul__(count, self): # real signature unknown; restored from __doc__
    """
    __rmul__(count: object, self: str) -> object
    __rmul__(count: Index, self: str) -> object
    __rmul__(other: int, self: str) -> str
    """
    return object()

def __str__(): # real signature unknown; restored from __doc__
    """ x.__str__() <==> str(x) """
    pass

# no classes
