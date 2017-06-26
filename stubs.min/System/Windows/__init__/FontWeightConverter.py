class FontWeightConverter(TypeConverter):
    """
    Converts instances of System.Windows.FontWeight to and from other data types.
    
    FontWeightConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: FontWeightConverter, td: ITypeDescriptorContext, t: Type) -> bool
        
            Returns a value that indicates whether this converter can convert an object of the given type to an instance of System.Windows.FontWeight.
        
            td: Context information of a type.
            t: The type of the source that is being evaluated for conversion.
            Returns: true if the converter can convert the provided type to an instance of System.Windows.FontWeight; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: FontWeightConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.FontWeight can be converted to a different type.
        
            context: Context information of a type.
            destinationType: The desired type that that this instance of System.Windows.FontWeight is being evaluated for conversion to.
            Returns: true if the converter can convert this instance of System.Windows.FontWeight; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: FontWeightConverter, td: ITypeDescriptorContext, ci: CultureInfo, value: object) -> object
        
            Attempts to convert a specified object to an instance of System.Windows.FontWeight.
        
            td: Context information of a type.
            ci: System.Globalization.CultureInfo of the type being converted.
            value: The object being converted.
            Returns: The instance of System.Windows.FontWeight created from the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: FontWeightConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert an instance of System.Windows.FontWeight to a specified type.
        
            context: Describes the context information of a type.
            culture: Describes the System.Globalization.CultureInfo of the type being converted.
            value: The instance of System.Windows.FontWeight to convert.
            destinationType: The type this instance of System.Windows.FontWeight is converted to.
            Returns: The object created from the converted instance of System.Windows.FontWeight.
        """
        pass

