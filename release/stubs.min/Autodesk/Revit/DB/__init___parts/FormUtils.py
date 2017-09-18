class FormUtils(object):
 """ Define Form utility functions """
 @staticmethod
 def CanBeDissolved(ADoc,elements):
  """ CanBeDissolved(ADoc: Document,elements: ICollection[ElementId]) -> bool """
  pass
 @staticmethod
 def DissolveForms(ADoc,elements,BondingPointSet=None):
  """
  DissolveForms(ADoc: Document,elements: ICollection[ElementId]) -> (ICollection[ElementId],ICollection[ElementId])

  DissolveForms(ADoc: Document,elements: ICollection[ElementId]) -> ICollection[ElementId]
  """
  pass
 __all__=[
  'CanBeDissolved',
  'DissolveForms',
 ]

