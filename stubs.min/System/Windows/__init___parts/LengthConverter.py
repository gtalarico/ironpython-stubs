class LengthConverter(TypeConverter):
    """
    Converts instances of other types to and from instances of a System.Double that represent an object's length.
    
    LengthConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: LengthConverter, typeDescriptorContext: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether conversion is possible from a specified type to a System.Double that represents an object's length.
        
            typeDescriptorContext: Provides contextual information about a component.
            sourceType: Identifies the data type to evaluate for conversion.
            Returns: true if conversion is possible; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: LengthConverter, typeDescriptorContext: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether conversion is possible to a specified type from a System.Double that represents an object's length.
        
            typeDescriptorContext: Provides contextual information about a component.
            destinationType: Identifies the data type to evaluate for conversion.
            Returns: true if conversion to the destinationType is possible; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: LengthConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, source: object) -> object
        
            Converts instances of other data types into instances of System.Double that represent an object's length.
        
            typeDescriptorContext: Provides contextual information about a component.
            cultureInfo: Represents culture-specific information that is maintained during a conversion.
            source: Identifies the object that is being converted to System.Double.
            Returns: An instance of System.Double that is the value of the conversion.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: LengthConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts other types into instances of System.Double that represent an object's length.
        
            typeDescriptorContext: Describes context information of a component, such as its container and System.ComponentModel.PropertyDescriptor.
            cultureInfo: Identifies culture-specific information, including the writing system and the calendar that is used.
            value: Identifies the System.Object that is being converted.
            destinationType: The data type that this instance of System.Double is being converted to.
            Returns: A new System.Object that is the value of the conversion.
        """
        pass

