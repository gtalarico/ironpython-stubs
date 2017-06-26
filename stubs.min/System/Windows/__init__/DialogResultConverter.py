class DialogResultConverter(TypeConverter):
    """
    Converts the System.Windows.Window.DialogResult property, which is a System.Nullable value of type System.Boolean, to and from other types.
    
    DialogResultConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: DialogResultConverter, typeDescriptorContext: ITypeDescriptorContext, sourceType: Type) -> bool
        
            System.Windows.DialogResultConverter does not support converting from other types to System.Windows.Window.DialogResult (a System.Nullable value of type System.Boolean).
        
            typeDescriptorContext: A System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type to convert from.
            Returns: A System.Boolean that always returns false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: DialogResultConverter, typeDescriptorContext: ITypeDescriptorContext, destinationType: Type) -> bool
        
            System.Windows.DialogResultConverter does not support converting from System.Windows.Window.DialogResult (a System.Nullable value of type System.Boolean) to other types.
        
            typeDescriptorContext: A System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type to convert to.
            Returns: A System.Boolean that always returns false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: DialogResultConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, source: object) -> object
        
            System.Windows.DialogResultConverter does not support converting from System.Windows.Window.DialogResult (a System.Nullable value of type System.Boolean) to other types.
        
            typeDescriptorContext: A System.ComponentModel.ITypeDescriptorContext that provides a format context.
            cultureInfo: The System.Globalization.CultureInfo to use as the current culture. If null is passed, the current culture is assumed.
            source: The System.Object to convert.
            Returns: Always raises System.InvalidOperationException.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: DialogResultConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, value: object, destinationType: Type) -> object
        
            System.Windows.DialogResultConverter does not support converting from other types to System.Windows.Window.DialogResult (a System.Nullable value of type System.Boolean).
        
            typeDescriptorContext: A System.ComponentModel.ITypeDescriptorContext that provides a format context.
            cultureInfo: The System.Globalization.CultureInfo to use as the current culture. If null is passed, the current culture is assumed.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value parameter to.
            Returns: Always raises System.InvalidOperationException.
        """
        pass

