# encoding: utf-8
# module System.Windows.Navigation calls itself Navigation
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BaseUriHelper(object):
    """ Provides a method to resolve relative uniform resource identifiers (URIs) with respect to the base URI of a container, such as a System.Windows.Controls.Frame. """
    @staticmethod
    def GetBaseUri(element):
        """
        GetBaseUri(element: DependencyObject) -> Uri
        
            Gets the value of the BaseUri�attached property for a specified System.Windows.UIElement.
        
            element: The element from which the property value is read.
            Returns: The base URI of a given element.
        """
        pass

    BaseUriProperty = None
    __all__ = [
        'BaseUriProperty',
        'GetBaseUri',
    ]


