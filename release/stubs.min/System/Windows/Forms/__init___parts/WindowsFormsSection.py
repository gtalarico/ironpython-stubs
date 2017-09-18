class WindowsFormsSection(ConfigurationSection):
 """
 Defines a new System.Configuration.ConfigurationSection for parsing application settings. This class cannot be inherited.

 

 WindowsFormsSection()
 """
 ElementProperty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.



"""

 EvaluationContext=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.



"""

 HasContext=property(lambda self: object(),lambda self,v: None,lambda self: None)

 JitDebugging=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether just-in-time (JIT) debugging is used.



Get: JitDebugging(self: WindowsFormsSection) -> bool



Set: JitDebugging(self: WindowsFormsSection)=value

"""

 Properties=property(lambda self: object(),lambda self,v: None,lambda self: None)


