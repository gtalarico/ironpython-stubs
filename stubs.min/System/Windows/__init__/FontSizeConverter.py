class FontSizeConverter(TypeConverter):
    """
    Converts font size values to and from other type representations.
    
    FontSizeConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: FontSizeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines if conversion from a specified type to a System.Double value is possible.
        
            context: Describes context information of a component such as its container and System.ComponentModel.PropertyDescriptor.
            sourceType: Identifies the data type to evaluate for purposes of conversion.
            Returns: true if sourceType can be converted to System.Double; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: FontSizeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines if conversion of a font size value to a specified type is possible.
        
            context: Context information of a component such as its container and System.ComponentModel.PropertyDescriptor.
            destinationType: The data type to evaluate for purposes of conversion.
            Returns: true if this type can be converted; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: FontSizeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts a specified type to a System.Double.
        
            context: Context information of a component such as its container and System.ComponentModel.PropertyDescriptor.
            culture: Cultural specific information, including the writing system and calendar used.
            value: The value which is being converted to a font size value.
            Returns: A System.Double value that represents the converted font size value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: FontSizeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts a System.Double value to a specified type.
        
            context: Context information of a component such as its container and System.ComponentModel.PropertyDescriptor.
            culture: Cultural specific information, including writing system and calendar used.
            value: The System.Object being converted.
            destinationType: The data type this font size value is being converted to.
            Returns: A new System.Object that is the value of the conversion.
        """
        pass

