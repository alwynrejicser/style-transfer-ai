# PowerShell script to automatically add Python user Scripts to PATH
# This ensures style-transfer-ai CLI is globally accessible

$userScriptsPath = "$env:APPDATA\Python\Python313\Scripts"
$currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")

# Check if the path is already in PATH
if ($currentPath -like "*$userScriptsPath*") {
    Write-Host "✅ Python user Scripts directory is already in PATH!" -ForegroundColor Green
    Write-Host "Path: $userScriptsPath" -ForegroundColor Cyan
} else {
    try {
        # Add to user PATH (persists across sessions)
        $newPath = "$currentPath;$userScriptsPath"
        [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
        
        Write-Host "✅ Successfully added to PATH!" -ForegroundColor Green
        Write-Host "Added: $userScriptsPath" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "🔄 Please restart your terminal or run:" -ForegroundColor Yellow
        Write-Host "   refreshenv" -ForegroundColor White
        Write-Host "   OR" -ForegroundColor Yellow
        Write-Host "   `$env:PATH = [Environment]::GetEnvironmentVariable('PATH', 'User')" -ForegroundColor White
        Write-Host ""
        Write-Host "Then you can run 'style-transfer-ai' from anywhere!" -ForegroundColor Green
    }
    catch {
        Write-Host "❌ Error adding to PATH: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "You may need to run PowerShell as Administrator" -ForegroundColor Yellow
    }
}

# Test if style-transfer-ai is accessible
Write-Host ""
Write-Host "🧪 Testing CLI accessibility..." -ForegroundColor Blue
try {
    $command = Get-Command "style-transfer-ai" -ErrorAction SilentlyContinue
    if ($command) {
        Write-Host "✅ style-transfer-ai CLI is accessible!" -ForegroundColor Green
        Write-Host "Location: $($command.Source)" -ForegroundColor Cyan
    } else {
        Write-Host "⚠️  style-transfer-ai CLI not found in current session" -ForegroundColor Yellow
        Write-Host "Try restarting terminal or refreshing environment" -ForegroundColor White
    }
}
catch {
    Write-Host "⚠️  Could not test CLI accessibility" -ForegroundColor Yellow
}