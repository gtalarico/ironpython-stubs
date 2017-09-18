# encoding: utf-8
# module System.Text calls itself Text
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Encoding(object, ICloneable):
    """ Represents a character encoding. """
    def Clone(self):
        """
        Clone(self: Encoding) -> object
        
            When overridden in a derived class, creates a shallow copy of the current System.Text.Encoding 
             object.
        
            Returns: A copy of the current System.Text.Encoding object.
        """
        pass

    @staticmethod
    def Convert(srcEncoding, dstEncoding, bytes, index=None, count=None):
        """
        Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: Array[Byte], index: int, count: int) -> Array[Byte]
        
            Converts a range of bytes in a byte array from one encoding to another.
        
            srcEncoding: The encoding of the source array, bytes.
            dstEncoding: The encoding of the output array.
            bytes: The array of bytes to convert.
            index: The index of the first element of bytes to convert.
            count: The number of bytes to convert.
            Returns: An array of type System.Byte containing the result of converting a range of bytes in bytes from 
             srcEncoding to dstEncoding.
        
        Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: Array[Byte]) -> Array[Byte]
        
            Converts an entire byte array from one encoding to another.
        
            srcEncoding: The encoding format of bytes.
            dstEncoding: The target encoding format.
            bytes: The bytes to convert.
            Returns: An array of type System.Byte containing the results of converting bytes from srcEncoding to 
             dstEncoding.
        """
        pass

    def Equals(self, value):
        """
        Equals(self: Encoding, value: object) -> bool
        
            Determines whether the specified System.Object is equal to the current instance.
        
            value: The System.Object to compare with the current instance.
            Returns: true if value is an instance of System.Text.Encoding and is equal to the current instance; 
             otherwise, false.
        """
        pass

    def GetByteCount(self, *__args):
        """
        GetByteCount(self: Encoding, chars: Array[Char], index: int, count: int) -> int
        
            When overridden in a derived class, calculates the number of bytes produced by encoding a set of 
             characters from the specified character array.
        
        
            chars: The character array containing the set of characters to encode.
            index: The index of the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: Encoding, chars: Char*, count: int) -> int
        
            When overridden in a derived class, calculates the number of bytes produced by encoding a set of 
             characters starting at the specified character pointer.
        
        
            chars: A pointer to the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: Encoding, chars: Array[Char]) -> int
        
            When overridden in a derived class, calculates the number of bytes produced by encoding all the 
             characters in the specified character array.
        
        
            chars: The character array containing the characters to encode.
            Returns: The number of bytes produced by encoding all the characters in the specified character array.
        GetByteCount(self: Encoding, s: str) -> int
        
            When overridden in a derived class, calculates the number of bytes produced by encoding the 
             characters in the specified string.
        
        
            s: The string containing the set of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        """
        pass

    def GetBytes(self, *__args):
        """
        GetBytes(self: Encoding, s: str) -> Array[Byte]
        
            When overridden in a derived class, encodes all the characters in the specified string into a 
             sequence of bytes.
        
        
            s: The string containing the characters to encode.
            Returns: A byte array containing the results of encoding the specified set of characters.
        GetBytes(self: Encoding, s: str, charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            When overridden in a derived class, encodes a set of characters from the specified string into 
             the specified byte array.
        
        
            s: The string containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        GetBytes(self: Encoding, chars: Char*, charCount: int, bytes: Byte*, byteCount: int) -> int
        
            When overridden in a derived class, encodes a set of characters starting at the specified 
             character pointer into a sequence of bytes that are stored starting at the specified byte 
             pointer.
        
        
            chars: A pointer to the first character to encode.
            charCount: The number of characters to encode.
            bytes: A pointer to the location at which to start writing the resulting sequence of bytes.
            byteCount: The maximum number of bytes to write.
            Returns: The actual number of bytes written at the location indicated by the bytes parameter.
        GetBytes(self: Encoding, chars: Array[Char]) -> Array[Byte]
        
            When overridden in a derived class, encodes all the characters in the specified character array 
             into a sequence of bytes.
        
        
            chars: The character array containing the characters to encode.
            Returns: A byte array containing the results of encoding the specified set of characters.
        GetBytes(self: Encoding, chars: Array[Char], index: int, count: int) -> Array[Byte]
        
            When overridden in a derived class, encodes a set of characters from the specified character 
             array into a sequence of bytes.
        
        
            chars: The character array containing the set of characters to encode.
            index: The index of the first character to encode.
            count: The number of characters to encode.
            Returns: A byte array containing the results of encoding the specified set of characters.
        GetBytes(self: Encoding, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            When overridden in a derived class, encodes a set of characters from the specified character 
             array into the specified byte array.
        
        
            chars: The character array containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        """
        pass

    def GetCharCount(self, bytes, *__args):
        """
        GetCharCount(self: Encoding, bytes: Byte*, count: int) -> int
        
            When overridden in a derived class, calculates the number of characters produced by decoding a 
             sequence of bytes starting at the specified byte pointer.
        
        
            bytes: A pointer to the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        GetCharCount(self: Encoding, bytes: Array[Byte], index: int, count: int) -> int
        
            When overridden in a derived class, calculates the number of characters produced by decoding a 
             sequence of bytes from the specified byte array.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        GetCharCount(self: Encoding, bytes: Array[Byte]) -> int
        
            When overridden in a derived class, calculates the number of characters produced by decoding all 
             the bytes in the specified byte array.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        """
        pass

    def GetChars(self, bytes, *__args):
        """
        GetChars(self: Encoding, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int) -> int
        
            When overridden in a derived class, decodes a sequence of bytes from the specified byte array 
             into the specified character array.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            byteIndex: The index of the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: The character array to contain the resulting set of characters.
            charIndex: The index at which to start writing the resulting set of characters.
            Returns: The actual number of characters written into chars.
        GetChars(self: Encoding, bytes: Byte*, byteCount: int, chars: Char*, charCount: int) -> int
        
            When overridden in a derived class, decodes a sequence of bytes starting at the specified byte 
             pointer into a set of characters that are stored starting at the specified character pointer.
        
        
            bytes: A pointer to the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: A pointer to the location at which to start writing the resulting set of characters.
            charCount: The maximum number of characters to write.
            Returns: The actual number of characters written at the location indicated by the chars parameter.
        GetChars(self: Encoding, bytes: Array[Byte]) -> Array[Char]
        
            When overridden in a derived class, decodes all the bytes in the specified byte array into a set 
             of characters.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            Returns: A character array containing the results of decoding the specified sequence of bytes.
        GetChars(self: Encoding, bytes: Array[Byte], index: int, count: int) -> Array[Char]
        
            When overridden in a derived class, decodes a sequence of bytes from the specified byte array 
             into a set of characters.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: A character array containing the results of decoding the specified sequence of bytes.
        """
        pass

    def GetDecoder(self):
        """
        GetDecoder(self: Encoding) -> Decoder
        
            When overridden in a derived class, obtains a decoder that converts an encoded sequence of bytes 
             into a sequence of characters.
        
            Returns: A System.Text.Decoder that converts an encoded sequence of bytes into a sequence of characters.
        """
        pass

    def GetEncoder(self):
        """
        GetEncoder(self: Encoding) -> Encoder
        
            When overridden in a derived class, obtains an encoder that converts a sequence of Unicode 
             characters into an encoded sequence of bytes.
        
            Returns: A System.Text.Encoder that converts a sequence of Unicode characters into an encoded sequence of 
             bytes.
        """
        pass

    @staticmethod
    def GetEncoding(*__args):
        """
        GetEncoding(name: str) -> Encoding
        
            Returns the encoding associated with the specified code page name.
        
            name: The code page name of the preferred encoding. Any value returned by the 
             System.Text.Encoding.WebName property is valid. Possible values are listed in the Name column of 
             the table that appears in the System.Text.Encoding class topic.
        
            Returns: The encoding  associated with the specified code page.
        GetEncoding(name: str, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding
        
            Returns the encoding associated with the specified code page name. Parameters specify an error 
             handler for characters that cannot be encoded and byte sequences that cannot be decoded.
        
        
            name: The code page name of the preferred encoding. Any value returned by the 
             System.Text.Encoding.WebName property is valid. Possible values are listed in the Name column of 
             the table that appears in the System.Text.Encoding class topic.
        
            encoderFallback: An object that provides an error-handling procedure when a character cannot be encoded with the 
             current encoding.
        
            decoderFallback: An object that provides an error-handling procedure when a byte sequence cannot be decoded with 
             the current encoding.
        
            Returns: The encoding that is associated with the specified code page.
        GetEncoding(codepage: int) -> Encoding
        
            Returns the encoding associated with the specified code page identifier.
        
            codepage: The code page identifier of the preferred encoding. Possible values are listed in the Code Page 
             column of the table that appears in the System.Text.Encoding class topic.-or- 0 (zero), to use 
             the default encoding.
        
            Returns: The encoding that is associated with the specified code page.
        GetEncoding(codepage: int, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding
        
            Returns the encoding associated with the specified code page identifier. Parameters specify an 
             error handler for characters that cannot be encoded and byte sequences that cannot be decoded.
        
        
            codepage: The code page identifier of the preferred encoding. Possible values are listed in the Code Page 
             column of the table that appears in the System.Text.Encoding class topic.-or- 0 (zero), to use 
             the default encoding.
        
            encoderFallback: An object that provides an error-handling procedure when a character cannot be encoded with the 
             current encoding.
        
            decoderFallback: An object that provides an error-handling procedure when a byte sequence cannot be decoded with 
             the current encoding.
        
            Returns: The encoding that is associated with the specified code page.
        """
        pass

    @staticmethod
    def GetEncodings():
        """
        GetEncodings() -> Array[EncodingInfo]
        
            Returns an array that contains all encodings.
            Returns: An array that contains all encodings.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Encoding) -> int
        
            Returns the hash code for the current instance.
            Returns: The hash code for the current instance.
        """
        pass

    def GetMaxByteCount(self, charCount):
        """
        GetMaxByteCount(self: Encoding, charCount: int) -> int
        
            When overridden in a derived class, calculates the maximum number of bytes produced by encoding 
             the specified number of characters.
        
        
            charCount: The number of characters to encode.
            Returns: The maximum number of bytes produced by encoding the specified number of characters.
        """
        pass

    def GetMaxCharCount(self, byteCount):
        """
        GetMaxCharCount(self: Encoding, byteCount: int) -> int
        
            When overridden in a derived class, calculates the maximum number of characters produced by 
             decoding the specified number of bytes.
        
        
            byteCount: The number of bytes to decode.
            Returns: The maximum number of characters produced by decoding the specified number of bytes.
        """
        pass

    def GetPreamble(self):
        """
        GetPreamble(self: Encoding) -> Array[Byte]
        
            When overridden in a derived class, returns a sequence of bytes that specifies the encoding used.
            Returns: A byte array containing a sequence of bytes that specifies the encoding used.-or- A byte array 
             of length zero, if a preamble is not required.
        """
        pass

    def GetString(self, bytes, *__args):
        """
        GetString(self: Encoding, bytes: Array[Byte], index: int, count: int) -> str
        
            When overridden in a derived class, decodes a sequence of bytes from the specified byte array 
             into a string.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: A System.String containing the results of decoding the specified sequence of bytes.
        GetString(self: Encoding, bytes: Array[Byte]) -> str
        
            When overridden in a derived class, decodes all the bytes in the specified byte array into a 
             string.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            Returns: A System.String containing the results of decoding the specified sequence of bytes.
        GetString(self: Encoding, bytes: Byte*, byteCount: int) -> str
        """
        pass

    def IsAlwaysNormalized(self, form=None):
        """
        IsAlwaysNormalized(self: Encoding, form: NormalizationForm) -> bool
        
            When overridden in a derived class, gets a value indicating whether the current encoding is 
             always normalized, using the specified normalization form.
        
        
            form: One of the System.Text.NormalizationForm values.
            Returns: true if the current System.Text.Encoding object is always normalized using the specified 
             System.Text.NormalizationForm value; otherwise, false. The default is false.
        
        IsAlwaysNormalized(self: Encoding) -> bool
        
            Gets a value indicating whether the current encoding is always normalized, using the default 
             normalization form.
        
            Returns: true if the current System.Text.Encoding is always normalized; otherwise, false. The default is 
             false.
        """
        pass

    @staticmethod
    def RegisterProvider(provider):
        """ RegisterProvider(provider: EncodingProvider) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, codePage: int)
        __new__(cls: type, codePage: int, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BodyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a name for the current encoding that can be used with mail agent body tags.

Get: BodyName(self: Encoding) -> str

"""

    CodePage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the code page identifier of the current System.Text.Encoding.

Get: CodePage(self: Encoding) -> int

"""

    DecoderFallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Text.DecoderFallback object for the current System.Text.Encoding object.

Get: DecoderFallback(self: Encoding) -> DecoderFallback

Set: DecoderFallback(self: Encoding) = value
"""

    EncoderFallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Text.EncoderFallback object for the current System.Text.Encoding object.

Get: EncoderFallback(self: Encoding) -> EncoderFallback

Set: EncoderFallback(self: Encoding) = value
"""

    EncodingName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the human-readable description of the current encoding.

Get: EncodingName(self: Encoding) -> str

"""

    HeaderName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a name for the current encoding that can be used with mail agent header tags.

Get: HeaderName(self: Encoding) -> str

"""

    IsBrowserDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the current encoding can be used by browser clients for displaying content.

Get: IsBrowserDisplay(self: Encoding) -> bool

"""

    IsBrowserSave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the current encoding can be used by browser clients for saving content.

Get: IsBrowserSave(self: Encoding) -> bool

"""

    IsMailNewsDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the current encoding can be used by mail and news clients for displaying content.

Get: IsMailNewsDisplay(self: Encoding) -> bool

"""

    IsMailNewsSave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the current encoding can be used by mail and news clients for saving content.

Get: IsMailNewsSave(self: Encoding) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the current encoding is read-only.

Get: IsReadOnly(self: Encoding) -> bool

"""

    IsSingleByte = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the current encoding uses single-byte code points.

Get: IsSingleByte(self: Encoding) -> bool

"""

    WebName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the name registered with the Internet Assigned Numbers Authority (IANA) for the current encoding.

Get: WebName(self: Encoding) -> str

"""

    WindowsCodePage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the Windows operating system code page that most closely corresponds to the current encoding.

Get: WindowsCodePage(self: Encoding) -> int

"""


    ASCII = None
    BigEndianUnicode = None
    Default = None
    Unicode = None
    UTF32 = None
    UTF7 = None
    UTF8 = None


class ASCIIEncoding(Encoding, ICloneable):
    """
    Represents an ASCII character encoding of Unicode characters.
    
    ASCIIEncoding()
    """
    def GetByteCount(self, chars, *__args):
        """
        GetByteCount(self: ASCIIEncoding, chars: Char*, count: int) -> int
        
            Calculates the number of bytes produced by encoding a set of characters starting at the 
             specified character pointer.
        
        
            chars: A pointer to the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: ASCIIEncoding, chars: str) -> int
        
            Calculates the number of bytes produced by encoding the characters in the specified 
             System.String.
        
        
            chars: The System.String containing the set of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: ASCIIEncoding, chars: Array[Char], index: int, count: int) -> int
        
            Calculates the number of bytes produced by encoding a set of characters from the specified 
             character array.
        
        
            chars: The character array containing the set of characters to encode.
            index: The index of the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        """
        pass

    def GetBytes(self, *__args):
        """
        GetBytes(self: ASCIIEncoding, chars: Char*, charCount: int, bytes: Byte*, byteCount: int) -> int
        
            Encodes a set of characters starting at the specified character pointer into a sequence of bytes 
             that are stored starting at the specified byte pointer.
        
        
            chars: A pointer to the first character to encode.
            charCount: The number of characters to encode.
            bytes: A pointer to the location at which to start writing the resulting sequence of bytes.
            byteCount: The maximum number of bytes to write.
            Returns: The actual number of bytes written at the location indicated by bytes.
        GetBytes(self: ASCIIEncoding, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            Encodes a set of characters from the specified character array into the specified byte array.
        
            chars: The character array containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        GetBytes(self: ASCIIEncoding, chars: str, charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            Encodes a set of characters from the specified System.String into the specified byte array.
        
            chars: The System.String containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        """
        pass

    def GetCharCount(self, bytes, *__args):
        """
        GetCharCount(self: ASCIIEncoding, bytes: Byte*, count: int) -> int
        
            Calculates the number of characters produced by decoding a sequence of bytes starting at the 
             specified byte pointer.
        
        
            bytes: A pointer to the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        GetCharCount(self: ASCIIEncoding, bytes: Array[Byte], index: int, count: int) -> int
        
            Calculates the number of characters produced by decoding a sequence of bytes from the specified 
             byte array.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        """
        pass

    def GetChars(self, bytes, *__args):
        """
        GetChars(self: ASCIIEncoding, bytes: Byte*, byteCount: int, chars: Char*, charCount: int) -> int
        
            Decodes a sequence of bytes starting at the specified byte pointer into a set of characters that 
             are stored starting at the specified character pointer.
        
        
            bytes: A pointer to the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: A pointer to the location at which to start writing the resulting set of characters.
            charCount: The maximum number of characters to write.
            Returns: The actual number of characters written at the location indicated by chars.
        GetChars(self: ASCIIEncoding, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int) -> int
        
            Decodes a sequence of bytes from the specified byte array into the specified character array.
        
            bytes: The byte array containing the sequence of bytes to decode.
            byteIndex: The index of the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: The character array to contain the resulting set of characters.
            charIndex: The index at which to start writing the resulting set of characters.
            Returns: The actual number of characters written into chars.
        """
        pass

    def GetDecoder(self):
        """
        GetDecoder(self: ASCIIEncoding) -> Decoder
        
            Obtains a decoder that converts an ASCII encoded sequence of bytes into a sequence of Unicode 
             characters.
        
            Returns: A System.Text.Decoder that converts an ASCII encoded sequence of bytes into a sequence of 
             Unicode characters.
        """
        pass

    def GetEncoder(self):
        """
        GetEncoder(self: ASCIIEncoding) -> Encoder
        
            Obtains an encoder that converts a sequence of Unicode characters into an ASCII encoded sequence 
             of bytes.
        
            Returns: An System.Text.Encoder that converts a sequence of Unicode characters into an ASCII encoded 
             sequence of bytes.
        """
        pass

    def GetMaxByteCount(self, charCount):
        """
        GetMaxByteCount(self: ASCIIEncoding, charCount: int) -> int
        
            Calculates the maximum number of bytes produced by encoding the specified number of characters.
        
            charCount: The number of characters to encode.
            Returns: The maximum number of bytes produced by encoding the specified number of characters.
        """
        pass

    def GetMaxCharCount(self, byteCount):
        """
        GetMaxCharCount(self: ASCIIEncoding, byteCount: int) -> int
        
            Calculates the maximum number of characters produced by decoding the specified number of bytes.
        
            byteCount: The number of bytes to decode.
            Returns: The maximum number of characters produced by decoding the specified number of bytes.
        """
        pass

    def GetString(self, bytes, *__args):
        """
        GetString(self: ASCIIEncoding, bytes: Array[Byte], byteIndex: int, byteCount: int) -> str
        
            Decodes a range of bytes from a byte array into a string.
        
            bytes: The byte array containing the sequence of bytes to decode.
            byteIndex: The index of the first byte to decode.
            byteCount: The number of bytes to decode.
            Returns: A System.String containing the results of decoding the specified sequence of bytes.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    IsSingleByte = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current encoding uses single-byte code points.

Get: IsSingleByte(self: ASCIIEncoding) -> bool

"""



class Decoder(object):
    """ Converts a sequence of encoded bytes into a set of characters. """
    def Convert(self, bytes, *__args):
        """
        Convert(self: Decoder, bytes: Byte*, byteCount: int, chars: Char*, charCount: int, flush: bool) -> (int, int, bool)
        
            Converts a buffer of encoded bytes to UTF-16 encoded characters and stores the result in another 
             buffer.
        
        
            bytes: The address of a buffer that contains the byte sequences to convert.
            byteCount: The number of bytes in bytes to convert.
            chars: The address of a buffer to store the converted characters.
            charCount: The maximum number of characters in chars to use in the conversion.
            flush: true to indicate no further data is to be converted; otherwise, false.
        Convert(self: Decoder, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int, charCount: int, flush: bool) -> (int, int, bool)
        
            Converts an array of encoded bytes to UTF-16 encoded characters and stores the result in a byte 
             array.
        
        
            bytes: A byte array to convert.
            byteIndex: The first element of bytes to convert.
            byteCount: The number of elements of bytes to convert.
            chars: An array to store the converted characters.
            charIndex: The first element of chars in which data is stored.
            charCount: The maximum number of elements of chars to use in the conversion.
            flush: true to indicate that no further data is to be converted; otherwise, false.
        """
        pass

    def GetCharCount(self, bytes, *__args):
        """
        GetCharCount(self: Decoder, bytes: Byte*, count: int, flush: bool) -> int
        
            When overridden in a derived class, calculates the number of characters produced by decoding a 
             sequence of bytes starting at the specified byte pointer. A parameter indicates whether to clear 
             the internal state of the decoder after the calculation.
        
        
            bytes: A pointer to the first byte to decode.
            count: The number of bytes to decode.
            flush: true to simulate clearing the internal state of the encoder after the calculation; otherwise, 
             false.
        
            Returns: The number of characters produced by decoding the specified sequence of bytes and any bytes in 
             the internal buffer.
        
        GetCharCount(self: Decoder, bytes: Array[Byte], index: int, count: int, flush: bool) -> int
        
            When overridden in a derived class, calculates the number of characters produced by decoding a 
             sequence of bytes from the specified byte array. A parameter indicates whether to clear the 
             internal state of the decoder after the calculation.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            flush: true to simulate clearing the internal state of the encoder after the calculation; otherwise, 
             false.
        
            Returns: The number of characters produced by decoding the specified sequence of bytes and any bytes in 
             the internal buffer.
        
        GetCharCount(self: Decoder, bytes: Array[Byte], index: int, count: int) -> int
        
            When overridden in a derived class, calculates the number of characters produced by decoding a 
             sequence of bytes from the specified byte array.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes and any bytes in 
             the internal buffer.
        """
        pass

    def GetChars(self, bytes, *__args):
        """
        GetChars(self: Decoder, bytes: Byte*, byteCount: int, chars: Char*, charCount: int, flush: bool) -> int
        
            When overridden in a derived class, decodes a sequence of bytes starting at the specified byte 
             pointer and any bytes in the internal buffer into a set of characters that are stored starting 
             at the specified character pointer. A parameter indicates whether to clear the internal state of 
             the decoder after the conversion.
        
        
            bytes: A pointer to the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: A pointer to the location at which to start writing the resulting set of characters.
            charCount: The maximum number of characters to write.
            flush: true to clear the internal state of the decoder after the conversion; otherwise, false.
            Returns: The actual number of characters written at the location indicated by the chars parameter.
        GetChars(self: Decoder, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int, flush: bool) -> int
        
            When overridden in a derived class, decodes a sequence of bytes from the specified byte array 
             and any bytes in the internal buffer into the specified character array. A parameter indicates 
             whether to clear the internal state of the decoder after the conversion.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            byteIndex: The index of the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: The character array to contain the resulting set of characters.
            charIndex: The index at which to start writing the resulting set of characters.
            flush: true to clear the internal state of the decoder after the conversion; otherwise, false.
            Returns: The actual number of characters written into the chars parameter.
        GetChars(self: Decoder, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int) -> int
        
            When overridden in a derived class, decodes a sequence of bytes from the specified byte array 
             and any bytes in the internal buffer into the specified character array.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            byteIndex: The index of the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: The character array to contain the resulting set of characters.
            charIndex: The index at which to start writing the resulting set of characters.
            Returns: The actual number of characters written into chars.
        """
        pass

    def Reset(self):
        """
        Reset(self: Decoder)
            When overridden in a derived class, sets the decoder back to its initial state.
        """
        pass

    Fallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Text.DecoderFallback object for the current System.Text.Decoder object.

Get: Fallback(self: Decoder) -> DecoderFallback

Set: Fallback(self: Decoder) = value
"""

    FallbackBuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Text.DecoderFallbackBuffer object associated with the current System.Text.Decoder object.

Get: FallbackBuffer(self: Decoder) -> DecoderFallbackBuffer

"""



class DecoderFallback(object):
    """ Provides a failure-handling mechanism, called a fallback, for an encoded input byte sequence that cannot be converted to an output character. """
    def CreateFallbackBuffer(self):
        """
        CreateFallbackBuffer(self: DecoderFallback) -> DecoderFallbackBuffer
        
            When overridden in a derived class, initializes a new instance of the 
             System.Text.DecoderFallbackBuffer class.
        
            Returns: An object that provides a fallback buffer for a decoder.
        """
        pass

    MaxCharCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the maximum number of characters the current System.Text.DecoderFallback object can return.

Get: MaxCharCount(self: DecoderFallback) -> int

"""


    ExceptionFallback = None
    ReplacementFallback = None


class DecoderExceptionFallback(DecoderFallback):
    """
    Throws System.Text.DecoderFallbackException if an encoded input byte sequence cannot be converted to a decoded output character. This class cannot be inherited.
    
    DecoderExceptionFallback()
    """
    def CreateFallbackBuffer(self):
        """
        CreateFallbackBuffer(self: DecoderExceptionFallback) -> DecoderFallbackBuffer
        
            Initializes a new instance of the System.Text.DecoderExceptionFallback class.
            Returns: A System.Text.DecoderFallbackBuffer object.
        """
        pass

    def Equals(self, value):
        """
        Equals(self: DecoderExceptionFallback, value: object) -> bool
        
            Indicates whether the current System.Text.DecoderExceptionFallback object and a specified object 
             are equal.
        
        
            value: An object that derives from the System.Text.DecoderExceptionFallback class.
            Returns: true if value is not null and is a System.Text.DecoderExceptionFallback object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DecoderExceptionFallback) -> int
        
            Retrieves the hash code for this instance.
            Returns: The return value is always the same arbitrary value, and has no special significance.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    MaxCharCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum number of characters this instance can return.

Get: MaxCharCount(self: DecoderExceptionFallback) -> int

"""



class DecoderFallbackBuffer(object):
    """ Provides a buffer that allows a fallback handler to return an alternate string to a decoder when it cannot decode an input byte sequence. """
    def Fallback(self, bytesUnknown, index):
        """
        Fallback(self: DecoderFallbackBuffer, bytesUnknown: Array[Byte], index: int) -> bool
        
            When overridden in a derived class, prepares the fallback buffer to handle the specified input 
             byte sequence.
        
        
            bytesUnknown: An input array of bytes.
            index: The index position of a byte in bytesUnknown.
            Returns: true if the fallback buffer can process bytesUnknown; false if the fallback buffer ignores 
             bytesUnknown.
        """
        pass

    def GetNextChar(self):
        """
        GetNextChar(self: DecoderFallbackBuffer) -> Char
        
            When overridden in a derived class, retrieves the next character in the fallback buffer.
            Returns: The next character in the fallback buffer.
        """
        pass

    def MovePrevious(self):
        """
        MovePrevious(self: DecoderFallbackBuffer) -> bool
        
            When overridden in a derived class, causes the next call to the 
             System.Text.DecoderFallbackBuffer.GetNextChar method to access the data buffer character 
             position that is prior to the current character position.
        
            Returns: true if the System.Text.DecoderFallbackBuffer.MovePrevious operation was successful; otherwise, 
             false.
        """
        pass

    def Reset(self):
        """
        Reset(self: DecoderFallbackBuffer)
            Initializes all data and state information pertaining to this fallback buffer.
        """
        pass

    Remaining = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the number of characters in the current System.Text.DecoderFallbackBuffer object that remain to be processed.

Get: Remaining(self: DecoderFallbackBuffer) -> int

"""



class DecoderExceptionFallbackBuffer(DecoderFallbackBuffer):
    """
    Throws System.Text.DecoderFallbackException when an encoded input byte sequence cannot be converted to a decoded output character. This class cannot be inherited.
    
    DecoderExceptionFallbackBuffer()
    """
    def Fallback(self, bytesUnknown, index):
        """
        Fallback(self: DecoderExceptionFallbackBuffer, bytesUnknown: Array[Byte], index: int) -> bool
        
            Throws System.Text.DecoderFallbackException when the input byte sequence cannot be decoded. The 
             nominal return value is not used.
        
        
            bytesUnknown: An input array of bytes.
            index: The index position of a byte in the input.
            Returns: None. No value is returned because the 
             System.Text.DecoderExceptionFallbackBuffer.Fallback(System.Byte[],System.Int32) method always 
             throws an exception. The nominal return value is true. A return value is defined, although it is 
             unchanging, because this method implements an abstract method.
        """
        pass

    def GetNextChar(self):
        """
        GetNextChar(self: DecoderExceptionFallbackBuffer) -> Char
        
            Retrieves the next character in the exception data buffer.
            Returns: The return value is always the Unicode character NULL (U+0000). A return value is defined, 
             although it is unchanging, because this method implements an abstract method.
        """
        pass

    def MovePrevious(self):
        """
        MovePrevious(self: DecoderExceptionFallbackBuffer) -> bool
        
            Causes the next call to System.Text.DecoderExceptionFallbackBuffer.GetNextChar to access the 
             exception data buffer character position that is prior to the current position.
        
            Returns: The return value is always false. A return value is defined, although it is unchanging, because 
             this method implements an abstract method.
        """
        pass

    Remaining = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of characters in the current System.Text.DecoderExceptionFallbackBuffer object that remain to be processed.

Get: Remaining(self: DecoderExceptionFallbackBuffer) -> int

"""



class DecoderFallbackException(ArgumentException, ISerializable, _Exception):
    """
    The exception that is thrown when a decoder fallback operation fails. This class cannot be inherited.
    
    DecoderFallbackException()
    DecoderFallbackException(message: str)
    DecoderFallbackException(message: str, innerException: Exception)
    DecoderFallbackException(message: str, bytesUnknown: Array[Byte], index: int)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str, bytesUnknown: Array[Byte], index: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BytesUnknown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the input byte sequence that caused the exception.

Get: BytesUnknown(self: DecoderFallbackException) -> Array[Byte]

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index position in the input byte sequence of the byte that caused the exception.

Get: Index(self: DecoderFallbackException) -> int

"""



class DecoderReplacementFallback(DecoderFallback):
    """
    Provides a failure-handling mechanism, called a fallback, for an encoded input byte sequence that cannot be converted to an output character. The fallback emits a user-specified replacement string instead of a decoded input byte sequence. This class cannot be inherited.
    
    DecoderReplacementFallback()
    DecoderReplacementFallback(replacement: str)
    """
    def CreateFallbackBuffer(self):
        """
        CreateFallbackBuffer(self: DecoderReplacementFallback) -> DecoderFallbackBuffer
        
            Creates a System.Text.DecoderFallbackBuffer object that is initialized with the replacement 
             string of this System.Text.DecoderReplacementFallback object.
        
            Returns: A System.Text.DecoderFallbackBuffer object that specifies a string to use instead of the 
             original decoding operation input.
        """
        pass

    def Equals(self, value):
        """
        Equals(self: DecoderReplacementFallback, value: object) -> bool
        
            Indicates whether the value of a specified object is equal to the 
             System.Text.DecoderReplacementFallback object.
        
        
            value: A System.Text.DecoderReplacementFallback object.
            Returns: true if value is a System.Text.DecoderReplacementFallback object having a 
             System.Text.DecoderReplacementFallback.DefaultString property that is equal to the 
             System.Text.DecoderReplacementFallback.DefaultString property of the current 
             System.Text.DecoderReplacementFallback object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DecoderReplacementFallback) -> int
        
            Retrieves the hash code for the value of the System.Text.DecoderReplacementFallback object.
            Returns: The hash code of the value of the object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, replacement=None):
        """
        __new__(cls: type)
        __new__(cls: type, replacement: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DefaultString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the replacement string that is the value of the System.Text.DecoderReplacementFallback object.

Get: DefaultString(self: DecoderReplacementFallback) -> str

"""

    MaxCharCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of characters in the replacement string for the System.Text.DecoderReplacementFallback object.

Get: MaxCharCount(self: DecoderReplacementFallback) -> int

"""



class DecoderReplacementFallbackBuffer(DecoderFallbackBuffer):
    """
    Represents a substitute output string that is emitted when the original input byte sequence cannot be decoded. This class cannot be inherited.
    
    DecoderReplacementFallbackBuffer(fallback: DecoderReplacementFallback)
    """
    def Fallback(self, bytesUnknown, index):
        """
        Fallback(self: DecoderReplacementFallbackBuffer, bytesUnknown: Array[Byte], index: int) -> bool
        
            Prepares the replacement fallback buffer to use the current replacement string.
        
            bytesUnknown: An input byte sequence. This parameter is ignored unless an exception is thrown.
            index: The index position of the byte in bytesUnknown. This parameter is ignored in this operation.
            Returns: true if the replacement string is not empty; false if the replacement string is empty.
        """
        pass

    def GetNextChar(self):
        """
        GetNextChar(self: DecoderReplacementFallbackBuffer) -> Char
        
            Retrieves the next character in the replacement fallback buffer.
            Returns: The next character in the replacement fallback buffer.
        """
        pass

    def MovePrevious(self):
        """
        MovePrevious(self: DecoderReplacementFallbackBuffer) -> bool
        
            Causes the next call to System.Text.DecoderReplacementFallbackBuffer.GetNextChar to access the 
             character position in the replacement fallback buffer prior to the current character position.
        
            Returns: true if the System.Text.DecoderReplacementFallbackBuffer.MovePrevious operation was successful; 
             otherwise, false.
        """
        pass

    def Reset(self):
        """
        Reset(self: DecoderReplacementFallbackBuffer)
            Initializes all internal state information and data in the 
             System.Text.DecoderReplacementFallbackBuffer object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fallback):
        """ __new__(cls: type, fallback: DecoderReplacementFallback) """
        pass

    Remaining = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of characters in the replacement fallback buffer that remain to be processed.

Get: Remaining(self: DecoderReplacementFallbackBuffer) -> int

"""



class Encoder(object):
    """ Converts a set of characters into a sequence of bytes. """
    def Convert(self, chars, *__args):
        """
        Convert(self: Encoder, chars: Char*, charCount: int, bytes: Byte*, byteCount: int, flush: bool) -> (int, int, bool)
        
            Converts a buffer of Unicode characters to an encoded byte sequence and stores the result in 
             another buffer.
        
        
            chars: The address of a string of UTF-16 encoded characters to convert.
            charCount: The number of characters in chars to convert.
            bytes: The address of a buffer to store the converted bytes.
            byteCount: The maximum number of bytes in bytes to use in the conversion.
            flush: true to indicate no further data is to be converted; otherwise, false.
        Convert(self: Encoder, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int, byteCount: int, flush: bool) -> (int, int, bool)
        
            Converts an array of Unicode characters to an encoded byte sequence and stores the result in an 
             array of bytes.
        
        
            chars: An array of characters to convert.
            charIndex: The first element of chars to convert.
            charCount: The number of elements of chars to convert.
            bytes: An array where the converted bytes are stored.
            byteIndex: The first element of bytes in which data is stored.
            byteCount: The maximum number of elements of bytes to use in the conversion.
            flush: true to indicate no further data is to be converted; otherwise, false.
        """
        pass

    def GetByteCount(self, chars, *__args):
        """
        GetByteCount(self: Encoder, chars: Char*, count: int, flush: bool) -> int
        
            When overridden in a derived class, calculates the number of bytes produced by encoding a set of 
             characters starting at the specified character pointer. A parameter indicates whether to clear 
             the internal state of the encoder after the calculation.
        
        
            chars: A pointer to the first character to encode.
            count: The number of characters to encode.
            flush: true to simulate clearing the internal state of the encoder after the calculation; otherwise, 
             false.
        
            Returns: The number of bytes produced by encoding the specified characters and any characters in the 
             internal buffer.
        
        GetByteCount(self: Encoder, chars: Array[Char], index: int, count: int, flush: bool) -> int
        
            When overridden in a derived class, calculates the number of bytes produced by encoding a set of 
             characters from the specified character array. A parameter indicates whether to clear the 
             internal state of the encoder after the calculation.
        
        
            chars: The character array containing the set of characters to encode.
            index: The index of the first character to encode.
            count: The number of characters to encode.
            flush: true to simulate clearing the internal state of the encoder after the calculation; otherwise, 
             false.
        
            Returns: The number of bytes produced by encoding the specified characters and any characters in the 
             internal buffer.
        """
        pass

    def GetBytes(self, chars, *__args):
        """
        GetBytes(self: Encoder, chars: Char*, charCount: int, bytes: Byte*, byteCount: int, flush: bool) -> int
        
            When overridden in a derived class, encodes a set of characters starting at the specified 
             character pointer and any characters in the internal buffer into a sequence of bytes that are 
             stored starting at the specified byte pointer. A parameter indicates whether to clear the 
             internal state of the encoder after the conversion.
        
        
            chars: A pointer to the first character to encode.
            charCount: The number of characters to encode.
            bytes: A pointer to the location at which to start writing the resulting sequence of bytes.
            byteCount: The maximum number of bytes to write.
            flush: true to clear the internal state of the encoder after the conversion; otherwise, false.
            Returns: The actual number of bytes written at the location indicated by the bytes parameter.
        GetBytes(self: Encoder, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int, flush: bool) -> int
        
            When overridden in a derived class, encodes a set of characters from the specified character 
             array and any characters in the internal buffer into the specified byte array. A parameter 
             indicates whether to clear the internal state of the encoder after the conversion.
        
        
            chars: The character array containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            flush: true to clear the internal state of the encoder after the conversion; otherwise, false.
            Returns: The actual number of bytes written into bytes.
        """
        pass

    def Reset(self):
        """
        Reset(self: Encoder)
            When overridden in a derived class, sets the encoder back to its initial state.
        """
        pass

    Fallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Text.EncoderFallback object for the current System.Text.Encoder object.

Get: Fallback(self: Encoder) -> EncoderFallback

Set: Fallback(self: Encoder) = value
"""

    FallbackBuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Text.EncoderFallbackBuffer object associated with the current System.Text.Encoder object.

Get: FallbackBuffer(self: Encoder) -> EncoderFallbackBuffer

"""



class EncoderFallback(object):
    """ Provides a failure-handling mechanism, called a fallback, for an input character that cannot be converted to an encoded output byte sequence. """
    def CreateFallbackBuffer(self):
        """
        CreateFallbackBuffer(self: EncoderFallback) -> EncoderFallbackBuffer
        
            When overridden in a derived class, initializes a new instance of the 
             System.Text.EncoderFallbackBuffer class.
        
            Returns: An  object that provides a fallback buffer for an encoder.
        """
        pass

    MaxCharCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the maximum number of characters the current System.Text.EncoderFallback object can return.

Get: MaxCharCount(self: EncoderFallback) -> int

"""


    ExceptionFallback = None
    ReplacementFallback = None


class EncoderExceptionFallback(EncoderFallback):
    """
    Throws a System.Text.EncoderFallbackException if an input character cannot be converted to an encoded output byte sequence. This class cannot be inherited.
    
    EncoderExceptionFallback()
    """
    def CreateFallbackBuffer(self):
        """
        CreateFallbackBuffer(self: EncoderExceptionFallback) -> EncoderFallbackBuffer
        
            Initializes a new instance of the System.Text.EncoderExceptionFallback class.
            Returns: A System.Text.EncoderFallbackBuffer object.
        """
        pass

    def Equals(self, value):
        """
        Equals(self: EncoderExceptionFallback, value: object) -> bool
        
            Indicates whether the current System.Text.EncoderExceptionFallback object and a specified object 
             are equal.
        
        
            value: An object that derives from the System.Text.EncoderExceptionFallback class.
            Returns: true if value is not null (Nothing in Visual Basic .NET) and is a 
             System.Text.EncoderExceptionFallback object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: EncoderExceptionFallback) -> int
        
            Retrieves the hash code for this instance.
            Returns: The return value is always the same arbitrary value, and has no special significance.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    MaxCharCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum number of characters this instance can return.

Get: MaxCharCount(self: EncoderExceptionFallback) -> int

"""



class EncoderFallbackBuffer(object):
    """ Provides a buffer that allows a fallback handler to return an alternate string to an encoder when it cannot encode an input character. """
    def Fallback(self, *__args):
        """
        Fallback(self: EncoderFallbackBuffer, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool
        
            When overridden in a derived class, prepares the fallback buffer to handle the specified 
             surrogate pair.
        
        
            charUnknownHigh: The high surrogate of the input pair.
            charUnknownLow: The low surrogate of the input pair.
            index: The index position of the surrogate pair in the input buffer.
            Returns: true if the fallback buffer can process charUnknownHigh and charUnknownLow; false if the 
             fallback buffer ignores the surrogate pair.
        
        Fallback(self: EncoderFallbackBuffer, charUnknown: Char, index: int) -> bool
        
            When overridden in a derived class, prepares the fallback buffer to handle the specified input 
             character.
        
        
            charUnknown: An input character.
            index: The index position of the character in the input buffer.
            Returns: true if the fallback buffer can process charUnknown; false if the fallback buffer ignores 
             charUnknown.
        """
        pass

    def GetNextChar(self):
        """
        GetNextChar(self: EncoderFallbackBuffer) -> Char
        
            When overridden in a derived class, retrieves the next character in the fallback buffer.
            Returns: The next character in the fallback buffer.
        """
        pass

    def MovePrevious(self):
        """
        MovePrevious(self: EncoderFallbackBuffer) -> bool
        
            When overridden in a derived class, causes the next call to the 
             System.Text.EncoderFallbackBuffer.GetNextChar method to access the data buffer character 
             position that is prior to the current character position.
        
            Returns: true if the System.Text.EncoderFallbackBuffer.MovePrevious operation was successful; otherwise, 
             false.
        """
        pass

    def Reset(self):
        """
        Reset(self: EncoderFallbackBuffer)
            Initializes all data and state information pertaining to this fallback buffer.
        """
        pass

    Remaining = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the number of characters in the current System.Text.EncoderFallbackBuffer object that remain to be processed.

Get: Remaining(self: EncoderFallbackBuffer) -> int

"""



class EncoderExceptionFallbackBuffer(EncoderFallbackBuffer):
    """
    Throws System.Text.EncoderFallbackException when an input character cannot be converted to an encoded output byte sequence. This class cannot be inherited.
    
    EncoderExceptionFallbackBuffer()
    """
    def Fallback(self, *__args):
        """
        Fallback(self: EncoderExceptionFallbackBuffer, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool
        
            Throws an exception because the input character cannot be encoded. Parameters specify the value 
             and index position of the surrogate pair in the input, and the nominal return value is not used.
        
        
            charUnknownHigh: The high surrogate of the input pair.
            charUnknownLow: The low surrogate of the input pair.
            index: The index position of the surrogate pair in the input buffer.
            Returns: None. No value is returned because the 
             System.Text.EncoderExceptionFallbackBuffer.Fallback(System.Char,System.Char,System.Int32) method 
             always throws an exception.
        
        Fallback(self: EncoderExceptionFallbackBuffer, charUnknown: Char, index: int) -> bool
        
            Throws an exception because the input character cannot be encoded. Parameters specify the value 
             and index position of the character that cannot be converted.
        
        
            charUnknown: An input character.
            index: The index position of the character in the input buffer.
            Returns: None. No value is returned because the 
             System.Text.EncoderExceptionFallbackBuffer.Fallback(System.Char,System.Int32) method always 
             throws an exception.
        """
        pass

    def GetNextChar(self):
        """
        GetNextChar(self: EncoderExceptionFallbackBuffer) -> Char
        
            Retrieves the next character in the exception fallback buffer.
            Returns: The return value is always the Unicode character, NULL (U+0000). A return value is defined, 
             although it is unchanging, because this method implements an abstract method.
        """
        pass

    def MovePrevious(self):
        """
        MovePrevious(self: EncoderExceptionFallbackBuffer) -> bool
        
            Causes the next call to the System.Text.EncoderExceptionFallbackBuffer.GetNextChar method to 
             access the exception data buffer character position that is prior to the current position.
        
            Returns: The return value is always false.A return value is defined, although it is unchanging, because 
             this method implements an abstract method.
        """
        pass

    Remaining = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of characters in the current System.Text.EncoderExceptionFallbackBuffer object that remain to be processed.

Get: Remaining(self: EncoderExceptionFallbackBuffer) -> int

"""



class EncoderFallbackException(ArgumentException, ISerializable, _Exception):
    """
    The exception that is thrown when an encoder fallback operation fails. This class cannot be inherited.
    
    EncoderFallbackException()
    EncoderFallbackException(message: str)
    EncoderFallbackException(message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def IsUnknownSurrogate(self):
        """
        IsUnknownSurrogate(self: EncoderFallbackException) -> bool
        
            Indicates whether the input that caused the exception is a surrogate pair.
            Returns: true if the input was a surrogate pair; otherwise, false.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CharUnknown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the input character that caused the exception.

Get: CharUnknown(self: EncoderFallbackException) -> Char

"""

    CharUnknownHigh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the high component character of the surrogate pair that caused the exception.

Get: CharUnknownHigh(self: EncoderFallbackException) -> Char

"""

    CharUnknownLow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the low component character of the surrogate pair that caused the exception.

Get: CharUnknownLow(self: EncoderFallbackException) -> Char

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index position in the input buffer of the character that caused the exception.

Get: Index(self: EncoderFallbackException) -> int

"""



class EncoderReplacementFallback(EncoderFallback):
    """
    Provides a failure handling mechanism, called a fallback, for an input character that cannot be converted to an output byte sequence. The fallback uses a user-specified replacement string instead of the original input character. This class cannot be inherited.
    
    EncoderReplacementFallback()
    EncoderReplacementFallback(replacement: str)
    """
    def CreateFallbackBuffer(self):
        """
        CreateFallbackBuffer(self: EncoderReplacementFallback) -> EncoderFallbackBuffer
        
            Creates a System.Text.EncoderFallbackBuffer object that is initialized with the replacement 
             string of this System.Text.EncoderReplacementFallback object.
        
            Returns: A System.Text.EncoderFallbackBuffer object equal to this System.Text.EncoderReplacementFallback 
             object.
        """
        pass

    def Equals(self, value):
        """
        Equals(self: EncoderReplacementFallback, value: object) -> bool
        
            Indicates whether the value of a specified object is equal to the 
             System.Text.EncoderReplacementFallback object.
        
        
            value: A System.Text.EncoderReplacementFallback object.
            Returns: true if the value parameter specifies an System.Text.EncoderReplacementFallback object and the 
             replacement string of that object is equal to the replacement string of this 
             System.Text.EncoderReplacementFallback object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: EncoderReplacementFallback) -> int
        
            Retrieves the hash code for the value of the System.Text.EncoderReplacementFallback object.
            Returns: The hash code of the value of the object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, replacement=None):
        """
        __new__(cls: type)
        __new__(cls: type, replacement: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DefaultString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the replacement string that is the value of the System.Text.EncoderReplacementFallback object.

Get: DefaultString(self: EncoderReplacementFallback) -> str

"""

    MaxCharCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of characters in the replacement string for the System.Text.EncoderReplacementFallback object.

Get: MaxCharCount(self: EncoderReplacementFallback) -> int

"""



class EncoderReplacementFallbackBuffer(EncoderFallbackBuffer):
    """
    Represents a substitute input string that is used when the original input character cannot be encoded. This class cannot be inherited.
    
    EncoderReplacementFallbackBuffer(fallback: EncoderReplacementFallback)
    """
    def Fallback(self, *__args):
        """
        Fallback(self: EncoderReplacementFallbackBuffer, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool
        
            Indicates whether a replacement string can be used when an input surrogate pair cannot be 
             encoded, or whether the surrogate pair can be ignored. Parameters specify the surrogate pair and 
             the index position of the pair in the input.
        
        
            charUnknownHigh: The high surrogate of the input pair.
            charUnknownLow: The low surrogate of the input pair.
            index: The index position of the surrogate pair in the input buffer.
            Returns: true if the replacement string is not empty; false if the replacement string is empty.
        Fallback(self: EncoderReplacementFallbackBuffer, charUnknown: Char, index: int) -> bool
        
            Prepares the replacement fallback buffer to use the current replacement string.
        
            charUnknown: An input character. This parameter is ignored in this operation unless an exception is thrown.
            index: The index position of the character in the input buffer. This parameter is ignored in this 
             operation.
        
            Returns: true if the replacement string is not empty; false if the replacement string is empty.
        """
        pass

    def GetNextChar(self):
        """
        GetNextChar(self: EncoderReplacementFallbackBuffer) -> Char
        
            Retrieves the next character in the replacement fallback buffer.
            Returns: The next Unicode character in the replacement fallback buffer that the application can encode.
        """
        pass

    def MovePrevious(self):
        """
        MovePrevious(self: EncoderReplacementFallbackBuffer) -> bool
        
            Causes the next call to the System.Text.EncoderReplacementFallbackBuffer.GetNextChar method to 
             access the character position in the replacement fallback buffer prior to the current character 
             position.
        
            Returns: true if the System.Text.EncoderReplacementFallbackBuffer.MovePrevious operation was successful; 
             otherwise, false.
        """
        pass

    def Reset(self):
        """
        Reset(self: EncoderReplacementFallbackBuffer)
            Initializes all internal state information and data in this instance of 
             System.Text.EncoderReplacementFallbackBuffer.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fallback):
        """ __new__(cls: type, fallback: EncoderReplacementFallback) """
        pass

    Remaining = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of characters in the replacement fallback buffer that remain to be processed.

Get: Remaining(self: EncoderReplacementFallbackBuffer) -> int

"""



class EncodingInfo(object):
    """ Provides basic information about an encoding. """
    def Equals(self, value):
        """
        Equals(self: EncodingInfo, value: object) -> bool
        
            Gets a value indicating whether the specified object is equal to the current 
             System.Text.EncodingInfo object.
        
        
            value: An object to compare to the current System.Text.EncodingInfo object.
            Returns: true if value is a System.Text.EncodingInfo object and is equal to the current 
             System.Text.EncodingInfo object; otherwise, false.
        """
        pass

    def GetEncoding(self):
        """
        GetEncoding(self: EncodingInfo) -> Encoding
        
            Returns a System.Text.Encoding object that corresponds to the current System.Text.EncodingInfo 
             object.
        
            Returns: A System.Text.Encoding object that corresponds to the current System.Text.EncodingInfo object.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: EncodingInfo) -> int
        
            Returns the hash code for the current System.Text.EncodingInfo object.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    CodePage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the code page identifier of the encoding.

Get: CodePage(self: EncodingInfo) -> int

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the human-readable description of the encoding.

Get: DisplayName(self: EncodingInfo) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name registered with the Internet Assigned Numbers Authority (IANA) for the encoding.

Get: Name(self: EncodingInfo) -> str

"""



class EncodingProvider(object):
    """ EncodingProvider() """
    def GetEncoding(self, *__args):
        """
        GetEncoding(self: EncodingProvider, name: str, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding
        GetEncoding(self: EncodingProvider, codepage: int, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding
        GetEncoding(self: EncodingProvider, name: str) -> Encoding
        GetEncoding(self: EncodingProvider, codepage: int) -> Encoding
        """
        pass


class NormalizationForm(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the type of normalization to perform.
    
    enum NormalizationForm, values: FormC (1), FormD (2), FormKC (5), FormKD (6)
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

    FormC = None
    FormD = None
    FormKC = None
    FormKD = None
    value__ = None


class StringBuilder(object, ISerializable):
    """
    Represents a mutable string of characters. This class cannot be inherited.
    
    StringBuilder()
    StringBuilder(capacity: int)
    StringBuilder(value: str)
    StringBuilder(value: str, capacity: int)
    StringBuilder(value: str, startIndex: int, length: int, capacity: int)
    StringBuilder(capacity: int, maxCapacity: int)
    """
    def Append(self, value, *__args):
        """
        Append(self: StringBuilder, value: Decimal) -> StringBuilder
        
            Appends the string representation of a specified decimal number to this instance.
        
            value: The value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: UInt16) -> StringBuilder
        
            Appends the string representation of a specified 16-bit unsigned integer to this instance.
        
            value: The value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: float) -> StringBuilder
        
            Appends the string representation of a specified double-precision floating-point number to this 
             instance.
        
        
            value: The value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: Int64) -> StringBuilder
        
            Appends the string representation of a specified 64-bit signed integer to this instance.
        
            value: The value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: Single) -> StringBuilder
        
            Appends the string representation of a specified single-precision floating-point number to this 
             instance.
        
        
            value: The value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: Array[Char]) -> StringBuilder
        
            Appends the string representation of the Unicode characters in a specified array to this 
             instance.
        
        
            value: The array of characters to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: Char*, valueCount: int) -> StringBuilder
        Append(self: StringBuilder, value: object) -> StringBuilder
        
            Appends the string representation of a specified object to this instance.
        
            value: The object to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: UInt32) -> StringBuilder
        
            Appends the string representation of a specified 32-bit unsigned integer to this instance.
        
            value: The value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: UInt64) -> StringBuilder
        
            Appends the string representation of a specified 64-bit unsigned integer to this instance.
        
            value: The value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: str, startIndex: int, count: int) -> StringBuilder
        
            Appends a copy of a specified substring to this instance.
        
            value: The string that contains the substring to append.
            startIndex: The starting position of the substring within value.
            count: The number of characters in value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: bool) -> StringBuilder
        
            Appends the string representation of a specified Boolean value to this instance.
        
            value: The Boolean value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: str) -> StringBuilder
        
            Appends a copy of the specified string to this instance.
        
            value: The string to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: Char, repeatCount: int) -> StringBuilder
        
            Appends a specified number of copies of the string representation of a Unicode character to this 
             instance.
        
        
            value: The character to append.
            repeatCount: The number of times to append value.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: Array[Char], startIndex: int, charCount: int) -> StringBuilder
        
            Appends the string representation of a specified subarray of Unicode characters to this instance.
        
            value: A character array.
            startIndex: The starting position in value.
            charCount: The number of characters to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: Int16) -> StringBuilder
        
            Appends the string representation of a specified 16-bit signed integer to this instance.
        
            value: The value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: int) -> StringBuilder
        
            Appends the string representation of a specified 32-bit signed integer to this instance.
        
            value: The value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: Char) -> StringBuilder
        
            Appends the string representation of a specified Unicode character to this instance.
        
            value: The Unicode character to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: SByte) -> StringBuilder
        
            Appends the string representation of a specified 8-bit signed integer to this instance.
        
            value: The value to append.
            Returns: A reference to this instance after the append operation has completed.
        Append(self: StringBuilder, value: Byte) -> StringBuilder
        
            Appends the string representation of a specified 8-bit unsigned integer to this instance.
        
            value: The value to append.
            Returns: A reference to this instance after the append operation has completed.
        """
        pass

    def AppendFormat(self, *__args):
        """
        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, arg0: object, arg1: object) -> StringBuilder
        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, arg0: object) -> StringBuilder
        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, *args: Array[object]) -> StringBuilder
        
            Appends the string returned by processing a composite format string, which contains zero or more 
             format items, to this instance. Each format item is replaced by the string representation of a 
             corresponding argument in a parameter array using a specified format provider.
        
        
            provider: An object that supplies culture-specific formatting information.
            format: A composite format string (see Remarks).
            args: An array of objects to format.
            Returns: A reference to this instance after the append operation has completed. After the append 
             operation, this instance contains any data that existed before the operation, suffixed by a copy 
             of format where any format specification is replaced by the string representation of the 
             corresponding object argument.
        
        AppendFormat(self: StringBuilder, provider: IFormatProvider, format: str, arg0: object, arg1: object, arg2: object) -> StringBuilder
        AppendFormat(self: StringBuilder, format: str, arg0: object, arg1: object) -> StringBuilder
        
            Appends the string returned by processing a composite format string, which contains zero or more 
             format items, to this instance. Each format item is replaced by the string representation of 
             either of two arguments.
        
        
            format: A composite format string (see Remarks).
            arg0: The first object to format.
            arg1: The second object to format.
            Returns: A reference to this instance with format appended. Each format item in format is replaced by the 
             string representation of the corresponding object argument.
        
        AppendFormat(self: StringBuilder, format: str, arg0: object) -> StringBuilder
        
            Appends the string returned by processing a composite format string, which contains zero or more 
             format items, to this instance. Each format item is replaced by the string representation of a 
             single argument.
        
        
            format: A composite format string (see Remarks).
            arg0: An object to format.
            Returns: A reference to this instance with format appended. Each format item in format is replaced by the 
             string representation of arg0.
        
        AppendFormat(self: StringBuilder, format: str, *args: Array[object]) -> StringBuilder
        
            Appends the string returned by processing a composite format string, which contains zero or more 
             format items, to this instance. Each format item is replaced by the string representation of a 
             corresponding argument in a parameter array.
        
        
            format: A composite format string (see Remarks).
            args: An array of objects to format.
            Returns: A reference to this instance with format appended. Each format item in format is replaced by the 
             string representation of the corresponding object argument.
        
        AppendFormat(self: StringBuilder, format: str, arg0: object, arg1: object, arg2: object) -> StringBuilder
        
            Appends the string returned by processing a composite format string, which contains zero or more 
             format items, to this instance. Each format item is replaced by the string representation of 
             either of three arguments.
        
        
            format: A composite format string (see Remarks).
            arg0: The first object to format.
            arg1: The second object to format.
            arg2: The third object to format.
            Returns: A reference to this instance with format appended. Each format item in format is replaced by the 
             string representation of the corresponding object argument.
        """
        pass

    def AppendLine(self, value=None):
        """
        AppendLine(self: StringBuilder, value: str) -> StringBuilder
        
            Appends a copy of the specified string followed by the default line terminator to the end of the 
             current System.Text.StringBuilder object.
        
        
            value: The string to append.
            Returns: A reference to this instance after the append operation has completed.
        AppendLine(self: StringBuilder) -> StringBuilder
        
            Appends the default line terminator to the end of the current System.Text.StringBuilder object.
            Returns: A reference to this instance after the append operation has completed.
        """
        pass

    def Clear(self):
        """
        Clear(self: StringBuilder) -> StringBuilder
        
            Removes all characters from the current System.Text.StringBuilder instance.
            Returns: An object whose System.Text.StringBuilder.Length is 0 (zero).
        """
        pass

    def CopyTo(self, sourceIndex, destination, destinationIndex, count):
        """
        CopyTo(self: StringBuilder, sourceIndex: int, destination: Array[Char], destinationIndex: int, count: int)
            Copies the characters from a specified segment of this instance to a specified segment of a 
             destination System.Char array.
        
        
            sourceIndex: The starting position in this instance where characters will be copied from. The index is 
             zero-based.
        
            destination: The array where characters will be copied.
            destinationIndex: The starting position in destination where characters will be copied. The index is zero-based.
            count: The number of characters to be copied.
        """
        pass

    def EnsureCapacity(self, capacity):
        """
        EnsureCapacity(self: StringBuilder, capacity: int) -> int
        
            Ensures that the capacity of this instance of System.Text.StringBuilder is at least the 
             specified value.
        
        
            capacity: The minimum capacity to ensure.
            Returns: The new capacity of this instance.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: StringBuilder, sb: StringBuilder) -> bool
        
            Returns a value indicating whether this instance is equal to a specified object.
        
            sb: An object to compare with this instance, or null.
            Returns: true if this instance and sb have equal string, System.Text.StringBuilder.Capacity, and 
             System.Text.StringBuilder.MaxCapacity values; otherwise, false.
        """
        pass

    def Insert(self, index, value, *__args):
        """
        Insert(self: StringBuilder, index: int, value: Single) -> StringBuilder
        
            Inserts the string representation of a single-precision floating point number into this instance 
             at the specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: float) -> StringBuilder
        
            Inserts the string representation of a double-precision floating-point number into this instance 
             at the specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: int) -> StringBuilder
        
            Inserts the string representation of a specified 32-bit signed integer into this instance at the 
             specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: Int64) -> StringBuilder
        
            Inserts the string representation of a 64-bit signed integer into this instance at the specified 
             character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: Decimal) -> StringBuilder
        
            Inserts the string representation of a decimal number into this instance at the specified 
             character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: UInt64) -> StringBuilder
        
            Inserts the string representation of a 64-bit unsigned integer into this instance at the 
             specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: object) -> StringBuilder
        
            Inserts the string representation of an object into this instance at the specified character 
             position.
        
        
            index: The position in this instance where insertion begins.
            value: The object to insert, or null.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: UInt16) -> StringBuilder
        
            Inserts the string representation of a 16-bit unsigned integer into this instance at the 
             specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: UInt32) -> StringBuilder
        
            Inserts the string representation of a 32-bit unsigned integer into this instance at the 
             specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: bool) -> StringBuilder
        
            Inserts the string representation of a Boolean value into this instance at the specified 
             character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: SByte) -> StringBuilder
        
            Inserts the string representation of a specified 8-bit signed integer into this instance at the 
             specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: str, count: int) -> StringBuilder
        
            Inserts one or more copies of a specified string into this instance at the specified character 
             position.
        
        
            index: The position in this instance where insertion begins.
            value: The string to insert.
            count: The number of times to insert value.
            Returns: A reference to this instance after insertion has completed.
        Insert(self: StringBuilder, index: int, value: str) -> StringBuilder
        
            Inserts a string into this instance at the specified character position.
        
            index: The position in this instance where insertion begins.
            value: The string to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: Byte) -> StringBuilder
        
            Inserts the string representation of a specified 8-bit unsigned integer into this instance at 
             the specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: Array[Char]) -> StringBuilder
        
            Inserts the string representation of a specified array of Unicode characters into this instance 
             at the specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: The character array to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: Array[Char], startIndex: int, charCount: int) -> StringBuilder
        
            Inserts the string representation of a specified subarray of Unicode characters into this 
             instance at the specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: A character array.
            startIndex: The starting index within value.
            charCount: The number of characters to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: Int16) -> StringBuilder
        
            Inserts the string representation of a specified 16-bit signed integer into this instance at the 
             specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        Insert(self: StringBuilder, index: int, value: Char) -> StringBuilder
        
            Inserts the string representation of a specified Unicode character into this instance at the 
             specified character position.
        
        
            index: The position in this instance where insertion begins.
            value: The value to insert.
            Returns: A reference to this instance after the insert operation has completed.
        """
        pass

    def Remove(self, startIndex, length):
        """
        Remove(self: StringBuilder, startIndex: int, length: int) -> StringBuilder
        
            Removes the specified range of characters from this instance.
        
            startIndex: The zero-based position in this instance where removal begins.
            length: The number of characters to remove.
            Returns: A reference to this instance after the excise operation has completed.
        """
        pass

    def Replace(self, *__args):
        """
        Replace(self: StringBuilder, oldChar: Char, newChar: Char) -> StringBuilder
        
            Replaces all occurrences of a specified character in this instance with another specified 
             character.
        
        
            oldChar: The character to replace.
            newChar: The character that replaces oldChar.
            Returns: A reference to this instance with oldChar replaced by newChar.
        Replace(self: StringBuilder, oldChar: Char, newChar: Char, startIndex: int, count: int) -> StringBuilder
        
            Replaces, within a substring of this instance, all occurrences of a specified character with 
             another specified character.
        
        
            oldChar: The character to replace.
            newChar: The character that replaces oldChar.
            startIndex: The position in this instance where the substring begins.
            count: The length of the substring.
            Returns: A reference to this instance with oldChar replaced by newChar in the range from startIndex to 
             startIndex + count -1.
        
        Replace(self: StringBuilder, oldValue: str, newValue: str) -> StringBuilder
        
            Replaces all occurrences of a specified string in this instance with another specified string.
        
            oldValue: The string to replace.
            newValue: The string that replaces oldValue, or null.
            Returns: A reference to this instance with all instances of oldValue replaced by newValue.
        Replace(self: StringBuilder, oldValue: str, newValue: str, startIndex: int, count: int) -> StringBuilder
        
            Replaces, within a substring of this instance, all occurrences of a specified string with 
             another specified string.
        
        
            oldValue: The string to replace.
            newValue: The string that replaces oldValue, or null.
            startIndex: The position in this instance where the substring begins.
            count: The length of the substring.
            Returns: A reference to this instance with all instances of oldValue replaced by newValue in the range 
             from startIndex to startIndex + count - 1.
        """
        pass

    def ToString(self, startIndex=None, length=None):
        """
        ToString(self: StringBuilder, startIndex: int, length: int) -> str
        
            Converts the value of a substring of this instance to a System.String.
        
            startIndex: The starting position of the substring in this instance.
            length: The length of the substring.
            Returns: A string whose value is the same as the specified substring of this instance.
        ToString(self: StringBuilder) -> str
        
            Converts the value of this instance to a System.String.
            Returns: A string whose value is the same as this instance.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, value: str)
        __new__(cls: type, value: str, capacity: int)
        __new__(cls: type, value: str, startIndex: int, length: int, capacity: int)
        __new__(cls: type, capacity: int, maxCapacity: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum number of characters that can be contained in the memory allocated by the current instance.

Get: Capacity(self: StringBuilder) -> int

Set: Capacity(self: StringBuilder) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the length of the current System.Text.StringBuilder object.

Get: Length(self: StringBuilder) -> int

Set: Length(self: StringBuilder) = value
"""

    MaxCapacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum capacity of this instance.

Get: MaxCapacity(self: StringBuilder) -> int

"""



class UnicodeEncoding(Encoding, ICloneable):
    """
    Represents a UTF-16 encoding of Unicode characters.
    
    UnicodeEncoding(bigEndian: bool, byteOrderMark: bool, throwOnInvalidBytes: bool)
    UnicodeEncoding()
    UnicodeEncoding(bigEndian: bool, byteOrderMark: bool)
    """
    def Equals(self, value):
        """
        Equals(self: UnicodeEncoding, value: object) -> bool
        
            Determines whether the specified System.Object is equal to the current 
             System.Text.UnicodeEncoding object.
        
        
            value: The System.Object to compare with the current object.
            Returns: true if value is an instance of System.Text.UnicodeEncoding and is equal to the current object; 
             otherwise, false.
        """
        pass

    def GetByteCount(self, *__args):
        """
        GetByteCount(self: UnicodeEncoding, chars: Char*, count: int) -> int
        
            Calculates the number of bytes produced by encoding a set of characters starting at the 
             specified character pointer.
        
        
            chars: A pointer to the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: UnicodeEncoding, s: str) -> int
        
            Calculates the number of bytes produced by encoding the characters in the specified 
             System.String.
        
        
            s: The System.String containing the set of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: UnicodeEncoding, chars: Array[Char], index: int, count: int) -> int
        
            Calculates the number of bytes produced by encoding a set of characters from the specified 
             character array.
        
        
            chars: The character array containing the set of characters to encode.
            index: The index of the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        """
        pass

    def GetBytes(self, *__args):
        """
        GetBytes(self: UnicodeEncoding, chars: Char*, charCount: int, bytes: Byte*, byteCount: int) -> int
        
            Encodes a set of characters starting at the specified character pointer into a sequence of bytes 
             that are stored starting at the specified byte pointer.
        
        
            chars: A pointer to the first character to encode.
            charCount: The number of characters to encode.
            bytes: A pointer to the location at which to start writing the resulting sequence of bytes.
            byteCount: The maximum number of bytes to write.
            Returns: The actual number of bytes written at the location indicated by the bytes parameter.
        GetBytes(self: UnicodeEncoding, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            Encodes a set of characters from the specified character array into the specified byte array.
        
            chars: The character array containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        GetBytes(self: UnicodeEncoding, s: str, charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            Encodes a set of characters from the specified System.String into the specified byte array.
        
            s: The System.String containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        """
        pass

    def GetCharCount(self, bytes, *__args):
        """
        GetCharCount(self: UnicodeEncoding, bytes: Byte*, count: int) -> int
        
            Calculates the number of characters produced by decoding a sequence of bytes starting at the 
             specified byte pointer.
        
        
            bytes: A pointer to the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        GetCharCount(self: UnicodeEncoding, bytes: Array[Byte], index: int, count: int) -> int
        
            Calculates the number of characters produced by decoding a sequence of bytes from the specified 
             byte array.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        """
        pass

    def GetChars(self, bytes, *__args):
        """
        GetChars(self: UnicodeEncoding, bytes: Byte*, byteCount: int, chars: Char*, charCount: int) -> int
        
            Decodes a sequence of bytes starting at the specified byte pointer into a set of characters that 
             are stored starting at the specified character pointer.
        
        
            bytes: A pointer to the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: A pointer to the location at which to start writing the resulting set of characters.
            charCount: The maximum number of characters to write.
            Returns: The actual number of characters written at the location indicated by the chars parameter.
        GetChars(self: UnicodeEncoding, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int) -> int
        
            Decodes a sequence of bytes from the specified byte array into the specified character array.
        
            bytes: The byte array containing the sequence of bytes to decode.
            byteIndex: The index of the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: The character array to contain the resulting set of characters.
            charIndex: The index at which to start writing the resulting set of characters.
            Returns: The actual number of characters written into chars.
        """
        pass

    def GetDecoder(self):
        """
        GetDecoder(self: UnicodeEncoding) -> Decoder
        
            Obtains a decoder that converts a UTF-16 encoded sequence of bytes into a sequence of Unicode 
             characters.
        
            Returns: A System.Text.Decoder that converts a UTF-16 encoded sequence of bytes into a sequence of 
             Unicode characters.
        """
        pass

    def GetEncoder(self):
        """
        GetEncoder(self: UnicodeEncoding) -> Encoder
        
            Obtains an encoder that converts a sequence of Unicode characters into a UTF-16 encoded sequence 
             of bytes.
        
            Returns: A System.Text.Encoder object that converts a sequence of Unicode characters into a UTF-16 
             encoded sequence of bytes.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UnicodeEncoding) -> int
        
            Returns the hash code for the current instance.
            Returns: The hash code for the current System.Text.UnicodeEncoding object.
        """
        pass

    def GetMaxByteCount(self, charCount):
        """
        GetMaxByteCount(self: UnicodeEncoding, charCount: int) -> int
        
            Calculates the maximum number of bytes produced by encoding the specified number of characters.
        
            charCount: The number of characters to encode.
            Returns: The maximum number of bytes produced by encoding the specified number of characters.
        """
        pass

    def GetMaxCharCount(self, byteCount):
        """
        GetMaxCharCount(self: UnicodeEncoding, byteCount: int) -> int
        
            Calculates the maximum number of characters produced by decoding the specified number of bytes.
        
            byteCount: The number of bytes to decode.
            Returns: The maximum number of characters produced by decoding the specified number of bytes.
        """
        pass

    def GetPreamble(self):
        """
        GetPreamble(self: UnicodeEncoding) -> Array[Byte]
        
            Returns a Unicode byte order mark encoded in UTF-16 format, if the constructor for this instance 
             requests a byte order mark.
        
            Returns: A byte array containing the Unicode byte order mark, if the constructor for this instance 
             requests a byte order mark. Otherwise, this method returns a byte array of length zero.
        """
        pass

    def GetString(self, bytes, *__args):
        """
        GetString(self: UnicodeEncoding, bytes: Array[Byte], index: int, count: int) -> str
        
            Decodes a range of bytes from a byte array into a string.
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: A System.String object containing the results of decoding the specified sequence of bytes.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, bigEndian=None, byteOrderMark=None, throwOnInvalidBytes=None):
        """
        __new__(cls: type)
        __new__(cls: type, bigEndian: bool, byteOrderMark: bool)
        __new__(cls: type, bigEndian: bool, byteOrderMark: bool, throwOnInvalidBytes: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    CharSize = 2


class UTF32Encoding(Encoding, ICloneable):
    """
    Represents a UTF-32 encoding of Unicode characters.
    
    UTF32Encoding()
    UTF32Encoding(bigEndian: bool, byteOrderMark: bool)
    UTF32Encoding(bigEndian: bool, byteOrderMark: bool, throwOnInvalidCharacters: bool)
    """
    def Equals(self, value):
        """
        Equals(self: UTF32Encoding, value: object) -> bool
        
            Determines whether the specified System.Object is equal to the current System.Text.UTF32Encoding 
             object.
        
        
            value: The System.Object to compare with the current object.
            Returns: true if value is an instance of System.Text.UTF32Encoding and is equal to the current object; 
             otherwise, false.
        """
        pass

    def GetByteCount(self, *__args):
        """
        GetByteCount(self: UTF32Encoding, chars: Char*, count: int) -> int
        
            Calculates the number of bytes produced by encoding a set of characters starting at the 
             specified character pointer.
        
        
            chars: A pointer to the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: UTF32Encoding, s: str) -> int
        
            Calculates the number of bytes produced by encoding the characters in the specified 
             System.String.
        
        
            s: The System.String containing the set of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: UTF32Encoding, chars: Array[Char], index: int, count: int) -> int
        
            Calculates the number of bytes produced by encoding a set of characters from the specified 
             character array.
        
        
            chars: The character array containing the set of characters to encode.
            index: The index of the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        """
        pass

    def GetBytes(self, *__args):
        """
        GetBytes(self: UTF32Encoding, chars: Char*, charCount: int, bytes: Byte*, byteCount: int) -> int
        
            Encodes a set of characters starting at the specified character pointer into a sequence of bytes 
             that are stored starting at the specified byte pointer.
        
        
            chars: A pointer to the first character to encode.
            charCount: The number of characters to encode.
            bytes: A pointer to the location at which to start writing the resulting sequence of bytes.
            byteCount: The maximum number of bytes to write.
            Returns: The actual number of bytes written at the location indicated by the bytes parameter.
        GetBytes(self: UTF32Encoding, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            Encodes a set of characters from the specified character array into the specified byte array.
        
            chars: The character array containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        GetBytes(self: UTF32Encoding, s: str, charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            Encodes a set of characters from the specified System.String into the specified byte array.
        
            s: The System.String containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        """
        pass

    def GetCharCount(self, bytes, *__args):
        """
        GetCharCount(self: UTF32Encoding, bytes: Byte*, count: int) -> int
        
            Calculates the number of characters produced by decoding a sequence of bytes starting at the 
             specified byte pointer.
        
        
            bytes: A pointer to the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        GetCharCount(self: UTF32Encoding, bytes: Array[Byte], index: int, count: int) -> int
        
            Calculates the number of characters produced by decoding a sequence of bytes from the specified 
             byte array.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        """
        pass

    def GetChars(self, bytes, *__args):
        """
        GetChars(self: UTF32Encoding, bytes: Byte*, byteCount: int, chars: Char*, charCount: int) -> int
        
            Decodes a sequence of bytes starting at the specified byte pointer into a set of characters that 
             are stored starting at the specified character pointer.
        
        
            bytes: A pointer to the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: A pointer to the location at which to start writing the resulting set of characters.
            charCount: The maximum number of characters to write.
            Returns: The actual number of characters written at the location indicated by chars.
        GetChars(self: UTF32Encoding, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int) -> int
        
            Decodes a sequence of bytes from the specified byte array into the specified character array.
        
            bytes: The byte array containing the sequence of bytes to decode.
            byteIndex: The index of the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: The character array to contain the resulting set of characters.
            charIndex: The index at which to start writing the resulting set of characters.
            Returns: The actual number of characters written into chars.
        """
        pass

    def GetDecoder(self):
        """
        GetDecoder(self: UTF32Encoding) -> Decoder
        
            Obtains a decoder that converts a UTF-32 encoded sequence of bytes into a sequence of Unicode 
             characters.
        
            Returns: A System.Text.Decoder that converts a UTF-32 encoded sequence of bytes into a sequence of 
             Unicode characters.
        """
        pass

    def GetEncoder(self):
        """
        GetEncoder(self: UTF32Encoding) -> Encoder
        
            Obtains an encoder that converts a sequence of Unicode characters into a UTF-32 encoded sequence 
             of bytes.
        
            Returns: A System.Text.Encoder that converts a sequence of Unicode characters into a UTF-32 encoded 
             sequence of bytes.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UTF32Encoding) -> int
        
            Returns the hash code for the current instance.
            Returns: The hash code for the current System.Text.UTF32Encoding object.
        """
        pass

    def GetMaxByteCount(self, charCount):
        """
        GetMaxByteCount(self: UTF32Encoding, charCount: int) -> int
        
            Calculates the maximum number of bytes produced by encoding the specified number of characters.
        
            charCount: The number of characters to encode.
            Returns: The maximum number of bytes produced by encoding the specified number of characters.
        """
        pass

    def GetMaxCharCount(self, byteCount):
        """
        GetMaxCharCount(self: UTF32Encoding, byteCount: int) -> int
        
            Calculates the maximum number of characters produced by decoding the specified number of bytes.
        
            byteCount: The number of bytes to decode.
            Returns: The maximum number of characters produced by decoding the specified number of bytes.
        """
        pass

    def GetPreamble(self):
        """
        GetPreamble(self: UTF32Encoding) -> Array[Byte]
        
            Returns a Unicode byte order mark encoded in UTF-32 format, if the constructor for this instance 
             requests a byte order mark.
        
            Returns: A byte array containing the Unicode byte order mark, if the constructor for this instance 
             requests a byte order mark. Otherwise, this method returns a byte array of length zero.
        """
        pass

    def GetString(self, bytes, *__args):
        """
        GetString(self: UTF32Encoding, bytes: Array[Byte], index: int, count: int) -> str
        
            Decodes a range of bytes from a byte array into a string.
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: A System.String containing the results of decoding the specified sequence of bytes.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, bigEndian=None, byteOrderMark=None, throwOnInvalidCharacters=None):
        """
        __new__(cls: type)
        __new__(cls: type, bigEndian: bool, byteOrderMark: bool)
        __new__(cls: type, bigEndian: bool, byteOrderMark: bool, throwOnInvalidCharacters: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class UTF7Encoding(Encoding, ICloneable):
    """
    Represents a UTF-7 encoding of Unicode characters.
    
    UTF7Encoding()
    UTF7Encoding(allowOptionals: bool)
    """
    def Equals(self, value):
        """
        Equals(self: UTF7Encoding, value: object) -> bool
        
            Gets a value indicating whether the specified object is equal to the current 
             System.Text.UTF7Encoding object.
        
        
            value: An object to compare to the current System.Text.UTF7Encoding object.
            Returns: true if value is a System.Text.UTF7Encoding object and is equal to the current 
             System.Text.UTF7Encoding object; otherwise, false.
        """
        pass

    def GetByteCount(self, *__args):
        """
        GetByteCount(self: UTF7Encoding, chars: Char*, count: int) -> int
        
            Calculates the number of bytes produced by encoding a set of characters starting at the 
             specified character pointer.
        
        
            chars: A pointer to the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: UTF7Encoding, s: str) -> int
        
            Calculates the number of bytes produced by encoding the characters in the specified 
             System.String object.
        
        
            s: The System.String object containing the set of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: UTF7Encoding, chars: Array[Char], index: int, count: int) -> int
        
            Calculates the number of bytes produced by encoding a set of characters from the specified 
             character array.
        
        
            chars: The character array containing the set of characters to encode.
            index: The index of the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        """
        pass

    def GetBytes(self, *__args):
        """
        GetBytes(self: UTF7Encoding, chars: Char*, charCount: int, bytes: Byte*, byteCount: int) -> int
        
            Encodes a set of characters starting at the specified character pointer into a sequence of bytes 
             that are stored starting at the specified byte pointer.
        
        
            chars: A pointer to the first character to encode.
            charCount: The number of characters to encode.
            bytes: A pointer to the location at which to start writing the resulting sequence of bytes.
            byteCount: The maximum number of bytes to write.
            Returns: The actual number of bytes written at the location indicated by bytes.
        GetBytes(self: UTF7Encoding, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            Encodes a set of characters from the specified character array into the specified byte array.
        
            chars: The character array containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        GetBytes(self: UTF7Encoding, s: str, charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            Encodes a set of characters from the specified System.String into the specified byte array.
        
            s: The System.String containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        """
        pass

    def GetCharCount(self, bytes, *__args):
        """
        GetCharCount(self: UTF7Encoding, bytes: Byte*, count: int) -> int
        
            Calculates the number of characters produced by decoding a sequence of bytes starting at the 
             specified byte pointer.
        
        
            bytes: A pointer to the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        GetCharCount(self: UTF7Encoding, bytes: Array[Byte], index: int, count: int) -> int
        
            Calculates the number of characters produced by decoding a sequence of bytes from the specified 
             byte array.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        """
        pass

    def GetChars(self, bytes, *__args):
        """
        GetChars(self: UTF7Encoding, bytes: Byte*, byteCount: int, chars: Char*, charCount: int) -> int
        
            Decodes a sequence of bytes starting at the specified byte pointer into a set of characters that 
             are stored starting at the specified character pointer.
        
        
            bytes: A pointer to the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: A pointer to the location at which to start writing the resulting set of characters.
            charCount: The maximum number of characters to write.
            Returns: The actual number of characters written at the location indicated by chars.
        GetChars(self: UTF7Encoding, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int) -> int
        
            Decodes a sequence of bytes from the specified byte array into the specified character array.
        
            bytes: The byte array containing the sequence of bytes to decode.
            byteIndex: The index of the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: The character array to contain the resulting set of characters.
            charIndex: The index at which to start writing the resulting set of characters.
            Returns: The actual number of characters written into chars.
        """
        pass

    def GetDecoder(self):
        """
        GetDecoder(self: UTF7Encoding) -> Decoder
        
            Obtains a decoder that converts a UTF-7 encoded sequence of bytes into a sequence of Unicode 
             characters.
        
            Returns: A System.Text.Decoder that converts a UTF-7 encoded sequence of bytes into a sequence of Unicode 
             characters.
        """
        pass

    def GetEncoder(self):
        """
        GetEncoder(self: UTF7Encoding) -> Encoder
        
            Obtains an encoder that converts a sequence of Unicode characters into a UTF-7 encoded sequence 
             of bytes.
        
            Returns: A System.Text.Encoder that converts a sequence of Unicode characters into a UTF-7 encoded 
             sequence of bytes.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UTF7Encoding) -> int
        
            Returns the hash code for the current System.Text.UTF7Encoding object.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def GetMaxByteCount(self, charCount):
        """
        GetMaxByteCount(self: UTF7Encoding, charCount: int) -> int
        
            Calculates the maximum number of bytes produced by encoding the specified number of characters.
        
            charCount: The number of characters to encode.
            Returns: The maximum number of bytes produced by encoding the specified number of characters.
        """
        pass

    def GetMaxCharCount(self, byteCount):
        """
        GetMaxCharCount(self: UTF7Encoding, byteCount: int) -> int
        
            Calculates the maximum number of characters produced by decoding the specified number of bytes.
        
            byteCount: The number of bytes to decode.
            Returns: The maximum number of characters produced by decoding the specified number of bytes.
        """
        pass

    def GetString(self, bytes, *__args):
        """
        GetString(self: UTF7Encoding, bytes: Array[Byte], index: int, count: int) -> str
        
            Decodes a range of bytes from a byte array into a string.
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: A System.String containing the results of decoding the specified sequence of bytes.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, allowOptionals=None):
        """
        __new__(cls: type)
        __new__(cls: type, allowOptionals: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class UTF8Encoding(Encoding, ICloneable):
    """
    Represents a UTF-8 encoding of Unicode characters.
    
    UTF8Encoding()
    UTF8Encoding(encoderShouldEmitUTF8Identifier: bool)
    UTF8Encoding(encoderShouldEmitUTF8Identifier: bool, throwOnInvalidBytes: bool)
    """
    def Equals(self, value):
        """
        Equals(self: UTF8Encoding, value: object) -> bool
        
            Determines whether the specified System.Object is equal to the current System.Text.UTF8Encoding 
             object.
        
        
            value: The System.Object to compare with the current instance.
            Returns: true if value is an instance of System.Text.UTF8Encoding and is equal to the current object; 
             otherwise, false.
        """
        pass

    def GetByteCount(self, chars, *__args):
        """
        GetByteCount(self: UTF8Encoding, chars: Char*, count: int) -> int
        
            Calculates the number of bytes produced by encoding a set of characters starting at the 
             specified character pointer.
        
        
            chars: A pointer to the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: UTF8Encoding, chars: str) -> int
        
            Calculates the number of bytes produced by encoding the characters in the specified 
             System.String.
        
        
            chars: The System.String containing the set of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        GetByteCount(self: UTF8Encoding, chars: Array[Char], index: int, count: int) -> int
        
            Calculates the number of bytes produced by encoding a set of characters from the specified 
             character array.
        
        
            chars: The character array containing the set of characters to encode.
            index: The index of the first character to encode.
            count: The number of characters to encode.
            Returns: The number of bytes produced by encoding the specified characters.
        """
        pass

    def GetBytes(self, *__args):
        """
        GetBytes(self: UTF8Encoding, chars: Char*, charCount: int, bytes: Byte*, byteCount: int) -> int
        
            Encodes a set of characters starting at the specified character pointer into a sequence of bytes 
             that are stored starting at the specified byte pointer.
        
        
            chars: A pointer to the first character to encode.
            charCount: The number of characters to encode.
            bytes: A pointer to the location at which to start writing the resulting sequence of bytes.
            byteCount: The maximum number of bytes to write.
            Returns: The actual number of bytes written at the location indicated by bytes.
        GetBytes(self: UTF8Encoding, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            Encodes a set of characters from the specified character array into the specified byte array.
        
            chars: The character array containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        GetBytes(self: UTF8Encoding, s: str, charIndex: int, charCount: int, bytes: Array[Byte], byteIndex: int) -> int
        
            Encodes a set of characters from the specified System.String into the specified byte array.
        
            s: The System.String containing the set of characters to encode.
            charIndex: The index of the first character to encode.
            charCount: The number of characters to encode.
            bytes: The byte array to contain the resulting sequence of bytes.
            byteIndex: The index at which to start writing the resulting sequence of bytes.
            Returns: The actual number of bytes written into bytes.
        """
        pass

    def GetCharCount(self, bytes, *__args):
        """
        GetCharCount(self: UTF8Encoding, bytes: Byte*, count: int) -> int
        
            Calculates the number of characters produced by decoding a sequence of bytes starting at the 
             specified byte pointer.
        
        
            bytes: A pointer to the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        GetCharCount(self: UTF8Encoding, bytes: Array[Byte], index: int, count: int) -> int
        
            Calculates the number of characters produced by decoding a sequence of bytes from the specified 
             byte array.
        
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: The number of characters produced by decoding the specified sequence of bytes.
        """
        pass

    def GetChars(self, bytes, *__args):
        """
        GetChars(self: UTF8Encoding, bytes: Byte*, byteCount: int, chars: Char*, charCount: int) -> int
        
            Decodes a sequence of bytes starting at the specified byte pointer into a set of characters that 
             are stored starting at the specified character pointer.
        
        
            bytes: A pointer to the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: A pointer to the location at which to start writing the resulting set of characters.
            charCount: The maximum number of characters to write.
            Returns: The actual number of characters written at the location indicated by chars.
        GetChars(self: UTF8Encoding, bytes: Array[Byte], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int) -> int
        
            Decodes a sequence of bytes from the specified byte array into the specified character array.
        
            bytes: The byte array containing the sequence of bytes to decode.
            byteIndex: The index of the first byte to decode.
            byteCount: The number of bytes to decode.
            chars: The character array to contain the resulting set of characters.
            charIndex: The index at which to start writing the resulting set of characters.
            Returns: The actual number of characters written into chars.
        """
        pass

    def GetDecoder(self):
        """
        GetDecoder(self: UTF8Encoding) -> Decoder
        
            Obtains a decoder that converts a UTF-8 encoded sequence of bytes into a sequence of Unicode 
             characters.
        
            Returns: A System.Text.Decoder that converts a UTF-8 encoded sequence of bytes into a sequence of Unicode 
             characters.
        """
        pass

    def GetEncoder(self):
        """
        GetEncoder(self: UTF8Encoding) -> Encoder
        
            Obtains an encoder that converts a sequence of Unicode characters into a UTF-8 encoded sequence 
             of bytes.
        
            Returns: A System.Text.Encoder that converts a sequence of Unicode characters into a UTF-8 encoded 
             sequence of bytes.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UTF8Encoding) -> int
        
            Returns the hash code for the current instance.
            Returns: The hash code for the current instance.
        """
        pass

    def GetMaxByteCount(self, charCount):
        """
        GetMaxByteCount(self: UTF8Encoding, charCount: int) -> int
        
            Calculates the maximum number of bytes produced by encoding the specified number of characters.
        
            charCount: The number of characters to encode.
            Returns: The maximum number of bytes produced by encoding the specified number of characters.
        """
        pass

    def GetMaxCharCount(self, byteCount):
        """
        GetMaxCharCount(self: UTF8Encoding, byteCount: int) -> int
        
            Calculates the maximum number of characters produced by decoding the specified number of bytes.
        
            byteCount: The number of bytes to decode.
            Returns: The maximum number of characters produced by decoding the specified number of bytes.
        """
        pass

    def GetPreamble(self):
        """
        GetPreamble(self: UTF8Encoding) -> Array[Byte]
        
            Returns a Unicode byte order mark encoded in UTF-8 format, if the constructor for this instance 
             requests a byte order mark.
        
            Returns: A byte array containing the Unicode byte order mark, if the constructor for this instance 
             requests a byte order mark. Otherwise, this method returns a byte array of length zero.
        """
        pass

    def GetString(self, bytes, *__args):
        """
        GetString(self: UTF8Encoding, bytes: Array[Byte], index: int, count: int) -> str
        
            Decodes a range of bytes from a byte array into a string.
        
            bytes: The byte array containing the sequence of bytes to decode.
            index: The index of the first byte to decode.
            count: The number of bytes to decode.
            Returns: A System.String containing the results of decoding the specified sequence of bytes.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, encoderShouldEmitUTF8Identifier=None, throwOnInvalidBytes=None):
        """
        __new__(cls: type)
        __new__(cls: type, encoderShouldEmitUTF8Identifier: bool)
        __new__(cls: type, encoderShouldEmitUTF8Identifier: bool, throwOnInvalidBytes: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


# variables with complex values

