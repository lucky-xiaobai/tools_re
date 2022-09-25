import string
import base64

table = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
t = input('输入被修改后的base64表: ')
s = input('输入base64加密后的字符串: ')

ss = ''
for i in range(len(s)):
    tmp = t.find(s[i])
    ss += table[tmp]

try:
    flag = base64.b64decode(ss.encode())
    print(flag)
except:
    try:
        flag = base64.b64decode((ss + '=').encode())
        print(flag)
    except:
        flag = base64.b64decode((ss + '==').encode())
        print(flag)
