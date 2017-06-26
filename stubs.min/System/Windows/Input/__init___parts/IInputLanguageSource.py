class IInputLanguageSource:
 """ Defines necessary facilities for an object that intends to behave as an input language source. """
 def Initialize(self):
  """
  Initialize(self: IInputLanguageSource)
   Initializes an input language source object.
  """
  pass
 def Uninitialize(self):
  """
  Uninitialize(self: IInputLanguageSource)
   Un-initializes an input language source object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 CurrentInputLanguage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current input language for this input language source object.

Get: CurrentInputLanguage(self: IInputLanguageSource) -> CultureInfo

Set: CurrentInputLanguage(self: IInputLanguageSource)=value
"""

 InputLanguageList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a list of input languages supported by this input language source object.

Get: InputLanguageList(self: IInputLanguageSource) -> IEnumerable

"""


