class ValidationRule(object):
 """ Provides a way to create a custom rule in order to check the validity of user input. """
 def Validate(self,value,cultureInfo,owner=None):
  """
  Validate(self: ValidationRule,value: object,cultureInfo: CultureInfo,owner: BindingGroup) -> ValidationResult

  Validate(self: ValidationRule,value: object,cultureInfo: CultureInfo,owner: BindingExpressionBase) -> ValidationResult

  Validate(self: ValidationRule,value: object,cultureInfo: CultureInfo) -> ValidationResult

  

   When overridden in a derived class,performs validation checks on a value.

  

   value: The value from the binding target to check.

   cultureInfo: The culture to use in this rule.

   Returns: A System.Windows.Controls.ValidationResult object.
  """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)

  __new__(cls: type,validationStep: ValidationStep,validatesOnTargetUpdated: bool)
  """
  pass
 ValidatesOnTargetUpdated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the validation rule runs when the target of the System.Windows.Data.Binding is updated.



Get: ValidatesOnTargetUpdated(self: ValidationRule) -> bool



Set: ValidatesOnTargetUpdated(self: ValidationRule)=value

"""

 ValidationStep=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets when the validation rule runs.



Get: ValidationStep(self: ValidationRule) -> ValidationStep



Set: ValidationStep(self: ValidationRule)=value

"""


