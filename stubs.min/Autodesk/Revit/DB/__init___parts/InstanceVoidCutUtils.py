class InstanceVoidCutUtils(object):
    """ Utilities for cutting elements by unattached voids in family instances. """
    @staticmethod
    def AddInstanceVoidCut(document, element, cuttingInstance):
        """
        AddInstanceVoidCut(document: Document, element: Element, cuttingInstance: Element)
            Add a cut to an element using the unattached voids inside a cutting instance.
        
            document: The document containing the two elements
            element: The element to be cut
            cuttingInstance: The cutting family instance
        """
        pass

    @staticmethod
    def CanBeCutWithVoid(element):
        """
        CanBeCutWithVoid(element: Element) -> bool
        
            Indicates if the element can be cut by an instance with unattached voids.
        
            element: The element to be cut
            Returns: Returns true if the element can be cut by an instance with unattached voids.
        """
        pass

    @staticmethod
    def GetCuttingVoidInstances(element):
        """
        GetCuttingVoidInstances(element: Element) -> ICollection[ElementId]
        
            Return ids of the instances with unattached voids cutting the element.
        
            element: The element being cut
            Returns: Ids of instances with unattached voids that cut this element
        """
        pass

    @staticmethod
    def GetElementsBeingCut(cuttingInstance):
        """
        GetElementsBeingCut(cuttingInstance: Element) -> ICollection[ElementId]
        
            Return ids of the elements being cut by the instance
        
            cuttingInstance: The cutting family instance
            Returns: Ids of elements being cut by cuttingInstance
        """
        pass

    @staticmethod
    def InstanceVoidCutExists(element, cuttingInstance):
        """
        InstanceVoidCutExists(element: Element, cuttingInstance: Element) -> bool
        
            Check whether the instance is cutting the element
        
            element: The element being cut
            cuttingInstance: The cutting family instance
            Returns: Returns true if the instance is cutting the element.
        """
        pass

    @staticmethod
    def IsVoidInstanceCuttingElement(element):
        """
        IsVoidInstanceCuttingElement(element: Element) -> bool
        
            Indicates if the element is a family instance with unattached voids that can 
             cut other elements.
        
        
            element: The cutting family instance
            Returns: Returns true if the element is a family instance with unattached voids that can 
             cut other elements.
        """
        pass

    @staticmethod
    def RemoveInstanceVoidCut(document, element, cuttingInstance):
        """
        RemoveInstanceVoidCut(document: Document, element: Element, cuttingInstance: Element)
            Remove a cut applied to the element by a cutting instance with unattached voids.
        
            document: The document containing the two elements
            element: The element being cut
            cuttingInstance: The cutting family instance
        """
        pass

    __all__ = [
        'AddInstanceVoidCut',
        'CanBeCutWithVoid',
        'GetCuttingVoidInstances',
        'GetElementsBeingCut',
        'InstanceVoidCutExists',
        'IsVoidInstanceCuttingElement',
        'RemoveInstanceVoidCut',
    ]

