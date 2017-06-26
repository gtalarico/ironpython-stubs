class Clipboard(object):
    """ Provides static methods that facilitate transferring data to and from the system Clipboard. """
    @staticmethod
    def Clear():
        """
        Clear()
            Clears any data from the system Clipboard.
        """
        pass

    @staticmethod
    def ContainsAudio():
        """
        ContainsAudio() -> bool
        
            Queries the Clipboard for the presence of data in the System.Windows.DataFormats.WaveAudio data format.
            Returns: true if the Clipboard contains data in the System.Windows.DataFormats.WaveAudio data format; otherwise, false.
        """
        pass

    @staticmethod
    def ContainsData(format):
        """
        ContainsData(format: str) -> bool
        
            Queries the Clipboard for the presence of data in a specified data format.
        
            format: The format of the data to look for. See System.Windows.DataFormats for predefined formats.
            Returns: true if data in the specified format is available on the Clipboard; otherwise, false. See Remarks.
        """
        pass

    @staticmethod
    def ContainsFileDropList():
        """
        ContainsFileDropList() -> bool
        
            Queries the Clipboard for the presence of data in the System.Windows.DataFormats.FileDrop data format.
            Returns: true if the Clipboard contains data in the System.Windows.DataFormats.FileDrop data format; otherwise, false.
        """
        pass

    @staticmethod
    def ContainsImage():
        """
        ContainsImage() -> bool
        
            Queries the Clipboard for the presence of data in the System.Windows.DataFormats.Bitmap data format.
            Returns: true if the Clipboard contains data in the System.Windows.DataFormats.Bitmap data format; otherwise, false.
        """
        pass

    @staticmethod
    def ContainsText(format=None):
        """
        ContainsText(format: TextDataFormat) -> bool
        
            Queries the Clipboard for the presence of data in a text data format.
        
            format: A member of the System.Windows.TextDataFormat enumeration that specifies the text data format to query for.
            Returns: true if the Clipboard contains data in the specified text data format; otherwise, false.
        ContainsText() -> bool
        
            Queries the Clipboard for the presence of data in the System.Windows.DataFormats.UnicodeText format.
            Returns: true if the Clipboard contains data in the System.Windows.DataFormats.UnicodeText data format; otherwise, false.
        """
        pass

    @staticmethod
    def Flush():
        """ Flush() """
        pass

    @staticmethod
    def GetAudioStream():
        """
        GetAudioStream() -> Stream
        
            Returns a stream of Clipboard data in the System.Windows.DataFormats.WaveAudio data format.
            Returns: A stream that contains the data in the System.Windows.DataFormats.WaveAudio format, or null if the Clipboard does not contain data in this format.
        """
        pass

    @staticmethod
    def GetData(format):
        """
        GetData(format: str) -> object
        
            Retrieves data in a specified format from the Clipboard.
        
            format: A string that specifies the format of the data to retrieve. For a set of predefined data formats, see the System.Windows.DataFormats class.
            Returns: An object that contains the data in the specified format, or null if the data is unavailable in the specified format.
        """
        pass

    @staticmethod
    def GetDataObject():
        """
        GetDataObject() -> IDataObject
        
            Returns a data object that represents the entire contents of the Clipboard.
            Returns: A data object that enables access to the entire contents of the system Clipboard, or null if there is no data on the Clipboard.
        """
        pass

    @staticmethod
    def GetFileDropList():
        """
        GetFileDropList() -> StringCollection
        
            Returns a string collection that contains a list of dropped files available on the Clipboard.
            Returns: A collection of strings, where each string specifies the name of a file in the list of dropped files on the Clipboard, or null if the data is unavailable in this format.
        """
        pass

    @staticmethod
    def GetImage():
        """
        GetImage() -> BitmapSource
        
            Returns a System.Windows.Media.Imaging.BitmapSource object from the Clipboard that contains data in the System.Windows.DataFormats.Bitmap format.
            Returns: A System.Windows.Media.Imaging.BitmapSource object that contains data in the System.Windows.DataFormats.Bitmap format, or null if the data is unavailable in this format.
        """
        pass

    @staticmethod
    def GetText(format=None):
        """
        GetText(format: TextDataFormat) -> str
        
            Returns a string containing text data on the Clipboard.
        
            format: A member of System.Windows.TextDataFormat that specifies the text data format to retrieve.
            Returns: A string containing text data in the specified data format, or an empty string if no corresponding text data is available.
        GetText() -> str
        
            Returns a string containing the System.Windows.DataFormats.UnicodeText data on the Clipboard.
            Returns: A string containing the System.Windows.DataFormats.UnicodeText data , or an empty string if no System.Windows.DataFormats.UnicodeText data is available on the Clipboard.
        """
        pass

    @staticmethod
    def IsCurrent(data):
        """
        IsCurrent(data: IDataObject) -> bool
        
            Compares a specified data object to the contents of the Clipboard.
        
            data: A data object to compare to the contents of the system Clipboard.
            Returns: true if the specified data object matches what is on the system Clipboard; otherwise, false.
        """
        pass

    @staticmethod
    def SetAudio(*__args):
        """
        SetAudio(audioStream: Stream)
            Stores audio data (System.Windows.DataFormats.WaveAudio data format) on the Clipboard.  The audio data is specified as a stream.
        
            audioStream: A stream that contains audio data to store on the Clipboard.
        SetAudio(audioBytes: Array[Byte])
            Stores audio data (System.Windows.DataFormats.WaveAudio data format) on the Clipboard.  The audio data is specified as a byte array.
        
            audioBytes: A byte array that contains audio data to store on the Clipboard.
        """
        pass

    @staticmethod
    def SetData(format, data):
        """
        SetData(format: str, data: object)
            Stores the specified data on the Clipboard in the specified format.
        
            format: A string that specifies the format to use to store the data. See the System.Windows.DataFormats class for a set of predefined data formats.
            data: An object representing the data to store on the Clipboard.
        """
        pass

    @staticmethod
    def SetDataObject(data, copy=None):
        """
        SetDataObject(data: object, copy: bool)
            Places a specified data object on the system Clipboard and accepts a Boolean parameter that indicates whether the data object should be left on the Clipboard when the application exits.
        
            data: A data object (an object that implements System.Windows.IDataObject) to place on the system Clipboard.
            copy: true to leave the data on the system Clipboard when the application exits; false to clear the data from the system Clipboard when the application exits.
        SetDataObject(data: object)
            Places a specified non-persistent data object on the system Clipboard.
        
            data: A data object (an object that implements System.Windows.IDataObject) to place on the system Clipboard.
        """
        pass

    @staticmethod
    def SetFileDropList(fileDropList):
        """
        SetFileDropList(fileDropList: StringCollection)
            Stores System.Windows.DataFormats.FileDrop data on the Clipboard.  The dropped file list is specified as a string collection.
        
            fileDropList: A string collection that contains the dropped file list to store in the data object.
        """
        pass

    @staticmethod
    def SetImage(image):
        """
        SetImage(image: BitmapSource)
            Stores System.Windows.DataFormats.Bitmap data on the Clipboard.  The image data is specified as a System.Windows.Media.Imaging.BitmapSource.
        
            image: A System.Windows.Media.Imaging.BitmapSource object that contains the image data to store on the Clipboard.
        """
        pass

    @staticmethod
    def SetText(text, format=None):
        """
        SetText(text: str, format: TextDataFormat)
            Stores text data on the Clipboard in a specified text data format.  The System.Windows.DataFormats.UnicodeText data to store is specified as a string.
        
            text: A string that contains the text data to store on the Clipboard.
            format: A member of System.Windows.TextDataFormat that specifies the specific text data format to store.
        SetText(text: str)
            Stores System.Windows.DataFormats.UnicodeText data on the Clipboard.
        
            text: A string that contains the System.Windows.DataFormats.UnicodeText data to store on the Clipboard.
        """
        pass

    __all__ = [
        'Clear',
        'ContainsAudio',
        'ContainsData',
        'ContainsFileDropList',
        'ContainsImage',
        'ContainsText',
        'Flush',
        'GetAudioStream',
        'GetData',
        'GetDataObject',
        'GetFileDropList',
        'GetImage',
        'GetText',
        'IsCurrent',
        'SetAudio',
        'SetData',
        'SetDataObject',
        'SetFileDropList',
        'SetImage',
        'SetText',
    ]

