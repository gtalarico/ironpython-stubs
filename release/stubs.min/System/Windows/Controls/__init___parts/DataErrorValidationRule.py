class DataErrorValidationRule(ValidationRule):
 """
 Represents a rule that checks for errors that are raised by the System.ComponentModel.IDataErrorInfo implementation of the source object.

 

 DataErrorValidationRule()
 """
 def Validate(self,value,cultureInfo,owner=None):
  """
  Validate(self: DataErrorValidationRule,value: object,cultureInfo: CultureInfo) -> ValidationResult

  

   Performs validation checks on a value.

  

   value: The value to check.

   cultureInfo: The culture to use in this rule.

   Returns: The result of the validation.
  """
  pass
