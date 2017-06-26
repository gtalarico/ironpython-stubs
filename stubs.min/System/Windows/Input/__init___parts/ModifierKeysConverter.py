class ModifierKeysConverter(TypeConverter):
    """
    Converts a System.Windows.Input.ModifierKeys object to and from other types.
    
    ModifierKeysConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: ModifierKeysConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.Input.ModifierKeys, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: true if sourceType is type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: ModifierKeysConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.Input.ModifierKeys can be converted to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: true if destinationType is type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: ModifierKeysConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Attempts to convert the specified object to a System.Windows.Input.ModifierKeys, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            source: The object to convert.
            Returns: The converted object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: ModifierKeysConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.Input.ModifierKeys to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass

    @staticmethod
    def IsDefinedModifierKeys(modifierKeys):
        """
        IsDefinedModifierKeys(modifierKeys: ModifierKeys) -> bool
        
            Determines whether the specified value is a valid System.Windows.Input.ModifierKeys value.
        
            modifierKeys: The value to check for validity.
            Returns: true if input is a valid System.Windows.Input.ModifierKeys value; otherwise, false.
        """
        pass

