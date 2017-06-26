class FontStretchConverter(TypeConverter):
    """
    Converts instances of System.Windows.FontStretch to and from other type representations.
    
    FontStretchConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: FontStretchConverter, td: ITypeDescriptorContext, t: Type) -> bool
        
            Determines if conversion from a specified type to a System.Windows.FontStretch value is possible.
        
            td: Context information of a type.
            t: The type of the source that is being evaluated for conversion.
            Returns: true if t can create a System.Windows.FontStretch; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: FontStretchConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.FontStretch can be converted to a different type.
        
            context: Context information of a type.
            destinationType: The desired type that that this instance of System.Windows.FontStretch is being evaluated for conversion to.
            Returns: true if the converter can convert System.Windows.FontStretch to destinationType; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: FontStretchConverter, td: ITypeDescriptorContext, ci: CultureInfo, value: object) -> object
        
            Attempts to convert a specified object to an instance of System.Windows.FontStretch.
        
            td: Context information of a type.
            ci: System.Globalization.CultureInfo of the type being converted.
            value: The object being converted.
            Returns: The instance of System.Windows.FontStretch created from the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: FontStretchConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert an instance of System.Windows.FontStretch to a specified type.
        
            context: Context information of a type.
            culture: System.Globalization.CultureInfo of the type being converted.
            value: The instance of System.Windows.FontStretch to convert.
            destinationType: The type this instance of System.Windows.FontStretch is converted to.
            Returns: The object created from the converted instance of System.Windows.FontStretch.
        """
        pass

