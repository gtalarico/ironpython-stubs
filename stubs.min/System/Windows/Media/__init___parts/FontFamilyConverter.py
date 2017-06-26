class FontFamilyConverter(TypeConverter):
    """
    Converts instances of the System.String type to and from System.Windows.Media.FontFamily instances.
    
    FontFamilyConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: FontFamilyConverter, td: ITypeDescriptorContext, t: Type) -> bool
        
            Determines whether a class can be converted from a given type to an instance of System.Windows.Media.FontFamily.
        
            td: Describes the context information of a type.
            t: The type of the source that is being evaluated for conversion.
            Returns: true if the converter can convert from the specified type to an instance of System.Windows.Media.FontFamily; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: FontFamilyConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.Media.FontFamily can be converted to a different type.
        
            context: Describes the context information of a type.
            destinationType: The desired type that this instance of System.Windows.Media.FontFamily is being evaluated for conversion.
            Returns: true if the converter can convert this instance of System.Windows.Media.FontFamily to the specified type; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: FontFamilyConverter, context: ITypeDescriptorContext, cultureInfo: CultureInfo, o: object) -> object
        
            Attempts to convert a specified object to an instance of System.Windows.Media.FontFamily.
        
            context: Describes the context information of a type.
            cultureInfo: Cultural-specific information that should be respected during conversion.
            o: The object being converted.
            Returns: The instance of System.Windows.Media.FontFamily that is created from the converted o parameter.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: FontFamilyConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a specified object to an instance of System.Windows.Media.FontFamily.
        
            context: Describes the context information of a type.
            culture: Cultural-specific information that should be respected during conversion.
            value: The object being converted.
            destinationType: The type that this instance of System.Windows.Media.FontFamily is converted to.
            Returns: The object that is created from the converted instance of System.Windows.Media.FontFamily.
        """
        pass

