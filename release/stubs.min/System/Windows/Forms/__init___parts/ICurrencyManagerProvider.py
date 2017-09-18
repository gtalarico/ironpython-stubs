class ICurrencyManagerProvider:
 """ Provides custom binding management for components. """
 def GetRelatedCurrencyManager(self,dataMember):
  """
  GetRelatedCurrencyManager(self: ICurrencyManagerProvider,dataMember: str) -> CurrencyManager

  

   Gets the System.Windows.Forms.CurrencyManager for this 

    System.Windows.Forms.ICurrencyManagerProvider and the specified data member.

  

  

   dataMember: The name of the column or list,within the data source,to obtain the 

    System.Windows.Forms.CurrencyManager for.

  

   Returns: The related System.Windows.Forms.CurrencyManager obtained from this 

    System.Windows.Forms.ICurrencyManagerProvider and the specified data member.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 CurrencyManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.CurrencyManager associated with this System.Windows.Forms.ICurrencyManagerProvider.



Get: CurrencyManager(self: ICurrencyManagerProvider) -> CurrencyManager



"""


