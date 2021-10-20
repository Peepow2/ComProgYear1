```
# dict เก็บเป็น {key:value, ...}
# คล้าย list แต่ใช้ key เก็บ index
# key -> value มอง Key เป็น Domain และ value เป็น Range
days = {"MO":"จ", "TU":"อ", "WE":"พ", "TH":"พฤ", "FR":"ศ", "SA":"ส","SU":"อา"}
print(days["MO"], days["WE"], days["FR"])

power2 = {3:9, 4:16, 5:25, 6:36, 9:81}
print(power2[3], power2[6]) # 10 Error เพราะไม่มีอยู่จริง
```

```
# การใส่ key ใหม่จะเพิ่มค่าลงไป
# การใส่ key เดิมจะเปลี่ยนค่าไป
grade = {};          print(grade)
grade["0621"] = "A"; print(grade)
grade["9821"] = "B"; print(grade)
grade["9821"] = "C"; print(grade)

# รันใน dict ให้หมด
power3 = {5:125, 3:27, 9:729, 4:64, 6:216}
for tmp in power3:
    print(tmp, "-->", power3[tmp])
```
