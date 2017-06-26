class ColorConverter(TypeConverter):
    """
    Converts instances of other types to and from an instance of System.Windows.Media.Color.
    
    ColorConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: ColorConverter, td: ITypeDescriptorContext, t: Type) -> bool
        
            Determines whether an object can be converted from a given type to an instance of a System.Windows.Media.Color.
        
            td: Describes the context information of a type.
            t: The type of the source that is being evaluated for conversion.
            Returns: true if the type can be converted to a System.Windows.Media.Color; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: ColorConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of a System.Windows.Media.Color can be converted to a different type.
        
            context: Describes the context information of a type.
            destinationType: The desired type this System.Windows.Media.Color is being evaluated for conversion.
            Returns: true if this System.Windows.Media.Color can be converted to destinationType; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: ColorConverter, td: ITypeDescriptorContext, ci: CultureInfo, value: object) -> object
        
            Attempts to convert the specified object to a System.Windows.Media.Color.
        
            td: Describes the context information of a type.
            ci: Cultural information to respect during conversion.
            value: The object being converted.
            Returns: The System.Windows.Media.Color created from converting value.
        """
        pass

    @staticmethod
    def ConvertFromString(*__args):
        """
        ConvertFromString(value: str) -> object
        
            Attempts to convert a string to a System.Windows.Media.Color.
        
            value: The string to convert to a System.Windows.Media.Color.
            Returns: A System.Windows.Media.Color that represents the converted text.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: ColorConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.Media.Color to a specified type.
        
            context: Describes the context information of a type.
            culture: Describes the System.Globalization.CultureInfo of the type being converted.
            value: The System.Windows.Media.Color to convert.
            destinationType: The type to convert this System.Windows.Media.Color to.
            Returns: The object created from converting this System.Windows.Media.Color.
        """
        pass

