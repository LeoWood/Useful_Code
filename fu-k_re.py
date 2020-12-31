import re

### 在某字符串中匹配特定字符开头结尾
text = "【我去干】嘛呢asdfsdjf [sdaf]【撒地方】"

## 贪婪匹配
re.findall(r'【.*】',text)
#  ['【我去干】嘛呢asdfsdjf [sdaf]【撒地方】']

## 非贪婪匹配
re.findall(r'【.*?】',text)
# ['【我去干】', '【撒地方】']

