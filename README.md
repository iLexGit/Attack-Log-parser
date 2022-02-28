# Log parser

## How to run
`python logParser.py [TYPE OF LOG] <LOG_FILE_PATH> [OPTIONS]`

## Help Menu
```
Log parser v1.01
Alejandro Marti, g3n3SYS
https://github.com/iLexGit/logParser 

[TYPE OF LOG]

	-A		Attacks log
	-L		Regular log

[ATTACK LOG OPTIONS]

	-l		List source IP with number of attacks performed
	-s <IP>		Print all logs from specified source IP
	-r <RegEx>	Print all logs from attack with a matching payload
	-ru <RegEx>	Print only matching logs

```
## Future Improvements
- [ ] Consider migrating to *Golang* (defo faster)
- [x] Beautify log output
- [ ] Sort attackers array (make sure its fastest sortin method)
- [ ] Add functionality to read and parse regular (non-attack) logs
- [x] Allow RegEx testing
- [ ] Add more stats
- [x] Replace menu with flag options and implement *-h*
- [ ] Add functionality to match logs againts [attackDB](https://github.com/Lupovis/attackDB) project
- [ ] Create dependency to also clone [attackDB](https://github.com/Lupovis/attackDB) when cloning this project
