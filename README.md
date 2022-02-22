# Log parser

## How to run
`python attack_interpreter [JSON_ATTACKS_LOG]`

## Help Menu
Log parser v1.01\
Alejandro Marti, Lupovis\ 
https://github.com/iLexGit/logParser 

Usage: python logParser.py [TYPE OF LOG] <LOG_FILE_PATH> [OPTIONS]

[TYPE OF LOG]

	-A		Attacks log
	-L		Regular log

[ATTACK LOG OPTIONS]

	-l		List source IP with number of attacks performed
	-s <IP>		Print all logs from specified source IP
	-r <RegEx>	Print all logs from attack with a matching payload
	-ru <RegEx>	Print only matching logs
## Future Improvements
- [ ] Consider migrating to *Golang* (defo faster)
- [x] Beautify log output
- [ ] Sort attackers array (make sure its fastest sortin method)
- [ ] Add functionality to read and parse regular (non-attack) logs
- [x] Allow RegEx testing
- [ ] Add more stats
- [x] Replace menu with flag options and implement *-h*
- [ ] Add functionality to match logs againts [attackDB](https://github.com/iLexGit/attackDB) project
- [ ] Create dependency to also clone [attackDB](https://github.com/iLexGit/attackDB) when cloning this project
