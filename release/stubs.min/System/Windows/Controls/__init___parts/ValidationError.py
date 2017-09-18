class ValidationError(object):
 """
 Represents a validation error that is created either by the binding engine when a System.Windows.Controls.ValidationRule reports a validation error,or through the System.Windows.Controls.Validation.MarkInvalid(System.Windows.Data.BindingExpressionBase,System.Windows.Controls.ValidationError) method explicitly.

 

 ValidationError(ruleInError: ValidationRule,bindingInError: object,errorContent: object,exception: Exception)

 ValidationError(ruleInError: ValidationRule,bindingInError: object)
 """
 @staticmethod
 def __new__(self,ruleInError,bindingInError,errorContent=None,exception=None):
  """
  __new__(cls: type,ruleInError: ValidationRule,bindingInError: object,errorContent: object,exception: Exception)

  __new__(cls: type,ruleInError: ValidationRule,bindingInError: object)
  """
  pass
 BindingInError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Data.BindingExpression or System.Windows.Data.MultiBindingExpression object of this System.Windows.Controls.ValidationError. The object is either marked invalid explicitly or has a failed validation rule.



Get: BindingInError(self: ValidationError) -> object



"""

 ErrorContent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that provides additional context for this System.Windows.Controls.ValidationError,such as a string describing the error.



Get: ErrorContent(self: ValidationError) -> object



Set: ErrorContent(self: ValidationError)=value

"""

 Exception=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Exception object that was the cause of this System.Windows.Controls.ValidationError,if the error is the result of an exception.



Get: Exception(self: ValidationError) -> Exception



Set: Exception(self: ValidationError)=value

"""

 RuleInError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Controls.ValidationRule object that was the cause of this System.Windows.Controls.ValidationError,if the error is the result of a validation rule.



Get: RuleInError(self: ValidationError) -> ValidationRule



Set: RuleInError(self: ValidationError)=value

"""


