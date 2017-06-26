class RectConverter(TypeConverter):
    """
    Converts instances of other types to and from instances of System.Windows.Rect.
    
    RectConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: RectConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object can be converted from a given type to an instance of System.Windows.Rect.
        
            context: Provides contextual information required for conversion.
            sourceType: The type of the source that is being evaluated for conversion.
            Returns: true if the type can be converted to a System.Windows.Rect; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: RectConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether a System.Windows.Rect can be converted to the specified type.
        
            context: Provides contextual information required for conversion.
            destinationType: The desired type this System.Windows.Rect is being evaluated for conversion.
            Returns: true if a System.Windows.Rect can be converted to destinationType; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: RectConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Attempts to convert the specified object to a System.Windows.Rect.
        
            context: Provides contextual information required for conversion.
            culture: Cultural information which is respected when converting.
            value: The object being converted.
            Returns: The System.Windows.Rect created from converting value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: RectConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.Rect to the specified type.
        
            context: Provides contextual information required for conversion.
            culture: Cultural information which is respected during conversion.
            value: The System.Windows.Rect to convert.
            destinationType: The type to convert this System.Windows.Rect to.
            Returns: The object created from converting this System.Windows.Rect.
        """
        pass

