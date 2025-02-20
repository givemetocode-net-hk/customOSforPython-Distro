# 安裝package
## 先看看有什麼package
```
git@none:/ ~$ get-list
                       Package List                        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃ Name                              ┃ Package Name        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ hello_package                     │ helloworld          │
│ easyhacking install and uninstall │ easyhacking-install │
│ easyhacking tools                 │ easyhacking         │
│ bois-cmd                          │ bois-cli            │
└───────────────────────────────────┴─────────────────────┘
```
透過輸入`get-list` 看看現在有什麼package
## 安裝你的第一個package
```
git@none:/ ~$ get
Package Name : helloworld
Package downloaded successfully
```
現在你就已經安裝好一個Package
## 使用package
```
git@none:/ ~$ package-use
Package Name: helloworld
```
透過輸入`package-use` 去使用你的package
## 解除安裝package
如果你覺得Package有點佔空間，你可以把它移除掉先
```
git@none:/ ~$ package-remove                 
Package Name : helloworld
Remove package ----- helloworld end.
```
輸入`package-remove` 去移除掉你的package
## 製作一個Package
你可以去看看 package-dev-1-chinese.md