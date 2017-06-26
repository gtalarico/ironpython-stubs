class StringWriter(TextWriter, IDisposable):
    """
    Implements a System.IO.TextWriter for writing information to a string. The information is stored in an underlying System.Text.StringBuilder.
    
    StringWriter()
    StringWriter(formatProvider: IFormatProvider)
    StringWriter(sb: StringBuilder)
    StringWriter(sb: StringBuilder, formatProvider: IFormatProvider)
    """
    def Close(self):
        """
        Close(self: StringWriter)
            Closes the current System.IO.StringWriter and the underlying stream.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: StringWriter, disposing: bool)
            Releases the unmanaged resources used by the System.IO.StringWriter and optionally releases the managed resources.
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def FlushAsync(self):
        """ FlushAsync(self: StringWriter) -> Task """
        pass

    def GetStringBuilder(self):
        """
        GetStringBuilder(self: StringWriter) -> StringBuilder
        
            Returns the underlying System.Text.StringBuilder.
            Returns: The underlying StringBuilder.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A value of false is 
             usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ToString(self):
        """
        ToString(self: StringWriter) -> str
        
            Returns a string containing the characters written to the current StringWriter so far.
            Returns: The string containing the characters written to the current StringWriter.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: StringWriter, value: str)
            Writes a string to this instance of the StringWriter.
        
            value: The string to write.
        Write(self: StringWriter, buffer: Array[Char], index: int, count: int)
            Writes the specified region of a character array to this instance of the StringWriter.
        
            buffer: The character array to read data from.
            index: The index at which to begin reading from buffer.
            count: The maximum number of characters to write.
        Write(self: StringWriter, value: Char)
            Writes a character to this instance of the StringWriter.
        
            value: The character to write.
        """
        pass

    def WriteAsync(self, *__args):
        """
        WriteAsync(self: StringWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteAsync(self: StringWriter, value: str) -> Task
        WriteAsync(self: StringWriter, value: Char) -> Task
        """
        pass

    def WriteLineAsync(self, *__args):
        """
        WriteLineAsync(self: StringWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteLineAsync(self: StringWriter, value: str) -> Task
        WriteLineAsync(self: StringWriter, value: Char) -> Task
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, formatProvider: IFormatProvider)
        __new__(cls: type, sb: StringBuilder)
        __new__(cls: type, sb: StringBuilder, formatProvider: IFormatProvider)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Text.Encoding in which the output is written.

Get: Encoding(self: StringWriter) -> Encoding

"""


    CoreNewLine = None

