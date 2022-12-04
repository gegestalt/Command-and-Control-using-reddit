import subprocess
STR_CMD = """
$action = New-ScheduledTaskAction -Execute "powershell.exe" 
$description = "very innocent scheduled task w/ powershell."
$settings = New-ScheduledTaskSettingsSet -DeleteExpiredTaskAfter (New-TimeSpan -Seconds 10)
$taskName = "Scheduled_Script"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddSeconds(5)
$trigger.EndBoundary = (Get-Date).AddSeconds(9).ToString("s")
Register-ScheduledTask -TaskName $taskName -Description $description -Action $action -Settings $settings -Trigger $trigger | Out-Null
"""
listProcess = [
    "",
    "-NoExit",
    "-NoProfile",
    "-Command",
    STR_CMD
]
subprocess.run(listProcess, check=True)