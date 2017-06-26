class DataObject(object, IDataObject, IDataObject):
    """
    Provides a basic implementation of the System.Windows.IDataObject interface, which defines a format-independent mechanism for transferring data.
    
    DataObject()
    DataObject(data: object)
    DataObject(format: str, data: object)
    DataObject(format: Type, data: object)
    DataObject(format: str, data: object, autoConvert: bool)
    """
    @staticmethod
    def AddCopyingHandler(element, handler):
        """
        AddCopyingHandler(element: DependencyObject, handler: DataObjectCopyingEventHandler)
            Adds a System.Windows.DataObject.Copying event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to add.
        """
        pass

    @staticmethod
    def AddPastingHandler(element, handler):
        """
        AddPastingHandler(element: DependencyObject, handler: DataObjectPastingEventHandler)
            Adds a System.Windows.DataObject.Pasting event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to add.
        """
        pass

    @staticmethod
    def AddSettingDataHandler(element, handler):
        """
        AddSettingDataHandler(element: DependencyObject, handler: DataObjectSettingDataEventHandler)
            Adds a System.Windows.DataObject.SettingData event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to add.
        """
        pass

    def ContainsAudio(self):
        """
        ContainsAudio(self: DataObject) -> bool
        
            Queries a data object for the presence of data in the System.Windows.DataFormats.WaveAudio data format.
            Returns: true if the data object contains data in the System.Windows.DataFormats.WaveAudio data format; otherwise, false.
        """
        pass

    def ContainsFileDropList(self):
        """
        ContainsFileDropList(self: DataObject) -> bool
        
            Queries a data object for the presence of data in the System.Windows.DataFormats.FileDrop data format.
            Returns: true if the data object contains data in the System.Windows.DataFormats.FileDrop data format; otherwise, false.
        """
        pass

    def ContainsImage(self):
        """
        ContainsImage(self: DataObject) -> bool
        
            Queries a data object for the presence of data in the System.Windows.DataFormats.Bitmap data format.
            Returns: true if the data object contains data in the System.Windows.DataFormats.Bitmap data format; otherwise, false.
        """
        pass

    def ContainsText(self, format=None):
        """
        ContainsText(self: DataObject, format: TextDataFormat) -> bool
        
            Queries a data object for the presence of data in a text data format.
        
            format: A member of the System.Windows.TextDataFormat enumeration that specifies the text data format to query for.
            Returns: true if the data object contains data in a text data format; otherwise, false.
        ContainsText(self: DataObject) -> bool
        
            Queries a data object for the presence of data in the System.Windows.DataFormats.UnicodeText format.
            Returns: true if the data object contains data in the System.Windows.DataFormats.UnicodeText data format; otherwise, false.
        """
        pass

    def GetAudioStream(self):
        """
        GetAudioStream(self: DataObject) -> Stream
        
            Returns a stream that contains data in the System.Windows.DataFormats.WaveAudio data format.
            Returns: A stream that contains data in the System.Windows.DataFormats.WaveAudio format, or null if the data is unavailable in this format.
        """
        pass

    def GetData(self, format, autoConvert=None):
        """
        GetData(self: DataObject, format: Type) -> object
        
            Returns a data object in a format specified by a System.Type object.
        
            format: A System.Type that specifies the format for the data. For a set of predefined data formats, see the System.Windows.DataFormats class.
            Returns: A data object with the data in the specified format, or null if the data is unavailable in the specified format.
        GetData(self: DataObject, format: str) -> object
        
            Returns data in a format specified by a string.
        
            format: A string that specifies the format for the data. For a set of predefined data formats, see the System.Windows.DataFormats class.
            Returns: An object that contains the data in the specified format, or null if the data is unavailable in the specified format.
        GetData(self: DataObject, format: str, autoConvert: bool) -> object
        
            Returns a data object in a specified format, optionally converting the data to the specified format.
        
            format: A string that specifies the format for the data. For a set of predefined data formats, see the System.Windows.DataFormats class.
            autoConvert: true to attempt to automatically convert the data to the specified format; false for no data format conversion.
            Returns: A data object with the data in the specified format, or null if the data is unavailable in the specified format.If the autoConvert parameter is true and the data cannot be converted to the specified 
             format, or if automatic conversion is disabled (by calling System.Windows.DataObject.SetData(System.String,System.Object,System.Boolean) with the autoConvert parameter set to false), this method returns 
             null.
        """
        pass

    def GetDataPresent(self, format, autoConvert=None):
        """
        GetDataPresent(self: DataObject, format: str) -> bool
        
            Determines whether the data is available in, or can be converted to, a format specified by a string.
        
            format: A string that specifies the format for the data. For a set of predefined data formats, see the System.Windows.DataFormats class.
            Returns: true if the data is in, or can be converted to, the specified format; otherwise, false.
        GetDataPresent(self: DataObject, format: str, autoConvert: bool) -> bool
        
            Determines whether the data is available in, or can be converted to, a specified format. A Boolean flag indicates whether to check if the data can be converted to the specified format if it is not 
             available in that format.
        
        
            format: A string that specifies the data format to check. For a set of predefined data formats, see the System.Windows.DataFormats class.
            autoConvert: false to check only for the specified format; true to also check whether data stored in this data object can be converted to the specified format.
            Returns: true if the data is in, or can be converted to, the specified format; otherwise, false.
        GetDataPresent(self: DataObject, format: Type) -> bool
        
            Determines whether the data is available in, or can be converted to, a format specified by a System.Type object.
        
            format: A System.Type that specifies the data format to check. F or a set of predefined data formats, see the System.Windows.DataFormats class.
            Returns: true if the data is in, or can be converted to, the specified format; otherwise, false.
        """
        pass

    def GetFileDropList(self):
        """
        GetFileDropList(self: DataObject) -> StringCollection
        
            Returns a string collection that contains a list of dropped files.
            Returns: A collection of strings, where each string specifies the name of a file in the list of dropped files, or null if the data is unavailable in this format.
        """
        pass

    def GetFormats(self, autoConvert=None):
        """
        GetFormats(self: DataObject) -> Array[str]
        
            Returns a list of formats in which the data in this data object is stored, or can be converted to.
            Returns: An array of strings, with each string specifying the name of a format that this data object supports.
        GetFormats(self: DataObject, autoConvert: bool) -> Array[str]
        
            Returns a list of formats in which the data in this data object is stored. A Boolean flag indicates whether to also include formats that the data can be automatically converted to.
        
            autoConvert: true to retrieve all formats in which the data in this data object is stored, or can be converted to; false to retrieve only formats in which the data in this data object is stored.
            Returns: An array of strings, with each string specifying the name of a format supported by this data object.
        """
        pass

    def GetImage(self):
        """
        GetImage(self: DataObject) -> BitmapSource
        
            Returns a System.Windows.Media.Imaging.BitmapSource object that contains data in the System.Windows.DataFormats.Bitmap format.
            Returns: A System.Windows.Media.Imaging.BitmapSource object that contains data in the System.Windows.DataFormats.Bitmap format, or null if the data is unavailable in this format.
        """
        pass

    def GetText(self, format=None):
        """
        GetText(self: DataObject, format: TextDataFormat) -> str
        
            Returns a string that contains text data of the specified format in this data object.
        
            format: A member of System.Windows.TextDataFormat that specifies the specific text data format to retrieve.
            Returns: A string containing text data in the specified data format, or an empty string if no corresponding text data is available.
        GetText(self: DataObject) -> str
        
            Returns a string that contains the System.Windows.DataFormats.UnicodeText data in this data object.
            Returns: A string that contains the System.Windows.DataFormats.UnicodeText data, or an empty string if no System.Windows.DataFormats.UnicodeText data is available.
        """
        pass

    @staticmethod
    def RemoveCopyingHandler(element, handler):
        """
        RemoveCopyingHandler(element: DependencyObject, handler: DataObjectCopyingEventHandler)
            Removes a System.Windows.DataObject.Copying event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to remove.
        """
        pass

    @staticmethod
    def RemovePastingHandler(element, handler):
        """
        RemovePastingHandler(element: DependencyObject, handler: DataObjectPastingEventHandler)
            Removes a System.Windows.DataObject.Pasting event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to remove.
        """
        pass

    @staticmethod
    def RemoveSettingDataHandler(element, handler):
        """
        RemoveSettingDataHandler(element: DependencyObject, handler: DataObjectSettingDataEventHandler)
            Removes a System.Windows.DataObject.SettingData event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to remove.
        """
        pass

    def SetAudio(self, *__args):
        """
        SetAudio(self: DataObject, audioStream: Stream)
            Stores audio data (System.Windows.DataFormats.WaveAudio data format) in this data object.  The audio data is specified as a stream.
        
            audioStream: A stream that contains audio data to store in the data object.
        SetAudio(self: DataObject, audioBytes: Array[Byte])
            Stores audio data (System.Windows.DataFormats.WaveAudio data format) in this data object. The audio data is specified as a byte array.
        
            audioBytes: A byte array that contains audio data to store in the data object.
        """
        pass

    def SetData(self, *__args):
        """
        SetData(self: DataObject, format: Type, data: object)
            Stores the specified data in this data object, along with one or more specified data formats; the data format is specified by a System.Type object.
        
            format: A System.Type object that specifies the format for the data. For a set of predefined data formats, see the System.Windows.DataFormats class.
            data: An object that represents the data to store in this data object.
        SetData(self: DataObject, format: str, data: object, autoConvert: bool)
            Stores the specified data in this data object, along with one or more specified data formats. This overload includes a Boolean flag to indicate whether the data can be converted to another format on 
             retrieval.
        
        
            format: A string that specifies the format for the data. For a set of predefined data formats, see the System.Windows.DataFormats class.
            data: An object that represents the data to store in this data object.
            autoConvert: true to allow the data to be converted to another format on retrieval; false to prohibit the data from being converted to another format on retrieval.
        SetData(self: DataObject, data: object)
            Stores the specified data in this data object, automatically determining the data format from the source object type.
        
            data: An object that represents the data to store in this data object.
        SetData(self: DataObject, format: str, data: object)
            Stores the specified data in this data object, along with one or more specified data formats; the data format is specified by a string.
        
            format: A string that specifies the format for the data. For a set of predefined data formats, see the System.Windows.DataFormats class.
            data: An object that represents the data to store in this data object.
        """
        pass

    def SetFileDropList(self, fileDropList):
        """
        SetFileDropList(self: DataObject, fileDropList: StringCollection)
            Stores System.Windows.DataFormats.FileDrop data in this data object.  The dropped file list is specified as a string collection.
        
            fileDropList: A string collection that contains the dropped file list to store in the data object.
        """
        pass

    def SetImage(self, image):
        """
        SetImage(self: DataObject, image: BitmapSource)
            Stores System.Windows.DataFormats.Bitmap data in this data object.  The image data is specified as a System.Windows.Media.Imaging.BitmapSource.
        
            image: A System.Windows.Media.Imaging.BitmapSource object that contains the image data to store in the data object.
        """
        pass

    def SetText(self, textData, format=None):
        """
        SetText(self: DataObject, textData: str, format: TextDataFormat)
            Stores text data in this data object. The format of the text data to store is specified with a member of System.Windows.TextDataFormat.
        
            textData: A string that contains the text data to store in the data object.
            format: A member of System.Windows.TextDataFormat that specifies the text data format to store.
        SetText(self: DataObject, textData: str)
            Stores System.Windows.DataFormats.UnicodeText data, specified as a string, in this data object.
        
            textData: A string that contains the System.Windows.DataFormats.UnicodeText data to store in the data object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, data: object)
        __new__(cls: type, format: str, data: object)
        __new__(cls: type, format: Type, data: object)
        __new__(cls: type, format: str, data: object, autoConvert: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CopyingEvent = None
    PastingEvent = None
    SettingDataEvent = None

