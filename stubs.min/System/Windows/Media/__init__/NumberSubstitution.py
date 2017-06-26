class NumberSubstitution(object):
    """
    Specifies how numbers in text are displayed in different cultures.
    
    NumberSubstitution()
    NumberSubstitution(source: NumberCultureSource, cultureOverride: CultureInfo, substitution: NumberSubstitutionMethod)
    """
    def Equals(self, obj):
        """
        Equals(self: NumberSubstitution, obj: object) -> bool
        
            Determines whether the specified object is equal to the current System.Windows.Media.NumberSubstitution object.
        
            obj: The System.Object to compare with the current System.Windows.Media.NumberSubstitution object.
            Returns: true if o is equal to the current System.Windows.Media.NumberSubstitution object; otherwise, false. If o is not a System.Windows.Media.NumberSubstitution object, false is returned.
        """
        pass

    @staticmethod
    def GetCultureOverride(target):
        """
        GetCultureOverride(target: DependencyObject) -> CultureInfo
        
            Returns the value of System.Windows.Media.NumberSubstitution.CultureOverride from the provided element.
        
            target: The element to return a System.Windows.Media.NumberSubstitution.CultureOverride value for.
            Returns: A System.Globalization.CultureInfo value that represents the culture that is used as an override.
        """
        pass

    @staticmethod
    def GetCultureSource(target):
        """
        GetCultureSource(target: DependencyObject) -> NumberCultureSource
        
            Returns the value of System.Windows.Media.NumberSubstitution.CultureSource from the provided element.
        
            target: The element to return a System.Windows.Media.NumberSubstitution.CultureSource value for.
            Returns: An enumerated value of System.Windows.Media.NumberCultureSource.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: NumberSubstitution) -> int
        
            Serves as a hash function for System.Windows.Media.NumberSubstitution. It is suitable for use in hashing algorithms and data structures such as a hash table.
            Returns: An System.Int32 value that represents the hash code for the current object.
        """
        pass

    @staticmethod
    def GetSubstitution(target):
        """
        GetSubstitution(target: DependencyObject) -> NumberSubstitutionMethod
        
            Returns the value of System.Windows.Media.NumberSubstitution.Substitution from the provided element.
        
            target: The element to return a System.Windows.Media.NumberSubstitution.Substitution value for.
            Returns: An enumerated value of System.Windows.Media.NumberSubstitutionMethod.
        """
        pass

    @staticmethod
    def SetCultureOverride(target, value):
        """
        SetCultureOverride(target: DependencyObject, value: CultureInfo)
            Sets the value of System.Windows.Media.NumberSubstitution.CultureOverride for a provided element.
        
            target: Element that is specifying a culture override.
            value: A culture override value of type System.Globalization.CultureInfo.
        """
        pass

    @staticmethod
    def SetCultureSource(target, value):
        """
        SetCultureSource(target: DependencyObject, value: NumberCultureSource)
            Sets the value of System.Windows.Media.NumberSubstitution.CultureSource for a provided element.
        
            target: Element that is specifying a culture override.
            value: A culture source value of type System.Windows.Media.NumberCultureSource.
        """
        pass

    @staticmethod
    def SetSubstitution(target, value):
        """
        SetSubstitution(target: DependencyObject, value: NumberSubstitutionMethod)
            Sets the value of System.Windows.Media.NumberSubstitution.Substitution for a provided element.
        
            target: Element that is specifying a substitution method.
            value: A substitution method value of type System.Windows.Media.NumberSubstitutionMethod.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source=None, cultureOverride=None, substitution=None):
        """
        __new__(cls: type)
        __new__(cls: type, source: NumberCultureSource, cultureOverride: CultureInfo, substitution: NumberSubstitutionMethod)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    CultureOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value which identifies which culture to use when the value of the System.Windows.Media.NumberSubstitution.CultureSource property is set to System.Windows.Media.NumberCultureSource.Override.

Get: CultureOverride(self: NumberSubstitution) -> CultureInfo

Set: CultureOverride(self: NumberSubstitution) = value
"""

    CultureSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value which identifies the source of the culture value that is used to determine number substitution.

Get: CultureSource(self: NumberSubstitution) -> NumberCultureSource

Set: CultureSource(self: NumberSubstitution) = value
"""

    Substitution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value which identifies the substitution method that is used to determine number substitution.

Get: Substitution(self: NumberSubstitution) -> NumberSubstitutionMethod

Set: Substitution(self: NumberSubstitution) = value
"""


    CultureOverrideProperty = None
    CultureSourceProperty = None
    SubstitutionProperty = None

