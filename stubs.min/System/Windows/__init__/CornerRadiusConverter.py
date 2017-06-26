class CornerRadiusConverter(TypeConverter):
    """
    Converts instances of other types to and from a System.Windows.CornerRadius.
    
    CornerRadiusConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: CornerRadiusConverter, typeDescriptorContext: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Indicates whether an object can be converted from a given type to a System.Windows.CornerRadius.
        
            typeDescriptorContext: Describes the context information of a type.
            sourceType: The source System.Type that is being queried for conversion support.
            Returns: true if sourceType is of type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: CornerRadiusConverter, typeDescriptorContext: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether System.Windows.CornerRadius values can be converted to the specified type.
        
            typeDescriptorContext: Describes the context information of a type.
            destinationType: The desired type this System.Windows.CornerRadius is being evaluated to be converted to.
            Returns: true if destinationType is of type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: CornerRadiusConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, source: object) -> object
        
            Converts the specified object to a System.Windows.CornerRadius.
        
            typeDescriptorContext: Describes the context information of a type.
            cultureInfo: Describes the System.Globalization.CultureInfo of the type being converted.
            source: The object being converted.
            Returns: The System.Windows.CornerRadius created from converting source.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: CornerRadiusConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified System.Windows.CornerRadius to the specified type.
        
            typeDescriptorContext: Describes the context information of a type.
            cultureInfo: Describes the System.Globalization.CultureInfo of the type being converted.
            value: The System.Windows.CornerRadius to convert.
            destinationType: The type to convert the System.Windows.CornerRadius to.
            Returns: The object created from converting this System.Windows.CornerRadius (a string).
        """
        pass

