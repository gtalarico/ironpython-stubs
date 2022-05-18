Function CreateTc-WebClient()
{
    $client = New-Object System.Net.WebClient

    $client.Proxy = [System.Net.WebRequest]::DefaultWebProxy
    $client.Proxy.Credentials = [System.Net.CredentialCache]::DefaultNetworkCredentials
    $client.Headers.Add("Authorization","Basic c2NyaXB0aW5nOk1DdlJNS1dGanhIamNHbkoxd0U5")

    return $client;
}

Function Get-ArtefactInfo()
{
    # Format: https://teamcity.trancon.nl/repository/download/BoxwiseProNuke_Release/$ReleaseId:id/Setup-$ShortVersion.zip!/Setup.exe
    # ReleaseId: int
    # ShortVersion: 1.34.2

    $client = $(CreateTc-WebClient)
    $client.Headers.Add("Accept", "application/json")

    $TcResponse = $client.DownloadString("https://teamcity.trancon.nl/httpAuth/app/rest/builds/?locator=buildType:(id:BoxwiseProNuke_Release),status:SUCCESS,branch:refs/heads/master,count:1") | ConvertFrom-Json

    $ReleaseId = $TcResponse.build.id
    $NetVersion = New-Object -TypeName System.Version -ArgumentList $TcResponse.build.number
    # Nuke version number omits $NetVersion.Build
    $ShortVersion = "$($NetVersion.Major).$($NetVersion.Minor).$($NetVersion.Revision)"

    $FullUrl = "https://teamcity.trancon.nl/repository/download/BoxwiseProNuke_Release/$($ReleaseId):id/Setup-$ShortVersion.zip!/Setup.exe"
    $LongVersion = "$($NetVersion.Major).$($NetVersion.Minor).$($NetVersion.Build).$($NetVersion.Revision)"

    return @($FullUrl, $LongVersion)
}

Function Download-BuildOutput()
{
    $dir = (pwd).Path
    $BwSetupFile = Join-Path $dir "Setup.exe"
    $BwExtractDir = Join-Path $dir "boxwise"
    $SetupFile = Join-Path $BwExtractDir "Setup.exe"
    $MsiFile = Join-Path $BwExtractDir "Wms.Setup.msi"

    $client = $(CreateTc-WebClient)

    # Download boxwise and extract Setup.exe/Wms.Setup.msi
    # expects 7z.exe to be available in $env:PATH
    $ArtefactUrl, $Version = Get-ArtefactInfo

    Write-Host "Downloading version $Version of boxwise from: $ArtefactUrl"
    $client.DownloadFile($ArtefactUrl, $BwSetupFile)

    Write-Host "Extracting boxwise to $BwExtractDir"
    # docs: https://sevenzip.osdn.jp/chm/cmdline/commands/extract_full.htm
    7z x $BwSetupFile "-o$BwExtractDir" -r -y -aoa | Out-Null

    if(Test-Path $SetupFile)
    {
        7z x $SetupFile "-o$BwExtractDir" -r -y -aoa | Out-Null
    }

    if(Test-Path $MsiFile)
    {
        7z x $MsiFile "-o$BwExtractDir" -r -y -aoa | Out-Null
    }

    rm $BwSetupFile

    return @($BwExtractDir, $Version)
}

Function Push-PythonStubs()
{
    $dir = (pwd).Path
    $PythonStubsFolder = Join-Path $dir "release/stubs"
    $LogFolder = Join-Path $dir "logs"
    $AssemblyList = Join-Path $dir "assemblylist.json"
    $GCloudCredentialsPath = Split-Path -path $dir  | Join-Path -ChildPath "googleCloudCredentials.json"

    $BwExtractDir, $Version = Download-BuildOutput
    $ZipFileName = "boxwise_linter_$Version.zip"
    $ZipFilePath = "$dir\$ZipFileName"

    if(-not(Test-Path $LogFolder)) {
        md $LogFolder
    }

    python ironstubs\make_assemblylist.py $BwExtractDir

    ipy -m ironstubs make Wms.RemotingImplementation,Wms.RemotingObjects,Wms.RemotingInterface,Wms.SharedInfra,Wms.EdiMessaging,TranCon.Printing.Interface,System,System.Globalization --path $BwExtractDir --overwrite

    7z a -tzip $ZipFileName $PythonStubsFolder $Assemblylist

    python uploadToCloud.py $ZipFilePath $ZipFileName $GCloudCredentialsPath
    rm $ZipFilePath
}

Push-PythonStubs
