class DragDrop(object):
    """ Provides helper methods and fields for initiating drag-and-drop operations, including a method to begin a drag-and-drop operation, and facilities for adding and removing drag-and-drop related event handlers. """
    @staticmethod
    def AddDragEnterHandler(element, handler):
        """
        AddDragEnterHandler(element: DependencyObject, handler: DragEventHandler)
            Adds a System.Windows.UIElement.DragEnter event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def AddDragLeaveHandler(element, handler):
        """
        AddDragLeaveHandler(element: DependencyObject, handler: DragEventHandler)
            Adds a System.Windows.UIElement.DragLeave event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def AddDragOverHandler(element, handler):
        """
        AddDragOverHandler(element: DependencyObject, handler: DragEventHandler)
            Adds a System.Windows.UIElement.DragOver event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def AddDropHandler(element, handler):
        """
        AddDropHandler(element: DependencyObject, handler: DragEventHandler)
            Adds a System.Windows.UIElement.Drop event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def AddGiveFeedbackHandler(element, handler):
        """
        AddGiveFeedbackHandler(element: DependencyObject, handler: GiveFeedbackEventHandler)
            Adds a System.Windows.UIElement.GiveFeedback event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def AddPreviewDragEnterHandler(element, handler):
        """
        AddPreviewDragEnterHandler(element: DependencyObject, handler: DragEventHandler)
            Adds a System.Windows.UIElement.PreviewDragEnter event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def AddPreviewDragLeaveHandler(element, handler):
        """
        AddPreviewDragLeaveHandler(element: DependencyObject, handler: DragEventHandler)
            Adds a System.Windows.UIElement.PreviewDragLeave event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def AddPreviewDragOverHandler(element, handler):
        """
        AddPreviewDragOverHandler(element: DependencyObject, handler: DragEventHandler)
            Adds a System.Windows.UIElement.PreviewDragOver event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def AddPreviewDropHandler(element, handler):
        """
        AddPreviewDropHandler(element: DependencyObject, handler: DragEventHandler)
            Adds a System.Windows.UIElement.PreviewDrop event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def AddPreviewGiveFeedbackHandler(element, handler):
        """
        AddPreviewGiveFeedbackHandler(element: DependencyObject, handler: GiveFeedbackEventHandler)
            Adds a System.Windows.UIElement.PreviewGiveFeedback event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def AddPreviewQueryContinueDragHandler(element, handler):
        """
        AddPreviewQueryContinueDragHandler(element: DependencyObject, handler: QueryContinueDragEventHandler)
            Adds a System.Windows.UIElement.PreviewQueryContinueDrag event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def AddQueryContinueDragHandler(element, handler):
        """
        AddQueryContinueDragHandler(element: DependencyObject, handler: QueryContinueDragEventHandler)
            Adds a System.Windows.UIElement.QueryContinueDrag event handler to a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) to which to add the event handler.
            handler: A delegate that references the handler method to be added.
        """
        pass

    @staticmethod
    def DoDragDrop(dragSource, data, allowedEffects):
        """
        DoDragDrop(dragSource: DependencyObject, data: object, allowedEffects: DragDropEffects) -> DragDropEffects
        
            Initiates a drag-and-drop operation.
        
            dragSource: A reference to the dependency object that is the source of the data being dragged.
            data: A data object that contains the data being dragged.
            allowedEffects: One of the System.Windows.DragDropEffects values that specifies permitted effects of the drag-and-drop operation.
            Returns: One of the System.Windows.DragDropEffects values that specifies the final effect that was performed during the drag-and-drop operation.
        """
        pass

    @staticmethod
    def RemoveDragEnterHandler(element, handler):
        """
        RemoveDragEnterHandler(element: DependencyObject, handler: DragEventHandler)
            Removes a System.Windows.UIElement.DragEnter event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    @staticmethod
    def RemoveDragLeaveHandler(element, handler):
        """
        RemoveDragLeaveHandler(element: DependencyObject, handler: DragEventHandler)
            Removes a System.Windows.UIElement.DragLeave event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    @staticmethod
    def RemoveDragOverHandler(element, handler):
        """
        RemoveDragOverHandler(element: DependencyObject, handler: DragEventHandler)
            Removes a System.Windows.UIElement.DragOver event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    @staticmethod
    def RemoveDropHandler(element, handler):
        """
        RemoveDropHandler(element: DependencyObject, handler: DragEventHandler)
            Removes a System.Windows.UIElement.Drop event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    @staticmethod
    def RemoveGiveFeedbackHandler(element, handler):
        """
        RemoveGiveFeedbackHandler(element: DependencyObject, handler: GiveFeedbackEventHandler)
            Removes a System.Windows.UIElement.GiveFeedback event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    @staticmethod
    def RemovePreviewDragEnterHandler(element, handler):
        """
        RemovePreviewDragEnterHandler(element: DependencyObject, handler: DragEventHandler)
            Removes a System.Windows.UIElement.PreviewDragEnter event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    @staticmethod
    def RemovePreviewDragLeaveHandler(element, handler):
        """
        RemovePreviewDragLeaveHandler(element: DependencyObject, handler: DragEventHandler)
            Removes a System.Windows.UIElement.PreviewDragLeave event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    @staticmethod
    def RemovePreviewDragOverHandler(element, handler):
        """
        RemovePreviewDragOverHandler(element: DependencyObject, handler: DragEventHandler)
            Removes a System.Windows.UIElement.PreviewDragOver event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    @staticmethod
    def RemovePreviewDropHandler(element, handler):
        """
        RemovePreviewDropHandler(element: DependencyObject, handler: DragEventHandler)
            Removes a System.Windows.UIElement.PreviewDrop event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    @staticmethod
    def RemovePreviewGiveFeedbackHandler(element, handler):
        """
        RemovePreviewGiveFeedbackHandler(element: DependencyObject, handler: GiveFeedbackEventHandler)
            Removes a System.Windows.UIElement.PreviewGiveFeedback event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    @staticmethod
    def RemovePreviewQueryContinueDragHandler(element, handler):
        """
        RemovePreviewQueryContinueDragHandler(element: DependencyObject, handler: QueryContinueDragEventHandler)
            Removes a System.Windows.UIElement.PreviewQueryContinueDrag event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    @staticmethod
    def RemoveQueryContinueDragHandler(element, handler):
        """
        RemoveQueryContinueDragHandler(element: DependencyObject, handler: QueryContinueDragEventHandler)
            Removes a System.Windows.UIElement.QueryContinueDrag event handler from a specified dependency object.
        
            element: The dependency object (a System.Windows.UIElement or System.Windows.ContentElement) from which to remove the event handler.
            handler: A delegate that references the handler method to be removed
        """
        pass

    DragEnterEvent = None
    DragLeaveEvent = None
    DragOverEvent = None
    DropEvent = None
    GiveFeedbackEvent = None
    PreviewDragEnterEvent = None
    PreviewDragLeaveEvent = None
    PreviewDragOverEvent = None
    PreviewDropEvent = None
    PreviewGiveFeedbackEvent = None
    PreviewQueryContinueDragEvent = None
    QueryContinueDragEvent = None
    __all__ = [
        'AddDragEnterHandler',
        'AddDragLeaveHandler',
        'AddDragOverHandler',
        'AddDropHandler',
        'AddGiveFeedbackHandler',
        'AddPreviewDragEnterHandler',
        'AddPreviewDragLeaveHandler',
        'AddPreviewDragOverHandler',
        'AddPreviewDropHandler',
        'AddPreviewGiveFeedbackHandler',
        'AddPreviewQueryContinueDragHandler',
        'AddQueryContinueDragHandler',
        'DoDragDrop',
        'DragEnterEvent',
        'DragLeaveEvent',
        'DragOverEvent',
        'DropEvent',
        'GiveFeedbackEvent',
        'PreviewDragEnterEvent',
        'PreviewDragLeaveEvent',
        'PreviewDragOverEvent',
        'PreviewDropEvent',
        'PreviewGiveFeedbackEvent',
        'PreviewQueryContinueDragEvent',
        'QueryContinueDragEvent',
        'RemoveDragEnterHandler',
        'RemoveDragLeaveHandler',
        'RemoveDragOverHandler',
        'RemoveDropHandler',
        'RemoveGiveFeedbackHandler',
        'RemovePreviewDragEnterHandler',
        'RemovePreviewDragLeaveHandler',
        'RemovePreviewDragOverHandler',
        'RemovePreviewDropHandler',
        'RemovePreviewGiveFeedbackHandler',
        'RemovePreviewQueryContinueDragHandler',
        'RemoveQueryContinueDragHandler',
    ]

