class Int32RectConverter(TypeConverter):
    """
    Converts instances of other types to and from an System.Windows.Int32Rect.
    
    Int32RectConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: Int32RectConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object can be converted from a given type to an instance of an System.Windows.Int32Rect.
        
            context: Describes the context information of a type.
            sourceType: The type of the source that is being evaluated for conversion.
            Returns: true if the type can be converted to an System.Windows.Int32Rect; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: Int32RectConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of an System.Windows.Int32Rect can be converted to a different type.
        
            context: Describes the context information of a type.
            destinationType: The desired type this System.Windows.Int32Rect is being evaluated for conversion.
            Returns: true if this System.Windows.Int32Rect can be converted to destinationType; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: Int32RectConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Attempts to convert the specified type to an System.Windows.Int32Rect.
        
            context: Provides contextual information required for conversion.
            culture: Cultural information to respect during conversion.
            value: The object being converted.
            Returns: The System.Windows.Int32Rect created from converting value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: Int32RectConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert an System.Windows.Int32Rect to a specified type.
        
            context: Provides contextual information required for conversion.
            culture: Cultural information to respect during conversion.
            value: The System.Windows.Int32Rect to convert.
            destinationType: The type to convert this System.Windows.Int32Rect to.
            Returns: The object created from converting this System.Windows.Int32Rect.
        """
        pass

