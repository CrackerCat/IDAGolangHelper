# IDAGolangHelper
Set of IDA Pro scripts for parsing GoLang types information stored in compiled binary


This is update for https://gitlab.com/zaytsevgu/GoUtils2.0

Differences:
  1. Add support for go1.8 and go1.9, go1.10 (well actually it seems no difference from go1.9)
  2. Automatically add user-defined types to IDA. (Can be checked in Shift+f9 view)
  3. Add some not very advanced string recognition. You can press Shift+S to process current function


https://2016.zeronights.ru/wp-content/uploads/2016/12/GO_Zaytsev.pdf - My presentation about Golang reversing

## 20200811
- Ported to Python3.0 and IDA 7.5 
- Gui re-written using pyqt
- Added GO src code parser 
- Executing Rename function adds function declaration and comments from Go SRC code. Example. 

```
.text:0044F710       ; // Valid reports whether p consists entirely of valid UTF-8-encoded runes.
.text:0044F710       ; func Valid(p []byte) bool
.text:0044F710       ; Attributes: info_from_lumina
.text:0044F710
.text:0044F710       ; void __cdecl unicode_utf8_Valid(__uint8 p, bool _r1)
```

Disclaimer: In progress. Modifying the project for learning. Credit goes to the original author. 