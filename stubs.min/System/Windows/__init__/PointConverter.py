class PointConverter(TypeConverter):
    """
    Converts instances of other types to and from a System.Windows.Point.
    
    PointConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: PointConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object can be converted from a given type to an instance of a System.Windows.Point.
        
            context: Describes the context information of a type.
            sourceType: The type of the source that is being evaluated for conversion.
            Returns: true if the type can be converted to a System.Windows.Point; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: PointConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of a System.Windows.Point can be converted to a different type.
        
            context: Describes the context information of a type.
            destinationType: The desired type this System.Windows.Point is being evaluated for conversion.
            Returns: true if this System.Windows.Point can be converted to destinationType; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: PointConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Attempts to convert the specified object to a System.Windows.Point.
        
            context: Provides contextual information required for conversion.
            culture: Cultural information to respect during conversion.
            value: The object being converted.
            Returns: The System.Windows.Point created from converting value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: PointConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.Point to a specified type.
        
            context: Provides contextual information required for conversion.
            culture: Cultural information to respect during conversion.
            value: The System.Windows.Point to convert.
            destinationType: The type to convert this System.Windows.Point to.
            Returns: The object created from converting this System.Windows.Point.
        """
        pass

