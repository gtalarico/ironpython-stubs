class Storyboard(ParallelTimeline, ISealable, IAnimatable, IResource, IAddChild):
    """
    A container timeline that provides object and property targeting information for its child animations.
    
    Storyboard()
    """
    def AddChild(self, *args): #cannot find CLR method
        """
        AddChild(self: TimelineGroup, child: object)
            Adds a child System.Windows.Media.Animation.Timeline to this System.Windows.Media.Animation.TimelineGroup.
        
            child: The object to be added as the child of this System.Windows.Media.Animation.TimelineGroup. If this object is a System.Windows.Media.Animation.Timeline it will be added to the 
             System.Windows.Media.Animation.TimelineGroup.Children collection; otherwise, an exception will be thrown.
        """
        pass

    def AddText(self, *args): #cannot find CLR method
        """
        AddText(self: TimelineGroup, childText: str)
            Adds a text string as a child of this System.Windows.Media.Animation.Timeline.
        
            childText: The text added to the System.Windows.Media.Animation.Timeline.
        """
        pass

    def AllocateClock(self, *args): #cannot find CLR method
        """
        AllocateClock(self: TimelineGroup) -> Clock
        
            Creates a type-specific clock for this timeline.
            Returns: A clock for this timeline.
        """
        pass

    def Begin(self, containingObject=None, *__args):
        """
        Begin(self: Storyboard, containingObject: FrameworkContentElement, handoffBehavior: HandoffBehavior)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets and initiates them, using the specified System.Windows.Media.Animation.HandoffBehavior.
        
            containingObject: An object contained within the same name scope as the targets of this storyboard's animations. Animations without a System.Windows.Media.Animation.Storyboard.TargetName are applied to containingObject.
            handoffBehavior: The behavior the new animation should use to interact with any current animations.
        Begin(self: Storyboard, containingObject: FrameworkContentElement)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets and initiates them.
        
            containingObject: An object contained within the same name scope as the targets of this storyboard's animations. Animations without a System.Windows.Media.Animation.Storyboard.TargetName are applied to containingObject.
        Begin(self: Storyboard, containingObject: FrameworkElement, frameworkTemplate: FrameworkTemplate, handoffBehavior: HandoffBehavior, isControllable: bool)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets within the specified template and initiates them.
        
            containingObject: The object to which the specified frameworkTemplate has been applied. Animations without a System.Windows.Media.Animation.Storyboard.TargetName are applied to containingObject.
            frameworkTemplate: The template to animate.
            handoffBehavior: The behavior the new animation should use to interact with any current animations.
            isControllable: true if the storyboard should be interactively controllable; otherwise, false.
        Begin(self: Storyboard)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets and initiates them.
        Begin(self: Storyboard, containingObject: FrameworkContentElement, handoffBehavior: HandoffBehavior, isControllable: bool)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets and initiates them, using the specified System.Windows.Media.Animation.HandoffBehavior.
        
            containingObject: An object contained within the same name scope as the targets of this storyboard's animations. Animations without a specified System.Windows.Media.Animation.Storyboard.TargetName are applied to 
             containingObject.
        
            handoffBehavior: The behavior the new animation should use to interact with any current animations.
            isControllable: Declares whether the animation is controllable (can be paused) once started.
        Begin(self: Storyboard, containingObject: FrameworkContentElement, isControllable: bool)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets and initiates them.
        
            containingObject: An object contained within the same name scope as the targets of this storyboard's animations. Animations without a System.Windows.Media.Animation.Storyboard.TargetName are applied to containingObject.
            isControllable: true if the storyboard should be interactively controllable; otherwise, false.
        Begin(self: Storyboard, containingObject: FrameworkElement, frameworkTemplate: FrameworkTemplate, isControllable: bool)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets within the specified template and initiates them.
        
            containingObject: The object to which the specified frameworkTemplate has been applied.  Animations without a System.Windows.Media.Animation.Storyboard.TargetName are applied to containingObject.
            frameworkTemplate: The template to animate.
            isControllable: true if the storyboard should be interactively controllable; otherwise, false.
        Begin(self: Storyboard, containingObject: FrameworkElement, isControllable: bool)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets and initiates them.
        
            containingObject: An object contained within the same name scope as the targets of this storyboard's animations. Animations without a System.Windows.Media.Animation.Storyboard.TargetName are applied to containingObject.
            isControllable: true if the storyboard should be interactively controllable; otherwise, false.
        Begin(self: Storyboard, containingObject: FrameworkElement, handoffBehavior: HandoffBehavior)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets and initiates them, using the specified System.Windows.Media.Animation.HandoffBehavior.
        
            containingObject: An object contained within the same name scope as the targets of this storyboard's animations. Animations without a specified System.Windows.Media.Animation.Storyboard.TargetName are applied to 
             containingObject.
        
            handoffBehavior: The behavior the new animation should use to interact with any current animations.
        Begin(self: Storyboard, containingObject: FrameworkElement)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets and initiates them.
        
            containingObject: An object contained within the same name scope as the targets of this storyboard's animations. Animations without a System.Windows.Media.Animation.Storyboard.TargetName are applied to containingObject.
        Begin(self: Storyboard, containingObject: FrameworkElement, frameworkTemplate: FrameworkTemplate, handoffBehavior: HandoffBehavior)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets within the specified template and initiates them.
        
            containingObject: The object to which the specified frameworkTemplate has been applied. Animations without a System.Windows.Media.Animation.Storyboard.TargetName are applied to containingObject.
            frameworkTemplate: The template to animate.
            handoffBehavior: The behavior the new animation should use to interact with any current animations.
        Begin(self: Storyboard, containingObject: FrameworkElement, frameworkTemplate: FrameworkTemplate)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets within the specified template and initiates them.
        
            containingObject: The object to which the specified frameworkTemplate has been applied. Animations without a System.Windows.Media.Animation.Storyboard.TargetName are applied to containingObject.
            frameworkTemplate: The template to animate.
        Begin(self: Storyboard, containingObject: FrameworkElement, handoffBehavior: HandoffBehavior, isControllable: bool)
            Applies the animations associated with this System.Windows.Media.Animation.Storyboard to their targets and initiates them.
        
            containingObject: An object contained within the same name scope as the targets of this storyboard's animations. Animations without a specified System.Windows.Media.Animation.Storyboard.TargetName are applied to 
             containingObject.
        
            handoffBehavior: The behavior the new animation should use to interact with any current animations.
            isControllable: Declares whether the animation is controllable (can be paused) once started.
        """
        pass

    def Clone(self):
        """
        Clone(self: Storyboard) -> Storyboard
        
            Creates a modifiable clone of this System.Windows.Media.Animation.Storyboard, making deep copies of this object's values. When copying dependency properties, this method copies resource references and data 
             bindings (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property is false even if the source's System.Windows.Freezable.IsFrozen property is true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base (non-animated) property values.
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable using current property values.
        
            sourceFreezable: The System.Windows.Freezable to be cloned.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """
        CreateInstanceCore(self: Storyboard) -> Freezable
        
            Creates a new instance of the System.Windows.Media.Animation.Storyboard class.
            Returns: A new System.Windows.Media.Animation.Storyboard instance.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Timeline, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Timeline unmodifiable or determines whether it can be made unmodifiable.
        
            isChecking: true to check if this instance can be frozen; false to freeze this instance.
            Returns: If isChecking is true, this method returns true if this instance can be made read-only, or false if it cannot be made read-only. If isChecking is false, this method returns true if this instance is now 
             read-only, or false if it cannot be made read-only, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Timeline, sourceFreezable: Freezable)
            Makes this instance a clone of the specified System.Windows.Media.Animation.Timeline object.
        
            sourceFreezable: The System.Windows.Media.Animation.Timeline instance to clone.
        """
        pass

    def GetCurrentGlobalSpeed(self, containingObject=None):
        """
        GetCurrentGlobalSpeed(self: Storyboard) -> float
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentGlobalSpeed of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
            Returns: The current global speed, or 0 if the clock is stopped.
        GetCurrentGlobalSpeed(self: Storyboard, containingObject: FrameworkContentElement) -> Nullable[float]
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentGlobalSpeed of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: The current global speed, or null if the clock is stopped.
        GetCurrentGlobalSpeed(self: Storyboard, containingObject: FrameworkElement) -> Nullable[float]
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentGlobalSpeed of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: The current global speed, or null if the clock is stopped.
        """
        pass

    def GetCurrentIteration(self, containingObject=None):
        """
        GetCurrentIteration(self: Storyboard) -> int
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentIteration of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
            Returns: This clock's current iteration within its current active period, or null if this clock is stopped.
        GetCurrentIteration(self: Storyboard, containingObject: FrameworkContentElement) -> Nullable[int]
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentIteration of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: This clock's current iteration within its current active period, or null if this clock is stopped.
        GetCurrentIteration(self: Storyboard, containingObject: FrameworkElement) -> Nullable[int]
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentIteration of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: This clock's current iteration within its current active period, or null if this clock is stopped.
        """
        pass

    def GetCurrentProgress(self, containingObject=None):
        """
        GetCurrentProgress(self: Storyboard) -> float
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentProgress of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
            Returns: null if this clock is System.Windows.Media.Animation.ClockState.Stopped, or 0.0 if this clock is active and its System.Windows.Media.Animation.Clock.Timeline has a 
             System.Windows.Media.Animation.Timeline.Duration of System.Windows.Duration.Forever; otherwise, a value between 0.0 and 1.0 that indicates the current progress of this clock within its current iteration. A 
             value of 0.0 indicates no progress, and a value of 1.0 indicates that the clock is at the end of its current iteration.
        
        GetCurrentProgress(self: Storyboard, containingObject: FrameworkContentElement) -> Nullable[float]
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentProgress of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: null if this clock is System.Windows.Media.Animation.ClockState.Stopped, or 0.0 if this clock is active and its System.Windows.Media.Animation.Clock.Timeline has a 
             System.Windows.Media.Animation.Timeline.Duration of System.Windows.Duration.Forever; otherwise, a value between 0.0 and 1.0 that indicates the current progress of this clock within its current iteration. A 
             value of 0.0 indicates no progress, and a value of 1.0 indicates that the clock is at the end of its current iteration.
        
        GetCurrentProgress(self: Storyboard, containingObject: FrameworkElement) -> Nullable[float]
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentProgress of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: null if this clock is System.Windows.Media.Animation.ClockState.Stopped, or 0.0 if this clock is active and its System.Windows.Media.Animation.Clock.Timeline has a 
             System.Windows.Media.Animation.Timeline.Duration of System.Windows.Duration.Forever; otherwise, a value between 0.0 and 1.0 that indicates the current progress of this clock within its current iteration. A 
             value of 0.0 indicates no progress, and a value of 1.0 indicates that the clock is at the end of its current iteration.
        """
        pass

    def GetCurrentState(self, containingObject=None):
        """
        GetCurrentState(self: Storyboard) -> ClockState
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentState of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
            Returns: The current state of the clock created for this storyboard: System.Windows.Media.Animation.ClockState.Active, System.Windows.Media.Animation.ClockState.Filling, or 
             System.Windows.Media.Animation.ClockState.Stopped.
        
        GetCurrentState(self: Storyboard, containingObject: FrameworkContentElement) -> ClockState
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentState of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: The current state of the clock created for this storyboard: System.Windows.Media.Animation.ClockState.Active, System.Windows.Media.Animation.ClockState.Filling, or 
             System.Windows.Media.Animation.ClockState.Stopped.
        
        GetCurrentState(self: Storyboard, containingObject: FrameworkElement) -> ClockState
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentState of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: The current state of the clock created for this storyboard: System.Windows.Media.Animation.ClockState.Active, System.Windows.Media.Animation.ClockState.Filling, or 
             System.Windows.Media.Animation.ClockState.Stopped.
        """
        pass

    def GetCurrentTime(self, containingObject=None):
        """
        GetCurrentTime(self: Storyboard) -> TimeSpan
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentTime of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
            Returns: null if this storyboard's clock is System.Windows.Media.Animation.ClockState.Stopped; otherwise, the current time of the storyboard's clock.
        GetCurrentTime(self: Storyboard, containingObject: FrameworkContentElement) -> Nullable[TimeSpan]
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentTime of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: null if this storyboard's clock is System.Windows.Media.Animation.ClockState.Stopped; otherwise, the current time of the storyboard's clock.
        GetCurrentTime(self: Storyboard, containingObject: FrameworkElement) -> Nullable[TimeSpan]
        
            Retrieves the System.Windows.Media.Animation.Clock.CurrentTime of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: null if this storyboard's clock is System.Windows.Media.Animation.ClockState.Stopped; otherwise, the current time of the storyboard's clock.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Timeline, sourceFreezable: Freezable)
            Makes this instance a frozen clone of the specified System.Windows.Media.Animation.Timeline. Resource references, data bindings, and animations are not copied, but their current values are.
        
            sourceFreezable: The System.Windows.Media.Animation.Timeline to copy and freeze.
        """
        pass

    def GetIsPaused(self, containingObject=None):
        """
        GetIsPaused(self: Storyboard) -> bool
        
            Retrieves a value that indicates whether the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard is paused.
            Returns: true if the System.Windows.Media.Animation.Clock created for this System.Windows.Media.Animation.Storyboard is paused; otherwise, false.
        GetIsPaused(self: Storyboard, containingObject: FrameworkContentElement) -> bool
        
            Retrieves a value that indicates whether the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard is paused.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: true if the System.Windows.Media.Animation.Clock created for this System.Windows.Media.Animation.Storyboard is paused; otherwise, false.
        GetIsPaused(self: Storyboard, containingObject: FrameworkElement) -> bool
        
            Retrieves a value that indicates whether the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard is paused.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            Returns: true if the System.Windows.Media.Animation.Clock created for this System.Windows.Media.Animation.Storyboard is paused; otherwise, false.
        """
        pass

    def GetNaturalDuration(self, *args): #cannot find CLR method
        """
        GetNaturalDuration(self: Timeline, clock: Clock) -> Duration
        
            Returns the length of a single iteration of this System.Windows.Media.Animation.Timeline.
        
            clock: The System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Timeline.
            Returns: The length of a single iteration of this System.Windows.Media.Animation.Timeline, or System.Windows.Duration.Automatic if the natural duration is unknown.
        """
        pass

    def GetNaturalDurationCore(self, *args): #cannot find CLR method
        """
        GetNaturalDurationCore(self: ParallelTimeline, clock: Clock) -> Duration
        
            Return the natural duration (duration of a single iteration) from a specified System.Windows.Media.Animation.Clock.
        
            clock: The System.Windows.Media.Animation.Clock to return the natural duration from.
            Returns: The System.Windows.Duration quantity representing the natural duration.
        """
        pass

    @staticmethod
    def GetTarget(element):
        """
        GetTarget(element: DependencyObject) -> DependencyObject
        
            Retrieves the System.Windows.Media.Animation.Storyboard.Target value of the specified System.Windows.Media.Animation.Timeline.
        
            element: The timeline from which to retrieve the System.Windows.Media.Animation.Storyboard.TargetName.
            Returns: The dependency object targeted by element.
        """
        pass

    @staticmethod
    def GetTargetName(element):
        """
        GetTargetName(element: DependencyObject) -> str
        
            Retrieves the System.Windows.Media.Animation.Storyboard.TargetName value of the specified System.Windows.Media.Animation.Timeline.
        
            element: The timeline from which to retrieve the System.Windows.Media.Animation.Storyboard.TargetName.
            Returns: The name of the dependency object targeted by element.
        """
        pass

    @staticmethod
    def GetTargetProperty(element):
        """
        GetTargetProperty(element: DependencyObject) -> PropertyPath
        
            Retrieves the System.Windows.Media.Animation.Storyboard.TargetProperty value of the specified System.Windows.Media.Animation.Timeline.
        
            element: The dependency object from which to get the System.Windows.Media.Animation.Storyboard.TargetProperty.
            Returns: The property targeted by element.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a System.Windows.DependencyObjectType data member that has just been set.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventArgs) to also invoke any 
             System.Windows.Freezable.Changed handlers in response to a changing dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def Pause(self, containingObject=None):
        """
        Pause(self: Storyboard)
            Pauses the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        Pause(self: Storyboard, containingObject: FrameworkContentElement)
            Pauses the System.Windows.Media.Animation.Clock of the specified System.Windows.FrameworkContentElement associated with this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
        Pause(self: Storyboard, containingObject: FrameworkElement)
            Pauses the System.Windows.Media.Animation.Clock of the specified System.Windows.FrameworkElement associated with this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of System.Windows.Freezable must call this method at the beginning of any API that reads data members that are 
             not dependency properties.
        """
        pass

    def Remove(self, containingObject=None):
        """
        Remove(self: Storyboard)
            Removes the System.Windows.Media.Animation.Clock objects that were created for this System.Windows.Media.Animation.Storyboard. Animations that belong to this System.Windows.Media.Animation.Storyboard no 
             longer affect the properties they once animated, regardless of their System.Windows.Media.Animation.Timeline.FillBehavior setting.
        
        Remove(self: Storyboard, containingObject: FrameworkContentElement)
            Removes the System.Windows.Media.Animation.Clock objects that were created for this System.Windows.Media.Animation.Storyboard. Animations that belong to this System.Windows.Media.Animation.Storyboard no 
             longer affect the properties they once animated, regardless of their System.Windows.Media.Animation.Timeline.FillBehavior setting.
        
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
        Remove(self: Storyboard, containingObject: FrameworkElement)
            Removes the System.Windows.Media.Animation.Clock objects that were created for this System.Windows.Media.Animation.Storyboard. Animations that belong to this System.Windows.Media.Animation.Storyboard no 
             longer affect the properties they once animated, regardless of their System.Windows.Media.Animation.Timeline.FillBehavior setting.
        
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        """
        pass

    def Resume(self, containingObject=None):
        """
        Resume(self: Storyboard)
            Resumes the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        Resume(self: Storyboard, containingObject: FrameworkContentElement)
            Resumes the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
        Resume(self: Storyboard, containingObject: FrameworkElement)
            Resumes the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        """
        pass

    def Seek(self, *__args):
        """
        Seek(self: Storyboard, offset: TimeSpan, origin: TimeSeekOrigin)
            Seeks this System.Windows.Media.Animation.Storyboard to the specified position. The System.Windows.Media.Animation.Storyboard performs the requested seek when the next clock tick occurs.
        
            offset: A positive or negative value that describes the amount by which the timeline should move forward or backward from the specified origin.
            origin: The position from which offset is applied.
        Seek(self: Storyboard, offset: TimeSpan)
            Seeks this System.Windows.Media.Animation.Storyboard to the specified position. The System.Windows.Media.Animation.Storyboard performs the requested seek when the next clock tick occurs.
        
            offset: A positive or negative value that describes the amount by which the timeline should move forward or backward.
        Seek(self: Storyboard, containingObject: FrameworkElement, offset: TimeSpan, origin: TimeSeekOrigin)
            Seeks this System.Windows.Media.Animation.Storyboard to the specified position. The System.Windows.Media.Animation.Storyboard performs the requested seek when the next clock tick occurs.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            offset: A positive or negative value that describes the amount by which the timeline should move forward or backward from the specified origin.
            origin: The position from which offset is applied.
        Seek(self: Storyboard, containingObject: FrameworkContentElement, offset: TimeSpan, origin: TimeSeekOrigin)
            Seeks this System.Windows.Media.Animation.Storyboard to the specified position. The System.Windows.Media.Animation.Storyboard performs the requested seek when the next clock tick occurs.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            offset: A positive or negative value that describes the amount by which the timeline should move forward or backward from the specified origin.
            origin: The position from which offset is applied.
        """
        pass

    def SeekAlignedToLastTick(self, *__args):
        """
        SeekAlignedToLastTick(self: Storyboard, offset: TimeSpan, origin: TimeSeekOrigin)
            Seeks this System.Windows.Media.Animation.Storyboard to a new position immediately (synchronously).
        
            offset: A positive or negative value that describes the amount by which the timeline should move forward or backward from the specified origin.
            origin: The position from which offset is applied.
        SeekAlignedToLastTick(self: Storyboard, offset: TimeSpan)
            Seeks this System.Windows.Media.Animation.Storyboard to a new position immediately (synchronously).
        
            offset: A positive or negative value that describes the amount by which the timeline should move forward or backward.
        SeekAlignedToLastTick(self: Storyboard, containingObject: FrameworkElement, offset: TimeSpan, origin: TimeSeekOrigin)
            Seeks this System.Windows.Media.Animation.Storyboard to a new position immediately (synchronously).
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            offset: A positive or negative value that describes the amount by which the timeline should move forward or backward from the specified origin.
            origin: The position from which offset is applied.
        SeekAlignedToLastTick(self: Storyboard, containingObject: FrameworkContentElement, offset: TimeSpan, origin: TimeSeekOrigin)
            Seeks this System.Windows.Media.Animation.Storyboard to a new position immediately (synchronously).
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            offset: A positive or negative value that describes the amount by which the timeline should move forward or backward from the specified origin.
            origin: The position from which offset is applied.
        """
        pass

    def SetSpeedRatio(self, *__args):
        """
        SetSpeedRatio(self: Storyboard, speedRatio: float)
            Sets the interactive speed ratio for the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            speedRatio: A finite value greater than zero that is the new interactive speed ratio of the storyboard. This value is multiplied against the storyboard's System.Windows.Media.Animation.Timeline.SpeedRatio value to 
             determine the storyboard's effective speed. This value does not overwrite the storyboard's System.Windows.Media.Animation.Timeline.SpeedRatio property. For example, calling this method and specifying an 
             interactive speed ratio of 3 on a storyboard with a System.Windows.Media.Animation.Timeline.SpeedRatio of 0.5 gives the storyboard an effective speed of 1.5.
        
        SetSpeedRatio(self: Storyboard, containingObject: FrameworkContentElement, speedRatio: float)
            Sets the interactive speed ratio of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            speedRatio: A finite value greater than zero that is the new interactive speed ratio of the storyboard. This value is multiplied against the storyboard's System.Windows.Media.Animation.Timeline.SpeedRatio value to 
             determine the storyboard's effective speed. This value does not overwrite the storyboard's System.Windows.Media.Animation.Timeline.SpeedRatio property. For example, calling this method and specifying an 
             interactive speed ratio of 3 on a storyboard with a System.Windows.Media.Animation.Timeline.SpeedRatio of 0.5 gives the storyboard an effective speed of 1.5.
        
        SetSpeedRatio(self: Storyboard, containingObject: FrameworkElement, speedRatio: float)
            Sets the interactive speed ratio of the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
            speedRatio: A finite value greater than zero that is the new interactive speed ratio of the storyboard. This value is multiplied against the storyboard's System.Windows.Media.Animation.Timeline.SpeedRatio value to 
             determine the storyboard's effective speed. This value does not overwrite the storyboard's System.Windows.Media.Animation.Timeline.SpeedRatio property. For example, calling this method and specifying an 
             interactive speed ratio of 3 on a storyboard with a System.Windows.Media.Animation.Timeline.SpeedRatio of 0.5 gives the storyboard an effective speed of 1.5.
        """
        pass

    @staticmethod
    def SetTarget(element, value):
        """
        SetTarget(element: DependencyObject, value: DependencyObject)
            Makes the specified System.Windows.Media.Animation.Timeline target the dependency object.
        
            element: The System.Windows.Media.Animation.Timeline that should target the specified dependency object.
            value: The dependency object to target.
        """
        pass

    @staticmethod
    def SetTargetName(element, name):
        """
        SetTargetName(element: DependencyObject, name: str)
            Makes the specified System.Windows.Media.Animation.Timeline target the dependency object with the specified name.
        
            element: The System.Windows.Media.Animation.Timeline that should target the specified dependency object.
            name: The name of the dependency object to target.
        """
        pass

    @staticmethod
    def SetTargetProperty(element, path):
        """
        SetTargetProperty(element: DependencyObject, path: PropertyPath)
            Makes the specified System.Windows.Media.Animation.Timeline target the specified dependency property.
        
            element: The System.Windows.Media.Animation.Timeline with which to associate the specified dependency property.
            path: A path that describe the dependency property to be animated.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for the provided dependency property.
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def SkipToFill(self, containingObject=None):
        """
        SkipToFill(self: Storyboard)
            Advances the current time of this storyboard's System.Windows.Media.Animation.Clock to the end of its active period.
        SkipToFill(self: Storyboard, containingObject: FrameworkContentElement)
            Advances the current time of this storyboard's System.Windows.Media.Animation.Clock to the end of its active period.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
        SkipToFill(self: Storyboard, containingObject: FrameworkElement)
            Advances the current time of this storyboard's System.Windows.Media.Animation.Clock to the end of its active period.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        """
        pass

    def Stop(self, containingObject=None):
        """
        Stop(self: Storyboard)
            Stops the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        Stop(self: Storyboard, containingObject: FrameworkContentElement)
            Stops the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkContentElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        
        Stop(self: Storyboard, containingObject: FrameworkElement)
            Stops the System.Windows.Media.Animation.Clock that was created for this System.Windows.Media.Animation.Storyboard.
        
            containingObject: The object specified when the System.Windows.Media.Animation.Storyboard.Begin(System.Windows.FrameworkElement,System.Boolean) method was called. This object contains the 
             System.Windows.Media.Animation.Clock objects that were created for this storyboard and its children.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable should call 
             this method at the end of any API that modifies class members that are not stored as dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a valid threading context. System.Windows.Freezable inheritors should call this method at the beginning of any 
             API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    TargetNameProperty = None
    TargetProperty = None
    TargetPropertyProperty = None

