import os

PATHS = [
    # | Local Binaries
  'C:\Program Files (x86)\TranCon\BOXwisePro\Server'
    ]

ASSEMBLIES = [
    # | BOXwise
	'Wms.RemotingImplementation',
    'Wms.RemotingObjects',
	'Wms.RemotingInterface',
	'Wms.SharedInfra',
	'Wms.EdiMessaging',
	
	#  | Trancon
	'TranCon.Printing.Interface',

    # | System
    'System',
	'System.Globalization',
    'System.Drawing',
    'System.Windows.Forms',

    # # microsoft
    'mscorlib',
    'Microsoft.Practices.EnterpriseLibrary.Common',
    'Microsoft.Practices.EnterpriseLibrary.Data',
    'Microsoft.ReportViewer.Common',
    'Microsoft.ReportViewer.WinForms'

    ]

BUILTINS = [
    'clr',
    ]

ASSEMBLIES.extend(BUILTINS)
ASSEMBLIES.sort()
