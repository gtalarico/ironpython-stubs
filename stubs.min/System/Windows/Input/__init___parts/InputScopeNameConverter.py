class InputScopeNameConverter(TypeConverter):
    """
    Converts instances of System.Windows.Input.InputScopeName to and from other data types.
    
    InputScopeNameConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: InputScopeNameConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Indicates whether an object can be converted from a given type to an instance of a System.Windows.Input.InputScopeName.
        
            context: Describes the context information of a type.
            sourceType: The source System.Type that is being queried for conversion support.
            Returns: true if sourceType is type System.String; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: InputScopeNameConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether instances of System.Windows.Input.InputScopeName can be converted to the specified type.
        
            context: Describes the context information of a type.
            destinationType: The desired type this System.Windows.Input.InputScopeName is being evaluated to be converted to.
            Returns: true if destinationType is type System.String; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: InputScopeNameConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Converts the specified object to a System.Windows.Input.InputScopeName.
        
            context: Describes the context information of a type.
            culture: Describes the System.Globalization.CultureInfo of the type being converted.
            source: The object being converted.
            Returns: The System.Windows.Input.InputScopeName created from converting source.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: InputScopeNameConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified System.Windows.Input.InputScopeName to the specified type.
        
            context: Describes the context information of a type.
            culture: Describes the System.Globalization.CultureInfo of the type being converted.
            value: The System.Windows.Input.InputScopeName to convert.
            destinationType: The type to convert the System.Windows.Input.InputScopeName to.
            Returns: The object created from converting this System.Windows.Input.InputScopeName.
        """
        pass

