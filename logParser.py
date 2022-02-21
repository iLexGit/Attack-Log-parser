import json
import sys
import re
attacks = []
attackers = []

class Attacker:
    def __init__(self, ip, reqs):
        self.ip = ip
        self.reqs = reqs

class Attack:
    def __init__(self, src, dst, logs):
        self.src = src
        self.dst = dst
        self.logs = logs

def main():
    
    if sys.argv[1] == "-A":
        file = json.load(loadAttacks())
        
        for entry in file:
            attacks.append(Attack(entry["sourceip"], entry["destinationip"], entry["logs"]))

        for attack in attacks:
            index = isUnique(attack.src)
            if index == 0:
                attackers.append(Attacker(attack.src, 1))
            else:
                attackers[index].reqs+=1
        
        if sys.argv[3] == "-l":
            listAttackers()
        
        elif (sys.argv[3] == "-s") and (len(sys.argv) > 4):
            showAttack(sys.argv[4])
        
        elif (sys.argv[3]) == "-r" and (len(sys.argv) > 4):
            for attack in attacks:
                regexAttack(attack, sys.argv[4])

        else:
            printHelp()
    
    elif sys.argv[1] == "-L":
        print("TODO - implement regular log parser")
    
    else:
        printHelp()
    

def loadAttacks():
    try:
        file = open(sys.argv[2], "r")
    except IOError:
        print("File: <", sys.argv[2], "> not found")
        sys.exit()
    print("\n[OK] Logs loaded\n")
    return file

def isUnique(src):
    index = 0
    for attacker in attackers:
        if attacker.ip == src:
            return index
        index+=1
    return 0

def listAttackers():
    print("\t#", "\tIP")
    for attacker in attackers:
        print("\t", attacker.reqs, "\t", attacker.ip)

def showAttack(ip):
    index=0
    if len(sys.argv) > 6 and sys.argv[5] == "-r":
        for attack in attacks:
            if attack.src == ip:
                regexAttack(attack, sys.argv[6])

    else:
        for attack in attacks:
            if attack.src == ip:
                index+=1
                print("\nATTACK ", index, "\n\tTarget: ", attack.dst, "\n\tLogs ", len(attack.logs),":")
                for i in range(len(attack.logs)):
                    print("\t\t", attack.logs[i]["time"], "\t[", attack.logs[i]["parsedMessage"]["level"], "]", "\n\t", attack.logs[i]["parsedMessage"]["message"][attack.logs[i]["parsedMessage"]["message"].index("\""):], "\n")

def regexAttack(attack, regex):
    x = "-"
    for i in range(len(attack.logs)):
        x = (re.findall(regex, attack.logs[i]["parsedMessage"]["message"][attack.logs[i]["parsedMessage"]["message"].index("\""):]))
        if len(x) > 0:
            print("\nSource", attack.src, "->", attack.dst)
            for p in range(len(attack.logs)):
                print("\t", attack.logs[p]["parsedMessage"]["message"][attack.logs[p]["parsedMessage"]["message"].index("\""):])
            break

def printHelp():
    print("Log parser v1\nAlejandro Marti, Lupovis\nhttps://github.com/iLexGit/logParser\n")
    print("Usage: python logParser.py [TYPE OF LOG] <LOG_FILE_PATH> [OPTIONS]\n")
    print("[TYPE OF LOG]\n\t-A\t\tAttacks log\n\t-L\t\tRegular log\n")
    print("[ATTACK LOG OPTIONS]\n")
    print("\t-l\t\tList source IP with number of attacks performed")
    print("\t-s <IP>\t\tPrint all logs from specified source IP")
    print("\t-r <RegEx> \tPrint matching logs with regular expression")

if __name__ == "__main__":
    main()