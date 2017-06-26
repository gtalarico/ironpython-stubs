class BrushConverter(TypeConverter):
    """
    Used to convert a System.Windows.Media.Brush object to or from another object type.
    
    BrushConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: BrushConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether this class can convert an object of a given type to a System.Windows.Media.Brush object.
        
            context: The conversion context.
            sourceType: The type from which to convert.
            Returns: Returns true if conversion is possible (object is string type); otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: BrushConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether this class can convert an object of a given type to the specified destination type.
        
            context: The conversion context.
            destinationType: The destination type.
            Returns: Returns true if conversion is possible; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: BrushConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts from an object of a given type to a System.Windows.Media.Brush object.
        
            context: The conversion context.
            culture: The culture information that applies to the conversion.
            value: The object to convert.
            Returns: Returns a new System.Windows.Media.Brush object if successful; otherwise, NULL.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: BrushConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts a System.Windows.Media.Brush object to a specified type, using the specified context and culture information.
        
            context: The conversion context.
            culture: The current culture information.
            value: The System.Windows.Media.Brush to convert.
            destinationType: The destination type that the value object is converted to.
            Returns: An object that represents the converted value.
        """
        pass

