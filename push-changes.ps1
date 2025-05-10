# چک می‌کنیم git نصب باشه
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git نصب نیست. لطفاً اول git را نصب کن." -ForegroundColor Red
    exit
}

# وارد پوشه پروژه بشو (در صورت نیاز مسیر رو تغییر بده)
Set-Location "$PSScriptRoot"

# اضافه کردن یک تغییر آزمایشی در app.py
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Add-Content -Path app.py -Value "# Auto-pushed at $timestamp"

# اضافه و commit
git add .
git commit -m "📦 Auto push at $timestamp"

# push به remote
Write-Host "`n🚀 در حال push به GitHub..."
git push origin main
