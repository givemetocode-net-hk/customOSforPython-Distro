# Make an installer for your package
## Program Example
```
import platform
import os

def install() :
 if platform.system() == "Linux" :
 os.system("pip install pytube")
 os.system("pip install scapy")
def uninstall() :
 if platform.system() == "Linux" :
 os.system("pip uninstall pytube")
 os.system("pip uninstall scapy")
 print("then, go to customOS to delete 'easyhacking' and 'asciigenerator-install'.")

true = input("Y = install N = uninstall :")
if true == "Y" :
 install()
else :
 uninstall()
```
This is a basic package installer, you can also make changes based on this.