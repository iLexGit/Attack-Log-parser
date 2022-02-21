import json
import sys
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
    file = json.load(loadAttacks())
    
    for entry in file:
        attacks.append(Attack(entry["sourceip"], entry["destinationip"], entry["logs"]))

    for attack in attacks:
            index = isUnique(attack.src)
            if index == 0:
                attackers.append(Attacker(attack.src, 1))
            else:
                attackers[index].reqs+=1

    if sys.argv[2] == "-h":
        printHelp()

    elif sys.argv[2] == "-l":
        listAttackers()
    
    elif sys.argv[2] == "-s":
        if len(sys.argv) == 3:
            showAttack(sys.argv[2])
        else:
            print("[KO] Bad use\n")
            printHelp()

    #while True:
        #Menu()

def loadAttacks ():
    try:
        file = open(sys.argv[1], "r")
    except IOError:
        print("File: <", sys.argv[1], "> not found")
        sys.exit()
    print("\n[OK] Logs loaded")
    return file

def Menu():
    op = input("-----------------------------------------\n\t1. Show Attackers\n\t2. Show Attack from IP\n\te. Exit\n\toption -> ")
    if op == "1":
        print("\nAttackers:\n")
        #listAttackers()
    elif op == "2":
        showAttack()
    elif op == "e":
        print("\nEXITING...\n")
        sys.exit(1)
    else:
        print("\tInvalid Input")

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
    for attack in attacks:
        if attack.src == ip:
            index+=1
            print("\nATTACK ", index, "\n\tTarget: ", attack.dst, "\n\tLogs ", len(attack.logs),":")
            for i in range(len(attack.logs)):
                print("\t\t", attack.logs[i]["time"], "\t[", attack.logs[i]["parsedMessage"]["level"], "]", "\n\t", attack.logs[i]["parsedMessage"]["message"][attack.logs[i]["parsedMessage"]["message"].index("\""):], "\n")

def printHelp():
    print("Log parser v1\nAlejandro Marti, Lupovis\nhttps://github.com/iLexGit/Attack-Log-parser\n")
    print("Usage: python logParser.py [LOG_FILE] [OPTIONS]\n")
    print("\t-h\t\tShow help ouptut")
    print("\t-l\t\tList source IP with number of requests sent")
    print("\t-s <IP>\t\tPrint all logs from specified source IP")

if __name__ == "__main__":
    main()