class SizeConverter(TypeConverter):
    """
    Converts instances of other types to and from instances of the System.Windows.Size class.
    
    SizeConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: SizeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether a class can be converted from a given type to an instance of System.Windows.Size.
        
            context: Provides contextual information about a component.
            sourceType: Identifies the data type to evaluate for conversion.
            Returns: true if the sourceType can be converted to an instance of System.Windows.Size; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: SizeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.Size can be converted to a different type.
        
            context: Provides contextual information about a component.
            destinationType: Identifies the data type to evaluate for conversion.
            Returns: true if this instance of System.Windows.Size can be converted to the destinationType; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: SizeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Attempts to convert a specified object to an instance of System.Windows.Size.
        
            context: Provides contextual information about a component.
            culture: Culture-specific information that should be respected during conversion.
            value: The source object that is being converted.
            Returns: The instance of System.Windows.Size that is created from the converted source.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: SizeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert an instance of System.Windows.Size to a specified type.
        
            context: Provides contextual information about a component.
            culture: Culture-specific information that should be respected during conversion.
            value: The instance of System.Windows.Size to convert.
            destinationType: The type that this instance of System.Windows.Size is converted to.
            Returns: The object that is created from the converted instance of System.Windows.Size.
        """
        pass

