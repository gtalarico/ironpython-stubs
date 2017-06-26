class TemplateBindingExtensionConverter(TypeConverter):
    """
    A type converter that is used to construct a System.Windows.TemplateBindingExtension from an instance during serialization.
    
    TemplateBindingExtensionConverter()
    """
    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: TemplateBindingExtensionConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns whether this converter can convert the object to the specified type, using the specified context.
        
            context: An System.ComponentModel.ITypeDescriptorContext implementation that provides a format context.
            destinationType: The desired type of the conversion's output.
            Returns: true if this converter can perform the requested conversion; otherwise, false. Only a destinationType of System.ComponentModel.Design.Serialization.InstanceDescriptor will return true.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: TemplateBindingExtensionConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified type.
        
            context: An System.ComponentModel.ITypeDescriptorContext implementation that provides a format context.
            culture: A System.Globalization.CultureInfo object. If a null reference is passed, the current culture is assumed.
            value: The value to convert.
            destinationType: The desired type to convert to.
            Returns: The converted value.
        """
        pass

