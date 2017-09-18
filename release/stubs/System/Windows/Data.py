# encoding: utf-8
# module System.Windows.Data calls itself Data
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BindingBase(MarkupExtension):
    """ Defines the common characteristics of the System.Windows.Data.Binding, System.Windows.Data.PriorityBinding, and System.Windows.Data.MultiBinding classes. """
    def ProvideValue(self, serviceProvider):
        """
        ProvideValue(self: BindingBase, serviceProvider: IServiceProvider) -> object
        
            Returns an object that should be set on the property where this binding and extension are 
             applied.
        
        
            serviceProvider: The object that can provide services for the markup extension. May be null; see the Remarks 
             section for more information.
        
            Returns: The value to set on the binding target property.
        """
        pass

    def ShouldSerializeFallbackValue(self):
        """
        ShouldSerializeFallbackValue(self: BindingBase) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the effective 
             value of the System.Windows.Data.BindingBase.FallbackValue property on instances of this class.
        
            Returns: true if the System.Windows.Data.BindingBase.FallbackValue property value should be serialized; 
             otherwise, false.
        """
        pass

    def ShouldSerializeTargetNullValue(self):
        """
        ShouldSerializeTargetNullValue(self: BindingBase) -> bool
        
            Returns a value that indicates whether the System.Windows.Data.BindingBase.TargetNullValue 
             property should be serialized.
        
            Returns: true if the System.Windows.Data.BindingBase.TargetNullValue property should be serialized; 
             otherwise, false.
        """
        pass

    BindingGroupName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Windows.Data.BindingGroup to which this binding belongs.

Get: BindingGroupName(self: BindingBase) -> str

Set: BindingGroupName(self: BindingBase) = value
"""

    Delay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Delay(self: BindingBase) -> int

Set: Delay(self: BindingBase) = value
"""

    FallbackValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value to use when the binding is unable to return a value.

Get: FallbackValue(self: BindingBase) -> object

Set: FallbackValue(self: BindingBase) = value
"""

    StringFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a string that specifies how to format the binding if it displays the bound value as a string.

Get: StringFormat(self: BindingBase) -> str

Set: StringFormat(self: BindingBase) = value
"""

    TargetNullValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value that is used in the target when the value of the source is null.

Get: TargetNullValue(self: BindingBase) -> object

Set: TargetNullValue(self: BindingBase) = value
"""



class Binding(BindingBase):
    """
    Provides high-level access to the definition of a binding, which connects the properties of binding target objects (typically, WPF elements), and any data source (for example, a database, an XML file, or any object that contains data).
    
    Binding()
    Binding(path: str)
    """
    @staticmethod
    def AddSourceUpdatedHandler(element, handler):
        """ AddSourceUpdatedHandler(element: DependencyObject, handler: EventHandler[DataTransferEventArgs]) """
        pass

    @staticmethod
    def AddTargetUpdatedHandler(element, handler):
        """ AddTargetUpdatedHandler(element: DependencyObject, handler: EventHandler[DataTransferEventArgs]) """
        pass

    @staticmethod
    def GetXmlNamespaceManager(target):
        """
        GetXmlNamespaceManager(target: DependencyObject) -> XmlNamespaceManager
        
            Returns an XML namespace manager object used by the binding attached to the specified�object.
        
            target: The object from which to get namespace information.
            Returns: A returned object used for viewing XML namespaces that relate to the binding on the passed 
             object element. This object should be cast as System.Xml.XmlNamespaceManager.
        """
        pass

    @staticmethod
    def RemoveSourceUpdatedHandler(element, handler):
        """ RemoveSourceUpdatedHandler(element: DependencyObject, handler: EventHandler[DataTransferEventArgs]) """
        pass

    @staticmethod
    def RemoveTargetUpdatedHandler(element, handler):
        """ RemoveTargetUpdatedHandler(element: DependencyObject, handler: EventHandler[DataTransferEventArgs]) """
        pass

    @staticmethod
    def SetXmlNamespaceManager(target, value):
        """
        SetXmlNamespaceManager(target: DependencyObject, value: XmlNamespaceManager)
            Sets a namespace manager object used by the binding attached to the provided element.
        
            target: The object from which to get namespace information.
            value: The System.Xml.XmlNamespaceManager to use for namespace evaluation in the passed element.
        """
        pass

    def ShouldSerializePath(self):
        """
        ShouldSerializePath(self: Binding) -> bool
        
            Indicates whether the System.Windows.Data.Binding.Path property should be persisted.
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def ShouldSerializeSource(self):
        """
        ShouldSerializeSource(self: Binding) -> bool
        
            Indicates whether the System.Windows.Data.Binding.Source property should be persisted.
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def ShouldSerializeValidationRules(self):
        """
        ShouldSerializeValidationRules(self: Binding) -> bool
        
            Indicates whether the System.Windows.Data.Binding.ValidationRules property should be persisted.
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, path=None):
        """
        __new__(cls: type)
        __new__(cls: type, path: str)
        """
        pass

    AsyncState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets opaque data passed to the asynchronous data dispatcher.

Get: AsyncState(self: Binding) -> object

Set: AsyncState(self: Binding) = value
"""

    BindsDirectlyToSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to evaluate the System.Windows.Data.Binding.Path relative to the data item or the System.Windows.Data.DataSourceProvider object.

Get: BindsDirectlyToSource(self: Binding) -> bool

Set: BindsDirectlyToSource(self: Binding) = value
"""

    Converter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the converter to use.

Get: Converter(self: Binding) -> IValueConverter

Set: Converter(self: Binding) = value
"""

    ConverterCulture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the culture in which to evaluate the converter.

Get: ConverterCulture(self: Binding) -> CultureInfo

Set: ConverterCulture(self: Binding) = value
"""

    ConverterParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the parameter to pass to the System.Windows.Data.Binding.Converter.

Get: ConverterParameter(self: Binding) -> object

Set: ConverterParameter(self: Binding) = value
"""

    ElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the element to use as the binding source object.

Get: ElementName(self: Binding) -> str

Set: ElementName(self: Binding) = value
"""

    IsAsync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the System.Windows.Data.Binding should get and set values asynchronously.

Get: IsAsync(self: Binding) -> bool

Set: IsAsync(self: Binding) = value
"""

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the direction of the data flow in the binding.

Get: Mode(self: Binding) -> BindingMode

Set: Mode(self: Binding) = value
"""

    NotifyOnSourceUpdated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to raise the System.Windows.Data.Binding.SourceUpdated event when a value is transferred from the binding target to the binding source.

Get: NotifyOnSourceUpdated(self: Binding) -> bool

Set: NotifyOnSourceUpdated(self: Binding) = value
"""

    NotifyOnTargetUpdated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to raise the System.Windows.Data.Binding.TargetUpdated event when a value is transferred from the binding source to the binding target.

Get: NotifyOnTargetUpdated(self: Binding) -> bool

Set: NotifyOnTargetUpdated(self: Binding) = value
"""

    NotifyOnValidationError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to raise the System.Windows.Controls.Validation.Error�attached event on the bound object.

Get: NotifyOnValidationError(self: Binding) -> bool

Set: NotifyOnValidationError(self: Binding) = value
"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the path to the binding source property.

Get: Path(self: Binding) -> PropertyPath

Set: Path(self: Binding) = value
"""

    RelativeSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the binding source by specifying its location relative to the position of the binding target.

Get: RelativeSource(self: Binding) -> RelativeSource

Set: RelativeSource(self: Binding) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object to use as the binding source.

Get: Source(self: Binding) -> object

Set: Source(self: Binding) = value
"""

    UpdateSourceExceptionFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a handler you can use to provide custom logic for handling exceptions that the binding engine encounters during the update of the binding source value. This is only applicable if you have associated an System.Windows.Controls.ExceptionValidationRule with your binding.

Get: UpdateSourceExceptionFilter(self: Binding) -> UpdateSourceExceptionFilterCallback

Set: UpdateSourceExceptionFilter(self: Binding) = value
"""

    UpdateSourceTrigger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines the timing of binding source updates.

Get: UpdateSourceTrigger(self: Binding) -> UpdateSourceTrigger

Set: UpdateSourceTrigger(self: Binding) = value
"""

    ValidatesOnDataErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to include the System.Windows.Controls.DataErrorValidationRule.

Get: ValidatesOnDataErrors(self: Binding) -> bool

Set: ValidatesOnDataErrors(self: Binding) = value
"""

    ValidatesOnExceptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to include the System.Windows.Controls.ExceptionValidationRule.

Get: ValidatesOnExceptions(self: Binding) -> bool

Set: ValidatesOnExceptions(self: Binding) = value
"""

    ValidatesOnNotifyDataErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidatesOnNotifyDataErrors(self: Binding) -> bool

Set: ValidatesOnNotifyDataErrors(self: Binding) = value
"""

    ValidationRules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of rules that check the validity of the user input.

Get: ValidationRules(self: Binding) -> Collection[ValidationRule]

"""

    XPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an XPath query that returns the value on the XML�binding source to use.

Get: XPath(self: Binding) -> str

Set: XPath(self: Binding) = value
"""


    DoNothing = None
    IndexerName = 'Item[]'
    SourceUpdatedEvent = None
    TargetUpdatedEvent = None
    XmlNamespaceManagerProperty = None


class BindingExpressionBase(Expression, IWeakEventListener):
    """ Represents the base class for System.Windows.Data.BindingExpression, System.Windows.Data.PriorityBindingExpression, and System.Windows.Data.MultiBindingExpression. """
    def UpdateSource(self):
        """
        UpdateSource(self: BindingExpressionBase)
            Sends the current binding target value to the binding source in 
             System.Windows.Data.BindingMode.TwoWay or System.Windows.Data.BindingMode.OneWayToSource 
             bindings.
        """
        pass

    def UpdateTarget(self):
        """
        UpdateTarget(self: BindingExpressionBase)
            Forces a data transfer from the binding source to the binding target.
        """
        pass

    def ValidateWithoutUpdate(self):
        """
        ValidateWithoutUpdate(self: BindingExpressionBase) -> bool
        
            Runs any System.Windows.Controls.ValidationRule objects on the associated 
             System.Windows.Data.Binding that have the System.Windows.Controls.ValidationRule.ValidationStep 
             property set to System.Windows.Controls.ValidationStep.RawProposedValue or 
             System.Windows.Controls.ValidationStep.ConvertedProposedValue. This method does not update the 
             source.
        
            Returns: true if the validation rules succeed; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BindingGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BindingGroup(self: BindingExpressionBase) -> BindingGroup

"""

    HasError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the parent binding has a failed validation rule.

Get: HasError(self: BindingExpressionBase) -> bool

"""

    HasValidationError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasValidationError(self: BindingExpressionBase) -> bool

"""

    IsDirty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDirty(self: BindingExpressionBase) -> bool

"""

    ParentBindingBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Data.BindingBase object from which this System.Windows.Data.BindingExpressionBase object is created.

Get: ParentBindingBase(self: BindingExpressionBase) -> BindingBase

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the status of the binding expression.

Get: Status(self: BindingExpressionBase) -> BindingStatus

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Target(self: BindingExpressionBase) -> DependencyObject

"""

    TargetProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetProperty(self: BindingExpressionBase) -> DependencyProperty

"""

    ValidationError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Controls.ValidationError that caused this instance of System.Windows.Data.BindingExpressionBase to be invalid.

Get: ValidationError(self: BindingExpressionBase) -> ValidationError

"""

    ValidationErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidationErrors(self: BindingExpressionBase) -> ReadOnlyCollection[ValidationError]

"""



class BindingExpression(BindingExpressionBase, IWeakEventListener, IDataBindEngineClient):
    """ Contains information about a single instance of a System.Windows.Data.Binding. """
    def UpdateSource(self):
        """
        UpdateSource(self: BindingExpression)
            Sends the current binding target value to the binding source property in 
             System.Windows.Data.BindingMode.TwoWay or System.Windows.Data.BindingMode.OneWayToSource 
             bindings.
        """
        pass

    def UpdateTarget(self):
        """
        UpdateTarget(self: BindingExpression)
            Forces a data transfer from the binding source property to the binding target property.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the binding source object that this System.Windows.Data.BindingExpression uses.

Get: DataItem(self: BindingExpression) -> object

"""

    ParentBinding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the System.Windows.Data.Binding object of the current System.Windows.Data.BindingExpression.

Get: ParentBinding(self: BindingExpression) -> Binding

"""

    ResolvedSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResolvedSource(self: BindingExpression) -> object

"""

    ResolvedSourcePropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResolvedSourcePropertyName(self: BindingExpression) -> str

"""



class BindingGroup(DependencyObject):
    """
    Contains a collection of bindings and System.Windows.Controls.ValidationRule objects that are used to validate an object.
    
    BindingGroup()
    """
    def BeginEdit(self):
        """
        BeginEdit(self: BindingGroup)
            Begins an edit transaction on the sources in the System.Windows.Data.BindingGroup.
        """
        pass

    def CancelEdit(self):
        """
        CancelEdit(self: BindingGroup)
            Ends the edit transaction and discards the pending changes.
        """
        pass

    def CommitEdit(self):
        """
        CommitEdit(self: BindingGroup) -> bool
        
            Runs all the System.Windows.Controls.ValidationRule objects and updates the binding sources if 
             all validation rules succeed.
        
            Returns: true if every System.Windows.Controls.ValidationRule succeeds and the values are committed to 
             the sources; otherwise, false.
        """
        pass

    def GetValue(self, *__args):
        """
        GetValue(self: BindingGroup, item: object, propertyName: str) -> object
        
            Returns the proposed value for the specified property and item.
        
            item: The object that contains the specified property.
            propertyName: The property whose proposed value to get.
            Returns: The proposed property value.
        """
        pass

    def TryGetValue(self, item, propertyName, value):
        """
        TryGetValue(self: BindingGroup, item: object, propertyName: str) -> (bool, object)
        
            Attempts to get the proposed value for the specified property and item.
        
            item: The object that contains the specified property.
            propertyName: The property whose proposed value to get.
            Returns: true if value is the proposed value for the specified property; otherwise, false.
        """
        pass

    def UpdateSources(self):
        """
        UpdateSources(self: BindingGroup) -> bool
        
            Runs the converter on the binding and the System.Windows.Controls.ValidationRule objects that 
             have the System.Windows.Controls.ValidationRule.ValidationStep property set to 
             System.Windows.Controls.ValidationStep.RawProposedValue, 
             System.Windows.Controls.ValidationStep.ConvertedProposedValue, or 
             System.Windows.Controls.ValidationStep.UpdatedValue and saves the values of the targets to the 
             source objects if all the validation rules succeed.
        
            Returns: true if all validation rules succeed; otherwise, false.
        """
        pass

    def ValidateWithoutUpdate(self):
        """
        ValidateWithoutUpdate(self: BindingGroup) -> bool
        
            Runs the converter on the binding and the System.Windows.Controls.ValidationRule objects that 
             have the System.Windows.Controls.ValidationRule.ValidationStep property set to 
             System.Windows.Controls.ValidationStep.RawProposedValue or 
             System.Windows.Controls.ValidationStep.ConvertedProposedValue.
        
            Returns: true if the validation rules succeed; otherwise, false.
        """
        pass

    BindingExpressions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.Windows.Data.BindingExpression objects that contains information for each Binding in the System.Windows.Data.BindingGroup.

Get: BindingExpressions(self: BindingGroup) -> Collection[BindingExpressionBase]

"""

    CanRestoreValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether each source in the binding can discard pending changes and restore the original values.

Get: CanRestoreValues(self: BindingGroup) -> bool

"""

    HasValidationError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasValidationError(self: BindingGroup) -> bool

"""

    IsDirty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDirty(self: BindingGroup) -> bool

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the sources that are used by the Binding objects in the System.Windows.Data.BindingGroup.

Get: Items(self: BindingGroup) -> IList

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name that identifies the System.Windows.Data.BindingGroup, which can be used to include and exclude Binding objects in the System.Windows.Data.BindingGroup.

Get: Name(self: BindingGroup) -> str

Set: Name(self: BindingGroup) = value
"""

    NotifyOnValidationError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the System.Windows.Controls.Validation.Error event occurs when the state of a System.Windows.Controls.ValidationRule changes.

Get: NotifyOnValidationError(self: BindingGroup) -> bool

Set: NotifyOnValidationError(self: BindingGroup) = value
"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Owner(self: BindingGroup) -> DependencyObject

"""

    SharesProposedValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the System.Windows.Data.BindingGroup reuses target values that have not been committed to the source.

Get: SharesProposedValues(self: BindingGroup) -> bool

Set: SharesProposedValues(self: BindingGroup) = value
"""

    ValidatesOnNotifyDataError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidatesOnNotifyDataError(self: BindingGroup) -> bool

Set: ValidatesOnNotifyDataError(self: BindingGroup) = value
"""

    ValidationErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidationErrors(self: BindingGroup) -> ReadOnlyCollection[ValidationError]

"""

    ValidationRules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.Windows.Controls.ValidationRule objects that validate the source objects in the System.Windows.Data.BindingGroup.

Get: ValidationRules(self: BindingGroup) -> Collection[ValidationRule]

"""



class CollectionView(DispatcherObject, ICollectionView, IEnumerable, INotifyCollectionChanged, INotifyPropertyChanged):
    """
    Represents a view for grouping, sorting, filtering, and navigating a data collection.
    
    CollectionView(collection: IEnumerable)
    """
    def add_CollectionChanged(self, *args): #cannot find CLR method
        """ add_CollectionChanged(self: CollectionView, value: NotifyCollectionChangedEventHandler) """
        pass

    def add_PropertyChanged(self, *args): #cannot find CLR method
        """ add_PropertyChanged(self: CollectionView, value: PropertyChangedEventHandler) """
        pass

    def ClearChangeLog(self, *args): #cannot find CLR method
        """
        ClearChangeLog(self: CollectionView)
            Clears any pending changes from the change log.
        """
        pass

    def ClearPendingChanges(self, *args): #cannot find CLR method
        """ ClearPendingChanges(self: CollectionView) """
        pass

    def Contains(self, item):
        """
        Contains(self: CollectionView, item: object) -> bool
        
            Returns a value that indicates whether the specified item belongs to the view.
        
            item: The object to check.
            Returns: true if the item belongs to the view; otherwise, false.
        """
        pass

    def DeferRefresh(self):
        """
        DeferRefresh(self: CollectionView) -> IDisposable
        
            Enters a defer cycle that you can use to merge changes to the view and delay automatic refresh.
            Returns: An System.IDisposable object that you can use to dispose of the calling object.
        """
        pass

    def DetachFromSourceCollection(self):
        """ DetachFromSourceCollection(self: CollectionView) """
        pass

    def GetEnumerator(self, *args): #cannot find CLR method
        """
        GetEnumerator(self: CollectionView) -> IEnumerator
        
            Returns an object that you can use to enumerate the items in the view.
            Returns: An System.Collections.IEnumerator object that you can use to enumerate the items in the view.
        """
        pass

    def GetItemAt(self, index):
        """
        GetItemAt(self: CollectionView, index: int) -> object
        
            Retrieves the item at the specified zero-based index in the view.
        
            index: The zero-based index of the item to retrieve.
            Returns: The item at the specified zero-based index in the view.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: CollectionView, item: object) -> int
        
            Returns the index at which the specified item is located.
        
            item: The item to locate.
                """
        pass

    def MoveCurrentTo(self, item):
        """
        MoveCurrentTo(self: CollectionView, item: object) -> bool
        
            Sets the specified item to be the System.Windows.Data.CollectionView.CurrentItem in the view.
        
            item: The item to set as the System.Windows.Data.CollectionView.CurrentItem.
            Returns: true if the resulting System.Windows.Data.CollectionView.CurrentItem is within the view; 
             otherwise, false.
        """
        pass

    def MoveCurrentToFirst(self):
        """
        MoveCurrentToFirst(self: CollectionView) -> bool
        
            Sets the first item in the view as the System.Windows.Data.CollectionView.CurrentItem.
            Returns: true if the resulting System.Windows.Data.CollectionView.CurrentItem is an item within the view; 
             otherwise, false.
        """
        pass

    def MoveCurrentToLast(self):
        """
        MoveCurrentToLast(self: CollectionView) -> bool
        
            Sets the last item in the view as the System.Windows.Data.CollectionView.CurrentItem.
            Returns: true if the resulting System.Windows.Data.CollectionView.CurrentItem is an item within the view; 
             otherwise, false.
        """
        pass

    def MoveCurrentToNext(self):
        """
        MoveCurrentToNext(self: CollectionView) -> bool
        
            Sets the item after the System.Windows.Data.CollectionView.CurrentItem in the view as the 
             System.Windows.Data.CollectionView.CurrentItem.
        
            Returns: true if the resulting System.Windows.Data.CollectionView.CurrentItem is an item within the view; 
             otherwise, false.
        """
        pass

    def MoveCurrentToPosition(self, position):
        """
        MoveCurrentToPosition(self: CollectionView, position: int) -> bool
        
            Sets the item at the specified index to be the System.Windows.Data.CollectionView.CurrentItem in 
             the view.
        
        
            position: The index to set the System.Windows.Data.CollectionView.CurrentItem to.
            Returns: true if the resulting System.Windows.Data.CollectionView.CurrentItem is an item within the view; 
             otherwise, false.
        """
        pass

    def MoveCurrentToPrevious(self):
        """
        MoveCurrentToPrevious(self: CollectionView) -> bool
        
            Sets the item before the System.Windows.Data.CollectionView.CurrentItem in the view as the 
             System.Windows.Data.CollectionView.CurrentItem.
        
            Returns: true if the resulting System.Windows.Data.CollectionView.CurrentItem is an item within the view; 
             otherwise, false.
        """
        pass

    def OKToChangeCurrent(self, *args): #cannot find CLR method
        """
        OKToChangeCurrent(self: CollectionView) -> bool
        
            Returns a value that indicates whether the view can change which item is the 
             System.Windows.Data.CollectionView.CurrentItem.
        
            Returns: false if a listener cancels the change; otherwise, true.
        """
        pass

    def OnAllowsCrossThreadChangesChanged(self, *args): #cannot find CLR method
        """ OnAllowsCrossThreadChangesChanged(self: CollectionView) """
        pass

    def OnBeginChangeLogging(self, *args): #cannot find CLR method
        """
        OnBeginChangeLogging(self: CollectionView, args: NotifyCollectionChangedEventArgs)
            Called by the base class to notify the derived class that an 
             System.Collections.Specialized.INotifyCollectionChanged.CollectionChanged event has been posted 
             to the message queue.
        
        
            args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object that is added to the 
             change log.
        """
        pass

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """
        OnCollectionChanged(self: CollectionView, sender: object, args: NotifyCollectionChangedEventArgs)
            Raises the System.Windows.Data.CollectionView.CollectionChanged event.
        
            sender: The sender of the event.
            args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object to pass to the event 
             handler.
        
        OnCollectionChanged(self: CollectionView, args: NotifyCollectionChangedEventArgs)
            Raises the System.Windows.Data.CollectionView.CollectionChanged event.
        
            args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object to pass to the event 
             handler.
        """
        pass

    def OnCurrentChanged(self, *args): #cannot find CLR method
        """
        OnCurrentChanged(self: CollectionView)
            Raises the System.Windows.Data.CollectionView.CurrentChanged event.
        """
        pass

    def OnCurrentChanging(self, *args): #cannot find CLR method
        """
        OnCurrentChanging(self: CollectionView, args: CurrentChangingEventArgs)
            Raises the System.Windows.Data.CollectionView.CurrentChanging event with the specified arguments.
        
            args: Information about the event.
        OnCurrentChanging(self: CollectionView)
            Raises a System.Windows.Data.CollectionView.CurrentChanging event that is not cancelable.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: CollectionView, e: PropertyChangedEventArgs)
            Raises the System.ComponentModel.INotifyPropertyChanged.PropertyChanged event using the 
             specified arguments.
        
        
            e: Arguments of the event being raised.
        """
        pass

    def PassesFilter(self, item):
        """
        PassesFilter(self: CollectionView, item: object) -> bool
        
            Returns a value that indicates whether the specified item in the underlying collection belongs 
             to the view.
        
        
            item: The item to check.
            Returns: true if the specified item belongs to the view or if there is not filter set on the collection 
             view; otherwise, false.
        """
        pass

    def ProcessCollectionChanged(self, *args): #cannot find CLR method
        """
        ProcessCollectionChanged(self: CollectionView, args: NotifyCollectionChangedEventArgs)
            When overridden in a derived class, processes a single change on the UI�thread.
        
            args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object to process.
        """
        pass

    def ProcessPendingChanges(self, *args): #cannot find CLR method
        """ ProcessPendingChanges(self: CollectionView) """
        pass

    def Refresh(self):
        """
        Refresh(self: CollectionView)
            Re-creates the view.
        """
        pass

    def RefreshOrDefer(self, *args): #cannot find CLR method
        """
        RefreshOrDefer(self: CollectionView)
            Refreshes the view or specifies that the view needs to be refreshed when the defer cycle 
             completes.
        """
        pass

    def RefreshOverride(self, *args): #cannot find CLR method
        """
        RefreshOverride(self: CollectionView)
            Re-creates the view.
        """
        pass

    def remove_CollectionChanged(self, *args): #cannot find CLR method
        """ remove_CollectionChanged(self: CollectionView, value: NotifyCollectionChangedEventHandler) """
        pass

    def remove_PropertyChanged(self, *args): #cannot find CLR method
        """ remove_PropertyChanged(self: CollectionView, value: PropertyChangedEventHandler) """
        pass

    def SetCurrent(self, *args): #cannot find CLR method
        """
        SetCurrent(self: CollectionView, newItem: object, newPosition: int, count: int)
            Sets the specified item and index as the values of the 
             System.Windows.Data.CollectionView.CurrentItem and 
             System.Windows.Data.CollectionView.CurrentPosition properties. This method can be called from a 
             constructor of a derived class.
        
        
            newItem: The item to set as the System.Windows.Data.CollectionView.CurrentItem.
            newPosition: The value to set as the System.Windows.Data.CollectionView.CurrentPosition property value.
            count: The number of items in the System.Windows.Data.CollectionView.
        SetCurrent(self: CollectionView, newItem: object, newPosition: int)
            Sets the specified item and index as the values of the 
             System.Windows.Data.CollectionView.CurrentItem and 
             System.Windows.Data.CollectionView.CurrentPosition properties.
        
        
            newItem: The item to set as the System.Windows.Data.CollectionView.CurrentItem.
            newPosition: The value to set as the System.Windows.Data.CollectionView.CurrentPosition property value.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, collection):
        """ __new__(cls: type, collection: IEnumerable) """
        pass

    AllowsCrossThreadChanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the view supports filtering.

Get: CanFilter(self: CollectionView) -> bool

"""

    CanGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the view supports grouping.

Get: CanGroup(self: CollectionView) -> bool

"""

    CanSort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the view supports sorting.

Get: CanSort(self: CollectionView) -> bool

"""

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns an object that you can use to compare items in the view.

Get: Comparer(self: CollectionView) -> IComparer

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of records in the view.

Get: Count(self: CollectionView) -> int

"""

    Culture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the culture information to use during sorting.

Get: Culture(self: CollectionView) -> CultureInfo

Set: Culture(self: CollectionView) = value
"""

    CurrentItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current item in the view.

Get: CurrentItem(self: CollectionView) -> object

"""

    CurrentPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ordinal position of the System.Windows.Data.CollectionView.CurrentItem within the (optionally sorted and filtered) view.

Get: CurrentPosition(self: CollectionView) -> int

"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a method used to determine if an item is suitable for inclusion in the view.

Get: Filter(self: CollectionView) -> Predicate[object]

Set: Filter(self: CollectionView) = value
"""

    GroupDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.ComponentModel.GroupDescription objects that describes how the items in the collection are grouped in the view.

Get: GroupDescriptions(self: CollectionView) -> ObservableCollection[GroupDescription]

"""

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of the top-level groups that is constructed based on the System.Windows.Data.CollectionView.GroupDescriptions property.

Get: Groups(self: CollectionView) -> ReadOnlyObservableCollection[object]

"""

    IsCurrentAfterLast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Data.CollectionView.CurrentItem of the view is beyond the end of the collection.

Get: IsCurrentAfterLast(self: CollectionView) -> bool

"""

    IsCurrentBeforeFirst = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Data.CollectionView.CurrentItem of the view is before the beginning of the collection.

Get: IsCurrentBeforeFirst(self: CollectionView) -> bool

"""

    IsCurrentInSync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Data.CollectionView.CurrentItem is at the System.Windows.Data.CollectionView.CurrentPosition.

"""

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the underlying collection provides change notifications.

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the resulting (filtered) view is empty.

Get: IsEmpty(self: CollectionView) -> bool

"""

    IsInUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInUse(self: CollectionView) -> bool

"""

    IsRefreshDeferred = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether there is an outstanding System.Windows.Data.CollectionView.DeferRefresh in use.

"""

    NeedsRefresh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the view needs to be refreshed.

Get: NeedsRefresh(self: CollectionView) -> bool

"""

    SortDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.ComponentModel.SortDescription structures that describes how the items in the collection are sorted in the view.

Get: SortDescriptions(self: CollectionView) -> SortDescriptionCollection

"""

    SourceCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the underlying unfiltered collection.

Get: SourceCollection(self: CollectionView) -> IEnumerable

"""

    UpdatedOutsideDispatcher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether it has been necessary to update the change log because a System.Windows.Data.CollectionView.CollectionChanged notification has been received on a different thread without first entering the user interface (UI) thread dispatcher.

"""


    CurrentChanged = None
    CurrentChanging = None
    NewItemPlaceholder = None


class BindingListCollectionView(CollectionView, ICollectionView, IEnumerable, INotifyCollectionChanged, INotifyPropertyChanged, IComparer, IEditableCollectionView, ICollectionViewLiveShaping, IItemProperties):
    """
    Represents the System.Windows.Data.CollectionView for collections that implement System.ComponentModel.IBindingList, such as Microsoft ActiveX Data Objects (ADO) data views.
    
    BindingListCollectionView(list: IBindingList)
    """
    def AddNew(self):
        """
        AddNew(self: BindingListCollectionView) -> object
        
            Starts an add transaction and returns the pending new item.
            Returns: The pending new item.
        """
        pass

    def add_CollectionChanged(self, *args): #cannot find CLR method
        """ add_CollectionChanged(self: CollectionView, value: NotifyCollectionChangedEventHandler) """
        pass

    def add_PropertyChanged(self, *args): #cannot find CLR method
        """ add_PropertyChanged(self: CollectionView, value: PropertyChangedEventHandler) """
        pass

    def CancelEdit(self):
        """
        CancelEdit(self: BindingListCollectionView)
            Ends the edit transaction and, if possible, restores the original value to the item.
        """
        pass

    def CancelNew(self):
        """
        CancelNew(self: BindingListCollectionView)
            Ends the add transaction and discards the pending new item.
        """
        pass

    def ClearChangeLog(self, *args): #cannot find CLR method
        """
        ClearChangeLog(self: CollectionView)
            Clears any pending changes from the change log.
        """
        pass

    def ClearPendingChanges(self, *args): #cannot find CLR method
        """ ClearPendingChanges(self: CollectionView) """
        pass

    def CommitEdit(self):
        """
        CommitEdit(self: BindingListCollectionView)
            Ends the edit transaction and saves the pending changes.
        """
        pass

    def CommitNew(self):
        """
        CommitNew(self: BindingListCollectionView)
            Ends the add transaction and saves the pending new item.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: BindingListCollectionView, item: object) -> bool
        
            Returns a value that indicates whether a given item belongs to the collection view.
        
            item: The object to check.
            Returns: true if the item belongs to the collection view; otherwise, false.
        """
        pass

    def DetachFromSourceCollection(self):
        """ DetachFromSourceCollection(self: BindingListCollectionView) """
        pass

    def EditItem(self, item):
        """
        EditItem(self: BindingListCollectionView, item: object)
            Begins an edit transaction of the specified item.
        
            item: The item to edit.
        """
        pass

    def GetEnumerator(self, *args): #cannot find CLR method
        """ GetEnumerator(self: BindingListCollectionView) -> IEnumerator """
        pass

    def GetItemAt(self, index):
        """
        GetItemAt(self: BindingListCollectionView, index: int) -> object
        
            Retrieves the item at the specified position in the view.
        
            index: The zero-based index at which the item is located.
            Returns: The item at the specified position in the view.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: BindingListCollectionView, item: object) -> int
        
            Returns the index at which the given item belongs in the collection view.
        
            item: The object to look for in the collection.
            Returns: The index of the item in the collection, or -1 if the item does not exist in the collection view.
        """
        pass

    def MoveCurrentToPosition(self, position):
        """
        MoveCurrentToPosition(self: BindingListCollectionView, position: int) -> bool
        
            Sets the item at the specified index to be the System.Windows.Data.CollectionView.CurrentItem in 
             the view.
        
        
            position: The index to set the System.Windows.Data.CollectionView.CurrentItem to.
            Returns: true if the resulting System.Windows.Data.CollectionView.CurrentItem is an item within the view; 
             otherwise, false.
        """
        pass

    def OKToChangeCurrent(self, *args): #cannot find CLR method
        """
        OKToChangeCurrent(self: CollectionView) -> bool
        
            Returns a value that indicates whether the view can change which item is the 
             System.Windows.Data.CollectionView.CurrentItem.
        
            Returns: false if a listener cancels the change; otherwise, true.
        """
        pass

    def OnAllowsCrossThreadChangesChanged(self, *args): #cannot find CLR method
        """ OnAllowsCrossThreadChangesChanged(self: BindingListCollectionView) """
        pass

    def OnBeginChangeLogging(self, *args): #cannot find CLR method
        """ OnBeginChangeLogging(self: BindingListCollectionView, args: NotifyCollectionChangedEventArgs) """
        pass

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """
        OnCollectionChanged(self: CollectionView, sender: object, args: NotifyCollectionChangedEventArgs)
            Raises the System.Windows.Data.CollectionView.CollectionChanged event.
        
            sender: The sender of the event.
            args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object to pass to the event 
             handler.
        
        OnCollectionChanged(self: CollectionView, args: NotifyCollectionChangedEventArgs)
            Raises the System.Windows.Data.CollectionView.CollectionChanged event.
        
            args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object to pass to the event 
             handler.
        """
        pass

    def OnCurrentChanged(self, *args): #cannot find CLR method
        """
        OnCurrentChanged(self: CollectionView)
            Raises the System.Windows.Data.CollectionView.CurrentChanged event.
        """
        pass

    def OnCurrentChanging(self, *args): #cannot find CLR method
        """
        OnCurrentChanging(self: CollectionView, args: CurrentChangingEventArgs)
            Raises the System.Windows.Data.CollectionView.CurrentChanging event with the specified arguments.
        
            args: Information about the event.
        OnCurrentChanging(self: CollectionView)
            Raises a System.Windows.Data.CollectionView.CurrentChanging event that is not cancelable.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: CollectionView, e: PropertyChangedEventArgs)
            Raises the System.ComponentModel.INotifyPropertyChanged.PropertyChanged event using the 
             specified arguments.
        
        
            e: Arguments of the event being raised.
        """
        pass

    def PassesFilter(self, item):
        """
        PassesFilter(self: BindingListCollectionView, item: object) -> bool
        
            Returns a value that indicates whether the specified item in the underlying collection belongs 
             to the view.
        
        
            item: The item to check.
            Returns: true if the specified item belongs to the view or if there is not filter set on the collection 
             view; otherwise, false.
        """
        pass

    def ProcessCollectionChanged(self, *args): #cannot find CLR method
        """ ProcessCollectionChanged(self: BindingListCollectionView, args: NotifyCollectionChangedEventArgs) """
        pass

    def ProcessPendingChanges(self, *args): #cannot find CLR method
        """ ProcessPendingChanges(self: CollectionView) """
        pass

    def RefreshOrDefer(self, *args): #cannot find CLR method
        """
        RefreshOrDefer(self: CollectionView)
            Refreshes the view or specifies that the view needs to be refreshed when the defer cycle 
             completes.
        """
        pass

    def RefreshOverride(self, *args): #cannot find CLR method
        """ RefreshOverride(self: BindingListCollectionView) """
        pass

    def Remove(self, item):
        """
        Remove(self: BindingListCollectionView, item: object)
            Removes the specified item from the collection.
        
            item: The item to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: BindingListCollectionView, index: int)
            Removes the item at the specified position from the collection.
        
            index: The zero-based index of the item to remove.
        """
        pass

    def remove_CollectionChanged(self, *args): #cannot find CLR method
        """ remove_CollectionChanged(self: CollectionView, value: NotifyCollectionChangedEventHandler) """
        pass

    def remove_PropertyChanged(self, *args): #cannot find CLR method
        """ remove_PropertyChanged(self: CollectionView, value: PropertyChangedEventHandler) """
        pass

    def SetCurrent(self, *args): #cannot find CLR method
        """
        SetCurrent(self: CollectionView, newItem: object, newPosition: int, count: int)
            Sets the specified item and index as the values of the 
             System.Windows.Data.CollectionView.CurrentItem and 
             System.Windows.Data.CollectionView.CurrentPosition properties. This method can be called from a 
             constructor of a derived class.
        
        
            newItem: The item to set as the System.Windows.Data.CollectionView.CurrentItem.
            newPosition: The value to set as the System.Windows.Data.CollectionView.CurrentPosition property value.
            count: The number of items in the System.Windows.Data.CollectionView.
        SetCurrent(self: CollectionView, newItem: object, newPosition: int)
            Sets the specified item and index as the values of the 
             System.Windows.Data.CollectionView.CurrentItem and 
             System.Windows.Data.CollectionView.CurrentPosition properties.
        
        
            newItem: The item to set as the System.Windows.Data.CollectionView.CurrentItem.
            newPosition: The value to set as the System.Windows.Data.CollectionView.CurrentPosition property value.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, list):
        """ __new__(cls: type, list: IBindingList) """
        pass

    AllowsCrossThreadChanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanAddNew = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a new item can be added to the collection.

Get: CanAddNew(self: BindingListCollectionView) -> bool

"""

    CanCancelEdit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection view can discard pending changes and restore the original values of an edited object.

Get: CanCancelEdit(self: BindingListCollectionView) -> bool

"""

    CanChangeLiveFiltering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveFiltering(self: BindingListCollectionView) -> bool

"""

    CanChangeLiveGrouping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveGrouping(self: BindingListCollectionView) -> bool

"""

    CanChangeLiveSorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveSorting(self: BindingListCollectionView) -> bool

"""

    CanCustomFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the view supports custom filtering.

Get: CanCustomFilter(self: BindingListCollectionView) -> bool

"""

    CanFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the view supports callback-based filtering.

Get: CanFilter(self: BindingListCollectionView) -> bool

"""

    CanGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the view supports grouping.

Get: CanGroup(self: BindingListCollectionView) -> bool

"""

    CanRemove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether an item can be removed from the collection.

Get: CanRemove(self: BindingListCollectionView) -> bool

"""

    CanSort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection supports sorting.

Get: CanSort(self: BindingListCollectionView) -> bool

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the estimated number of records in the collection.

Get: Count(self: BindingListCollectionView) -> int

"""

    CurrentAddItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item that is being added during the current add transaction.

Get: CurrentAddItem(self: BindingListCollectionView) -> object

"""

    CurrentEditItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item in the collection that is being edited.

Get: CurrentEditItem(self: BindingListCollectionView) -> object

"""

    CustomFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a custom filter.

Get: CustomFilter(self: BindingListCollectionView) -> str

Set: CustomFilter(self: BindingListCollectionView) = value
"""

    GroupBySelector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a delegate to select the System.ComponentModel.GroupDescription as a function of the parent group and its level.

Get: GroupBySelector(self: BindingListCollectionView) -> GroupDescriptionSelectorCallback

Set: GroupBySelector(self: BindingListCollectionView) = value
"""

    GroupDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.ComponentModel.GroupDescription objects that describe how the items in the collection are grouped in the view.

Get: GroupDescriptions(self: BindingListCollectionView) -> ObservableCollection[GroupDescription]

"""

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the top-level groups.

Get: Groups(self: BindingListCollectionView) -> ReadOnlyObservableCollection[object]

"""

    IsAddingNew = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether an add transaction is in progress.

Get: IsAddingNew(self: BindingListCollectionView) -> bool

"""

    IsCurrentInSync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Data.CollectionView.CurrentItem is at the System.Windows.Data.CollectionView.CurrentPosition.

"""

    IsDataInGroupOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the list of items (after applying the sort and filters, if any) is already in the correct order for grouping.

Get: IsDataInGroupOrder(self: BindingListCollectionView) -> bool

Set: IsDataInGroupOrder(self: BindingListCollectionView) = value
"""

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the underlying collection provides change notifications.

"""

    IsEditingItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether an edit transaction is in progress.

Get: IsEditingItem(self: BindingListCollectionView) -> bool

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a value that indicates whether the resulting (filtered) view is empty.

Get: IsEmpty(self: BindingListCollectionView) -> bool

"""

    IsLiveFiltering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveFiltering(self: BindingListCollectionView) -> Nullable[bool]

Set: IsLiveFiltering(self: BindingListCollectionView) = value
"""

    IsLiveGrouping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveGrouping(self: BindingListCollectionView) -> Nullable[bool]

Set: IsLiveGrouping(self: BindingListCollectionView) = value
"""

    IsLiveSorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveSorting(self: BindingListCollectionView) -> Nullable[bool]

Set: IsLiveSorting(self: BindingListCollectionView) = value
"""

    IsRefreshDeferred = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether there is an outstanding System.Windows.Data.CollectionView.DeferRefresh in use.

"""

    ItemProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of objects that describes the properties of the items in the collection.

Get: ItemProperties(self: BindingListCollectionView) -> ReadOnlyCollection[ItemPropertyInfo]

"""

    LiveFilteringProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveFilteringProperties(self: BindingListCollectionView) -> ObservableCollection[str]

"""

    LiveGroupingProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveGroupingProperties(self: BindingListCollectionView) -> ObservableCollection[str]

"""

    LiveSortingProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveSortingProperties(self: BindingListCollectionView) -> ObservableCollection[str]

"""

    NewItemPlaceholderPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position of the new item placeholder in the System.Windows.Data.BindingListCollectionView.

Get: NewItemPlaceholderPosition(self: BindingListCollectionView) -> NewItemPlaceholderPosition

Set: NewItemPlaceholderPosition(self: BindingListCollectionView) = value
"""

    SortDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.ComponentModel.SortDescription objects that describes how the items in the collection are sorted in the view.

Get: SortDescriptions(self: BindingListCollectionView) -> SortDescriptionCollection

"""

    UpdatedOutsideDispatcher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether it has been necessary to update the change log because a System.Windows.Data.CollectionView.CollectionChanged notification has been received on a different thread without first entering the user interface (UI) thread dispatcher.

"""



class BindingMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the direction of the data flow in a binding.
    
    enum BindingMode, values: Default (4), OneTime (2), OneWay (1), OneWayToSource (3), TwoWay (0)
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

    Default = None
    OneTime = None
    OneWay = None
    OneWayToSource = None
    TwoWay = None
    value__ = None


class BindingOperations(object):
    """ Provides static methods to manipulate bindings, including System.Windows.Data.Binding, System.Windows.Data.MultiBinding, and System.Windows.Data.PriorityBinding objects. """
    @staticmethod
    def AccessCollection(collection, accessMethod, writeAccess):
        """ AccessCollection(collection: IEnumerable, accessMethod: Action, writeAccess: bool) """
        pass

    @staticmethod
    def ClearAllBindings(target):
        """
        ClearAllBindings(target: DependencyObject)
            Removes all bindings, including bindings of type System.Windows.Data.Binding, 
             System.Windows.Data.MultiBinding, and System.Windows.Data.PriorityBinding, from the specified 
             System.Windows.DependencyObject.
        
        
            target: The object from which to remove bindings.
        """
        pass

    @staticmethod
    def ClearBinding(target, dp):
        """
        ClearBinding(target: DependencyObject, dp: DependencyProperty)
            Removes the binding from a property if there is one.
        
            target: The object from which to remove the binding.
            dp: The dependency property from which to remove the binding.
        """
        pass

    @staticmethod
    def DisableCollectionSynchronization(collection):
        """ DisableCollectionSynchronization(collection: IEnumerable) """
        pass

    @staticmethod
    def EnableCollectionSynchronization(collection, *__args):
        """ EnableCollectionSynchronization(collection: IEnumerable, lockObject: object)EnableCollectionSynchronization(collection: IEnumerable, context: object, synchronizationCallback: CollectionSynchronizationCallback) """
        pass

    @staticmethod
    def GetBinding(target, dp):
        """
        GetBinding(target: DependencyObject, dp: DependencyProperty) -> Binding
        
            Retrieves the System.Windows.Data.Binding object that is set on the specified property.
        
            target: The object where dp is.
            dp: The binding target property from which to retrieve the binding.
            Returns: The System.Windows.Data.Binding object set on the given property or null if no 
             System.Windows.Data.Binding object has been set.
        """
        pass

    @staticmethod
    def GetBindingBase(target, dp):
        """
        GetBindingBase(target: DependencyObject, dp: DependencyProperty) -> BindingBase
        
            Retrieves the System.Windows.Data.BindingBase object that is set on the specified property.
        
            target: The object where dp is.
            dp: The binding target property from which to retrieve the System.Windows.Data.BindingBase object.
            Returns: The System.Windows.Data.BindingBase object that is set on the given property or null if no 
             binding object has been set.
        """
        pass

    @staticmethod
    def GetBindingExpression(target, dp):
        """
        GetBindingExpression(target: DependencyObject, dp: DependencyProperty) -> BindingExpression
        
            Returns the System.Windows.Data.BindingExpression object associated with the specified binding 
             target property on the specified object.
        
        
            target: The binding target object where dp is.
            dp: The binding target property from which to retrieve the System.Windows.Data.BindingExpression 
             object.
        
            Returns: The System.Windows.Data.BindingExpression object associated with the given property or null if 
             none exists. If a System.Windows.Data.PriorityBindingExpression object is set on the property, 
             the System.Windows.Data.PriorityBindingExpression.ActiveBindingExpression is returned.
        """
        pass

    @staticmethod
    def GetBindingExpressionBase(target, dp):
        """
        GetBindingExpressionBase(target: DependencyObject, dp: DependencyProperty) -> BindingExpressionBase
        
            Retrieves the System.Windows.Data.BindingExpressionBase object that is set on the specified 
             property.
        
        
            target: The object where dp is.
            dp: The binding target property from which to retrieve the System.Windows.Data.BindingExpressionBase 
             object.
        
            Returns: The System.Windows.Data.BindingExpressionBase object that is set on the given property or null 
             if no binding object has been set.
        """
        pass

    @staticmethod
    def GetMultiBinding(target, dp):
        """
        GetMultiBinding(target: DependencyObject, dp: DependencyProperty) -> MultiBinding
        
            Retrieves the System.Windows.Data.MultiBinding object that is set on the specified property.
        
            target: The object where dp is.
            dp: The binding target property from which to retrieve the binding.
            Returns: The System.Windows.Data.MultiBinding object set on the given property or null if no 
             System.Windows.Data.MultiBinding object has been set.
        """
        pass

    @staticmethod
    def GetMultiBindingExpression(target, dp):
        """
        GetMultiBindingExpression(target: DependencyObject, dp: DependencyProperty) -> MultiBindingExpression
        
            Returns the System.Windows.Data.MultiBindingExpression object associated with the specified 
             binding target property on the specified object.
        
        
            target: The binding target object where dp is.
            dp: The binding target property from which to retrieve the 
             System.Windows.Data.MultiBindingExpression object.
        
            Returns: The System.Windows.Data.MultiBindingExpression object associated with the given property or null 
             if none exists.
        """
        pass

    @staticmethod
    def GetPriorityBinding(target, dp):
        """
        GetPriorityBinding(target: DependencyObject, dp: DependencyProperty) -> PriorityBinding
        
            Retrieves the System.Windows.Data.PriorityBinding object that is set on the specified property.
        
            target: The object where dp is.
            dp: The binding target property from which to retrieve the binding.
            Returns: The System.Windows.Data.PriorityBinding object set on the given property or null if no 
             System.Windows.Data.PriorityBinding object has been set.
        """
        pass

    @staticmethod
    def GetPriorityBindingExpression(target, dp):
        """
        GetPriorityBindingExpression(target: DependencyObject, dp: DependencyProperty) -> PriorityBindingExpression
        
            Returns the System.Windows.Data.PriorityBindingExpression object associated with the specified 
             binding target property on the specified object.
        
        
            target: The binding target object where dp is.
            dp: The binding target property from which to retrieve the 
             System.Windows.Data.PriorityBindingExpression object.
        
            Returns: The System.Windows.Data.PriorityBindingExpression object associated with the given property or 
             null if none exists.
        """
        pass

    @staticmethod
    def GetSourceUpdatingBindingGroups(root):
        """ GetSourceUpdatingBindingGroups(root: DependencyObject) -> ReadOnlyCollection[BindingGroup] """
        pass

    @staticmethod
    def GetSourceUpdatingBindings(root):
        """ GetSourceUpdatingBindings(root: DependencyObject) -> ReadOnlyCollection[BindingExpressionBase] """
        pass

    @staticmethod
    def IsDataBound(target, dp):
        """
        IsDataBound(target: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether the specified property is currently data-bound.
        
            target: The object where dp is.
            dp: The dependency property to check.
            Returns: true if the specified property is data-bound; otherwise, false.
        """
        pass

    @staticmethod
    def SetBinding(target, dp, binding):
        """
        SetBinding(target: DependencyObject, dp: DependencyProperty, binding: BindingBase) -> BindingExpressionBase
        
            Creates and associates a new instance of System.Windows.Data.BindingExpressionBase with the 
             specified binding target property.
        
        
            target: The binding target of the binding.
            dp: The target property of the binding.
            binding: The System.Windows.Data.BindingBase object that describes the binding.
            Returns: The instance of System.Windows.Data.BindingExpressionBase created for and associated with the 
             specified property. The System.Windows.Data.BindingExpressionBase class is the base class of 
             System.Windows.Data.BindingExpression, System.Windows.Data.MultiBindingExpression, and 
             System.Windows.Data.PriorityBindingExpression.
        """
        pass

    CollectionRegistering = None
    CollectionViewRegistering = None
    DisconnectedSource = None
    __all__ = [
        'AccessCollection',
        'ClearAllBindings',
        'ClearBinding',
        'CollectionRegistering',
        'CollectionViewRegistering',
        'DisableCollectionSynchronization',
        'EnableCollectionSynchronization',
        'GetBinding',
        'GetBindingBase',
        'GetBindingExpression',
        'GetBindingExpressionBase',
        'GetMultiBinding',
        'GetMultiBindingExpression',
        'GetPriorityBinding',
        'GetPriorityBindingExpression',
        'GetSourceUpdatingBindingGroups',
        'GetSourceUpdatingBindings',
        'IsDataBound',
        'SetBinding',
    ]


class BindingStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the status of a binding.
    
    enum BindingStatus, values: Active (2), AsyncRequestPending (4), Detached (3), Inactive (1), PathError (5), Unattached (0), UpdateSourceError (7), UpdateTargetError (6)
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

    Active = None
    AsyncRequestPending = None
    Detached = None
    Inactive = None
    PathError = None
    Unattached = None
    UpdateSourceError = None
    UpdateTargetError = None
    value__ = None


class CollectionContainer(DependencyObject, INotifyCollectionChanged, IWeakEventListener):
    """
    Holds an existing collection structure, such as an System.Collections.ObjectModel.ObservableCollection or a System.Data.DataSet, to be used inside a System.Windows.Data.CompositeCollection.
    
    CollectionContainer()
    """
    def add_CollectionChanged(self, *args): #cannot find CLR method
        """ add_CollectionChanged(self: CollectionContainer, value: NotifyCollectionChangedEventHandler) """
        pass

    def OnContainedCollectionChanged(self, *args): #cannot find CLR method
        """
        OnContainedCollectionChanged(self: CollectionContainer, args: NotifyCollectionChangedEventArgs)
            Raises the System.Windows.Data.CollectionContainer.CollectionChanged event.
        
            args: The event data.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DependencyObject, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.DependencyObject has been updated. The specific dependency property that changed 
             is reported in the event data.
        
        
            e: Event data that will contain the dependency property identifier of interest, the property 
             metadata for the type, and old and new values.
        """
        pass

    def ReceiveWeakEvent(self, *args): #cannot find CLR method
        """
        ReceiveWeakEvent(self: CollectionContainer, managerType: Type, sender: object, e: EventArgs) -> bool
        
            Handles events from the centralized event table.
        
            managerType: The type of the System.Windows.WeakEventManager calling this method. This only recognizes 
             manager objects of type System.Collections.Specialized.CollectionChangedEventManager.
        
            sender: The object that originated the event.
            e: The event data.
            Returns: true if the listener handled the event; otherwise, false.
        """
        pass

    def remove_CollectionChanged(self, *args): #cannot find CLR method
        """ remove_CollectionChanged(self: CollectionContainer, value: NotifyCollectionChangedEventHandler) """
        pass

    def ShouldSerializeCollection(self):
        """
        ShouldSerializeCollection(self: CollectionContainer) -> bool
        
            Indicates whether the System.Windows.Data.CollectionContainer.Collection property should be 
             persisted.
        
            Returns: true if the property value has changed from its default; otherwise, false.
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Collection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the collection to add.

Get: Collection(self: CollectionContainer) -> IEnumerable

Set: Collection(self: CollectionContainer) = value
"""


    CollectionProperty = None


class CollectionRegisteringEventArgs(EventArgs):
    # no doc
    Collection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Collection(self: CollectionRegisteringEventArgs) -> IEnumerable

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: CollectionRegisteringEventArgs) -> object

"""



class CollectionSynchronizationCallback(MulticastDelegate, ICloneable, ISerializable):
    """ CollectionSynchronizationCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, collection, context, accessMethod, writeAccess, callback, object):
        """ BeginInvoke(self: CollectionSynchronizationCallback, collection: IEnumerable, context: object, accessMethod: Action, writeAccess: bool, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: CollectionSynchronizationCallback, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, collection, context, accessMethod, writeAccess):
        """ Invoke(self: CollectionSynchronizationCallback, collection: IEnumerable, context: object, accessMethod: Action, writeAccess: bool) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class CollectionViewGroup(object, INotifyPropertyChanged):
    """ Represents a group created by a System.Windows.Data.CollectionView object based on the System.Windows.Data.CollectionView.GroupDescriptions. """
    def add_PropertyChanged(self, *args): #cannot find CLR method
        """ add_PropertyChanged(self: CollectionViewGroup, value: PropertyChangedEventHandler) """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: CollectionViewGroup, e: PropertyChangedEventArgs)
            Raises the System.Windows.Data.CollectionViewGroup.PropertyChanged event using the provided 
             arguments.
        
        
            e: Arguments of the event being raised.
        """
        pass

    def remove_PropertyChanged(self, *args): #cannot find CLR method
        """ remove_PropertyChanged(self: CollectionViewGroup, value: PropertyChangedEventHandler) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: object) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsBottomLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this group has any subgroups.

Get: IsBottomLevel(self: CollectionViewGroup) -> bool

"""

    ItemCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items in the subtree under this group.

Get: ItemCount(self: CollectionViewGroup) -> int

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the immediate items contained in this group.

Get: Items(self: CollectionViewGroup) -> ReadOnlyObservableCollection[object]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of this group.

Get: Name(self: CollectionViewGroup) -> object

"""

    ProtectedItemCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets the number of items in the subtree under this group.

"""

    ProtectedItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the immediate items contained in this group.

"""



class CollectionViewRegisteringEventArgs(EventArgs):
    # no doc
    CollectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollectionView(self: CollectionViewRegisteringEventArgs) -> CollectionView

"""



class CollectionViewSource(DependencyObject, ISupportInitialize, IWeakEventListener):
    """
    The Extensible Application Markup Language (XAML) proxy of a�System.Windows.Data.CollectionView class.
    
    CollectionViewSource()
    """
    def DeferRefresh(self):
        """
        DeferRefresh(self: CollectionViewSource) -> IDisposable
        
            Enters a defer cycle that you can use to merge changes to the view and delay automatic refresh.
            Returns: An System.IDisposable object that you can use to dispose of the calling object.
        """
        pass

    @staticmethod
    def GetDefaultView(source):
        """
        GetDefaultView(source: object) -> ICollectionView
        
            Returns the default view for the given source.
        
            source: An object reference to the binding source.
            Returns: Returns an System.ComponentModel.ICollectionView object that is the default view for the given 
             source collection.
        """
        pass

    @staticmethod
    def IsDefaultView(view):
        """
        IsDefaultView(view: ICollectionView) -> bool
        
            Returns a value that indicates whether the given view is the default view for the 
             System.Windows.Data.CollectionViewSource.Source collection.
        
        
            view: The view object to check.
            Returns: true if the given view is the default view for the 
             System.Windows.Data.CollectionViewSource.Source collection or if the given view is nulll; 
             otherwise, false.
        """
        pass

    def OnCollectionViewTypeChanged(self, *args): #cannot find CLR method
        """
        OnCollectionViewTypeChanged(self: CollectionViewSource, oldCollectionViewType: Type, newCollectionViewType: Type)
            Invoked when the System.Windows.Data.CollectionViewSource.CollectionViewType property changes.
        
            oldCollectionViewType: The old value of the System.Windows.Data.CollectionViewSource.CollectionViewType property.
            newCollectionViewType: The new value of the System.Windows.Data.CollectionViewSource.CollectionViewType property.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DependencyObject, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.DependencyObject has been updated. The specific dependency property that changed 
             is reported in the event data.
        
        
            e: Event data that will contain the dependency property identifier of interest, the property 
             metadata for the type, and old and new values.
        """
        pass

    def OnSourceChanged(self, *args): #cannot find CLR method
        """
        OnSourceChanged(self: CollectionViewSource, oldSource: object, newSource: object)
            Invoked when the System.Windows.Data.CollectionViewSource.Source property changes.
        
            oldSource: The old value of the System.Windows.Data.CollectionViewSource.Source property.
            newSource: The new value of the System.Windows.Data.CollectionViewSource.Source property.
        """
        pass

    def ReceiveWeakEvent(self, *args): #cannot find CLR method
        """
        ReceiveWeakEvent(self: CollectionViewSource, managerType: Type, sender: object, e: EventArgs) -> bool
        
            Handles events from the centralized event table.
        
            managerType: The type of the System.Windows.WeakEventManager calling this method. This only recognizes 
             manager objects of type System.Windows.Data.DataChangedEventManager.
        
            sender: Object that originated the event.
            e: Event data.
            Returns: true if the listener handled the event; otherwise, false.
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CanChangeLiveFiltering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveFiltering(self: CollectionViewSource) -> bool

"""

    CanChangeLiveGrouping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveGrouping(self: CollectionViewSource) -> bool

"""

    CanChangeLiveSorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveSorting(self: CollectionViewSource) -> bool

"""

    CollectionViewType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the desired view type.

Get: CollectionViewType(self: CollectionViewSource) -> Type

Set: CollectionViewType(self: CollectionViewSource) = value
"""

    Culture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the culture that is used for operations such as sorting and comparisons.

Get: Culture(self: CollectionViewSource) -> CultureInfo

Set: Culture(self: CollectionViewSource) = value
"""

    GroupDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a collection of System.ComponentModel.GroupDescription objects that describes how the items in the collection are grouped in the view.

Get: GroupDescriptions(self: CollectionViewSource) -> ObservableCollection[GroupDescription]

"""

    IsLiveFiltering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveFiltering(self: CollectionViewSource) -> Nullable[bool]

"""

    IsLiveFilteringRequested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveFilteringRequested(self: CollectionViewSource) -> bool

Set: IsLiveFilteringRequested(self: CollectionViewSource) = value
"""

    IsLiveGrouping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveGrouping(self: CollectionViewSource) -> Nullable[bool]

"""

    IsLiveGroupingRequested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveGroupingRequested(self: CollectionViewSource) -> bool

Set: IsLiveGroupingRequested(self: CollectionViewSource) = value
"""

    IsLiveSorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveSorting(self: CollectionViewSource) -> Nullable[bool]

"""

    IsLiveSortingRequested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveSortingRequested(self: CollectionViewSource) -> bool

Set: IsLiveSortingRequested(self: CollectionViewSource) = value
"""

    LiveFilteringProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveFilteringProperties(self: CollectionViewSource) -> ObservableCollection[str]

"""

    LiveGroupingProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveGroupingProperties(self: CollectionViewSource) -> ObservableCollection[str]

"""

    LiveSortingProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveSortingProperties(self: CollectionViewSource) -> ObservableCollection[str]

"""

    SortDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a collection of System.ComponentModel.SortDescription objects that describes how the items in the collection are sorted in the view.

Get: SortDescriptions(self: CollectionViewSource) -> SortDescriptionCollection

"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the collection object from which to create this view.

Get: Source(self: CollectionViewSource) -> object

Set: Source(self: CollectionViewSource) = value
"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the view object that is currently associated with this instance of System.Windows.Data.CollectionViewSource.

Get: View(self: CollectionViewSource) -> ICollectionView

"""


    CanChangeLiveFilteringProperty = None
    CanChangeLiveGroupingProperty = None
    CanChangeLiveSortingProperty = None
    CollectionViewTypeProperty = None
    Filter = None
    IsLiveFilteringProperty = None
    IsLiveFilteringRequestedProperty = None
    IsLiveGroupingProperty = None
    IsLiveGroupingRequestedProperty = None
    IsLiveSortingProperty = None
    IsLiveSortingRequestedProperty = None
    SourceProperty = None
    ViewProperty = None


class CompositeCollection(object, IList, ICollection, IEnumerable, INotifyCollectionChanged, ICollectionViewFactory, IWeakEventListener):
    """
    Enables multiple collections and items to be displayed as a single list.
    
    CompositeCollection()
    CompositeCollection(capacity: int)
    """
    def Add(self, newItem):
        """
        Add(self: CompositeCollection, newItem: object) -> int
        
            Adds the specified item to this collection.
        
            newItem: New item to add to the collection.
            Returns: Zero-based index where the new item is added.
        """
        pass

    def add_CollectionChanged(self, *args): #cannot find CLR method
        """ add_CollectionChanged(self: CompositeCollection, value: NotifyCollectionChangedEventHandler) """
        pass

    def Clear(self):
        """
        Clear(self: CompositeCollection)
            Clears the collection.
        """
        pass

    def Contains(self, containItem):
        """
        Contains(self: CompositeCollection, containItem: object) -> bool
        
            Checks to see if a given item is in this collection.
        
            containItem: The item to check.
            Returns: true if the collection contains the given item; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CompositeCollection, array: Array, index: int)
            Makes a shallow copy of object references from this collection to the given array.
        
            array: The array that is the destination of the copy operation.
            index: Zero-based index in the target array at which the copying starts.
        """
        pass

    def IndexOf(self, indexItem):
        """
        IndexOf(self: CompositeCollection, indexItem: object) -> int
        
            Returns the index in this collection where the given item is found.
        
            indexItem: The item to retrieve the index for.
            Returns: If the item appears in the collection, then the zero-based index in the collection where the 
             given item is found; otherwise, -1.
        """
        pass

    def Insert(self, insertIndex, insertItem):
        """
        Insert(self: CompositeCollection, insertIndex: int, insertItem: object)
            Inserts an item in the collection at a given index. All items after the given position are moved 
             down by one.
        
        
            insertIndex: The index to insert the item at.
            insertItem: The item reference to add to the collection.
        """
        pass

    def ReceiveWeakEvent(self, *args): #cannot find CLR method
        """
        ReceiveWeakEvent(self: CompositeCollection, managerType: Type, sender: object, e: EventArgs) -> bool
        
            Handles events from the centralized event table.
        
            managerType: The type of the System.Windows.WeakEventManager calling this method. This only recognizes 
             manager objects of type System.Collections.Specialized.CollectionChangedEventManager.
        
            sender: Object that originated the event.
            e: Event data.
            Returns: true if the listener handled the event; otherwise, false.
        """
        pass

    def Remove(self, removeItem):
        """
        Remove(self: CompositeCollection, removeItem: object)
            Removes the given item reference from the collection. All remaining items move up by one.
        
            removeItem: The item to remove.
        """
        pass

    def RemoveAt(self, removeIndex):
        """
        RemoveAt(self: CompositeCollection, removeIndex: int)
            Removes an item from the collection at the given index. All remaining items move up by one.
        
            removeIndex: The index at which to remove an item.
        """
        pass

    def remove_CollectionChanged(self, *args): #cannot find CLR method
        """ remove_CollectionChanged(self: CompositeCollection, value: NotifyCollectionChangedEventHandler) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
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
    def __new__(self, capacity=None):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items stored in this collection.

Get: Count(self: CompositeCollection) -> int

"""



class DataChangedEventManager(WeakEventManager):
    """ Provides a System.Windows.WeakEventManager implementation so that you can use the "weak event listener" pattern to attach listeners for the System.Windows.Data.DataSourceProvider.DataChanged event. """
    @staticmethod
    def AddHandler(source, handler):
        """ AddHandler(source: DataSourceProvider, handler: EventHandler[EventArgs]) """
        pass

    @staticmethod
    def AddListener(source, listener):
        """
        AddListener(source: DataSourceProvider, listener: IWeakEventListener)
            Adds the specified listener to the System.Windows.Data.DataSourceProvider.DataChanged event of 
             the specified source.
        
        
            source: The object with the event.
            listener: The object to add as a listener.
        """
        pass

    @staticmethod
    def RemoveHandler(source, handler):
        """ RemoveHandler(source: DataSourceProvider, handler: EventHandler[EventArgs]) """
        pass

    @staticmethod
    def RemoveListener(source, listener):
        """
        RemoveListener(source: DataSourceProvider, listener: IWeakEventListener)
            Removes the specified listener from the System.Windows.Data.DataSourceProvider.DataChanged event 
             of the specified source.
        
        
            source: The object with the event.
            listener: The listener to remove.
        """
        pass

    ReadLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Establishes a read-lock on the underlying data table, and returns an System.IDisposable.

"""

    WriteLock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Establishes a write-lock on the underlying data table, and returns an System.IDisposable.

"""



class DataTransferEventArgs(RoutedEventArgs):
    """ Encapsulates arguments for data transfer events. """
    Property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the specific binding target property that is involved in the data transfer event.

Get: Property(self: DataTransferEventArgs) -> DependencyProperty

"""

    TargetObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the binding target object of the binding that raised the event.

Get: TargetObject(self: DataTransferEventArgs) -> DependencyObject

"""



class FilterEventArgs(EventArgs):
    """ Provides information and event data that is associated with the System.Windows.Data.CollectionViewSource.Filter event. """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Accepted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the item passes the filter.

Get: Accepted(self: FilterEventArgs) -> bool

Set: Accepted(self: FilterEventArgs) = value
"""

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object that the filter should test.

Get: Item(self: FilterEventArgs) -> object

"""



class FilterEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Data.CollectionViewSource.Filter event.
    
    FilterEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: FilterEventHandler, sender: object, e: FilterEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FilterEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: FilterEventHandler, sender: object, e: FilterEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class GroupDescriptionSelectorCallback(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents a method that is used to provide custom logic to select the System.ComponentModel.GroupDescription based on the parent group and its level.
    
    GroupDescriptionSelectorCallback(object: object, method: IntPtr)
    """
    def BeginInvoke(self, group, level, callback, object):
        """ BeginInvoke(self: GroupDescriptionSelectorCallback, group: CollectionViewGroup, level: int, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GroupDescriptionSelectorCallback, result: IAsyncResult) -> GroupDescription """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, group, level):
        """ Invoke(self: GroupDescriptionSelectorCallback, group: CollectionViewGroup, level: int) -> GroupDescription """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class IMultiValueConverter:
    """ Provides a way to apply custom logic in a System.Windows.Data.MultiBinding. """
    def Convert(self, values, targetType, parameter, culture):
        """
        Convert(self: IMultiValueConverter, values: Array[object], targetType: Type, parameter: object, culture: CultureInfo) -> object
        
            Converts source values to a value for the binding target. The data binding engine calls this 
             method when it propagates the values from source bindings to the binding target.
        
        
            values: The array of values that the source bindings in the System.Windows.Data.MultiBinding produces. 
             The value System.Windows.DependencyProperty.UnsetValue indicates that the source binding has no 
             value to provide for conversion.
        
            targetType: The type of the binding target property.
            parameter: The converter parameter to use.
            culture: The culture to use in the converter.
            Returns: A converted value.If the method returns null, the valid null value is used.A return value of 
             System.Windows.DependencyProperty.System.Windows.DependencyProperty.UnsetValue indicates that 
             the converter did not produce a value, and that the binding will use the 
             System.Windows.Data.BindingBase.FallbackValue if it is available, or else will use the default 
             value.A return value of System.Windows.Data.Binding.System.Windows.Data.Binding.DoNothing 
             indicates that the binding does not transfer the value or use the 
             System.Windows.Data.BindingBase.FallbackValue or the default value.
        """
        pass

    def ConvertBack(self, value, targetTypes, parameter, culture):
        """
        ConvertBack(self: IMultiValueConverter, value: object, targetTypes: Array[Type], parameter: object, culture: CultureInfo) -> Array[object]
        
            Converts a binding target value to the source binding values.
        
            value: The value that the binding target produces.
            targetTypes: The array of types to convert to. The array length indicates the number and types of values that 
             are suggested for the method to return.
        
            parameter: The converter parameter to use.
            culture: The culture to use in the converter.
            Returns: An array of values that have been converted from the target value back to the source values.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IValueConverter:
    """ Provides a way to apply custom logic to a binding. """
    def Convert(self, value, targetType, parameter, culture):
        """
        Convert(self: IValueConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object
        
            Converts a value.
        
            value: The value produced by the binding source.
            targetType: The type of the binding target property.
            parameter: The converter parameter to use.
            culture: The culture to use in the converter.
            Returns: A converted value. If the method returns null, the valid null value is used.
        """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """
        ConvertBack(self: IValueConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object
        
            Converts a value.
        
            value: The value that is produced by the binding target.
            targetType: The type to convert to.
            parameter: The converter parameter to use.
            culture: The culture to use in the converter.
            Returns: A converted value. If the method returns null, the valid null value is used.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ListCollectionView(CollectionView, ICollectionView, IEnumerable, INotifyCollectionChanged, INotifyPropertyChanged, IComparer, IEditableCollectionViewAddNewItem, IEditableCollectionView, ICollectionViewLiveShaping, IItemProperties):
    """
    Represents the collection view for collections that implement System.Collections.IList.
    
    ListCollectionView(list: IList)
    """
    def AddNew(self):
        """
        AddNew(self: ListCollectionView) -> object
        
            Starts an add transaction and returns the pending new item.
            Returns: The pending new item.
        """
        pass

    def AddNewItem(self, newItem):
        """
        AddNewItem(self: ListCollectionView, newItem: object) -> object
        
            Adds the specified object to the collection.
        
            newItem: The object to add to the collection.
            Returns: The object that was added to the collection.
        """
        pass

    def add_CollectionChanged(self, *args): #cannot find CLR method
        """ add_CollectionChanged(self: CollectionView, value: NotifyCollectionChangedEventHandler) """
        pass

    def add_PropertyChanged(self, *args): #cannot find CLR method
        """ add_PropertyChanged(self: CollectionView, value: PropertyChangedEventHandler) """
        pass

    def CancelEdit(self):
        """
        CancelEdit(self: ListCollectionView)
            Ends the edit transaction, and if possible, restores the original value to the item.
        """
        pass

    def CancelNew(self):
        """
        CancelNew(self: ListCollectionView)
            Ends the add transaction and discards the pending new item.
        """
        pass

    def ClearChangeLog(self, *args): #cannot find CLR method
        """
        ClearChangeLog(self: CollectionView)
            Clears any pending changes from the change log.
        """
        pass

    def ClearPendingChanges(self, *args): #cannot find CLR method
        """ ClearPendingChanges(self: CollectionView) """
        pass

    def CommitEdit(self):
        """
        CommitEdit(self: ListCollectionView)
            Ends the edit transaction and saves the pending changes.
        """
        pass

    def CommitNew(self):
        """
        CommitNew(self: ListCollectionView)
            Ends the add transaction and saves the pending new item.
        """
        pass

    def Compare(self, *args): #cannot find CLR method
        """
        Compare(self: ListCollectionView, o1: object, o2: object) -> int
        
            Compares two objects and returns a value that indicates whether one is less than, equal to, or 
             greater than the other.
        
        
            o1: The first object to compare.
            o2: The second object to compare.
            Returns: Less than zero if o1 is less than o2, zero if o1 and o2 are equal, or greater than zero if o1 is 
             greater than o2.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: ListCollectionView, item: object) -> bool
        
            Returns a value that indicates whether a given item belongs to the collection view.
        
            item: The object to check.
            Returns: true if the item belongs to the collection view; otherwise, false.
        """
        pass

    def EditItem(self, item):
        """
        EditItem(self: ListCollectionView, item: object)
            Begins an edit transaction of the specified item.
        
            item: The item to edit.
        """
        pass

    def GetEnumerator(self, *args): #cannot find CLR method
        """
        GetEnumerator(self: ListCollectionView) -> IEnumerator
        
            Returns an object that you can use to enumerate the items in the view.
            Returns: An System.Collections.IEnumerator object that you can use to enumerate the items in the view.
        """
        pass

    def GetItemAt(self, index):
        """
        GetItemAt(self: ListCollectionView, index: int) -> object
        
            Retrieves the item at the specified position in the view.
        
            index: The zero-based index at which the item is located.
            Returns: The item at the specified position in the view.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: ListCollectionView, item: object) -> int
        
            Returns the index where the given data item belongs in the collection, or -1 if the index of 
             that item is unknown.
        
        
            item: The object to check for in the collection.
            Returns: The index of the item in the collection, or -1 if the item does not exist in the collection.
        """
        pass

    def InternalContains(self, *args): #cannot find CLR method
        """
        InternalContains(self: ListCollectionView, item: object) -> bool
        
            Return a value that indicates whether the System.Windows.Data.ListCollectionView.InternalList 
             contains the item.
        
        
            item: The item to locate.
            Returns: true if the System.Windows.Data.ListCollectionView.InternalList contains the item; otherwise, 
             false.
        """
        pass

    def InternalGetEnumerator(self, *args): #cannot find CLR method
        """
        InternalGetEnumerator(self: ListCollectionView) -> IEnumerator
        
            Returns an enumerator for the System.Windows.Data.ListCollectionView.InternalList.
            Returns: An enumerator for the System.Windows.Data.ListCollectionView.InternalList.
        """
        pass

    def InternalIndexOf(self, *args): #cannot find CLR method
        """
        InternalIndexOf(self: ListCollectionView, item: object) -> int
        
            Returns the index of the specified item in the 
             System.Windows.Data.ListCollectionView.InternalList.
        
        
            item: The item to return an index for.
            Returns: The index of the specified item in the System.Windows.Data.ListCollectionView.InternalList.
        """
        pass

    def InternalItemAt(self, *args): #cannot find CLR method
        """
        InternalItemAt(self: ListCollectionView, index: int) -> object
        
            Returns the item at the given index in the System.Windows.Data.ListCollectionView.InternalList.
        
            index: The index at which the item is located.
            Returns: The item at the specified zero-based index in the view.
        """
        pass

    def MoveCurrentToPosition(self, position):
        """
        MoveCurrentToPosition(self: ListCollectionView, position: int) -> bool
        
            Sets the item at the specified index to be the System.Windows.Data.CollectionView.CurrentItem in 
             the view.
        
        
            position: The index to set the System.Windows.Data.CollectionView.CurrentItem to.
            Returns: true if the resulting System.Windows.Data.CollectionView.CurrentItem is an item within the view; 
             otherwise, false.
        """
        pass

    def OKToChangeCurrent(self, *args): #cannot find CLR method
        """
        OKToChangeCurrent(self: CollectionView) -> bool
        
            Returns a value that indicates whether the view can change which item is the 
             System.Windows.Data.CollectionView.CurrentItem.
        
            Returns: false if a listener cancels the change; otherwise, true.
        """
        pass

    def OnAllowsCrossThreadChangesChanged(self, *args): #cannot find CLR method
        """ OnAllowsCrossThreadChangesChanged(self: ListCollectionView) """
        pass

    def OnBeginChangeLogging(self, *args): #cannot find CLR method
        """
        OnBeginChangeLogging(self: ListCollectionView, args: NotifyCollectionChangedEventArgs)
            Called by the base class to notify the derived class that a 
             System.Collections.Specialized.INotifyCollectionChanged.CollectionChanged event has been posted 
             to the message queue.
        
        
            args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object that is added to the 
             change log.
        """
        pass

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """
        OnCollectionChanged(self: CollectionView, sender: object, args: NotifyCollectionChangedEventArgs)
            Raises the System.Windows.Data.CollectionView.CollectionChanged event.
        
            sender: The sender of the event.
            args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object to pass to the event 
             handler.
        
        OnCollectionChanged(self: CollectionView, args: NotifyCollectionChangedEventArgs)
            Raises the System.Windows.Data.CollectionView.CollectionChanged event.
        
            args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object to pass to the event 
             handler.
        """
        pass

    def OnCurrentChanged(self, *args): #cannot find CLR method
        """
        OnCurrentChanged(self: CollectionView)
            Raises the System.Windows.Data.CollectionView.CurrentChanged event.
        """
        pass

    def OnCurrentChanging(self, *args): #cannot find CLR method
        """
        OnCurrentChanging(self: CollectionView, args: CurrentChangingEventArgs)
            Raises the System.Windows.Data.CollectionView.CurrentChanging event with the specified arguments.
        
            args: Information about the event.
        OnCurrentChanging(self: CollectionView)
            Raises a System.Windows.Data.CollectionView.CurrentChanging event that is not cancelable.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: CollectionView, e: PropertyChangedEventArgs)
            Raises the System.ComponentModel.INotifyPropertyChanged.PropertyChanged event using the 
             specified arguments.
        
        
            e: Arguments of the event being raised.
        """
        pass

    def PassesFilter(self, item):
        """
        PassesFilter(self: ListCollectionView, item: object) -> bool
        
            Returns a value that indicates whether the specified item in the underlying collection belongs 
             to the view.
        
        
            item: The item to check.
            Returns: true if the specified item belongs to the view or if there is not filter set on the collection 
             view; otherwise, false.
        """
        pass

    def ProcessCollectionChanged(self, *args): #cannot find CLR method
        """
        ProcessCollectionChanged(self: ListCollectionView, args: NotifyCollectionChangedEventArgs)
            Handles System.Collections.Specialized.INotifyCollectionChanged.CollectionChanged events.
        
            args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object to process.
        """
        pass

    def ProcessPendingChanges(self, *args): #cannot find CLR method
        """ ProcessPendingChanges(self: CollectionView) """
        pass

    def RefreshOrDefer(self, *args): #cannot find CLR method
        """
        RefreshOrDefer(self: CollectionView)
            Refreshes the view or specifies that the view needs to be refreshed when the defer cycle 
             completes.
        """
        pass

    def RefreshOverride(self, *args): #cannot find CLR method
        """
        RefreshOverride(self: ListCollectionView)
            Recreates the view.
        """
        pass

    def Remove(self, item):
        """
        Remove(self: ListCollectionView, item: object)
            Removes the specified item from the collection.
        
            item: The item to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: ListCollectionView, index: int)
            Removes the item at the specified position from the collection.
        
            index: The zero-based index of the item to remove.
        """
        pass

    def remove_CollectionChanged(self, *args): #cannot find CLR method
        """ remove_CollectionChanged(self: CollectionView, value: NotifyCollectionChangedEventHandler) """
        pass

    def remove_PropertyChanged(self, *args): #cannot find CLR method
        """ remove_PropertyChanged(self: CollectionView, value: PropertyChangedEventHandler) """
        pass

    def SetCurrent(self, *args): #cannot find CLR method
        """
        SetCurrent(self: CollectionView, newItem: object, newPosition: int, count: int)
            Sets the specified item and index as the values of the 
             System.Windows.Data.CollectionView.CurrentItem and 
             System.Windows.Data.CollectionView.CurrentPosition properties. This method can be called from a 
             constructor of a derived class.
        
        
            newItem: The item to set as the System.Windows.Data.CollectionView.CurrentItem.
            newPosition: The value to set as the System.Windows.Data.CollectionView.CurrentPosition property value.
            count: The number of items in the System.Windows.Data.CollectionView.
        SetCurrent(self: CollectionView, newItem: object, newPosition: int)
            Sets the specified item and index as the values of the 
             System.Windows.Data.CollectionView.CurrentItem and 
             System.Windows.Data.CollectionView.CurrentPosition properties.
        
        
            newItem: The item to set as the System.Windows.Data.CollectionView.CurrentItem.
            newPosition: The value to set as the System.Windows.Data.CollectionView.CurrentPosition property value.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, list):
        """ __new__(cls: type, list: IList) """
        pass

    ActiveComparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current active comparer that is used in sorting.

"""

    ActiveFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current active System.Windows.Data.CollectionView.Filter callback.

"""

    AllowsCrossThreadChanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanAddNew = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a new item can be added to the collection.

Get: CanAddNew(self: ListCollectionView) -> bool

"""

    CanAddNewItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a specified object can be added to the collection.

Get: CanAddNewItem(self: ListCollectionView) -> bool

"""

    CanCancelEdit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection view can discard pending changes and restore the original values of an edited object.

Get: CanCancelEdit(self: ListCollectionView) -> bool

"""

    CanChangeLiveFiltering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveFiltering(self: ListCollectionView) -> bool

"""

    CanChangeLiveGrouping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveGrouping(self: ListCollectionView) -> bool

"""

    CanChangeLiveSorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeLiveSorting(self: ListCollectionView) -> bool

"""

    CanFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the view supports callback-based filtering.

Get: CanFilter(self: ListCollectionView) -> bool

"""

    CanGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection view supports grouping.

Get: CanGroup(self: ListCollectionView) -> bool

"""

    CanRemove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether an item can be removed from the collection.

Get: CanRemove(self: ListCollectionView) -> bool

"""

    CanSort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection view supports sorting.

Get: CanSort(self: ListCollectionView) -> bool

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the estimated number of records.

Get: Count(self: ListCollectionView) -> int

"""

    CurrentAddItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item that is being added during the current add transaction.

Get: CurrentAddItem(self: ListCollectionView) -> object

"""

    CurrentEditItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item in the collection that is being edited.

Get: CurrentEditItem(self: ListCollectionView) -> object

"""

    CustomSort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a custom object that implements System.Collections.IComparer to sort items in the view.

Get: CustomSort(self: ListCollectionView) -> IComparer

Set: CustomSort(self: ListCollectionView) = value
"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a method that is used to determine whether an item is suitable for inclusion in the view.

Get: Filter(self: ListCollectionView) -> Predicate[object]

Set: Filter(self: ListCollectionView) = value
"""

    GroupBySelector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a delegate to select the System.ComponentModel.GroupDescription as a function of the parent group and its level.

Get: GroupBySelector(self: ListCollectionView) -> GroupDescriptionSelectorCallback

Set: GroupBySelector(self: ListCollectionView) = value
"""

    GroupDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.ComponentModel.GroupDescription objects that describe how the items in the collection are grouped in the view.

Get: GroupDescriptions(self: ListCollectionView) -> ObservableCollection[GroupDescription]

"""

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the top-level groups.

Get: Groups(self: ListCollectionView) -> ReadOnlyObservableCollection[object]

"""

    InternalCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of records in the System.Windows.Data.ListCollectionView.InternalList.

"""

    InternalList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the complete and unfiltered underlying collection.

"""

    IsAddingNew = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether an add transaction is in progress.

Get: IsAddingNew(self: ListCollectionView) -> bool

"""

    IsCurrentInSync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Data.CollectionView.CurrentItem is at the System.Windows.Data.CollectionView.CurrentPosition.

"""

    IsDataInGroupOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the list of items (after applying the sort and filters, if any) is already in the correct order for grouping.

Get: IsDataInGroupOrder(self: ListCollectionView) -> bool

Set: IsDataInGroupOrder(self: ListCollectionView) = value
"""

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the underlying collection provides change notifications.

"""

    IsEditingItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether an edit transaction is in progress.

Get: IsEditingItem(self: ListCollectionView) -> bool

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a value that indicates whether the resulting (filtered) view is empty.

Get: IsEmpty(self: ListCollectionView) -> bool

"""

    IsGrouping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether there are groups in the view.

"""

    IsLiveFiltering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveFiltering(self: ListCollectionView) -> Nullable[bool]

Set: IsLiveFiltering(self: ListCollectionView) = value
"""

    IsLiveGrouping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveGrouping(self: ListCollectionView) -> Nullable[bool]

Set: IsLiveGrouping(self: ListCollectionView) = value
"""

    IsLiveSorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiveSorting(self: ListCollectionView) -> Nullable[bool]

Set: IsLiveSorting(self: ListCollectionView) = value
"""

    IsRefreshDeferred = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether there is an outstanding System.Windows.Data.CollectionView.DeferRefresh in use.

"""

    ItemProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of objects that describes the properties of the items in the collection.

Get: ItemProperties(self: ListCollectionView) -> ReadOnlyCollection[ItemPropertyInfo]

"""

    LiveFilteringProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveFilteringProperties(self: ListCollectionView) -> ObservableCollection[str]

"""

    LiveGroupingProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveGroupingProperties(self: ListCollectionView) -> ObservableCollection[str]

"""

    LiveSortingProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveSortingProperties(self: ListCollectionView) -> ObservableCollection[str]

"""

    NewItemPlaceholderPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position of the new item placeholder in the System.Windows.Data.ListCollectionView.

Get: NewItemPlaceholderPosition(self: ListCollectionView) -> NewItemPlaceholderPosition

Set: NewItemPlaceholderPosition(self: ListCollectionView) = value
"""

    SortDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.ComponentModel.SortDescription objects that describes how the items in the collection are sorted in the view.

Get: SortDescriptions(self: ListCollectionView) -> SortDescriptionCollection

"""

    UpdatedOutsideDispatcher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether it has been necessary to update the change log because a System.Windows.Data.CollectionView.CollectionChanged notification has been received on a different thread without first entering the user interface (UI) thread dispatcher.

"""

    UsesLocalArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a private copy of the data is needed for sorting and filtering.

"""



class MultiBinding(BindingBase, IAddChild):
    """
    Describes a collection of System.Windows.Data.Binding objects attached to a single binding target property.
    
    MultiBinding()
    """
    def ShouldSerializeBindings(self):
        """
        ShouldSerializeBindings(self: MultiBinding) -> bool
        
            Indicates whether the System.Windows.Data.MultiBinding.Bindings property should be persisted.
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def ShouldSerializeValidationRules(self):
        """
        ShouldSerializeValidationRules(self: MultiBinding) -> bool
        
            Indicates whether the System.Windows.Data.MultiBinding.ValidationRules property should be 
             persisted.
        
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Data.Binding objects within this System.Windows.Data.MultiBinding instance.

Get: Bindings(self: MultiBinding) -> Collection[BindingBase]

"""

    Converter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the converter to use to convert the source values to or from the target value.

Get: Converter(self: MultiBinding) -> IMultiValueConverter

Set: Converter(self: MultiBinding) = value
"""

    ConverterCulture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Globalization.CultureInfo object that applies to any converter assigned to bindings wrapped by the System.Windows.Data.MultiBinding or on the System.Windows.Data.MultiBinding itself.

Get: ConverterCulture(self: MultiBinding) -> CultureInfo

Set: ConverterCulture(self: MultiBinding) = value
"""

    ConverterParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an optional parameter to pass to a converter as additional information.

Get: ConverterParameter(self: MultiBinding) -> object

Set: ConverterParameter(self: MultiBinding) = value
"""

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the direction of the data flow of this binding.

Get: Mode(self: MultiBinding) -> BindingMode

Set: Mode(self: MultiBinding) = value
"""

    NotifyOnSourceUpdated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to raise the System.Windows.FrameworkElement.SourceUpdated event when a value is transferred from the binding target to the binding source.

Get: NotifyOnSourceUpdated(self: MultiBinding) -> bool

Set: NotifyOnSourceUpdated(self: MultiBinding) = value
"""

    NotifyOnTargetUpdated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to raise the System.Windows.FrameworkElement.TargetUpdated event when a value is transferred from the binding source to the binding target.

Get: NotifyOnTargetUpdated(self: MultiBinding) -> bool

Set: NotifyOnTargetUpdated(self: MultiBinding) = value
"""

    NotifyOnValidationError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to raise the System.Windows.Controls.Validation.Error�attached event on the bound element.

Get: NotifyOnValidationError(self: MultiBinding) -> bool

Set: NotifyOnValidationError(self: MultiBinding) = value
"""

    UpdateSourceExceptionFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a handler you can use to provide custom logic for handling exceptions that the binding engine encounters during the update of the binding source value. This is only applicable if you have associated the System.Windows.Controls.ExceptionValidationRule with your System.Windows.Data.MultiBinding object.

Get: UpdateSourceExceptionFilter(self: MultiBinding) -> UpdateSourceExceptionFilterCallback

Set: UpdateSourceExceptionFilter(self: MultiBinding) = value
"""

    UpdateSourceTrigger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines the timing of binding source updates.

Get: UpdateSourceTrigger(self: MultiBinding) -> UpdateSourceTrigger

Set: UpdateSourceTrigger(self: MultiBinding) = value
"""

    ValidatesOnDataErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to include the System.Windows.Controls.DataErrorValidationRule.

Get: ValidatesOnDataErrors(self: MultiBinding) -> bool

Set: ValidatesOnDataErrors(self: MultiBinding) = value
"""

    ValidatesOnExceptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to include the System.Windows.Controls.ExceptionValidationRule.

Get: ValidatesOnExceptions(self: MultiBinding) -> bool

Set: ValidatesOnExceptions(self: MultiBinding) = value
"""

    ValidatesOnNotifyDataErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidatesOnNotifyDataErrors(self: MultiBinding) -> bool

Set: ValidatesOnNotifyDataErrors(self: MultiBinding) = value
"""

    ValidationRules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Controls.ValidationRule objects for this instance of System.Windows.Data.MultiBinding.

Get: ValidationRules(self: MultiBinding) -> Collection[ValidationRule]

"""



class MultiBindingExpression(BindingExpressionBase, IWeakEventListener, IDataBindEngineClient):
    """ Contains instance information about a single instance of a System.Windows.Data.MultiBinding. """
    def UpdateSource(self):
        """
        UpdateSource(self: MultiBindingExpression)
            Sends the current binding target value to the binding source properties in 
             System.Windows.Data.BindingMode.TwoWay or System.Windows.Data.BindingMode.OneWayToSource 
             bindings.
        """
        pass

    def UpdateTarget(self):
        """
        UpdateTarget(self: MultiBindingExpression)
            Forces a data transfer from the binding source properties to the binding target property.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BindingExpressions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Data.BindingExpression objects in this instance of System.Windows.Data.MultiBindingExpression.

Get: BindingExpressions(self: MultiBindingExpression) -> ReadOnlyCollection[BindingExpressionBase]

"""

    HasError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a value that indicates whether any of the inner System.Windows.Data.Binding objects or the System.Windows.Data.MultiBinding itself has a failing validation rule.

Get: HasError(self: MultiBindingExpression) -> bool

"""

    HasValidationError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasValidationError(self: MultiBindingExpression) -> bool

"""

    ParentMultiBinding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Data.MultiBinding object from which this System.Windows.Data.MultiBindingExpression is created.

Get: ParentMultiBinding(self: MultiBindingExpression) -> MultiBinding

"""

    ValidationError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Controls.ValidationError object that caused this instance of System.Windows.Data.MultiBindingExpression to be invalid.

Get: ValidationError(self: MultiBindingExpression) -> ValidationError

"""



class ObjectDataProvider(DataSourceProvider, INotifyPropertyChanged, ISupportInitialize):
    """
    Wraps and creates an object that you can use as a binding source.
    
    ObjectDataProvider()
    """
    def add_PropertyChanged(self, *args): #cannot find CLR method
        """ add_PropertyChanged(self: DataSourceProvider, value: PropertyChangedEventHandler) """
        pass

    def BeginInit(self, *args): #cannot find CLR method
        """
        BeginInit(self: DataSourceProvider)
            Indicates that initialization of this object is about to begin; no implicit 
             System.Windows.Data.DataSourceProvider.Refresh occurs until the matched 
             System.Windows.Data.DataSourceProvider.EndInit method is called.
        """
        pass

    def BeginQuery(self, *args): #cannot find CLR method
        """
        BeginQuery(self: ObjectDataProvider)
            Starts to create the requested object, either immediately or on a background thread, based on 
             the value of the System.Windows.Data.ObjectDataProvider.IsAsynchronous property.
        """
        pass

    def EndInit(self, *args): #cannot find CLR method
        """
        EndInit(self: DataSourceProvider)
            Indicates that the initialization of this object has completed; this causes a 
             System.Windows.Data.DataSourceProvider.Refresh if no other 
             System.Windows.Data.DataSourceProvider.DeferRefresh is outstanding.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DataSourceProvider, e: PropertyChangedEventArgs)
            Raises the System.Windows.Data.DataSourceProvider.PropertyChanged event with the provided 
             arguments.
        
        
            e: Arguments of the event being raised.
        """
        pass

    def OnQueryFinished(self, *args): #cannot find CLR method
        """
        OnQueryFinished(self: DataSourceProvider, newData: object, error: Exception, completionWork: DispatcherOperationCallback, callbackArguments: object)
            Derived classes call this method to indicate that a query has finished.
        
            newData: The data that is the result of the query.
            error: The error that occurred while running the query. This value is null if there is no error.
            completionWork: Optional delegate that is used to execute completion work on the UI thread, for example, to set 
             additional properties.
        
            callbackArguments: Optional arguments to send as a parameter with the completionWork delegate.
        OnQueryFinished(self: DataSourceProvider, newData: object)
            Derived classes call this method to indicate that a query has finished.
        
            newData: The data that is the result of the query.
        """
        pass

    def remove_PropertyChanged(self, *args): #cannot find CLR method
        """ remove_PropertyChanged(self: DataSourceProvider, value: PropertyChangedEventHandler) """
        pass

    def ShouldSerializeConstructorParameters(self):
        """
        ShouldSerializeConstructorParameters(self: ObjectDataProvider) -> bool
        
            Indicates whether the System.Windows.Data.ObjectDataProvider.ConstructorParameters property 
             should be persisted.
        
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def ShouldSerializeMethodParameters(self):
        """
        ShouldSerializeMethodParameters(self: ObjectDataProvider) -> bool
        
            Indicates whether the System.Windows.Data.ObjectDataProvider.MethodParameters property should be 
             persisted.
        
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def ShouldSerializeObjectInstance(self):
        """
        ShouldSerializeObjectInstance(self: ObjectDataProvider) -> bool
        
            Indicates whether the System.Windows.Data.ObjectDataProvider.ObjectInstance property should be 
             persisted.
        
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def ShouldSerializeObjectType(self):
        """
        ShouldSerializeObjectType(self: ObjectDataProvider) -> bool
        
            Indicates whether the System.Windows.Data.ObjectDataProvider.ObjectType property should be 
             persisted.
        
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ConstructorParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of parameters to pass to the constructor.

Get: ConstructorParameters(self: ObjectDataProvider) -> IList

"""

    Dispatcher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current System.Windows.Threading.Dispatcher object to the UI�thread to use.

"""

    IsAsynchronous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to perform object creation in a worker thread or in the active context.

Get: IsAsynchronous(self: ObjectDataProvider) -> bool

Set: IsAsynchronous(self: ObjectDataProvider) = value
"""

    IsRefreshDeferred = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether there is an outstanding System.Windows.Data.DataSourceProvider.DeferRefresh in use.

"""

    MethodName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the method to call.

Get: MethodName(self: ObjectDataProvider) -> str

Set: MethodName(self: ObjectDataProvider) = value
"""

    MethodParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of parameters to pass to the method.

Get: MethodParameters(self: ObjectDataProvider) -> IList

"""

    ObjectInstance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object used as the binding source.

Get: ObjectInstance(self: ObjectDataProvider) -> object

Set: ObjectInstance(self: ObjectDataProvider) = value
"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of object to create an instance of.

Get: ObjectType(self: ObjectDataProvider) -> Type

Set: ObjectType(self: ObjectDataProvider) = value
"""



class PriorityBinding(BindingBase, IAddChild):
    """
    Describes a collection of System.Windows.Data.Binding objects that is attached to a single binding target property, which receives its value from the first binding in the collection that produces a value successfully.
    
    PriorityBinding()
    """
    def ShouldSerializeBindings(self):
        """
        ShouldSerializeBindings(self: PriorityBinding) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the effective 
             value of the System.Windows.Data.PriorityBinding.Bindings property on instances of this class.
        
            Returns: true if the System.Windows.Data.PriorityBinding.Bindings property value should be serialized; 
             otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Data.Binding objects that is established for this instance of System.Windows.Data.PriorityBinding.

Get: Bindings(self: PriorityBinding) -> Collection[BindingBase]

"""



class PriorityBindingExpression(BindingExpressionBase, IWeakEventListener):
    """ Contains instance information about a single instance of a System.Windows.Data.PriorityBinding. """
    def UpdateSource(self):
        """
        UpdateSource(self: PriorityBindingExpression)
            Updates the source on the active binding.
        """
        pass

    def UpdateTarget(self):
        """
        UpdateTarget(self: PriorityBindingExpression)
            Updates the target on the active binding.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ActiveBindingExpression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the active System.Windows.Data.BindingExpression object.

Get: ActiveBindingExpression(self: PriorityBindingExpression) -> BindingExpressionBase

"""

    BindingExpressions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Data.BindingExpression objects inside this instance of System.Windows.Data.PriorityBindingExpression.

Get: BindingExpressions(self: PriorityBindingExpression) -> ReadOnlyCollection[BindingExpressionBase]

"""

    HasValidationError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasValidationError(self: PriorityBindingExpression) -> bool

"""

    ParentPriorityBinding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Data.PriorityBinding object from which this System.Windows.Data.PriorityBindingExpression is created.

Get: ParentPriorityBinding(self: PriorityBindingExpression) -> PriorityBinding

"""



class PropertyGroupDescription(GroupDescription, INotifyPropertyChanged):
    """
    Describes the grouping of items using a property name as the criteria.
    
    PropertyGroupDescription()
    PropertyGroupDescription(propertyName: str)
    PropertyGroupDescription(propertyName: str, converter: IValueConverter)
    PropertyGroupDescription(propertyName: str, converter: IValueConverter, stringComparison: StringComparison)
    """
    def add_PropertyChanged(self, *args): #cannot find CLR method
        """ add_PropertyChanged(self: GroupDescription, value: PropertyChangedEventHandler) """
        pass

    def GroupNameFromItem(self, item, level, culture):
        """
        GroupNameFromItem(self: PropertyGroupDescription, item: object, level: int, culture: CultureInfo) -> object
        
            Returns the group name(s) for the given item.
        
            item: The item to return group names for.
            level: The level of grouping.
            culture: The System.Globalization.CultureInfo to supply to the converter.
            Returns: The group name(s) for the given item.
        """
        pass

    def NamesMatch(self, groupName, itemName):
        """
        NamesMatch(self: PropertyGroupDescription, groupName: object, itemName: object) -> bool
        
            Returns a value that indicates whether the group name and the item name match so that the item 
             belongs to the group.
        
        
            groupName: The name of the group to check.
            itemName: The name of the item to check.
            Returns: true if the names match and the item belongs to the group; otherwise, false.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: GroupDescription, e: PropertyChangedEventArgs)
            Raises the System.ComponentModel.GroupDescription.PropertyChanged event.
        
            e: Arguments of the event being raised.
        """
        pass

    def remove_PropertyChanged(self, *args): #cannot find CLR method
        """ remove_PropertyChanged(self: GroupDescription, value: PropertyChangedEventHandler) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, propertyName=None, converter=None, stringComparison=None):
        """
        __new__(cls: type)
        __new__(cls: type, propertyName: str)
        __new__(cls: type, propertyName: str, converter: IValueConverter)
        __new__(cls: type, propertyName: str, converter: IValueConverter, stringComparison: StringComparison)
        """
        pass

    Converter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a converter to apply to the property value or the item to produce the final value that is used to determine which group(s) an item belongs to.

Get: Converter(self: PropertyGroupDescription) -> IValueConverter

Set: Converter(self: PropertyGroupDescription) = value
"""

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the property that is used to determine which group(s) an item belongs to.

Get: PropertyName(self: PropertyGroupDescription) -> str

Set: PropertyName(self: PropertyGroupDescription) = value
"""

    StringComparison = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.StringComparison value that specifies the comparison between the value of an item (as determined by System.Windows.Data.PropertyGroupDescription.PropertyName and System.Windows.Data.PropertyGroupDescription.Converter) and the name of a group.

Get: StringComparison(self: PropertyGroupDescription) -> StringComparison

Set: StringComparison(self: PropertyGroupDescription) = value
"""


    CompareNameAscending = None
    CompareNameDescending = None


class RelativeSource(MarkupExtension, ISupportInitialize):
    """
    Implements a markup extension that describes the location of the binding source relative to the position of the binding target.
    
    RelativeSource()
    RelativeSource(mode: RelativeSourceMode)
    RelativeSource(mode: RelativeSourceMode, ancestorType: Type, ancestorLevel: int)
    """
    def ProvideValue(self, serviceProvider):
        """
        ProvideValue(self: RelativeSource, serviceProvider: IServiceProvider) -> object
        
            Returns an object that should be set as the value on the target object's property for this 
             markup extension. For System.Windows.Data.RelativeSource, this is another 
             System.Windows.Data.RelativeSource, using the appropriate source for the specified mode.
        
        
            serviceProvider: An object that can provide services for the markup extension. In this implementation, this 
             parameter can be null.
        
            Returns: Another System.Windows.Data.RelativeSource.
        """
        pass

    def ShouldSerializeAncestorLevel(self):
        """
        ShouldSerializeAncestorLevel(self: RelativeSource) -> bool
        
            Indicates whether the System.Windows.Data.RelativeSource.AncestorLevel property should be 
             persisted.
        
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def ShouldSerializeAncestorType(self):
        """
        ShouldSerializeAncestorType(self: RelativeSource) -> bool
        
            Indicates whether the System.Windows.Data.RelativeSource.AncestorType property should be 
             persisted.
        
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, mode=None, ancestorType=None, ancestorLevel=None):
        """
        __new__(cls: type)
        __new__(cls: type, mode: RelativeSourceMode)
        __new__(cls: type, mode: RelativeSourceMode, ancestorType: Type, ancestorLevel: int)
        """
        pass

    AncestorLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the level of ancestor to look for, in System.Windows.Data.RelativeSourceMode.FindAncestor mode. Use 1 to indicate the one nearest to the binding target element.

Get: AncestorLevel(self: RelativeSource) -> int

Set: AncestorLevel(self: RelativeSource) = value
"""

    AncestorType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of ancestor to look for.

Get: AncestorType(self: RelativeSource) -> Type

Set: AncestorType(self: RelativeSource) = value
"""

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Data.RelativeSourceMode value that describes the location of the binding source relative to the position of the binding target.

Get: Mode(self: RelativeSource) -> RelativeSourceMode

Set: Mode(self: RelativeSource) = value
"""


    PreviousData = None
    Self = None
    TemplatedParent = None


class RelativeSourceMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the location of the binding source relative to the position of the binding target.
    
    enum RelativeSourceMode, values: FindAncestor (3), PreviousData (0), Self (2), TemplatedParent (1)
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

    FindAncestor = None
    PreviousData = None
    Self = None
    TemplatedParent = None
    value__ = None


class UpdateSourceExceptionFilterCallback(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles exceptions that are thrown during the update of the binding source value. This must be used with the System.Windows.Controls.ExceptionValidationRule.
    
    UpdateSourceExceptionFilterCallback(object: object, method: IntPtr)
    """
    def BeginInvoke(self, bindExpression, exception, callback, object):
        """ BeginInvoke(self: UpdateSourceExceptionFilterCallback, bindExpression: object, exception: Exception, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: UpdateSourceExceptionFilterCallback, result: IAsyncResult) -> object """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, bindExpression, exception):
        """ Invoke(self: UpdateSourceExceptionFilterCallback, bindExpression: object, exception: Exception) -> object """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class UpdateSourceTrigger(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the timing of binding source updates.
    
    enum UpdateSourceTrigger, values: Default (0), Explicit (3), LostFocus (2), PropertyChanged (1)
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

    Default = None
    Explicit = None
    LostFocus = None
    PropertyChanged = None
    value__ = None


class ValueConversionAttribute(Attribute, _Attribute):
    """
    Represents an attribute that allows the author of a value converter to specify the data types involved in the implementation of the converter.
    
    ValueConversionAttribute(sourceType: Type, targetType: Type)
    """
    def GetHashCode(self):
        """
        GetHashCode(self: ValueConversionAttribute) -> int
        
            Returns the hash code for this instance of System.Windows.Data.ValueConversionAttribute.
            Returns: The hash code for this instance of System.Windows.Data.ValueConversionAttribute.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sourceType, targetType):
        """ __new__(cls: type, sourceType: Type, targetType: Type) """
        pass

    ParameterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets the type of the optional value converter parameter object.

Get: ParameterType(self: ValueConversionAttribute) -> Type

Set: ParameterType(self: ValueConversionAttribute) = value
"""

    SourceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type this converter converts.

Get: SourceType(self: ValueConversionAttribute) -> Type

"""

    TargetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type this converter converts to.

Get: TargetType(self: ValueConversionAttribute) -> Type

"""

    TypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unique identifier of this System.Windows.Data.ValueConversionAttribute instance.

Get: TypeId(self: ValueConversionAttribute) -> object

"""



class ValueUnavailableException(SystemException, ISerializable, _Exception):
    """
    The exception that is thrown by the System.Windows.Data.BindingGroup.GetValue(System.Object,System.String) method when the value is not available.
    
    ValueUnavailableException()
    ValueUnavailableException(message: str)
    ValueUnavailableException(message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class XmlDataProvider(DataSourceProvider, INotifyPropertyChanged, ISupportInitialize, IUriContext):
    """
    Enables declarative access to XML data for data binding.
    
    XmlDataProvider()
    """
    def add_PropertyChanged(self, *args): #cannot find CLR method
        """ add_PropertyChanged(self: DataSourceProvider, value: PropertyChangedEventHandler) """
        pass

    def BeginInit(self, *args): #cannot find CLR method
        """
        BeginInit(self: DataSourceProvider)
            Indicates that initialization of this object is about to begin; no implicit 
             System.Windows.Data.DataSourceProvider.Refresh occurs until the matched 
             System.Windows.Data.DataSourceProvider.EndInit method is called.
        """
        pass

    def BeginQuery(self, *args): #cannot find CLR method
        """
        BeginQuery(self: XmlDataProvider)
            Prepares the loading of either the inline XML or the external XML file to produce a collection 
             of XML nodes.
        """
        pass

    def EndInit(self, *args): #cannot find CLR method
        """
        EndInit(self: XmlDataProvider)
            Indicates that the initialization of this element has completed; this causes a 
             System.Windows.Data.DataSourceProvider.Refresh if no other 
             System.Windows.Data.DataSourceProvider.DeferRefresh is outstanding.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DataSourceProvider, e: PropertyChangedEventArgs)
            Raises the System.Windows.Data.DataSourceProvider.PropertyChanged event with the provided 
             arguments.
        
        
            e: Arguments of the event being raised.
        """
        pass

    def OnQueryFinished(self, *args): #cannot find CLR method
        """
        OnQueryFinished(self: DataSourceProvider, newData: object, error: Exception, completionWork: DispatcherOperationCallback, callbackArguments: object)
            Derived classes call this method to indicate that a query has finished.
        
            newData: The data that is the result of the query.
            error: The error that occurred while running the query. This value is null if there is no error.
            completionWork: Optional delegate that is used to execute completion work on the UI thread, for example, to set 
             additional properties.
        
            callbackArguments: Optional arguments to send as a parameter with the completionWork delegate.
        OnQueryFinished(self: DataSourceProvider, newData: object)
            Derived classes call this method to indicate that a query has finished.
        
            newData: The data that is the result of the query.
        """
        pass

    def remove_PropertyChanged(self, *args): #cannot find CLR method
        """ remove_PropertyChanged(self: DataSourceProvider, value: PropertyChangedEventHandler) """
        pass

    def ShouldSerializeSource(self):
        """
        ShouldSerializeSource(self: XmlDataProvider) -> bool
        
            Indicates whether the System.Windows.Data.XmlDataProvider.Source property should be persisted.
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def ShouldSerializeXmlSerializer(self):
        """
        ShouldSerializeXmlSerializer(self: XmlDataProvider) -> bool
        
            Indicates whether the System.Windows.Data.XmlDataProvider.XmlSerializer property should be 
             persisted.
        
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def ShouldSerializeXPath(self):
        """
        ShouldSerializeXPath(self: XmlDataProvider) -> bool
        
            Indicates whether the System.Windows.Data.XmlDataProvider.XPath property should be persisted.
            Returns: true if the property value has changed from its default; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BaseUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This type or member supports the WPF infrastructure and is not intended to be used directly from your code.

"""

    Dispatcher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current System.Windows.Threading.Dispatcher object to the UI�thread to use.

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Xml.XmlDocument to use as the binding source.

Get: Document(self: XmlDataProvider) -> XmlDocument

Set: Document(self: XmlDataProvider) = value
"""

    IsAsynchronous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether node collection creation will be performed in a worker thread or in the active context.

Get: IsAsynchronous(self: XmlDataProvider) -> bool

Set: IsAsynchronous(self: XmlDataProvider) = value
"""

    IsRefreshDeferred = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether there is an outstanding System.Windows.Data.DataSourceProvider.DeferRefresh in use.

"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Uri of the XML data file to use as the binding source.

Get: Source(self: XmlDataProvider) -> Uri

Set: Source(self: XmlDataProvider) = value
"""

    XmlNamespaceManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Xml.XmlNamespaceManager used to run System.Windows.Data.XmlDataProvider.XPath queries.

Get: XmlNamespaceManager(self: XmlDataProvider) -> XmlNamespaceManager

Set: XmlNamespaceManager(self: XmlDataProvider) = value
"""

    XmlSerializer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the inline XML content.

Get: XmlSerializer(self: XmlDataProvider) -> IXmlSerializable

"""

    XPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the XPath query used to generate the data collection.

Get: XPath(self: XmlDataProvider) -> str

Set: XPath(self: XmlDataProvider) = value
"""



class XmlNamespaceMapping(object, ISupportInitialize):
    """
    Declares a mapping between a uniform resource identifier (URI) and a prefix.
    
    XmlNamespaceMapping()
    XmlNamespaceMapping(prefix: str, uri: Uri)
    """
    def Equals(self, obj):
        """
        Equals(self: XmlNamespaceMapping, obj: object) -> bool
        
            Returns a value that indicates whether this System.Windows.Data.XmlNamespaceMapping is 
             equivalent to the specified instance.
        
        
            obj: The instance to compare for equality.
            Returns: true if the two instances are the same; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: XmlNamespaceMapping) -> int
        
            Returns the hash code for this System.Windows.Data.XmlNamespaceMapping.
            Returns: The hash code for this System.Windows.Data.XmlNamespaceMapping.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, prefix=None, uri=None):
        """
        __new__(cls: type)
        __new__(cls: type, prefix: str, uri: Uri)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the prefix to use in Extensible Application Markup Language (XAML).

Get: Prefix(self: XmlNamespaceMapping) -> str

Set: Prefix(self: XmlNamespaceMapping) = value
"""

    Uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Uri of the namespace for which to create a mapping.

Get: Uri(self: XmlNamespaceMapping) -> Uri

Set: Uri(self: XmlNamespaceMapping) = value
"""



class XmlNamespaceMappingCollection(XmlNamespaceManager, IXmlNamespaceResolver, IEnumerable, ICollection[XmlNamespaceMapping], IEnumerable[XmlNamespaceMapping], IAddChildInternal, IAddChild):
    """
    Represents a collection of System.Windows.Data.XmlNamespaceMapping objects.
    
    XmlNamespaceMappingCollection()
    """
    def Add(self, mapping):
        """
        Add(self: XmlNamespaceMappingCollection, mapping: XmlNamespaceMapping)
            Adds a System.Windows.Data.XmlNamespaceMapping object to this collection.
        
            mapping: The System.Windows.Data.XmlNamespaceMapping object to add. This cannot be null.
        """
        pass

    def AddChild(self, *args): #cannot find CLR method
        """
        AddChild(self: XmlNamespaceMappingCollection, value: object)
            Adds a System.Windows.Data.XmlNamespaceMapping object to this collection.
        
            value: The System.Windows.Data.XmlNamespaceMapping object to add. This cannot be null.
        """
        pass

    def AddText(self, *args): #cannot find CLR method
        """
        AddText(self: XmlNamespaceMappingCollection, text: str)
            Adds a text string as a child of this System.Windows.Data.XmlNamespaceMappingCollection object.
        
            text: The text string to add as a child.
        """
        pass

    def Clear(self):
        """
        Clear(self: XmlNamespaceMappingCollection)
            Removes all System.Windows.Data.XmlNamespaceMapping objects in this collection.
        """
        pass

    def Contains(self, mapping):
        """
        Contains(self: XmlNamespaceMappingCollection, mapping: XmlNamespaceMapping) -> bool
        
            Returns a value that indicates whether this collection contains the specified 
             System.Windows.Data.XmlNamespaceMapping object.
        
        
            mapping: The System.Windows.Data.XmlNamespaceMapping object of interest. This cannot be null.
            Returns: true if this collection contains the specified System.Windows.Data.XmlNamespaceMapping object; 
             otherwise, false.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """
        CopyTo(self: XmlNamespaceMappingCollection, array: Array[XmlNamespaceMapping], arrayIndex: int)
            Copies the items of the collection to the specified array, starting at the specified index.
        
            array: The array that is the destination of the items copied from the collection.
            arrayIndex: The zero-based index in array at which copying starts.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: XmlNamespaceMappingCollection) -> IEnumerator
        
            Returns an System.Collections.IEnumerator object that you can use to enumerate the items in this 
             collection.
        
            Returns: An System.Collections.IEnumerator object that you can use to enumerate the items in this 
             collection.
        """
        pass

    def ProtectedGetEnumerator(self, *args): #cannot find CLR method
        """
        ProtectedGetEnumerator(self: XmlNamespaceMappingCollection) -> IEnumerator[XmlNamespaceMapping]
        
            Returns a generic System.Collections.Generic.IEnumerator object.
            Returns: A generic System.Collections.Generic.IEnumerator object.
        """
        pass

    def Remove(self, mapping):
        """
        Remove(self: XmlNamespaceMappingCollection, mapping: XmlNamespaceMapping) -> bool
        
            Removes the specified System.Windows.Data.XmlNamespaceMapping object from this collection.
        
            mapping: The System.Windows.Data.XmlNamespaceMapping object to remove. This cannot be null.
            Returns: true if the specified System.Windows.Data.XmlNamespaceMapping object has been successfully 
             removed; otherwise, false.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[XmlNamespaceMapping], item: XmlNamespaceMapping) -> bool """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Windows.Data.XmlNamespaceMapping objects in the collection.

Get: Count(self: XmlNamespaceMappingCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this collection is read-only.

Get: IsReadOnly(self: XmlNamespaceMappingCollection) -> bool

"""



