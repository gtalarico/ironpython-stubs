class TextDecorationCollectionConverter(TypeConverter):
    """
    Converts instances of System.Windows.TextDecorationCollection from other data types.
    
    TextDecorationCollectionConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: TextDecorationCollectionConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Returns a value that indicates whether this converter can convert an object of the given type to an instance of System.Windows.TextDecorationCollection.
        
            context: Describes the context information of a type.
            sourceType: The type of the source that is being evaluated for conversion.
            Returns: true if the converter can convert the provided type to an instance of System.Windows.TextDecorationCollection; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: TextDecorationCollectionConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.TextDecorationCollection can be converted to a different type.
        
            context: Describes the context information of a type.
            destinationType: The type of the source that is being evaluated for conversion.
            Returns: false is always returned because the System.Windows.TextDecorationCollection cannot be converted to another type.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: TextDecorationCollectionConverter, context: ITypeDescriptorContext, culture: CultureInfo, input: object) -> object
        
            Attempts to convert a specified object to an instance of System.Windows.TextDecorationCollection.
        
            context: Describes the context information of a type.
            culture: Describes the System.Globalization.CultureInfo of the type being converted.
            input: The object being converted.
            Returns: The instance of System.Windows.FontWeight created from the converted input.
        """
        pass

    @staticmethod
    def ConvertFromString(*__args):
        """
        ConvertFromString(text: str) -> TextDecorationCollection
        
            Attempts to convert a specified string to an instance of System.Windows.TextDecorationCollection.
        
            text: The System.String to be converted into the System.Windows.TextDecorationCollection object.
            Returns: The instance of System.Windows.TextDecorationCollection created from the converted text.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: TextDecorationCollectionConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert an instance of System.Windows.TextDecorationCollection to a specified type.
        
            context: Describes the context information of a type.
            culture: Describes the System.Globalization.CultureInfo of the type being converted.
            value: The instance of System.Windows.TextDecorationCollection to convert.
            destinationType: The type this instance of System.Windows.TextDecorationCollection is converted to.
            Returns: null is always returned because System.Windows.TextDecorationCollection cannot be converted to any other type.
        """
        pass

