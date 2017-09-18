class CounterSampleCalculator(object):
 """ Provides a set of utility functions for interpreting performance counter data. """
 @staticmethod
 def ComputeCounterValue(*__args):
  """
  ComputeCounterValue(oldSample: CounterSample,newSample: CounterSample) -> Single

  

   Computes the calculated value of two raw counter samples.

  

   oldSample: A System.Diagnostics.CounterSample that indicates a previous sample the system has taken.

   newSample: A System.Diagnostics.CounterSample that indicates the most recent sample the system has taken.

   Returns: A floating-point representation of the performance counter's calculated value.

  ComputeCounterValue(newSample: CounterSample) -> Single

  

   Computes the calculated value of a single raw counter sample.

  

   newSample: A System.Diagnostics.CounterSample that indicates the most recent sample the system has taken.

   Returns: A floating-point representation of the performance counter's calculated value.
  """
  pass
 __all__=[
  'ComputeCounterValue',
 ]

