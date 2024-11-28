# === Configuration ===
$ProjectRoot = "C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\NovaAI"
$OutputFolder = "$ProjectRoot\Output"
$OutputFile = "$OutputFolder\Overall_Filepath.bash"
$LogFile = "$OutputFolder\folder_sync.log"

# Ensure the Output folder exists
if (!(Test-Path $OutputFolder)) {
    New-Item -ItemType Directory -Path $OutputFolder
    Write-Output "$(Get-Date): Created Output folder at $OutputFolder." | Out-File -Append $LogFile
}

# === Functions ===

# Generate the directory structure
function Generate-Tree {
    Write-Output "$(Get-Date): Generating mind map..." | Out-File -Append $LogFile
    try {
        tree /F $ProjectRoot | Out-File -Encoding UTF8 $OutputFile
        Write-Output "$(Get-Date): Mind map updated successfully." | Out-File -Append $LogFile
    } catch {
        Write-Output "$(Get-Date): Error generating mind map: $_" | Out-File -Append $LogFile
    }
}

# Monitor file changes and regenerate the directory structure
function Monitor-Changes {
    Write-Output "$(Get-Date): Setting up file system watcher..." | Out-File -Append $LogFile

    $Watcher = New-Object System.IO.FileSystemWatcher
    $Watcher.Path = $ProjectRoot
    $Watcher.Filter = "*.*"
    $Watcher.IncludeSubdirectories = $true
    $Watcher.NotifyFilter = `
        [System.IO.NotifyFilters]::FileName, `
        [System.IO.NotifyFilters]::DirectoryName
    $Watcher.EnableRaisingEvents = $true

    # Event handlers
    $ChangeHandler = {
        $Path = $Event.SourceEventArgs.FullPath
        $ChangeType = $Event.SourceEventArgs.ChangeType

        if (Test-Path $Path) {
            $Item = Get-Item $Path
            if ($Item.PSIsContainer) {
                Write-Output "$(Get-Date): New or modified folder: $Path - Event: $ChangeType. Triggering rescan." | Out-File -Append $LogFile
                Generate-Tree
            } else {
                Write-Output "$(Get-Date): File change detected: $Path - Event: $ChangeType" | Out-File -Append $LogFile
            }
        } else {
            Write-Output "$(Get-Date): Item deleted or inaccessible: $Path - Event: $ChangeType" | Out-File -Append $LogFile
        }
    }

    # Register events
    Register-ObjectEvent $Watcher Created -Action $ChangeHandler | Out-Null
    Register-ObjectEvent $Watcher Changed -Action $ChangeHandler | Out-Null
    Register-ObjectEvent $Watcher Deleted -Action $ChangeHandler | Out-Null
    Register-ObjectEvent $Watcher Renamed -Action $ChangeHandler | Out-Null

    Write-Output "$(Get-Date): File system watcher initialized successfully." | Out-File -Append $LogFile

    # Keep the script running
    while ($true) {
        Start-Sleep -Seconds 1
    }
}

# === Main Execution ===
if (Test-Path $ProjectRoot) {
    Write-Output "$(Get-Date): Starting folder monitoring and directory generation..." | Out-File $LogFile
    Generate-Tree  # Initial generation
    Monitor-Changes  # Begin monitoring
} else {
    Write-Output "$(Get-Date): Error: Directory $ProjectRoot does not exist!" | Out-File -Append $LogFile
    exit
}



