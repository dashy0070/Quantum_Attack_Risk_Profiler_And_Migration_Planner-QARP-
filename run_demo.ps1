# Quantum Attack Risk Profiler & Migration Planner (QARP) - PowerShell Launcher
Write-Host "=======================================================================" -ForegroundColor Cyan
Write-Host " Quantum Attack Risk Profiler & Migration Planner (QARP) - Demo" -ForegroundColor Yellow
Write-Host "=======================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Launching local interactive cockpit on http://localhost:8501..." -ForegroundColor Green
Write-Host ""

python -m streamlit run app.py
