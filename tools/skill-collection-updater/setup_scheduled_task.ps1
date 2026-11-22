# Windows Task Scheduler setup
# Use this script's directory so it works after repository relocation.

$TaskName = "SkillStoreAutoUpdate"
$ScriptPath = Join-Path $PSScriptRoot "main.py"
$WorkingDir = $PSScriptRoot
$PythonPath = (Get-Command python).Source

$Action = New-ScheduledTaskAction -Execute $PythonPath -Argument "$ScriptPath --once" -WorkingDirectory $WorkingDir
$Trigger = New-ScheduledTaskTrigger -Daily -At 2:00AM
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RunOnlyIfNetworkAvailable
Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "自动从 GitHub 更新技能商店数据" -Force
Write-Host "定时任务已创建: $TaskName"
Write-Host "执行时间: 每天凌晨 2:00"
Write-Host "可在任务计划程序中查看和管理"
