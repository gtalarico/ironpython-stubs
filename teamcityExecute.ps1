
Function Create-TeamCity-Web-Client 
{
    $wc = New-Object System.Net.WebClient;
    $wc.Proxy = [System.Net.WebRequest]::DefaultWebProxy;
    $wc.Proxy.Credentials = [System.Net.CredentialCache]::DefaultNetworkCredentials;
    $wc.Headers.Add("Authorization","Basic c2NyaXB0aW5nOk1DdlJNS1dGanhIamNHbkoxd0U5");
    Write-Host "credentials added"
    return $wc;
    
}

Function Get-The-Latest-Succesful-Build
{
    $wc = $(Create-TeamCity-Web-Client);
    $wc.Headers.Add("Accept","application/json");

    $r = $wc.DownloadString('https://teamcity.trancon.nl/httpAuth/app/rest/builds/?locator=buildType:(id:wmspro_release),status:SUCCESS,branch:refs/heads/master,count:20')
    $j = $r | ConvertFrom-Json

    $major_minors = @{}
    $versions = @{}
    
    $options = New-Object System.Collections.ObjectModel.Collection[System.Management.Automation.Host.ChoiceDescription]
    $options.Add((New-Object System.Management.Automation.Host.ChoiceDescription "&Latest", 'Latest')) 
    $count = 1
    foreach ($build in $j.build) {
        $major_minor = $($build.number -split '\.')[0,1,2] -join '.'
        if ($major_minors.ContainsKey($major_minor)) {
            continue
        }
        $major_minors.Add($major_minor, $null)
        $versions.Add($build.number, $build.id)
        $choice = [char]$(64+$count)
        $options.Add((New-Object System.Management.Automation.Host.ChoiceDescription "&${choice} => $($build.number)", $build.number))
        $count++
    }

    $selection = $options[1]
    
    if ($selection.HelpMessage -eq "Latest") {
        return 'latest.lastSuccessful'
    }
    return $selection.HelpMessage
}


Function Download-And-unzip($version)
{
    $version = Get-The-Latest-Succesful-Build
    Color-Write -Magenta "Download voor versie ${version} wordt gestart."
    $wc = $(Create-TeamCity-Web-Client);
    
    # download boxwise and start setup
    # expects 7z.exe to be available in Path (automatic on choco install 7zip.install -y)
    $ArtifactUrl = "https://teamcity.trancon.nl/httpAuth/repository/downloadAll/BOXwisePro_WmsproRelease/${version}?branch=refs/heads/master";
    
    Write-Host "Downloading version of BOXwisePro from: $ArtifactUrl"
    $dir = (Get-Location).Path;
    $bwZip = Join-Path $dir 'BOXwisePro.zip'
    $wc.DownloadFile($ArtifactUrl,$bwZip)

    $bwExtractDir = Join-Path $dir 'BOXwisePro'
    $to = Join-Path $dir 'BOXwisePro'
    Write-Host "Extracting BOXwisePro to $to"
    # docs: https://sevenzip.osdn.jp/chm/cmdline/commands/extract_full.htm
    &"7z" x $bwZip "-o$bwExtractDir" -r -y -aoa
    $releaseZipPath = (Get-ChildItem .\BOXwisePro\x86\Release).FullName
    # $to = Join-Path $dir 'BOXwisePro'
    &"7z" x $releaseZipPath "-o$bwExtractDir" -r -y -aoa
    $setupFile = Join-Path $bwExtractDir 'Setup.exe'
    if(Test-Path $setupFile)
    {
        Write-Host  'if succes'
        &"7z" x $setupFile "-o$bwExtractDir" -r -y -aoa
    }

    $msiFile = Join-Path $bwExtractDir 'Wms.Setup.msi'
    if(Test-Path $msiFile)
    {
        Write-Host  'if succes'
        &"7z" x $msiFile "-o$bwExtractDir" -r -y -aoa
    }    
    Remove-Item $bwZip #Delete the zip file
    $path = (pwd).Path; (gc ironstubs\default_settings.py).Replace( 'C:\Program Files (x86)\TranCon\BOXwisePro\Server',$path+'\test') | Out-File -encoding utf8 ironstubs\default_settings.py
    $path = (pwd).Path; (gc ironstubs\default_settings.py).Replace( '\','/') | Out-File -encoding utf8 ironstubs\default_settings.py

    $path = (pwd).Path; (gc ironstubs\make_assemblylist.py).Replace( 'C:\Program Files (x86)\TranCon\BOXwisePro\Server',$path+'\test') | Out-File -encoding utf8 ironstubs\make_assemblylist.py
    $path = (pwd).Path; (gc ironstubs\make_assemblylist.py).Replace( '\','/') | Out-File -encoding utf8 ironstubs\make_assemblylist.py

    Remove-Item $bwZip #Delete the zip file
    & "ipy -m ironstubs make --all --overwrite"
	& "python uploadToCloud.py "+  $version
}
Download-And-unzip