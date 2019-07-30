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

    # | System
    'System',
    #'System.Drawing',
    #'System.Windows.Forms',

    ]

BUILTINS = [
    'clr',
    ]

ASSEMBLIES.extend(BUILTINS)
ASSEMBLIES.sort()
