# 如何在customOSforPython製作package
## 日常規則
```
1. 有一些變數是系統變數不能更改或使用，但是你可以閱讀，例如：
#<start_define_system_var>
dir = "/"
system_version = "v1.0.0.9.3 dev"
#</start_define_system_var>
請不要嘗試更改他否則customOS將會損壞。
2. 一定要製造一個 README.MD 方便我們的人員閱讀
```
## 如何製作
我們的customOS是透過 `python package/xxx.py` 去訪問的 所以你需要這樣編寫：
```
def main() :
    # 這裏是你的程式
# 你也可以增加其他的function
if __name__ == "__main__" :
    main() # 防止你的package被人濫用
```
## 如何給我們
你可以透過github/email info@givemetocode.onmicrosoft.com 的方式 但是github可能會比較慢