class MouseActionValueSerializer(ValueSerializer):
    """
    Converts instances of System.String to and from instances of System.Windows.Input.MouseAction.
    
    MouseActionValueSerializer()
    """
    def CanConvertFromString(self, value, context):
        """
        CanConvertFromString(self: MouseActionValueSerializer, value: str, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.String can be convert to an instance of System.Windows.Input.MouseAction.
        
            value: String to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: Always returns true.
        """
        pass

    def CanConvertToString(self, value, context):
        """
        CanConvertToString(self: MouseActionValueSerializer, value: object, context: IValueSerializerContext) -> bool
        
            Determines if the specified System.Windows.Input.MouseAction can be converted to a System.String.
        
            value: The modifier keys to evaluate for conversion.
            context: Context information that is used for conversion.
            Returns: true if value can be converted into a System.String; otherwise, false.
        """
        pass

    def ConvertFromString(self, value, context):
        """
        ConvertFromString(self: MouseActionValueSerializer, value: str, context: IValueSerializerContext) -> object
        
            Converts a System.String into a System.Windows.Input.MouseAction.
        
            value: The string to convert into a System.Windows.Input.MouseAction.
            context: Context information that is used for conversion.
            Returns: A new instance of System.Windows.Input.MouseAction based on the supplied value.
        """
        pass

    def ConvertToString(self, value, context):
        """
        ConvertToString(self: MouseActionValueSerializer, value: object, context: IValueSerializerContext) -> str
        
            Converts an instance of System.Windows.Input.MouseAction to a System.String.
        
            value: The key to convert into a string.
            context: Context information that is used for conversion.
            Returns: An invariant string representation of the specified System.Windows.Input.MouseAction.
        """
        pass

