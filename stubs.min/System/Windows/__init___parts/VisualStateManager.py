class VisualStateManager(DependencyObject):
    """
    Manages states and the logic for transitioning between states for controls.
    
    VisualStateManager()
    """
    @staticmethod
    def GetCustomVisualStateManager(obj):
        """
        GetCustomVisualStateManager(obj: FrameworkElement) -> VisualStateManager
        
            Gets the System.Windows.VisualStateManager.CustomVisualStateManager attached property.
        
            obj: The element to get the System.Windows.VisualStateManager.CustomVisualStateManager attached property from.
            Returns: The visual state manager that transitions between the states of a control.
        """
        pass

    @staticmethod
    def GetVisualStateGroups(obj):
        """
        GetVisualStateGroups(obj: FrameworkElement) -> IList
        
            Gets the System.Windows.VisualStateManager.VisualStateGroups attached property.
        
            obj: The element to get the System.Windows.VisualStateManager.VisualStateGroups attached property from.
            Returns: The collection of System.Windows.VisualStateGroup objects that is associated with the specified object.
        """
        pass

    @staticmethod
    def GoToElementState(stateGroupsRoot, stateName, useTransitions):
        """
        GoToElementState(stateGroupsRoot: FrameworkElement, stateName: str, useTransitions: bool) -> bool
        
            Transitions the element between two states. Use this method to transition states that are defined by an application, rather than defined by a control.
        
            stateGroupsRoot: The root element that contains the System.Windows.VisualStateManager.
            stateName: The state to transition to.
            useTransitions: true to use a System.Windows.VisualTransition object to transition between states; otherwise, false.
            Returns: true if the control successfully transitioned to the new state; otherwise, false.
        """
        pass

    @staticmethod
    def GoToState(control, stateName, useTransitions):
        """
        GoToState(control: FrameworkElement, stateName: str, useTransitions: bool) -> bool
        
            Transitions the control between two states. Use this method to transition states on control that has a System.Windows.Controls.ControlTemplate.
        
            control: The control to transition between states.
            stateName: The state to transition to.
            useTransitions: true to use a System.Windows.VisualTransition object to transition between states; otherwise, false.
            Returns: true if the control successfully transitioned to the new state; otherwise, false.
        """
        pass

    def GoToStateCore(self, *args): #cannot find CLR method
        """
        GoToStateCore(self: VisualStateManager, control: FrameworkElement, stateGroupsRoot: FrameworkElement, stateName: str, group: VisualStateGroup, state: VisualState, useTransitions: bool) -> bool
        
            Transitions a control between states.
        
            control: The control to transition between states.
            stateGroupsRoot: The root element that contains the System.Windows.VisualStateManager.
            stateName: The name of the state to transition to.
            group: The System.Windows.VisualStateGroup that the state belongs to.
            state: The representation of the state to transition to.
            useTransitions: true to use a System.Windows.VisualTransition object to transition between states; otherwise, false.
            Returns: true if the control successfully transitioned to the new state; otherwise, false.
        """
        pass

    def RaiseCurrentStateChanged(self, *args): #cannot find CLR method
        """
        RaiseCurrentStateChanged(self: VisualStateManager, stateGroup: VisualStateGroup, oldState: VisualState, newState: VisualState, control: FrameworkElement, stateGroupsRoot: FrameworkElement)
            Raises the System.Windows.VisualStateGroup.CurrentStateChanging event on the specified System.Windows.VisualStateGroup object.
        
            stateGroup: The object that the System.Windows.VisualStateGroup.CurrentStateChanging event occurred on.
            oldState: The state that the control is transitioning from.
            newState: The state that the control is transitioning to.
            control: The control that is transitioning states.
            stateGroupsRoot: The root element that contains the System.Windows.VisualStateManager.
        """
        pass

    def RaiseCurrentStateChanging(self, *args): #cannot find CLR method
        """
        RaiseCurrentStateChanging(self: VisualStateManager, stateGroup: VisualStateGroup, oldState: VisualState, newState: VisualState, control: FrameworkElement, stateGroupsRoot: FrameworkElement)
            Raises the System.Windows.VisualStateGroup.CurrentStateChanging event on the specified System.Windows.VisualStateGroup object.
        
            stateGroup: The object that the System.Windows.VisualStateGroup.CurrentStateChanging event occurred on.
            oldState: The state that the control is transitioning from.
            newState: The state that the control is transitioning to.
            control: The control that is transitioning states.
            stateGroupsRoot: The root element that contains the System.Windows.VisualStateManager.
        """
        pass

    @staticmethod
    def SetCustomVisualStateManager(obj, value):
        """
        SetCustomVisualStateManager(obj: FrameworkElement, value: VisualStateManager)
            Sets the System.Windows.VisualStateManager.CustomVisualStateManager attached property.
        
            obj: The object to set the property on.
            value: The visual state manager that transitions between the states of a control.
        """
        pass

    CustomVisualStateManagerProperty = None
    VisualStateGroupsProperty = None

