class TupleExtensions(object):
 # no doc
 @staticmethod
 def Deconstruct(value,item1,item2=None,item3=None,item4=None,item5=None,item6=None,item7=None,item8=None,item9=None,item10=None,item11=None,item12=None,item13=None,item14=None,item15=None,item16=None,item17=None,item18=None,item19=None,item20=None,item21=None):
  """
  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15]]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16]]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18,T19,T20]]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18,T19,T20,T21]]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18,T19]]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17]]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18]]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11)

  Deconstruct[(T1,T2,T3,T4)](value: Tuple[T1,T2,T3,T4]) -> (T1,T2,T3,T4)

  Deconstruct[(T1,T2,T3,T4,T5)](value: Tuple[T1,T2,T3,T4,T5]) -> (T1,T2,T3,T4,T5)

  Deconstruct[(T1,T2,T3)](value: Tuple[T1,T2,T3]) -> (T1,T2,T3)

  Deconstruct[T1](value: Tuple[T1]) -> T1

  Deconstruct[(T1,T2)](value: Tuple[T1,T2]) -> (T1,T2)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10]]) -> (T1,T2,T3,T4,T5,T6,T7,T8,T9,T10)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7,T8)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8]]) -> (T1,T2,T3,T4,T5,T6,T7,T8)

  Deconstruct[(T1,T2,T3,T4,T5,T6)](value: Tuple[T1,T2,T3,T4,T5,T6]) -> (T1,T2,T3,T4,T5,T6)

  Deconstruct[(T1,T2,T3,T4,T5,T6,T7)](value: Tuple[T1,T2,T3,T4,T5,T6,T7]) -> (T1,T2,T3,T4,T5,T6,T7)
  """
  pass
 @staticmethod
 def ToTuple(value):
  """
  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15]]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15]]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16]]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16]]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16,T17,T18,T19,T20]]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18,T19,T20]]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16,T17,T18,T19,T20,T21]]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18,T19,T20,T21]]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16,T17,T18,T19]]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18,T19]]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16,T17]]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17]]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16,T17,T18]]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18]]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11]]

  ToTuple[(T1,T2,T3,T4)](value: ValueTuple[T1,T2,T3,T4]) -> Tuple[T1,T2,T3,T4]

  ToTuple[(T1,T2,T3,T4,T5)](value: ValueTuple[T1,T2,T3,T4,T5]) -> Tuple[T1,T2,T3,T4,T5]

  ToTuple[(T1,T2,T3)](value: ValueTuple[T1,T2,T3]) -> Tuple[T1,T2,T3]

  ToTuple[T1](value: ValueTuple[T1]) -> Tuple[T1]

  ToTuple[(T1,T2)](value: ValueTuple[T1,T2]) -> Tuple[T1,T2]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10]]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7,T8)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8]]) -> Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8]]

  ToTuple[(T1,T2,T3,T4,T5,T6)](value: ValueTuple[T1,T2,T3,T4,T5,T6]) -> Tuple[T1,T2,T3,T4,T5,T6]

  ToTuple[(T1,T2,T3,T4,T5,T6,T7)](value: ValueTuple[T1,T2,T3,T4,T5,T6,T7]) -> Tuple[T1,T2,T3,T4,T5,T6,T7]
  """
  pass
 @staticmethod
 def ToValueTuple(value):
  """
  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15]]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15]]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16]]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16]]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18,T19,T20]]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16,T17,T18,T19,T20]]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18,T19,T20,T21]]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16,T17,T18,T19,T20,T21]]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18,T19]]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16,T17,T18,T19]]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17]]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16,T17]]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11,T12,T13,T14,Tuple[T15,T16,T17,T18]]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11,T12,T13,T14,ValueTuple[T15,T16,T17,T18]]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10,T11]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10,T11]]

  ToValueTuple[(T1,T2,T3,T4)](value: Tuple[T1,T2,T3,T4]) -> ValueTuple[T1,T2,T3,T4]

  ToValueTuple[(T1,T2,T3,T4,T5)](value: Tuple[T1,T2,T3,T4,T5]) -> ValueTuple[T1,T2,T3,T4,T5]

  ToValueTuple[(T1,T2,T3)](value: Tuple[T1,T2,T3]) -> ValueTuple[T1,T2,T3]

  ToValueTuple[T1](value: Tuple[T1]) -> ValueTuple[T1]

  ToValueTuple[(T1,T2)](value: Tuple[T1,T2]) -> ValueTuple[T1,T2]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8,T9,T10]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8,T9,T10]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7,T8)](value: Tuple[T1,T2,T3,T4,T5,T6,T7,Tuple[T8]]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7,ValueTuple[T8]]

  ToValueTuple[(T1,T2,T3,T4,T5,T6)](value: Tuple[T1,T2,T3,T4,T5,T6]) -> ValueTuple[T1,T2,T3,T4,T5,T6]

  ToValueTuple[(T1,T2,T3,T4,T5,T6,T7)](value: Tuple[T1,T2,T3,T4,T5,T6,T7]) -> ValueTuple[T1,T2,T3,T4,T5,T6,T7]
  """
  pass
 __all__=[
  'Deconstruct',
  'ToTuple',
  'ToValueTuple',
 ]

