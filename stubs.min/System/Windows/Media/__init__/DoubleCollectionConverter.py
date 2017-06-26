class DoubleCollectionConverter(TypeConverter):
    """
    Converts instances of other types to and from a System.Windows.Media.DoubleCollection.
    
    DoubleCollectionConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: DoubleCollectionConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object can be converted from a specified type to an instance of a System.Windows.Media.DoubleCollection.
        
            context: The context information of a type.
            sourceType: The type of the source that is being evaluated for conversion.
            Returns: true if the type can be converted to a System.Windows.Media.DoubleCollection; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: DoubleCollectionConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of a System.Windows.Media.DoubleCollection can be converted to a different type.
        
            context: The context information of a type.
            destinationType: The needed type for which you are evaluating this System.Windows.Media.DoubleCollection for conversion.
            Returns: true if this System.Windows.Media.DoubleCollection can be converted to destinationType; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: DoubleCollectionConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Attempts to convert the specified object to a System.Windows.Media.DoubleCollection.
        
            context: The context information of a type.
            culture: The System.Globalization.CultureInfo of the type you want to convert.
            value: The object being converted.
            Returns: The System.Windows.Media.DoubleCollection that is created from converting value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: DoubleCollectionConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.Media.DoubleCollection to a specified type.
        
            context: The context information of a type.
            culture: The System.Globalization.CultureInfo of the type you want to convert.
            value: The System.Windows.Media.DoubleCollection to convert.
            destinationType: The type to convert this System.Windows.Media.DoubleCollection to.
            Returns: The object you create when you convert this System.Windows.Media.DoubleCollection.
        """
        pass

