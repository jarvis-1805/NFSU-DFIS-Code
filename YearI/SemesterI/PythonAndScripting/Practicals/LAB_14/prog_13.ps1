# Regex

"book" -match "oo"
"coopy" -match "c...y"
"big" -match "b[iou]g"
"cnd" -match "[a-e]nd"
"and" -match "[^brt]nd"
"book" -match "^bo"
"book" -match "ok$"
"luggage" -match "g*"
"baggy" -match "g?"

1234 -match "\P{Ll}+"

"abcd defg" -match "\w+" #(this matches abcd)
"abcd defg" -match "\W+" #(this matches the space)
"abcd defg" -match "\s+"

12345 -match "\d+"

"abcd" -match "\D+"
"abc" -match "\w*"
"xyxyxy" -match "xy+"
"xyxyxy" -match "x+"
"abc" -match "\w{2}"
"abc" -match "\w{2,5}"
