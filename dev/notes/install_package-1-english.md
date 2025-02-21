# Install package
## First see what packages are available
```
git@none:/ ~$ get-list
 Package List
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Name ┃ Package Name ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ hello_package │ helloworld │
│ easyhacking install and uninstall │ easyhacking-install │
│ easyhacking tools │ easyhacking │
│ bois-cmd │ bois-cli │
└──────────────────────────────────┴─────────────────────────┘
```
Type `get-list` to see what packages are available.
## Installing your first package
```
git@none:/ ~$ get
Package Name: helloworld
Package downloaded successfully
```
Now you have installed a Package
## Using package
```
git@none:/ ~$ package-use
Package Name: helloworld
```
Use your package by typing `package-use`
## Uninstall package
If you think the package takes up a lot of space, you can remove it first.
```
git@none:/ ~$ package-remove
Package Name: helloworld
Remove package ----- helloworld end.
```
Type `package-remove` to remove your package
## Make a Package
You can check out package-dev-1-chinese.md