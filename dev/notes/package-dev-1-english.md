# How to create a package in customOSforPython
## Daily Rules
```
1. Some variables are system variables that cannot be changed or used, but you can read them, for example:
#<start_define_system_var>
dir = "/"
system_version = "v1.0.0.9.3 dev"
#</start_define_system_var>
Please do not try to change it or customOS will be corrupted.
2. Make sure to create a README.MD for our staff to read
```
## How to make
Our customOS is accessed through `python package/xxx.py` so you need to write like this:
```
def main() :
 # Your program goes here
# You can also add other functions
if __name__ == "__main__" :
 main() # Prevent your package from being abused
```
## How to give us
You can do this via github/email info@givemetocode.onmicrosoft.com, but github may be slower