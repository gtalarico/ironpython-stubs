# encoding: utf-8
# module System.Windows.Media.Effects calls itself Effects
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BitmapEffect(Animatable, ISealable, IAnimatable, IResource):
    """ Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Defines a bitmap effect. Derived classes define effects that can be applied to a System.Windows.Media.Visual object, such as a System.Windows.Controls.Button or an System.Windows.Controls.Image. """
    def Clone(self):
        """
        Clone(self: BitmapEffect) -> BitmapEffect
        
            Creates a modifiable clone of this System.Windows.Media.Effects.BitmapEffect, making deep copies 
             of this object's values. When copying dependency properties, this method copies resource 
             references and data bindings (but they might no longer resolve) but not animations or their 
             current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: BitmapEffect) -> BitmapEffect
        
            Creates a modifiable clone of this System.Windows.Media.Effects.BitmapEffect object, making deep 
             copies of this object's current values. Resource references, data bindings, and animations are 
             not copied, but their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
            sourceFreezable: The System.Windows.Freezable to be cloned.
        """
        pass

    def CreateBitmapEffectOuter(self, *args): #cannot find CLR method
        """
        CreateBitmapEffectOuter() -> SafeHandle
        
            Creates a handle to an IMILBitmapEffect object that is used to initialize a custom effect.
            Returns: A handle to an IMILBitmapEffect object.
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
        CreateInstanceCore(self: Freezable) -> Freezable
        
            When implemented in a derived class, creates a new instance of the System.Windows.Freezable 
             derived class.
        
            Returns: The new instance.
        """
        pass

    def CreateUnmanagedEffect(self, *args): #cannot find CLR method
        """
        CreateUnmanagedEffect(self: BitmapEffect) -> SafeHandle
        
            When overridden in a derived class, creates a clone of the unmanaged effect.
            Returns: A handle to the unmanaged effect clone.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
        """
        pass

    def GetOutput(self, input):
        """
        GetOutput(self: BitmapEffect, input: BitmapEffectInput) -> BitmapSource
        
            Returns the System.Windows.Media.Imaging.BitmapSource that results when the effect is applied to 
             the specified System.Windows.Media.Effects.BitmapEffectInput.
        
        
            input: The input to apply the effect to.
            Returns: The System.Windows.Media.Imaging.BitmapSource with the effect applied to the input.
        """
        pass

    def InitializeBitmapEffect(self, *args): #cannot find CLR method
        """
        InitializeBitmapEffect(outerObject: SafeHandle, innerObject: SafeHandle)
            Initializes an IMILBitmapEffect handle obtained from 
             System.Windows.Media.Effects.BitmapEffect.CreateBitmapEffectOuter with the given 
             IMILBitmapEffectPrimitive.
        
        
            outerObject: The outer IMILBitmapEffect wrapper to initialize.
            innerObject: The inner IMILBitmapEffectPrimitive.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def SetValue(self, *__args):
        """
        SetValue(effect: SafeHandle, propertyName: str, value: object)
            Sets the specified property to the given value.
        
            effect: The handle to the effect that contains the property to change.
            propertyName: The name of the property to change.
            value: The value to use to set the property.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def UpdateUnmanagedPropertyState(self, *args): #cannot find CLR method
        """
        UpdateUnmanagedPropertyState(self: BitmapEffect, unmanagedEffect: SafeHandle)
            When overridden in a derived class, updates the property states of the unmanaged properties of 
             the effect.
        
        
            unmanagedEffect: The handle to the effect that contains the properties to update.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class BevelBitmapEffect(BitmapEffect, ISealable, IAnimatable, IResource):
    """
    Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Creates a bevel which raises the surface of the image according to a specified curve.
    
    BevelBitmapEffect()
    """
    def Clone(self):
        """
        Clone(self: BevelBitmapEffect) -> BevelBitmapEffect
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.BevelBitmapEffect, making deep copies of this object's values. When 
             copying dependency properties, this method copies resource references and data bindings (but 
             they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: BevelBitmapEffect) -> BevelBitmapEffect
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.BevelBitmapEffect object, making deep copies of this object's 
             current values. Resource references, data bindings, and animations are not copied, but their 
             current values are
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
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
        """ CreateInstanceCore(self: BevelBitmapEffect) -> Freezable """
        pass

    def CreateUnmanagedEffect(self, *args): #cannot find CLR method
        """ CreateUnmanagedEffect(self: BevelBitmapEffect) -> SafeHandle """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def UpdateUnmanagedPropertyState(self, *args): #cannot find CLR method
        """ UpdateUnmanagedPropertyState(self: BevelBitmapEffect, unmanagedEffect: SafeHandle) """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BevelWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets or sets the width of the bevel.

Get: BevelWidth(self: BevelBitmapEffect) -> float

Set: BevelWidth(self: BevelBitmapEffect) = value
"""

    EdgeProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets or sets the curve of the bevel.

Get: EdgeProfile(self: BevelBitmapEffect) -> EdgeProfile

Set: EdgeProfile(self: BevelBitmapEffect) = value
"""

    LightAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets or sets the direction the "virtual light" is coming from that creates the shadows of the bevel.

Get: LightAngle(self: BevelBitmapEffect) -> float

Set: LightAngle(self: BevelBitmapEffect) = value
"""

    Relief = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets or sets the height of the relief of the bevel.

Get: Relief(self: BevelBitmapEffect) -> float

Set: Relief(self: BevelBitmapEffect) = value
"""

    Smoothness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets or sets how smooth the shadows of the bevel are.

Get: Smoothness(self: BevelBitmapEffect) -> float

Set: Smoothness(self: BevelBitmapEffect) = value
"""


    BevelWidthProperty = None
    EdgeProfileProperty = None
    LightAngleProperty = None
    ReliefProperty = None
    SmoothnessProperty = None


class BitmapEffectCollection(Animatable, ISealable, IAnimatable, IResource, IList, ICollection, IEnumerable, IList[BitmapEffect], ICollection[BitmapEffect], IEnumerable[BitmapEffect]):
    """
    Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Represents a collection of System.Windows.Media.Effects.BitmapEffect objects. This collection is used as part of a System.Windows.Media.Effects.BitmapEffectGroup to apply multiple bitmap effects to visual content.
    
    BitmapEffectCollection()
    BitmapEffectCollection(capacity: int)
    BitmapEffectCollection(collection: IEnumerable[BitmapEffect])
    """
    def Add(self, value):
        """
        Add(self: BitmapEffectCollection, value: BitmapEffect)
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Adds a System.Windows.Media.Effects.BitmapEffect at the end 
             of the collection.
        
        
            value: The System.Windows.Media.Effects.BitmapEffect to add to the end of the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: BitmapEffectCollection)
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Removes all effects from the collection.
        """
        pass

    def Clone(self):
        """
        Clone(self: BitmapEffectCollection) -> BitmapEffectCollection
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.BitmapEffectCollection, making deep copies of this object's values. 
             When copying dependency properties, this method copies resource references and data bindings 
             (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: BitmapEffectCollection, source: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: BitmapEffectCollection) -> BitmapEffectCollection
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.BitmapEffectCollection object, making deep copies of this object's 
             current values. Resource references, data bindings, and animations are not copied, but their 
             current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: BitmapEffectCollection, source: Freezable) """
        pass

    def Contains(self, value):
        """
        Contains(self: BitmapEffectCollection, value: BitmapEffect) -> bool
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Indicates whether the collection contains the specified 
             System.Windows.Media.Effects.BitmapEffect.
        
        
            value: The bitmap effect to locate in the collection.
            Returns: true if the collection contains value; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: BitmapEffectCollection, array: Array[BitmapEffect], index: int)
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Copies the elements of the collection to an array starting 
             at the given index.
        
        
            array: The array to copy to.
            index: The collection index to begin coping.
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
        """ CreateInstanceCore(self: BitmapEffectCollection) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """ FreezeCore(self: BitmapEffectCollection, isChecking: bool) -> bool """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: BitmapEffectCollection, source: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: BitmapEffectCollection, source: Freezable) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: BitmapEffectCollection) -> Enumerator
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Returns an enumerator that can iterate through the 
             collection.
        
            Returns: An System.Windows.Media.Effects.BitmapEffectCollection.Enumerator that can iterate through the 
             collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: BitmapEffectCollection, value: BitmapEffect) -> int
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Retrieves the index of the first instance of the specified 
             System.Windows.Media.Effects.BitmapEffect.
        
        
            value: The effect to find in the collection.
            Returns: The index of the specified effect.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: BitmapEffectCollection, index: int, value: BitmapEffect)
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Inserts a System.Windows.Media.Effects.BitmapEffect into 
             this collection at the specified index.
        
        
            index: The index to insert the effect at.
            value: The specified effect to insert.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: BitmapEffectCollection, value: BitmapEffect) -> bool
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Removes the first occurrence of the specified 
             System.Windows.Media.Effects.BitmapEffect for this collection.
        
        
            value: The effect to remove from the collection
            Returns: true if value was removed; otherwise, false.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: BitmapEffectCollection, index: int)
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Remove the System.Windows.Media.Effects.BitmapEffect at the 
             specified index from the collection.
        
        
            index: The index of the effect to remove.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[BitmapEffect], item: BitmapEffect) -> bool
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, collection: IEnumerable[BitmapEffect])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets the number of effects contained in the System.Windows.Media.Effects.BitmapEffectCollection.

Get: Count(self: BitmapEffectCollection) -> int

"""


    Enumerator = None


class BitmapEffectGroup(BitmapEffect, ISealable, IAnimatable, IResource):
    """
    Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Represents a group of System.Windows.Media.Effects.BitmapEffect objects that is used to apply multiple effects to a visible object.
    
    BitmapEffectGroup()
    """
    def Clone(self):
        """
        Clone(self: BitmapEffectGroup) -> BitmapEffectGroup
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.BitmapEffectGroup object, making deep copies of this object's 
             current values. Resource references, data bindings, and animations are not copied, but their 
             current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: BitmapEffectGroup) -> BitmapEffectGroup
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.BitmapEffectGroup object, making deep copies of this object's 
             current values. Resource references, data bindings, and animations are not copied, but their 
             current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
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
        """ CreateInstanceCore(self: BitmapEffectGroup) -> Freezable """
        pass

    def CreateUnmanagedEffect(self, *args): #cannot find CLR method
        """ CreateUnmanagedEffect(self: BitmapEffectGroup) -> SafeHandle """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def UpdateUnmanagedPropertyState(self, *args): #cannot find CLR method
        """ UpdateUnmanagedPropertyState(self: BitmapEffectGroup, unmanagedEffect: SafeHandle) """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets or sets the children of the System.Windows.Media.Effects.BitmapEffectGroup.

Get: Children(self: BitmapEffectGroup) -> BitmapEffectCollection

Set: Children(self: BitmapEffectGroup) = value
"""


    ChildrenProperty = None


class BitmapEffectInput(Animatable, ISealable, IAnimatable, IResource):
    """
    Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Applies the System.Windows.Media.Effects.BitmapEffect given in the System.Windows.UIElement.BitmapEffect property to a specified region of the visual object.
    
    BitmapEffectInput()
    BitmapEffectInput(input: BitmapSource)
    """
    def Clone(self):
        """
        Clone(self: BitmapEffectInput) -> BitmapEffectInput
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.BitmapEffectInput, making deep copies of this object's values. When 
             copying dependency properties, this method copies resource references and data bindings (but 
             they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: BitmapEffectInput) -> BitmapEffectInput
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.BitmapEffectInput object, making deep copies of this object's 
             current values. Resource references, data bindings, and animations are not copied, but their 
             current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
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
        """ CreateInstanceCore(self: BitmapEffectInput) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeInput(self):
        """
        ShouldSerializeInput(self: BitmapEffectInput) -> bool
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Determines if 
             System.Windows.Media.Effects.BitmapEffectInput.Input should be serialized.
        
            Returns: true if System.Windows.Media.Effects.BitmapEffectInput.Input should be serialized; otherwise 
             false.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, input=None):
        """
        __new__(cls: type)
        __new__(cls: type, input: BitmapSource)
        """
        pass

    AreaToApplyEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets or sets a rectangular region on the visual to which the System.Windows.Media.Effects.BitmapEffect is applied.

Get: AreaToApplyEffect(self: BitmapEffectInput) -> Rect

Set: AreaToApplyEffect(self: BitmapEffectInput) = value
"""

    AreaToApplyEffectUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets or sets the method in which to interpret the rectangle provided by System.Windows.Media.Effects.BitmapEffectInput.AreaToApplyEffect.

Get: AreaToApplyEffectUnits(self: BitmapEffectInput) -> BrushMappingMode

Set: AreaToApplyEffectUnits(self: BitmapEffectInput) = value
"""

    Input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets or sets the System.Windows.Media.Imaging.BitmapSource that is used for the input for the object.

Get: Input(self: BitmapEffectInput) -> BitmapSource

Set: Input(self: BitmapEffectInput) = value
"""


    AreaToApplyEffectProperty = None
    AreaToApplyEffectUnitsProperty = None
    ContextInputSource = None
    InputProperty = None


class BlurBitmapEffect(BitmapEffect, ISealable, IAnimatable, IResource):
    """
    Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.BlurEffect. Simulates looking at an object through an out-of-focus lens.
    
    BlurBitmapEffect()
    """
    def Clone(self):
        """
        Clone(self: BlurBitmapEffect) -> BlurBitmapEffect
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.BlurEffect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.BlurBitmapEffect, making deep copies of this object's values. When 
             copying dependency properties, this method copies resource references and data bindings (but 
             they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: BlurBitmapEffect) -> BlurBitmapEffect
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.BlurEffect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.BlurBitmapEffect object, making deep copies of this object's 
             current values. Resource references, data bindings, and animations are not copied, but their 
             current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
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
        """ CreateInstanceCore(self: BlurBitmapEffect) -> Freezable """
        pass

    def CreateUnmanagedEffect(self, *args): #cannot find CLR method
        """ CreateUnmanagedEffect(self: BlurBitmapEffect) -> SafeHandle """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def UpdateUnmanagedPropertyState(self, *args): #cannot find CLR method
        """ UpdateUnmanagedPropertyState(self: BlurBitmapEffect, unmanagedEffect: SafeHandle) """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    KernelType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.BlurEffect. Gets or sets the type of blur kernel to use for the System.Windows.Media.Effects.BlurBitmapEffect.

Get: KernelType(self: BlurBitmapEffect) -> KernelType

Set: KernelType(self: BlurBitmapEffect) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.BlurEffect. Gets or sets the radius used in the blur kernel. A larger radius implies more blurring.

Get: Radius(self: BlurBitmapEffect) -> float

Set: Radius(self: BlurBitmapEffect) = value
"""


    KernelTypeProperty = None
    RadiusProperty = None


class Effect(Animatable, ISealable, IAnimatable, IResource):
    """ Provides a custom bitmap effect. """
    def Clone(self):
        """
        Clone(self: Effect) -> Effect
        
            Creates a modifiable clone of this System.Windows.Media.Effects.Effect object, making deep 
             copies of this object's values. When copying this object's dependency properties, this method 
             copies resource references and data bindings (which may no longer resolve), but not animations 
             or their current values.
        
            Returns: A modifiable clone of this instance. The returned clone is effectively a deep copy of the 
             current object. The clone's System.Windows.Freezable.IsFrozen property is false.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: Effect) -> Effect
        
            Creates a modifiable clone of this System.Windows.Media.Effects.Effect object, making deep 
             copies of this object's current values. Resource references, data bindings, and animations are 
             not copied, but their current values are copied.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
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
        CreateInstanceCore(self: Freezable) -> Freezable
        
            When implemented in a derived class, creates a new instance of the System.Windows.Freezable 
             derived class.
        
            Returns: The new instance.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    EffectMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, transforms mouse input and coordinate systems through the effect.

"""


    ImplicitInput = None


class BlurEffect(Effect, ISealable, IAnimatable, IResource):
    """
    A bitmap effect that blurs the target texture.
    
    BlurEffect()
    """
    def Clone(self):
        """
        Clone(self: BlurEffect) -> BlurEffect
        
            Creates a modifiable clone of this System.Windows.Media.Effects.Effect object, making deep 
             copies of this object's values. When copying this object's dependency properties, this method 
             copies resource references and data bindings (which may no longer resolve), but not animations 
             or their current values.
        
            Returns: A modifiable clone of this instance. The returned clone is effectively a deep copy of the 
             current object. The clone's System.Windows.Freezable.IsFrozen property is false.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: BlurEffect) -> BlurEffect
        
            Creates a modifiable clone of this System.Windows.Media.Effects.Effect object, making deep 
             copies of this object's current values. Resource references, data bindings, and animations are 
             not copied, but their current values are copied.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
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
        """ CreateInstanceCore(self: BlurEffect) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    EffectMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, transforms mouse input and coordinate systems through the effect.

"""

    KernelType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value representing the curve that is used to calculate the blur.

Get: KernelType(self: BlurEffect) -> KernelType

Set: KernelType(self: BlurEffect) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the radius of the blur effect's curve.

Get: Radius(self: BlurEffect) -> float

Set: Radius(self: BlurEffect) = value
"""

    RenderingBias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the system renders an effect with emphasis on speed or quality.

Get: RenderingBias(self: BlurEffect) -> RenderingBias

Set: RenderingBias(self: BlurEffect) = value
"""


    KernelTypeProperty = None
    RadiusProperty = None
    RenderingBiasProperty = None


class DropShadowBitmapEffect(BitmapEffect, ISealable, IAnimatable, IResource):
    """
    Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.DropShadowEffect. Applies a shadow behind a visual object at a slight offset. The offset is determined by mimicking a casting shadow from an imaginary light source.
    
    DropShadowBitmapEffect()
    """
    def Clone(self):
        """
        Clone(self: DropShadowBitmapEffect) -> DropShadowBitmapEffect
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.DropShadowEffect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.DropShadowBitmapEffect, making deep copies of this object's values. 
             When copying dependency properties, this method copies resource references and data bindings 
             (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: DropShadowBitmapEffect) -> DropShadowBitmapEffect
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.DropShadowEffect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.DropShadowBitmapEffect object, making deep copies of this object's 
             current values. Resource references, data bindings, and animations are not copied, but their 
             current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
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
        """ CreateInstanceCore(self: DropShadowBitmapEffect) -> Freezable """
        pass

    def CreateUnmanagedEffect(self, *args): #cannot find CLR method
        """ CreateUnmanagedEffect(self: DropShadowBitmapEffect) -> SafeHandle """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def UpdateUnmanagedPropertyState(self, *args): #cannot find CLR method
        """ UpdateUnmanagedPropertyState(self: DropShadowBitmapEffect, unmanagedEffect: SafeHandle) """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.DropShadowEffect. Gets or sets the color of the shadow.

Get: Color(self: DropShadowBitmapEffect) -> Color

Set: Color(self: DropShadowBitmapEffect) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.DropShadowEffect. Gets or sets the angle at which the shadow is cast.

Get: Direction(self: DropShadowBitmapEffect) -> float

Set: Direction(self: DropShadowBitmapEffect) = value
"""

    Noise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.DropShadowEffect. Gets or sets the graininess, or "noise level," of the shadow.

Get: Noise(self: DropShadowBitmapEffect) -> float

Set: Noise(self: DropShadowBitmapEffect) = value
"""

    Opacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.DropShadowEffect. Gets or sets the degree of opacity of the shadow.

Get: Opacity(self: DropShadowBitmapEffect) -> float

Set: Opacity(self: DropShadowBitmapEffect) = value
"""

    ShadowDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.DropShadowEffect. Gets or sets the distance between the object and the shadow that it casts.

Get: ShadowDepth(self: DropShadowBitmapEffect) -> float

Set: ShadowDepth(self: DropShadowBitmapEffect) = value
"""

    Softness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.DropShadowEffect. Gets or sets the softness of the shadow.

Get: Softness(self: DropShadowBitmapEffect) -> float

Set: Softness(self: DropShadowBitmapEffect) = value
"""


    ColorProperty = None
    DirectionProperty = None
    NoiseProperty = None
    OpacityProperty = None
    ShadowDepthProperty = None
    SoftnessProperty = None


class DropShadowEffect(Effect, ISealable, IAnimatable, IResource):
    """
    A bitmap effect that paints a drop shadow around the target texture.
    
    DropShadowEffect()
    """
    def Clone(self):
        """
        Clone(self: DropShadowEffect) -> DropShadowEffect
        
            Creates a modifiable clone of this System.Windows.Media.Effects.Effect object, making deep 
             copies of this object's values. When copying this object's dependency properties, this method 
             copies resource references and data bindings (which may no longer resolve), but not animations 
             or their current values.
        
            Returns: A modifiable clone of this instance. The returned clone is effectively a deep copy of the 
             current object. The clone's System.Windows.Freezable.IsFrozen property is false.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: DropShadowEffect) -> DropShadowEffect
        
            Creates a modifiable clone of this System.Windows.Media.Effects.Effect object, making deep 
             copies of this object's current values. Resource references, data bindings, and animations are 
             not copied, but their current values are copied.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
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
        """ CreateInstanceCore(self: DropShadowEffect) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BlurRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the radius of the shadow's blur effect.

Get: BlurRadius(self: DropShadowEffect) -> float

Set: BlurRadius(self: DropShadowEffect) = value
"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the drop shadow.

Get: Color(self: DropShadowEffect) -> Color

Set: Color(self: DropShadowEffect) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the direction of the drop shadow.

Get: Direction(self: DropShadowEffect) -> float

Set: Direction(self: DropShadowEffect) = value
"""

    EffectMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, transforms mouse input and coordinate systems through the effect.

"""

    Opacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of the drop shadow.

Get: Opacity(self: DropShadowEffect) -> float

Set: Opacity(self: DropShadowEffect) = value
"""

    RenderingBias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the system renders the drop shadow with emphasis on speed or quality.

Get: RenderingBias(self: DropShadowEffect) -> RenderingBias

Set: RenderingBias(self: DropShadowEffect) = value
"""

    ShadowDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the distance of the drop shadow below the texture.

Get: ShadowDepth(self: DropShadowEffect) -> float

Set: ShadowDepth(self: DropShadowEffect) = value
"""


    BlurRadiusProperty = None
    ColorProperty = None
    DirectionProperty = None
    OpacityProperty = None
    RenderingBiasProperty = None
    ShadowDepthProperty = None


class EdgeProfile(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of curve to apply to the edge of a bitmap.
    
    enum EdgeProfile, values: BulgedUp (3), CurvedIn (1), CurvedOut (2), Linear (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BulgedUp = None
    CurvedIn = None
    CurvedOut = None
    Linear = None
    value__ = None


class EmbossBitmapEffect(BitmapEffect, ISealable, IAnimatable, IResource):
    """
    Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Creates a bump mapping of the visual object to give the impression of depth and texture from an artificial light source.
    
    EmbossBitmapEffect()
    """
    def Clone(self):
        """
        Clone(self: EmbossBitmapEffect) -> EmbossBitmapEffect
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.EmbossBitmapEffect, making deep copies of this object's values. 
             When copying dependency properties, this method copies resource references and data bindings 
             (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: EmbossBitmapEffect) -> EmbossBitmapEffect
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.Effect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.EmbossBitmapEffect object, making deep copies of this object's 
             current values. Resource references, data bindings, and animations are not copied, but their 
             current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
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
        """ CreateInstanceCore(self: EmbossBitmapEffect) -> Freezable """
        pass

    def CreateUnmanagedEffect(self, *args): #cannot find CLR method
        """ CreateUnmanagedEffect(self: EmbossBitmapEffect) -> SafeHandle """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def UpdateUnmanagedPropertyState(self, *args): #cannot find CLR method
        """ UpdateUnmanagedPropertyState(self: EmbossBitmapEffect, unmanagedEffect: SafeHandle) """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    LightAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets or sets the direction the artificial light is cast upon the embossed object.

Get: LightAngle(self: EmbossBitmapEffect) -> float

Set: LightAngle(self: EmbossBitmapEffect) = value
"""

    Relief = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.Effect. Gets or sets the amount of relief of the emboss.

Get: Relief(self: EmbossBitmapEffect) -> float

Set: Relief(self: EmbossBitmapEffect) = value
"""


    LightAngleProperty = None
    ReliefProperty = None


class KernelType(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the kernel used to create the effect.
    
    enum KernelType, values: Box (1), Gaussian (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Box = None
    Gaussian = None
    value__ = None


class OuterGlowBitmapEffect(BitmapEffect, ISealable, IAnimatable, IResource):
    """
    Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.BlurEffect. Creates a halo of color around objects or areas of color.
    
    OuterGlowBitmapEffect()
    """
    def Clone(self):
        """
        Clone(self: OuterGlowBitmapEffect) -> OuterGlowBitmapEffect
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.BlurEffect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.OuterGlowBitmapEffect, making deep copies of this object's values. 
             When copying dependency properties, this method copies resource references and data bindings 
             (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: OuterGlowBitmapEffect) -> OuterGlowBitmapEffect
        
            Note: This API is now obsolete. The non-obsolete alternative is 
             System.Windows.Media.Effects.BlurEffect. Creates a modifiable clone of this 
             System.Windows.Media.Effects.OuterGlowBitmapEffect object, making deep copies of this object's 
             current values. Resource references, data bindings, and animations are not copied, but their 
             current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 
             using current property values.
        
        
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
        """ CreateInstanceCore(self: OuterGlowBitmapEffect) -> Freezable """
        pass

    def CreateUnmanagedEffect(self, *args): #cannot find CLR method
        """ CreateUnmanagedEffect(self: OuterGlowBitmapEffect) -> SafeHandle """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base 
             (non-animated) property values.
        
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 
             object has animated dependency properties, their current animated values are copied.
        
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def UpdateUnmanagedPropertyState(self, *args): #cannot find CLR method
        """ UpdateUnmanagedPropertyState(self: OuterGlowBitmapEffect, unmanagedEffect: SafeHandle) """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GlowColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.BlurEffect. Gets or sets the color of the halo glow.

Get: GlowColor(self: OuterGlowBitmapEffect) -> Color

Set: GlowColor(self: OuterGlowBitmapEffect) = value
"""

    GlowSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.BlurEffect. Gets or sets the thickness of the halo glow.

Get: GlowSize(self: OuterGlowBitmapEffect) -> float

Set: GlowSize(self: OuterGlowBitmapEffect) = value
"""

    Noise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.BlurEffect. Gets or sets the graininess of the halo glow.

Get: Noise(self: OuterGlowBitmapEffect) -> float

Set: Noise(self: OuterGlowBitmapEffect) = value
"""

    Opacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Note: This API is now obsolete. The non-obsolete alternative is System.Windows.Media.Effects.BlurEffect. Gets or sets the degree of opacity of the halo glow.

Get: Opacity(self: OuterGlowBitmapEffect) -> float

Set: Opacity(self: OuterGlowBitmapEffect) = value
"""


    GlowColorProperty = None
    GlowSizeProperty = None
    NoiseProperty = None
    OpacityProperty = None


class PixelShader(Animatable, ISealable, IAnimatable, IResource):
    """
    Provides a managed wrapper around a High Level Shading Language (HLSL) pixel shader.
    
    PixelShader()
    """
    def Clone(self):
        """
        Clone(self: PixelShader) -> PixelShader
        
            Creates a modifiable clone of this System.Windows.Media.Effects.PixelShader object, making deep 
             copies of this object's values. When copying this object's dependency properties, this method 
             copies resource references and data bindings (which may no longer resolve), but not animations 
             or their current values.
        
            Returns: A modifiable clone of this instance. The returned clone is effectively a deep copy of the 
             current object. The clone's System.Windows.Freezable.IsFrozen property is false.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: PixelShader, sourceFreezable: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: PixelShader) -> PixelShader
        
            Creates a modifiable clone of this System.Windows.Media.Effects.PixelShader object, making deep 
             copies of this object's current values. Resource references, data bindings, and animations are 
             not copied, but their current values are copied.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: PixelShader, sourceFreezable: Freezable) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: PixelShader) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: PixelShader, sourceFreezable: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: PixelShader, sourceFreezable: Freezable) """
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def SetStreamSource(self, source):
        """
        SetStreamSource(self: PixelShader, source: Stream)
            Assigns the System.IO.Stream to use as the source of HLSL bytecode.
        
            source: The stream to read the HLSL bytecode from.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ShaderRenderMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to use hardware or software rendering.

Get: ShaderRenderMode(self: PixelShader) -> ShaderRenderMode

Set: ShaderRenderMode(self: PixelShader) = value
"""

    UriSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Pack URI reference to HLSL bytecode in the assembly.

Get: UriSource(self: PixelShader) -> Uri

Set: UriSource(self: PixelShader) = value
"""


    InvalidPixelShaderEncountered = None
    ShaderRenderModeProperty = None
    UriSourceProperty = None


class RenderingBias(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates whether the system renders an effect with emphasis on speed or quality.
    
    enum RenderingBias, values: Performance (0), Quality (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Performance = None
    Quality = None
    value__ = None


class SamplingMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates the way System.Windows.Media.Brush-valued dependency properties are sampled in a custom shader effect.
    
    enum SamplingMode, values: Auto (2), Bilinear (1), NearestNeighbor (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Auto = None
    Bilinear = None
    NearestNeighbor = None
    value__ = None


class ShaderEffect(Effect, ISealable, IAnimatable, IResource):
    """ Provides a custom bitmap effect by using a System.Windows.Media.Effects.PixelShader. """
    def Clone(self):
        """
        Clone(self: ShaderEffect) -> ShaderEffect
        
            Creates a modifiable clone of this System.Windows.Media.Effects.ShaderEffect object, making deep 
             copies of this object's values. When copying this object's dependency properties, this method 
             copies resource references and data bindings (which may no longer resolve), but not animations 
             or their current values.
        
            Returns: A modifiable clone of this instance. The returned clone is effectively a deep copy of the 
             current object. The clone's System.Windows.Freezable.IsFrozen property is false.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: ShaderEffect, sourceFreezable: Freezable)
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: ShaderEffect) -> ShaderEffect
        
            Creates a modifiable clone of this System.Windows.Media.Effects.ShaderEffect object, making deep 
             copies of this object's current values. Resource references, data bindings, and animations are 
             not copied, but their current values are copied.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: ShaderEffect, sourceFreezable: Freezable)
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
        """ CreateInstanceCore(self: ShaderEffect) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 
             it can be made unmodifiable.
        
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this 
             instance should actually freeze itself when this method is called.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: ShaderEffect, sourceFreezable: Freezable)
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: ShaderEffect, sourceFreezable: Freezable)
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def PixelShaderConstantCallback(self, *args): #cannot find CLR method
        """
        PixelShaderConstantCallback(floatRegisterIndex: int) -> PropertyChangedCallback
        
            Associates a dependency property value with a pixel shader's float constant register.
        
            floatRegisterIndex: The index of the shader register associated with the dependency property.
            Returns: A System.Windows.PropertyChangedCallback delegate that associates a dependency property and the 
             shader constant register specified by floatRegisterIndex.
        """
        pass

    def PixelShaderSamplerCallback(self, *args): #cannot find CLR method
        """
        PixelShaderSamplerCallback(samplerRegisterIndex: int, samplingMode: SamplingMode) -> PropertyChangedCallback
        
            Associates a dependency property value with a pixel shader's sampler register and a 
             System.Windows.Media.Effects.SamplingMode.
        
        
            samplerRegisterIndex: The index of the shader sampler associated with the dependency property.
            samplingMode: The System.Windows.Media.Effects.SamplingMode for the shader sampler.
            Returns: A System.Windows.PropertyChangedCallback delegate that associates a dependency property and the 
             shader sampler register specified by samplerRegisterIndex.
        
        PixelShaderSamplerCallback(samplerRegisterIndex: int) -> PropertyChangedCallback
        
            Associates a dependency property value with a pixel shader's sampler register.
        
            samplerRegisterIndex: The index of the shader sampler associated with the dependency property.
            Returns: A System.Windows.PropertyChangedCallback delegate that associates a dependency property and the 
             shader sampler register specified by samplerRegisterIndex.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def RegisterPixelShaderSamplerProperty(self, *args): #cannot find CLR method
        """
        RegisterPixelShaderSamplerProperty(dpName: str, ownerType: Type, samplerRegisterIndex: int, samplingMode: SamplingMode) -> DependencyProperty
        
            Associates a dependency property with a shader sampler register and a 
             System.Windows.Media.Effects.SamplingMode.
        
        
            dpName: The name of the dependency property.
            ownerType: The type of the effect that has the dependency property.
            samplerRegisterIndex: The index of the shader sampler associated with the dependency property.
            samplingMode: The System.Windows.Media.Effects.SamplingMode for the shader sampler.
            Returns: A dependency property associated with the shader sampler specified by samplerRegisterIndex.
        RegisterPixelShaderSamplerProperty(dpName: str, ownerType: Type, samplerRegisterIndex: int) -> DependencyProperty
        
            Associates a dependency property with a shader sampler register.
        
            dpName: The name of the dependency property.
            ownerType: The type of the effect that has the dependency property.
            samplerRegisterIndex: The index of the shader sampler associated with the dependency property.
            Returns: A dependency property associated with the shader sampler specified by samplerRegisterIndex.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def UpdateShaderValue(self, *args): #cannot find CLR method
        """
        UpdateShaderValue(self: ShaderEffect, dp: DependencyProperty)
            Notifies the effect that the shader constant or sampler corresponding to the specified 
             dependency property should be updated.
        
        
            dp: The dependency property to be updated.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DdxUvDdyUvRegisterIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the shader register to use for the partial derivatives of the texture coordinates with respect to screen space.

"""

    EffectMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, transforms mouse input and coordinate systems through the effect.

"""

    PaddingBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating that the effect's output texture is larger than its input texture along the bottom edge.

"""

    PaddingLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating that the effect's output texture is larger than its input texture along the left edge.

"""

    PaddingRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating that the effect's output texture is larger than its input texture along the right edge.

"""

    PaddingTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating that the effect's output texture is larger than its input texture along the top edge.

"""

    PixelShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.PixelShader to use for the effect.

"""


    PixelShaderProperty = None


class ShaderRenderMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates the policy for rendering a System.Windows.Media.Effects.ShaderEffect in software.
    
    enum ShaderRenderMode, values: Auto (0), HardwareOnly (2), SoftwareOnly (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Auto = None
    HardwareOnly = None
    SoftwareOnly = None
    value__ = None


