class InputScopeConverter(TypeConverter):
    """
    Converts a System.Windows.Input.InputScope to and from other types.
    
    InputScopeConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: InputScopeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an System.Windows.Input.InputScope object can be converted from an object of a specified type.
        
            context: An object that describes any type descriptor context.  This object must implement the System.ComponentModel.ITypeDescriptorContext interface.  This parameter may be null.
            sourceType: A System.Type to check for conversion compatibility.
            Returns: true if sourceType is type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: InputScopeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an System.Windows.Input.InputScope object can be converted to an object of a specified type.
        
            context: An object that describes any type descriptor context.  This object must implement the System.ComponentModel.ITypeDescriptorContext interface.  This parameter may be null.
            destinationType: A System.Type to check for conversion compatibility.
            Returns: true if destinationType is type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: InputScopeConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Converts a source object (string) into an System.Windows.Input.InputScope object.
        
            context: An object that describes any type descriptor context.  This object must implement the System.ComponentModel.ITypeDescriptorContext interface.  This parameter may be null.
            culture: A System.Globalization.CultureInfo object containing any cultural context for the conversion.  This parameter may be null.
            source: A source object to convert from.  This object must be a string.
            Returns: An System.Windows.Input.InputScope object converted from the specified source object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: InputScopeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts an System.Windows.Input.InputScope object into a specified object type (string).
        
            context: An object that describes any type descriptor context.  This object must implement the System.ComponentModel.ITypeDescriptorContext interface.  This parameter may be null.
            culture: A System.Globalization.CultureInfo object containing any cultural context for the conversion.  This parameter may be null.
            value: An object to convert from.  This object must be of type System.Windows.Input.InputScope.
            destinationType: A destination type to convert type.  This type must be string.
            Returns: A new object of the specified type (string) converted from the given System.Windows.Input.InputScope object.
        """
        pass

