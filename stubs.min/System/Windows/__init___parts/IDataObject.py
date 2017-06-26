class IDataObject:
    """ Provides a format-independent mechanism for transferring data. """
    def GetData(self, format, autoConvert=None):
        """
        GetData(self: IDataObject, format: str, autoConvert: bool) -> object
        
            Retrieves a data object in a specified format, optionally converting the data to the specified format.
        
            format: A string that specifies what format to retrieve the data as. See the System.Windows.DataFormats class for a set of predefined data formats.
            autoConvert: true to attempt to automatically convert the data to the specified format; false for no data format conversion.�If this parameter is false, the method returns data in the specified format if available, or 
             null if the data is not available in the specified format.
        
            Returns: A data object with the data in the specified format, or null if the data is not available in the specified format.
        GetData(self: IDataObject, format: Type) -> object
        
            Retrieves a data object in a specified format; the data format is specified by a System.Type object.
        
            format: A System.Type object that specifies what format to retrieve the data as. See the System.Windows.DataFormats class for a set of predefined data formats.
            Returns: A data object with the data in the specified format, or null if the data is not available in the specified format.
        GetData(self: IDataObject, format: str) -> object
        
            Retrieves a data object in a specified format; the data format is specified by a string.
        
            format: A string that specifies what format to retrieve the data as. See the System.Windows.DataFormats class for a set of predefined data formats.
            Returns: A data object with the data in the specified format, or null if the data is not available in the specified format.
        """
        pass

    def GetDataPresent(self, format, autoConvert=None):
        """
        GetDataPresent(self: IDataObject, format: str, autoConvert: bool) -> bool
        
            Checks to see whether the data is available in, or can be converted to, a specified format. A Boolean flag indicates whether to check if the data can be converted to the specified format, if it is not 
             available in that format.
        
        
            format: A string that specifies what format to check for. See the System.Windows.DataFormats class for a set of pre-defined data formats.
            autoConvert: false to only check for the specified format; true to also check whether or not data stored in this data object can be converted to the specified format.
            Returns: true if the data is in, or can be converted to, the specified format; otherwise, false.
        GetDataPresent(self: IDataObject, format: Type) -> bool
        
            Checks to see whether the data is available in, or can be converted to, a specified format. The data format is specified by a System.Type object.
        
            format: A System.Type that specifies what format to check for. See the System.Windows.DataFormats class for a set of predefined data formats.
            Returns: true if the data is in, or can be converted to, the specified format; otherwise, false.
        GetDataPresent(self: IDataObject, format: str) -> bool
        
            Checks to see whether the data is available in, or can be converted to, a specified format; the data format is specified by a string.
        
            format: A string that specifies what format to check for. See the System.Windows.DataFormats class for a set of pre-defined data formats.
            Returns: true if the data is in, or can be converted to, the specified format; otherwise, false.
        """
        pass

    def GetFormats(self, autoConvert=None):
        """
        GetFormats(self: IDataObject, autoConvert: bool) -> Array[str]
        
            Returns a list of all formats that the data in this data object is stored in. A Boolean flag indicates whether or not to also include formats that the data can be automatically converted to.
        
            autoConvert: true to retrieve all formats that data stored in this data object is stored in, or can be converted to; false to retrieve only formats that data stored in this data object is stored in (excluding formats 
             that the data is not stored in, but can be automatically converted to).
        
            Returns: An array of strings, with each string specifying the name of a format supported by this data object.
        GetFormats(self: IDataObject) -> Array[str]
        
            Returns a list of all formats that the data in this data object is stored in, or can be converted to.
            Returns: An array of strings, with each string specifying the name of a format supported by this data object.
        """
        pass

    def SetData(self, *__args):
        """
        SetData(self: IDataObject, format: Type, data: object)
            Stores the specified data in this data object, along with one or more specified data formats. The data format is specified by a System.Type class.
        
            format: A System.Type that specifies what format to store the data in. See the System.Windows.DataFormats class for a set of predefined data formats.
            data: The data to store in this data object.
        SetData(self: IDataObject, format: str, data: object, autoConvert: bool)
            Stores the specified data in this data object, along with one or more specified data formats. This overload includes a Boolean flag to indicate whether the data may be converted to another format on 
             retrieval.
        
        
            format: A string that specifies what format to store the data in. See the System.Windows.DataFormats class for a set of pre-defined data formats.
            data: The data to store in this data object.
            autoConvert: true to allow the data to be converted to another format on retrieval; false to prohibit the data from being converted to another format on retrieval.
        SetData(self: IDataObject, data: object)
            Stores the specified data in this data object, automatically converting the data format from the source object type.
        
            data: The data to store in this data object.
        SetData(self: IDataObject, format: str, data: object)
            Stores the specified data in this data object, along with one or more specified data formats. The data format is specified by a string.
        
            format: A string that specifies what format to store the data in. See the System.Windows.DataFormats class for a set of pre-defined data formats.
            data: The data to store in this data object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

