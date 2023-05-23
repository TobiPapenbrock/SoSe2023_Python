import os 
import platform
import pwd

# Temp Verz
#print(os.environ['TMP'])

# aktuelles Verz
print(os.getcwd())
# Betriebssystem
print(platform.system())

# Prozessor Typ
print(platform.machine()) 

# Aktueller Username 
print(os.getlogin())
print(pwd.getpwuid(os.getuid())[0])

