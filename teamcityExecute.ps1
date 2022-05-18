Function CreateTC-WebClient
{
    $wc = New-Object System.Net.WebClient;
    $wc.Proxy = [System.Net.WebRequest]::DefaultWebProxy;
    $wc.Proxy.Credentials = [System.Net.CredentialCache]::DefaultNetworkCredentials;
    $wc.Headers.Add("Authorization","Basic c2NyaXB0aW5nOk1DdlJNS1dGanhIamNHbkoxd0U5");
    return $wc;
}

Function Get-ArtefactInfo
{
    # Format: https://teamcity.trancon.nl/repository/download/BoxwiseProNuke_Release/$ReleaseId:id/Setup-$ShortVersion.zip!/Setup.exe
    # ReleaseId: int
    # ShortVersion: 1.34.2

    $wc = $(CreateTC-WebClient);
    $wc.Headers.Add("Accept","application/json");

    $r = $wc.DownloadString("https://teamcity.trancon.nl/httpAuth/app/rest/builds/?locator=buildType:(id:BoxwiseProNuke_Release),status:SUCCESS,branch:refs/heads/master,count:1")
    $j = $r | ConvertFrom-Json

    $ReleaseId = $j.build.id
    $NetVersion = New-Object -TypeName System.Version -ArgumentList $j.build.number

    $ShortVersion = "$($NetVersion.Major).$($NetVersion.Minor).$($NetVersion.Revision)"

    $FullUrl = "https://teamcity.trancon.nl/repository/download/BoxwiseProNuke_Release/$($ReleaseId):id/Setup-$ShortVersion.zip!/Setup.exe"
    $LongVersion = "$($NetVersion.Major).$($NetVersion.Minor).$($NetVersion.Build).$($NetVersion.Revision)"

    return @($FullUrl, $LongVersion)
}

Function Download-BuildOutput()
{
    $wc = $(CreateTC-WebClient)

    # download boxwise and start setup
    # expects 7z.exe to be available in Path (automatic on choco install 7zip.install -y)
    $ArtefactUrl, $Version = Get-ArtefactInfo

    Write-Host "Downloading version of BOXwisePro from: $ArtefactUrl"
    $dir = (Get-Location).Path;
    $bwZip = Join-Path $dir "Setup.exe"
    $wc.DownloadFile($ArtefactUrl, $bwZip)

    $bwExtractDir = Join-Path $dir "BOXwisePro"

    Write-Host "Extracting BOXwisePro to $bwExtractDir"
    # docs: https://sevenzip.osdn.jp/chm/cmdline/commands/extract_full.htm
    7z x $bwZip "-o$bwExtractDir" -r -y -aoa | Out-Null

    $setupFile = Join-Path $bwExtractDir "Setup.exe"
    if(Test-Path $setupFile)
    {
        7z x $setupFile "-o$bwExtractDir" -r -y -aoa | Out-Null
    }

    $msiFile = Join-Path $bwExtractDir 'Wms.Setup.msi'
    if(Test-Path $msiFile)
    {
        7z x $msiFile "-o$bwExtractDir" -r -y -aoa
    }

    Remove-Item $bwZip #Delete the zip file

    return @($dir, $bwExtractDir, $Version)
}

Function Push-PythonStubs()
{
    $dir, $bwExtractDir, $Version = Download-BuildOutput
    $toBeZipped = Join-Path $dir "stubs"

    python ironstubs\make_assemblylist.py $bwExtractDir

    ipy -m ironstubs make Wms.RemotingImplementation,Wms.RemotingObjects,Wms.RemotingInterface,Wms.SharedInfra,Wms.EdiMessaging,TranCon.Printing.Interface,System,System.Globalization --path $bwExtractDir --overwrite
    $name = "boxwise_linter_"+ $version+ ".zip"

    $assemblyList = Join-Path $dir "assemblylist.json"
    $classlist = Join-Path $dir "classlist.json"
    $typedict = Join-Path $dir "typedict.json"
    7z a -tzip $name $toBeZipped $assemblylist
    7z a -tzip $name $toBeZipped $classlist
    7z a -tzip $name $toBeZipped $typedict

    $credentials = Split-Path -path $dir  | Join-Path -ChildPath "googleCloudCredentials.json"

    $pathToStubs = $dir + "\"+ $name
    python uploadToCloud.py $pathToStubs $name $credentials
    Remove-Item $pathToStubs
}

Push-PythonStubs
