class IIntellisenseBuilder:
 """ Provides an interface to facilitate the retrieval of the builder's name and to display the builder. """
 def Show(self,language,value,newValue):
  """
  Show(self: IIntellisenseBuilder,language: str,value: str,newValue: str) -> (bool,str)

  

   Shows the builder.

  

   language: The language service that is calling the builder.

   value: The expression being edited.

   newValue: The new value.

   Returns: true if the value should be replaced with newValue; otherwise,false (if the user cancels,for 

    example).
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a localized name.



Get: Name(self: IIntellisenseBuilder) -> str



"""


