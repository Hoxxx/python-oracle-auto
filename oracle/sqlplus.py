'''
通过 Python 与 SQL*Plus 进程通信
'''

import os
from subprocess import Popen, PIPE

sqlplus = Popen(["sqlplus", "-S", "/", "as", "sysdba"], stdout=PIPE, stdin=PIPE)
sqlplus.stdin.write("select sysdate from dual;"+os.linesep)
sqlplus.stdin.write("select count(*) from all_objects;"+os.linesep)
out, err = sqlplus.communicate()
print out
