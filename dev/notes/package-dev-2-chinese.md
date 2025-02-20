# 為你的package製作installer
## 程式例子
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

true = input("Y = install N= uninstall :")
if true == "Y" :
    install()
else :
    uninstall()
```
這是一個基礎的package installer， 你也可以在這個的基礎上作出更改。