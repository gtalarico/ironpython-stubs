class DesignerProperties(object):
    """ Provides attached properties used to communicate with a designer. """
    @staticmethod
    def GetIsInDesignMode(element):
        """
        GetIsInDesignMode(element: DependencyObject) -> bool
        
            Gets the value of the System.ComponentModel.DesignerProperties.IsInDesignMode�attached property for the specified System.Windows.UIElement.
        
            element: The element from which the property value is read.
            Returns: The System.ComponentModel.DesignerProperties.IsInDesignMode property value for the element.
        """
        pass

    @staticmethod
    def SetIsInDesignMode(element, value):
        """
        SetIsInDesignMode(element: DependencyObject, value: bool)
            Sets the value of the System.ComponentModel.DesignerProperties.IsInDesignMode�attached property to a specified element.
        
            element: The element to which the attached property is written.
            value: The needed System.Boolean value.
        """
        pass

    IsInDesignModeProperty = None
    __all__ = [
        'GetIsInDesignMode',
        'IsInDesignModeProperty',
        'SetIsInDesignMode',
    ]

