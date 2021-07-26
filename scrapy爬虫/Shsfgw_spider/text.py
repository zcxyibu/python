import re
str='发布日期：2020-11-16'
dd = re.findall('(\d+-\d+-\d+)',str)
print(dd)