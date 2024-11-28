### **Dynamic Script Execution Setup**

This ensures your executable always runs the latest version of your script.

#### **Step 1: Create a Wrapper Script**

1. Open a text editor and paste the following code:

   ```powershell
   $ScriptPath = "C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\RealTimeFolderSync.ps1"
   if (Test-Path $ScriptPath) {
       Write-Output "$(Get-Date): Executing the latest script from $ScriptPath."
       . $ScriptPath
   } else {
       Write-Output "$(Get-Date): Script not found at $ScriptPath."
   }
   ```

2. Save this file as `Wrapper.ps1` in the project folder:

   C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\Wrapper.ps1

---

#### **Step 2: Convert the Wrapper Script to an Executable**

1. Install `ps2exe`:

   ```powershell
   Install-Module -Name ps2exe -Scope CurrentUser
   ```

2. Run the following command to create the executable:

   ```powershell
   ps2exe -inputFile "C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\Wrapper.ps1" -outputFile "C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\RealTimeFolderSync.exe"
   ```

**Outcome**: Every time you run the `RealTimeFolderSync.exe` file, it will execute the latest version of `RealTimeFolderSync.ps1`.

---

### **Automated Compilation Pipeline**

For more stability, set up an automated pipeline to recompile the script whenever it is updated.

#### **Step 1: Create an Auto-Compile Script**

1. Open a text editor and paste the following code:

   ```powershell
   $ScriptFile = "C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\RealTimeFolderSync.ps1"
   $ExecutableFile = "C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\RealTimeFolderSync.exe"
   $LastModifiedFile = "C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\last_modified.log"

   # Check if the script has been updated
   if (!(Test-Path $LastModifiedFile) -or (Get-Item $ScriptFile).LastWriteTime -ne (Get-Content $LastModifiedFile | Out-String).Trim()) {
       Write-Output "$(Get-Date): Script updated. Recompiling to executable..."

       # Recompile the script
       ps2exe -inputFile $ScriptFile -outputFile $ExecutableFile
       Write-Output "$(Get-Date): Compilation complete. New executable created at $ExecutableFile."

       # Update the last modified log
       (Get-Item $ScriptFile).LastWriteTime | Out-File $LastModifiedFile
   } else {
       Write-Output "$(Get-Date): Script unchanged. No action taken."
   }
   ```

2. Save this file as `AutoCompile.ps1` in the project folder:

   C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\AutoCompile.ps1

---

#### **Step 2: Run the Auto-Compile Script**

1. Run the `AutoCompile.ps1` script periodically:

   ```powershell
   .\AutoCompile.ps1
   ```

2. Automate this by adding it to **Task Scheduler**:
   - Open **Task Scheduler** → Create a new task.
   - Set the trigger to run the script every time the `.ps1` file changes or at regular intervals.

**Outcome**: Whenever the `RealTimeFolderSync.ps1` file is updated, the script will automatically recompile the `.exe`.

---

### **Manual Update Instructions**

For cases where automated methods are unavailable, follow these steps to manually update the `.exe`.

#### **Instructions to Save in `.txt`**

Save the following content in a `.txt` file named `Manual_Update_Instructions.txt` at:

C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn\Manual_Update_Instructions.txt

#### **Content for the `.txt` File**

# Manual Update Instructions for RealTimeFolderSync Executable

## File Path

C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn

## Steps

1. Open PowerShell.
2. Navigate to the project directory:

   ```powershell
   cd C:\Users\seanj\OneDrive\Documents\GitHub\Project-Nova-Dawn
   ```

3. Compile the updated script:

   ```powershell
   ps2exe -inputFile "RealTimeFolderSync.ps1" -outputFile "RealTimeFolderSync.exe"
   ```

4. Test the new executable:

   ```powershell
   .\RealTimeFolderSync.exe
   ```

5. Confirm the executable works:
   - Check the logs for any errors.
   - Ensure the script performs as expected.

## Notes

- Always back up the previous executable before recompiling.
- Ensure you have `ps2exe` installed:

   ```powershell
   Install-Module -Name ps2exe -Scope CurrentUser
   ```

- For troubleshooting, refer to the `folder_sync.log` file in the `Output` directory.

---
