# encoding: utf-8
# module System.Net.Mime calls itself Mime
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ContentDisposition(object):
    """
    Represents a MIME protocol Content-Disposition header.
    
    ContentDisposition()
    ContentDisposition(disposition: str)
    """
    def Equals(self, rparam):
        """
        Equals(self: ContentDisposition, rparam: object) -> bool
        
            Determines whether the content-disposition header of the specified 
             System.Net.Mime.ContentDisposition object is equal to the content-disposition header of this 
             object.
        
        
            rparam: The System.Net.Mime.ContentDisposition object to compare with this object.
            Returns: true if the content-disposition headers are the same; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ContentDisposition) -> int
        
            Determines the hash code of the specified System.Net.Mime.ContentDisposition object
            Returns: An integer hash value.
        """
        pass

    def ToString(self):
        """
        ToString(self: ContentDisposition) -> str
        
            Returns a System.String representation of this instance.
            Returns: A System.String that contains the property values for this instance.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, disposition=None):
        """
        __new__(cls: type)
        __new__(cls: type, disposition: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    CreationDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the creation date for a file attachment.

Get: CreationDate(self: ContentDisposition) -> DateTime

Set: CreationDate(self: ContentDisposition) = value
"""

    DispositionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the disposition type for an e-mail attachment.

Get: DispositionType(self: ContentDisposition) -> str

Set: DispositionType(self: ContentDisposition) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the suggested file name for an e-mail attachment.

Get: FileName(self: ContentDisposition) -> str

Set: FileName(self: ContentDisposition) = value
"""

    Inline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Boolean value that determines the disposition type (Inline or Attachment) for an e-mail attachment.

Get: Inline(self: ContentDisposition) -> bool

Set: Inline(self: ContentDisposition) = value
"""

    ModificationDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the modification date for a file attachment.

Get: ModificationDate(self: ContentDisposition) -> DateTime

Set: ModificationDate(self: ContentDisposition) = value
"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parameters included in the Content-Disposition header represented by this instance.

Get: Parameters(self: ContentDisposition) -> StringDictionary

"""

    ReadDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the read date for a file attachment.

Get: ReadDate(self: ContentDisposition) -> DateTime

Set: ReadDate(self: ContentDisposition) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size of a file attachment.

Get: Size(self: ContentDisposition) -> Int64

Set: Size(self: ContentDisposition) = value
"""



class ContentType(object):
    """
    Represents a MIME protocol Content-Type header.
    
    ContentType()
    ContentType(contentType: str)
    """
    def Equals(self, rparam):
        """
        Equals(self: ContentType, rparam: object) -> bool
        
            Determines whether the content-type header of the specified System.Net.Mime.ContentType object 
             is equal to the content-type header of this object.
        
        
            rparam: The System.Net.Mime.ContentType object to compare with this object.
            Returns: true if the content-type headers are the same; otherwise false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ContentType) -> int
        
            Determines the hash code of the specified System.Net.Mime.ContentType object
            Returns: An integer hash value.
        """
        pass

    def ToString(self):
        """
        ToString(self: ContentType) -> str
        
            Returns a string representation of this System.Net.Mime.ContentType object.
            Returns: A System.String that contains the current settings for this System.Net.Mime.ContentType.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, contentType=None):
        """
        __new__(cls: type)
        __new__(cls: type, contentType: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Boundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the boundary parameter included in the Content-Type header represented by this instance.

Get: Boundary(self: ContentType) -> str

Set: Boundary(self: ContentType) = value
"""

    CharSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the charset parameter included in the Content-Type header represented by this instance.

Get: CharSet(self: ContentType) -> str

Set: CharSet(self: ContentType) = value
"""

    MediaType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the media type value included in the Content-Type header represented by this instance.

Get: MediaType(self: ContentType) -> str

Set: MediaType(self: ContentType) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the name parameter included in the Content-Type header represented by this instance.

Get: Name(self: ContentType) -> str

Set: Name(self: ContentType) = value
"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the dictionary that contains the parameters included in the Content-Type header represented by this instance.

Get: Parameters(self: ContentType) -> StringDictionary

"""



class DispositionTypeNames(object):
    """ Supplies the strings used to specify the disposition type for an e-mail attachment. """
    Attachment = 'attachment'
    Inline = 'inline'
    __all__ = [
        'Attachment',
        'Inline',
    ]


class MediaTypeNames(object):
    """ Specifies the media type information for an e-mail message attachment. """
    Application = None
    Image = None
    Text = None
    __all__ = [
        'Application',
        'Image',
        'Text',
    ]


class TransferEncoding(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the Content-Transfer-Encoding header information for an e-mail message attachment.
    
    enum TransferEncoding, values: Base64 (1), EightBit (3), QuotedPrintable (0), SevenBit (2), Unknown (-1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Base64 = None
    EightBit = None
    QuotedPrintable = None
    SevenBit = None
    Unknown = None
    value__ = None


