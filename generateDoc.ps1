Push-Location
Set-Location src
$Module = Read-Host "Name of module"
python -m pydoc $Module
Pop-Location