class CacheModeConverter(TypeConverter):
    """
    Converts a System.Windows.Media.CacheMode from one data type to another.
    
    CacheModeConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: CacheModeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether this System.Windows.Media.CacheModeConverter can convert an instance of the specified type to a System.Windows.Media.CacheMode, using the specified context.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that specifies the type you want to convert from.
            Returns: true if this System.Windows.Media.CacheModeConverter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: CacheModeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether this System.Windows.Media.CacheModeConverter can convert a System.Windows.Media.CacheMode to an instance of a specified type, using the specified context.
        
            context: A System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A type representing the type to convert to.
            Returns: true if this System.Windows.Media.CacheModeConverter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: CacheModeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts a specified object to a System.Windows.Media.CacheMode.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that holds information about a specific culture.
            value: The System.Object to be converted.
            Returns: The System.Windows.Media.CacheMode that is created by converting value; otherwise, an exception is raised.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: CacheModeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts a System.Windows.Media.CacheMode to the specified type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that represents information about a culture, such as language and calendar system. Can be null.
            value: The System.Object to convert.
            destinationType: The System.Type to convert to.
            Returns: The converted object.
        """
        pass

