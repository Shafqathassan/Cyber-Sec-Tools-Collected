#Author : ShafqatHassan
#Dated : 1st; of Mar 2023
#Repo : Shafqathassan/Cyber-Sec_Tools
#Credit : Georgia Weidman and HeathAdams https://youtube.com/@TCMSecurityAcademy

#!/usr/bin/bash is a shebang line used in script files to set bash, present in the '/bin' directory.It defines an absolute path /usr/bin/bash to the Bash shell 
#(for more info : https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjBzO_tsJ3-AhUvplYBHVQjCAwQFnoECA8QAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FShebang_(Unix)&usg=AOvVaw2JO5JC-ojjNYqhPOD6J7aP )
#!/bin/bash

if ["$1" == " "]
then 
echo "You forgot an IP Address !"
echo "Syntax : ./ipsweep.sh 192.168.1

else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done 
fi
