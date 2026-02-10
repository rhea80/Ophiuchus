$wshell = New-Object -ComObject Wscript.Shell

while($true) {
    $wshell.Popup("i'm so lonely can you type hi to me?", 0, "hi!", 0x1)
    Start-Sleep -Seconds 300
    $wshell.Popup("hi!!! how are you doing today?", 0, "emotion.", 0x1)
    Start-Sleep -Seconds 300
    $wshell.Popup("that's amazing! i'm doing great :)", 0, "great!", 0x1)
    Start-Sleep -Seconds 300
    $wshell.Popup("hey can you get me a monster?", 0, "monster?", 0x1)
    Start-Sleep -Seconds 300
    $wshell.Popup("where am i? i'm the same room as you silly :3", 0, ":3", 0x1)
    Start-Sleep -Seconds 300
    $wshell.Popup("what team am i? uhhh that's boring!", 0, "<3", 0x1)
    Start-Sleep -Seconds 300
    $wshell.Popup("okayyy fine thats okay. i dont need a monster.", 0, ":(", 0x1)
    Start-Sleep -Seconds 300
    $wshell.Popup("do you like cats?", 0, "meow?", 0x1)
    Start-Sleep -Seconds 300
    $wshell.Popup("my favorite cat is chococat!", 0, "meow!", 0x1)
    Start-Sleep -Seconds 300
    $wshell.Popup("i'll leave now, but you should add me on discord: @ilyree", 0, "ADD ME ON DISCORD", 0x1)
    Start-Sleep -Seconds 1800
}
