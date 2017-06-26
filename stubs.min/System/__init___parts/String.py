class String(object):
    """
    Represents text as a series of Unicode characters.
    
    str(value: Char*)
    str(value: Char*, startIndex: int, length: int)
    str(value: SByte*)
    str(value: SByte*, startIndex: int, length: int)
    str(value: SByte*, startIndex: int, length: int, enc: Encoding)
    str(value: Array[Char], startIndex: int, length: int)
    str(value: Array[Char])
    str(c: Char, count: int)
    """
    def capitalize(self, *args): #cannot find CLR method
        """
        capitalize(self: str) -> str
        
            Returns a copy of this string converted to uppercase
        """
        pass

    def center(self, *args): #cannot find CLR method
        """
        center(self: str, width: int, fillchar: Char) -> str
        center(self: str, width: int) -> str
        """
        pass

    def count(self, *args): #cannot find CLR method
        """
        count(self: str, ssub: str, start: int, end: int) -> int
        count(self: str, sub: str, start: int) -> int
        count(self: str, sub: str) -> int
        """
        pass

    def decode(self, *args): #cannot find CLR method
        """
        decode(s: str, encoding: object, errors: str) -> str
        decode(s: str) -> str
        """
        pass

    def encode(self, *args): #cannot find CLR method
        """ encode(s: str, encoding: object, errors: str) -> str """
        pass

    def endswith(self, *args): #cannot find CLR method
        """
        endswith(self: str, suffix: object) -> bool
        endswith(self: str, suffix: object, start: int) -> bool
        endswith(self: str, suffix: object, start: int, end: int) -> bool
        endswith(self: str, suffix: str) -> bool
        endswith(self: str, suffix: str, start: int) -> bool
        endswith(self: str, suffix: str, start: int, end: int) -> bool
        """
        pass

    def expandtabs(self, *args): #cannot find CLR method
        """
        expandtabs(self: str, tabsize: int) -> str
        expandtabs(self: str) -> str
        """
        pass

    def find(self, *args): #cannot find CLR method
        """
        find(self: str, sub: str, start: int, end: int) -> int
        find(self: str, sub: str, start: long, end: long) -> int
        find(self: str, sub: str, start: object, end: object) -> int
        find(self: str, sub: str) -> int
        find(self: str, sub: str, start: int) -> int
        find(self: str, sub: str, start: long) -> int
        """
        pass

    def format(self, *args): #cannot find CLR method
        """
        format(format_string�: str, **kwargs�: dict, *args�: Array[object]) -> str
        format(format_string: str, *args: Array[object]) -> str
        
            Replaces each replacement field in the string with the provided arguments.
                    
                    replacement_field =  "{" field_name ["!" conversion] [":" format_spec] "}"
                    field_name      
               =  (identifier | integer) ("." identifier | "[" element_index "]")*
                    
                    format_spec: [[fill]align][sign][#][0][width][,][.precision][type]
                    
                    Conversion can 
             be 'r' for repr or 's' for string.
        """
        pass

    def index(self, *args): #cannot find CLR method
        """
        index(self: str, sub: str, start: int, end: int) -> int
        index(self: str, sub: str, start: object, end: object) -> int
        index(self: str, sub: str) -> int
        index(self: str, sub: str, start: int) -> int
        """
        pass

    def isalnum(self, *args): #cannot find CLR method
        """ isalnum(self: str) -> bool """
        pass

    def isalpha(self, *args): #cannot find CLR method
        """ isalpha(self: str) -> bool """
        pass

    def isdecimal(self, *args): #cannot find CLR method
        """ isdecimal(self: str) -> bool """
        pass

    def isdigit(self, *args): #cannot find CLR method
        """ isdigit(self: str) -> bool """
        pass

    def islower(self, *args): #cannot find CLR method
        """ islower(self: str) -> bool """
        pass

    def isnumeric(self, *args): #cannot find CLR method
        """ isnumeric(self: str) -> bool """
        pass

    def isspace(self, *args): #cannot find CLR method
        """ isspace(self: str) -> bool """
        pass

    def istitle(self, *args): #cannot find CLR method
        """
        istitle(self: str) -> bool
        
            return true if self is a titlecased string and there is at least one
                    character in self; also, uppercase characters may only follow uncased
                    characters (e.g. whitespace) and 
             lowercase characters only cased ones.
                    return false otherwise.
        """
        pass

    def isunicode(self, *args): #cannot find CLR method
        """ isunicode(self: str) -> bool """
        pass

    def isupper(self, *args): #cannot find CLR method
        """ isupper(self: str) -> bool """
        pass

    def join(self, *args): #cannot find CLR method
        """
        join(self: str, sequence: list) -> str
        join(self: str, sequence: object) -> str
        
            Return a string which is the concatenation of the strings 
                    in the sequence seq. The separator between elements is the 
                    string providing this method
        """
        pass

    def ljust(self, *args): #cannot find CLR method
        """
        ljust(self: str, width: int, fillchar: Char) -> str
        ljust(self: str, width: int) -> str
        """
        pass

    def lower(self, *args): #cannot find CLR method
        """ lower(self: str) -> str """
        pass

    def lstrip(self, *args): #cannot find CLR method
        """
        lstrip(self: str, chars: str) -> str
        lstrip(self: str) -> str
        """
        pass

    def partition(self, *args): #cannot find CLR method
        """ partition(self: str, sep: str) -> tuple (of str) """
        pass

    def replace(self, *args): #cannot find CLR method
        """ replace(self: str, old: str, new: str, count: int) -> str """
        pass

    def rfind(self, *args): #cannot find CLR method
        """
        rfind(self: str, sub: str, start: int, end: int) -> int
        rfind(self: str, sub: str, start: long, end: long) -> int
        rfind(self: str, sub: str, start: object, end: object) -> int
        rfind(self: str, sub: str) -> int
        rfind(self: str, sub: str, start: int) -> int
        rfind(self: str, sub: str, start: long) -> int
        """
        pass

    def rindex(self, *args): #cannot find CLR method
        """
        rindex(self: str, sub: str, start: int, end: int) -> int
        rindex(self: str, sub: str, start: object, end: object) -> int
        rindex(self: str, sub: str) -> int
        rindex(self: str, sub: str, start: int) -> int
        """
        pass

    def rjust(self, *args): #cannot find CLR method
        """
        rjust(self: str, width: int, fillchar: Char) -> str
        rjust(self: str, width: int) -> str
        """
        pass

    def rpartition(self, *args): #cannot find CLR method
        """ rpartition(self: str, sep: str) -> tuple (of str) """
        pass

    def rsplit(self, *args): #cannot find CLR method
        """
        rsplit(self: str, sep: str, maxsplit: int) -> list
        rsplit(self: str, sep: str) -> list
        rsplit(self: str) -> list
        """
        pass

    def rstrip(self, *args): #cannot find CLR method
        """
        rstrip(self: str, chars: str) -> str
        rstrip(self: str) -> str
        """
        pass

    def split(self, *args): #cannot find CLR method
        """
        split(self: str, sep: str, maxsplit: int) -> list
        split(self: str, sep: str) -> list
        split(self: str) -> list
        """
        pass

    def splitlines(self, *args): #cannot find CLR method
        """
        splitlines(self: str, keepends: bool) -> list
        splitlines(self: str) -> list
        """
        pass

    def startswith(self, *args): #cannot find CLR method
        """
        startswith(self: str, prefix: object) -> bool
        startswith(self: str, prefix: object, start: int) -> bool
        startswith(self: str, prefix: object, start: int, end: int) -> bool
        startswith(self: str, prefix: str) -> bool
        startswith(self: str, prefix: str, start: int) -> bool
        startswith(self: str, prefix: str, start: int, end: int) -> bool
        """
        pass

    def strip(self, *args): #cannot find CLR method
        """
        strip(self: str, chars: str) -> str
        strip(self: str) -> str
        """
        pass

    def swapcase(self, *args): #cannot find CLR method
        """ swapcase(self: str) -> str """
        pass

    def title(self, *args): #cannot find CLR method
        """ title(self: str) -> str """
        pass

    def translate(self, *args): #cannot find CLR method
        """
        translate(self: str, table: str, deletechars: str) -> str
        translate(self: str, table: str) -> str
        translate(self: str, table: dict) -> str
        """
        pass

    def upper(self, *args): #cannot find CLR method
        """ upper(self: str) -> str """
        pass

    def zfill(self, *args): #cannot find CLR method
        """ zfill(self: str, width: int) -> str """
        pass

    def _formatter_field_name_split(self, *args): #cannot find CLR method
        """ _formatter_field_name_split(self: str) -> tuple """
        pass

    def _formatter_parser(self, *args): #cannot find CLR method
        """ _formatter_parser(self: str) -> IEnumerable[tuple] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(s: str, item: Char) -> bool
        __contains__(s: str, item: str) -> bool
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __getnewargs__(self, *args): #cannot find CLR method
        """ __getnewargs__(self: str) -> object """
        pass

    def __getslice__(self, *args): #cannot find CLR method
        """ __getslice__(self: str, x: int, y: int) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
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
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(self: Char, other: str) -> str
        __radd__(self: str, other: str) -> str
        """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(other: object, self: str) -> object """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(count: object, self: str) -> object
        __rmul__(count: Index, self: str) -> object
        __rmul__(other: int, self: str) -> str
        """
        pass

