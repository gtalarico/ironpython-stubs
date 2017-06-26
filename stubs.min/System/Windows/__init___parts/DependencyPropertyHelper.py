class DependencyPropertyHelper(object):
    """ Provides a single helper method (System.Windows.DependencyPropertyHelper.GetValueSource(System.Windows.DependencyObject,System.Windows.DependencyProperty)) that reports the property system source for the effective value of a dependency property. """
    @staticmethod
    def GetValueSource(dependencyObject, dependencyProperty):
        """
        GetValueSource(dependencyObject: DependencyObject, dependencyProperty: DependencyProperty) -> ValueSource
        
            Returns a structure that reports various metadata and property system characteristics of a specified dependency property on a particular System.Windows.DependencyObject.
        
            dependencyObject: The element that contains the dependencyProperty to report information for.
            dependencyProperty: The identifier for the dependency property to report information for.
            Returns: A System.Windows.ValueSource structure that reports the specific information.
        """
        pass

    __all__ = [
        'GetValueSource',
    ]

