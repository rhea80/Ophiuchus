[CmdletBinding()]
param(
    [switch]$VerboseOutput
)

function Write-Status {
    param($Message)
    Write-Host "[*] $Message"
}

function Write-Change {
    param($Message)
    Write-Host "[+] $Message" -ForegroundColor Green
}

function Write-WarnNote {
    param($Message)
    Write-Host "[!] $Message" -ForegroundColor Yellow
}

$rebootRecommended = $false

# ---------------------------
# 1. Disable SMBv1
# ---------------------------
try {
    $smb = Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -ErrorAction Stop
    if ($smb.State -ne 'Disabled') {
    
