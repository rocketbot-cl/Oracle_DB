import os
import json
from subprocess import Popen, PIPE
import sys

global cred_oracle
base_path = tmp_global_obj["basepath"]
curpath = base_path  + "modules" + os.sep + "Oracle" + os.sep + "libs"
bin_path = base_path + "modules" + os.sep + "Oracle" + os.sep + "bin"

if bin_path not in os.environ['PATH']:
    os.environ["PATH"] += os.pathsep + bin_path

if curpath not in sys.path:
    sys.path.append(curpath)
import cx_Oracle

global con
global cursor


module = GetParams('module')

if module == "connect":
    user = GetParams('user')
    password = GetParams('password')
    dsn = GetParams('dsn')
    result = GetParams('result')
    #process = "oracle.exe {user} {password} {dsn} \"select name from v$database\"".format(user=user, password=password,
                                                                                          #dsn=dsn)
    #con = Popen(process, env=os.environ.copy(), shell=True, stdout=PIPE, stderr=PIPE)
    con = cx_Oracle.connect(user, password, dsn)
    try:
        cursor = con.cursor()
        res = True
        SetVar(result, res)
    except Exception as e:
        PrintException()
        raise e

if module == "execute":
    query = GetParams('query')
    result = GetParams('result')

    # user = cred_oracle['user']
    # password = cred_oracle['password']
    # dsn = cred_oracle['dsn']
    # # print("ddd", cred_oracle)
    # process = "oracle.exe {user} {password} {dsn} \"{query}\"".format(user=user, password=password,
    #                                                                   dsn=dsn, query=query)

    # print('ddd', process)
    # con = Popen(process, env=os.environ.copy(), shell=True, stdout=PIPE, stderr=PIPE)

    try:
       cursor.execute(query)
       if query.lower().startswith("insert") or query.lower().startswith("update") or query.lower().startswith(
               "delete") or query.lower().startswith("alter"):
           con.commit()
           if result:
               SetVar(result, True)
        # cred_oracle = {"user": user, "password": password, "dsn": dsn}
       else:
           data = [r for r in cursor]
           if result:
               SetVar(result, data)
    except Exception as e:
        PrintException()
        raise e
