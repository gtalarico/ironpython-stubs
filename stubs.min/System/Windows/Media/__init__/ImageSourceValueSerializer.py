class ImageSourceValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Media.ImageSource.
    
    ImageSourceValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: ImageSourceValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if a System.String can be converted to an instance of System.Windows.Media.ImageSource.
        
            value: System.String to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if value can be converted; otherwise, false.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: ImageSourceValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if an instance of System.Windows.Media.ImageSource can be converted to a System.String.
        
            value: Instance of System.Windows.Media.ImageSource to evaluate for conversion.
            context: Context information used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: ImageSourceValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String to an System.Windows.Media.ImageSource.
        
            value: String value to convert into an System.Windows.Media.ImageSource.
            context: Context information used for conversion.
            Returns: A new instance of System.Windows.Media.ImageSource based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: ImageSourceValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Media.ImageSource to a System.String.
        
            value: The System.Windows.Media.ImageSource to evaluate for conversion.
            context: Context information used for conversion.
            Returns: A System.String representation of the supplied System.Windows.Media.ImageSource object.
        """
        pass

