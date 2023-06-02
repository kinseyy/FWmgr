import os
import colorama
import sys
import platform

from colorama import init, Fore, Back
init()

global version
version = "1.1"

global fail
global success
global info
global warn
fail = (Fore.RED + "fail " + Fore.RESET);
success = (Fore.GREEN + "success " + Fore.RESET);
info = (Fore.BLUE + "info " + Fore.RESET);
warn = (Fore.YELLOW + "warn " + Fore.RESET);

# platform check process
def check(state):
    global uos
    uos = platform.system()
    if state == 1:
        if uos != 'Linux':
            print(f'{fail}only linux systems supported.')
        else:
            print(f'{info}Linux distributive components found.')
            pass
    else:
        print(f'{warn}Operational system check is disabled. Be careful.')
        pass
check(0)

def main():
    case1 = input("fwm>")
    if case1 == "":
        main()
    elif case1 == "help":
        print(f'{info}FWmgr v{version}')
        print('"ban useragent" - block any user agent of ipv4\ipv6')
        print('"ban port" - block any port or traffic')
        print('"accept port" - allow any port or traffic')
        print('"ban v4mask" - Block Mask of ipv4/24')
        print('"ban v6mask" - Block Mask of ipv6/48/80')
        print('"ban ipv4" - Block ipv4')
        print('"ban ipv6" - Block ipv6')
        print(f'{info} github.com/@kinseyy')
        main()
    elif case1 == "ban useragent":
        case2 = input("UserAgent=")
        os.system(f'sudo iptables -A INPUT -m string --string "{case2}" --algo bm -j DROP')
        print(f'{success}useragent was requested to be banned.')
        os.system('sudo iptables-save | sudo tee /etc/iptables/rules.v4')
        main()
    elif case1 == "ban port":
        case3 = input("port=")
        case4 = input("tcp/udp=")
        am1 = int(case3)
        os.system(f'sudo iptables -A INPUT -p {case4} --dport {am1} -j DROP')
        print(f'{success}port was requested to be banned.')
        os.system('sudo iptables-save | sudo tee /etc/iptables/rules.v4')
        main()
    elif case1 == "accept port":
        case3 = input("port=")
        case4 = input("tcp/udp=")
        am1 = int(case3)
        os.system(f'sudo iptables -A INPUT -p {case4} --dport {am1} -j ACCEPT')
        print(f'{success}port was requested to be allowed.')
        os.system('sudo iptables-save | sudo tee /etc/iptables/rules.v4')
        main()
    elif case1 == "ban v4mask":
        case7 = input("mask(ex: 1.0.10.1/24)=")
        os.system(f'sudo iptables -A INPUT -s {case7} -j DROP')
        print(f'{success}mask was requested to be banned (v4).')
        os.system('sudo iptables-save | sudo tee /etc/iptables/rules.v4')
        main()
    elif case1 == "ban v6mask":
        case7 = input("mask(ex: 2001:db8:abcd::/48)=")
        os.system(f'sudo ip6tables -A INPUT -s {case7} -j DROP')
        print(f'{success}mask was requested to be banned (v6).')
        os.system('sudo ip6tables-save | sudo tee /etc/iptables/rules.v6')
        main()
    elif case1 == "ban ipv4":
        case7 = input("ipv4(ex: 192.168.1.100)=")
        os.system(f'sudo iptables -A INPUT -s {case7} -j DROP')
        print(f'{success}ip was requested to be banned (v4).')
        os.system('sudo iptables-save | sudo tee /etc/iptables/rules.v4')
        main()
    elif case1 == "ban ipv6":
        case7 = input("ipv6(ex: 2001:db8::1)=")
        os.system(f'sudo ip6tables -A INPUT -s {case7} -j DROP')
        print(f'{success}ip was requested to be banned (v6).')
        os.system('sudo ip6tables-save | sudo tee /etc/iptables/rules.v6')
        main()
    elif case1 == "exit":
        exit('You exited from FWmgr main screen.')

main()
