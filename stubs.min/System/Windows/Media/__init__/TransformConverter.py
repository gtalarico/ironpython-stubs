class TransformConverter(TypeConverter):
    """
    Converts a System.Windows.Media.Transform object to or from another object type.
    
    TransformConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: TransformConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether this class can convert an object of a specified type to a System.Windows.Media.Transform type.
        
            context: The conversion context.
            sourceType: The type from which to convert.
            Returns: true if conversion is possible; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: TransformConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether this class can convert an object of a specified type to the specified destination type.
        
            context: The conversion context.
            destinationType: The destination type.
            Returns: true if conversion is possible; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: TransformConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts from an object of a specified type to a System.Windows.Media.Transform object.
        
            context: The conversion context.
            culture: The culture information that applies to the conversion.
            value: The object to convert.
            Returns: A new System.Windows.Media.Transform object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: TransformConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified System.Windows.Media.Transform to the specified type by using the specified context and culture information.
        
            context: The conversion context.
            culture: The culture information that applies to the conversion.
            value: The System.Windows.Media.Transform to convert.
            destinationType: The destination type that the value object is converted to.
            Returns: An object that represents the converted value.
        """
        pass

