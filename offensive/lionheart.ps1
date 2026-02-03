Add-Type -AssemblyName System.Windows.Forms    
$screens = [System.Windows.Forms.SystemInformation]::VirtualScreen   
while ($true) {
    [Windows.Forms.Cursor]::Position = "$($screens.Width - 500),$($screens.Height - 500)"
    Start-Sleep -Milliseconds 100   
}
