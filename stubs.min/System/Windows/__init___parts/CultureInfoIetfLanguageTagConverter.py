class CultureInfoIetfLanguageTagConverter(TypeConverter):
    """
    Converts instances of System.Globalization.CultureInfo to and from other data types.
    
    CultureInfoIetfLanguageTagConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: CultureInfoIetfLanguageTagConverter, typeDescriptorContext: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether System.Windows.CultureInfoIetfLanguageTagConverter can convert from a given type.
        
            typeDescriptorContext: The System.ComponentModel.ITypeDescriptorContext value.
            sourceType: The System.Type being queried for conversion support.
            Returns: true if System.Windows.CultureInfoIetfLanguageTagConverter can convert; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: CultureInfoIetfLanguageTagConverter, typeDescriptorContext: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether System.Windows.CultureInfoIetfLanguageTagConverter can convert to a given type.
        
            typeDescriptorContext: The System.ComponentModel.ITypeDescriptorContext value.
            destinationType: The System.Type being queried for conversion support.
            Returns: true if System.Windows.CultureInfoIetfLanguageTagConverter can convert; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: CultureInfoIetfLanguageTagConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, source: object) -> object
        
            Converts a given object type to a System.Globalization.CultureInfo object.
        
            typeDescriptorContext: The System.ComponentModel.ITypeDescriptorContext value.
            cultureInfo: The System.Globalization.CultureInfo object whose value is respected during conversion.
            source: The System.Type being converted.
            Returns: A System.Globalization.CultureInfo object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: CultureInfoIetfLanguageTagConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts a System.Globalization.CultureInfo object to a given object type.
        
            typeDescriptorContext: The System.ComponentModel.ITypeDescriptorContext value.
            cultureInfo: The System.Globalization.CultureInfo object whose value is respected during conversion.
            value: The object that represents the System.Globalization.CultureInfo to convert.
            destinationType: The System.Type of the returned converted object.
            Returns: A System.Object.
        """
        pass

