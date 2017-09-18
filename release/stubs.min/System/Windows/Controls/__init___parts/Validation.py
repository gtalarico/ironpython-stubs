class Validation(object):
 """ Provides methods and attached properties that support data validation. """
 @staticmethod
 def AddErrorHandler(element,handler):
  """ AddErrorHandler(element: DependencyObject,handler: EventHandler[ValidationErrorEventArgs]) """
  pass
 @staticmethod
 def ClearInvalid(bindingExpression):
  """
  ClearInvalid(bindingExpression: BindingExpressionBase)

   Removes all System.Windows.Controls.ValidationError objects from the specified 

    System.Windows.Data.BindingExpressionBase object.

  

  

   bindingExpression: The object to turn valid.
  """
  pass
 @staticmethod
 def GetErrors(element):
  """
  GetErrors(element: DependencyObject) -> ReadOnlyObservableCollection[ValidationError]

  

   Gets the value of the System.Windows.Controls.Validation.Errors�attached property of the 

    specified element.

  

  

   element: The System.Windows.UIElement or System.Windows.ContentElement object to read the value from.

   Returns: A System.Collections.ObjectModel.ReadOnlyObservableCollection of 

    System.Windows.Controls.ValidationError objects.
  """
  pass
 @staticmethod
 def GetErrorTemplate(element):
  """
  GetErrorTemplate(element: DependencyObject) -> ControlTemplate

  

   Gets the value of the System.Windows.Controls.Validation.ErrorTemplate�attached property of the 

    specified element.

  

  

   element: The System.Windows.UIElement or System.Windows.ContentElement object to read the value from.

   Returns: The System.Windows.Controls.ControlTemplate used to generate validation error feedback on the 

    adorner layer.
  """
  pass
 @staticmethod
 def GetHasError(element):
  """
  GetHasError(element: DependencyObject) -> bool

  

   Gets the value of the System.Windows.Controls.Validation.HasError�attached property of the 

    specified element.

  

  

   element: The System.Windows.UIElement or System.Windows.ContentElement object to read the value from.

   Returns: The value of the System.Windows.Controls.Validation.HasError attached property of the specified 

    element.
  """
  pass
 @staticmethod
 def GetValidationAdornerSite(element):
  """
  GetValidationAdornerSite(element: DependencyObject) -> DependencyObject

  

   Gets the value of the System.Windows.Controls.Validation.ValidationAdornerSite attached property 

    for the specified element.

  

  

   element: The element from which to get the System.Windows.Controls.Validation.ValidationAdornerSite.

   Returns: The value of the System.Windows.Controls.Validation.ValidationAdornerSite.
  """
  pass
 @staticmethod
 def GetValidationAdornerSiteFor(element):
  """
  GetValidationAdornerSiteFor(element: DependencyObject) -> DependencyObject

  

   Gets the value of the System.Windows.Controls.Validation.ValidationAdornerSiteFor attached 

    property for the specified element.

  

  

   element: The element from which to get the System.Windows.Controls.Validation.ValidationAdornerSiteFor.

   Returns: The value of the System.Windows.Controls.Validation.ValidationAdornerSiteFor.
  """
  pass
 @staticmethod
 def MarkInvalid(bindingExpression,validationError):
  """
  MarkInvalid(bindingExpression: BindingExpressionBase,validationError: ValidationError)

   Marks the specified System.Windows.Data.BindingExpression object as invalid with the specified 

    System.Windows.Controls.ValidationError object.

  

  

   bindingExpression: The System.Windows.Data.BindingExpression object to mark as invalid.

   validationError: The System.Windows.Controls.ValidationError object to use.
  """
  pass
 @staticmethod
 def RemoveErrorHandler(element,handler):
  """ RemoveErrorHandler(element: DependencyObject,handler: EventHandler[ValidationErrorEventArgs]) """
  pass
 @staticmethod
 def SetErrorTemplate(element,value):
  """
  SetErrorTemplate(element: DependencyObject,value: ControlTemplate)

   Sets the value of the System.Windows.Controls.Validation.ErrorTemplate�attached property to the 

    specified element.

  

  

   element: The System.Windows.UIElement or System.Windows.ContentElement object to set value on.

   value: The System.Windows.Controls.ControlTemplate to use to generate validation error feedback on the 

    adorner layer.
  """
  pass
 @staticmethod
 def SetValidationAdornerSite(element,value):
  """
  SetValidationAdornerSite(element: DependencyObject,value: DependencyObject)

   Sets the System.Windows.Controls.Validation.ValidationAdornerSite attached property to the 

    specified value on the specified element.

  

  

   element: The element on which to set the System.Windows.Controls.Validation.ValidationAdornerSite.

   value: The System.Windows.Controls.Validation.ValidationAdornerSite of the specified element.
  """
  pass
 @staticmethod
 def SetValidationAdornerSiteFor(element,value):
  """
  SetValidationAdornerSiteFor(element: DependencyObject,value: DependencyObject)

   Sets the System.Windows.Controls.Validation.ValidationAdornerSiteFor attached property to the 

    specified value on the specified element.

  

  

   element: The element on which to set the System.Windows.Controls.Validation.ValidationAdornerSiteFor.

   value: The System.Windows.Controls.Validation.ValidationAdornerSiteFor of the specified element.
  """
  pass
 ErrorEvent=None
 ErrorsProperty=None
 ErrorTemplateProperty=None
 HasErrorProperty=None
 ValidationAdornerSiteForProperty=None
 ValidationAdornerSiteProperty=None
 __all__=[
  'AddErrorHandler',
  'ClearInvalid',
  'ErrorEvent',
  'ErrorsProperty',
  'ErrorTemplateProperty',
  'GetErrors',
  'GetErrorTemplate',
  'GetHasError',
  'GetValidationAdornerSite',
  'GetValidationAdornerSiteFor',
  'HasErrorProperty',
  'MarkInvalid',
  'RemoveErrorHandler',
  'SetErrorTemplate',
  'SetValidationAdornerSite',
  'SetValidationAdornerSiteFor',
  'ValidationAdornerSiteForProperty',
  'ValidationAdornerSiteProperty',
 ]

