class ValidationResult(object):
 """
 Represents the result returned by the System.Windows.Controls.ValidationRule.System.Windows.Controls.ValidationRule.Validate(System.Object,System.Globalization.CultureInfo) method that indicates whether the checked value passed the System.Windows.Controls.ValidationRule.

 

 ValidationResult(isValid: bool,errorContent: object)
 """
 def Equals(self,obj):
  """
  Equals(self: ValidationResult,obj: object) -> bool

  

   Compares the specified instance and the current instance of 

    System.Windows.Controls.ValidationResult for value equality.

  

  

   obj: The System.Windows.Controls.ValidationResult instance to compare.

   Returns: true if obj and this instance of System.Windows.Controls.ValidationResult.have the same values.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ValidationResult) -> int

  

   Returns the hash code for this System.Windows.Controls.ValidationResult.

   Returns: The hash code for this System.Windows.Controls.ValidationResult.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,isValid,errorContent):
  """ __new__(cls: type,isValid: bool,errorContent: object) """
  pass
 def __ne__(self,*args):
  pass
 ErrorContent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that provides additional information about the invalidity.



Get: ErrorContent(self: ValidationResult) -> object



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the value checked against the System.Windows.Controls.ValidationRule is valid.



Get: IsValid(self: ValidationResult) -> bool



"""


 ValidResult=None

