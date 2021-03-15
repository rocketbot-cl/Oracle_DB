import os
import json
from subprocess import Popen, PIPE
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Oracle" + os.sep + "libs"
bin_path = base_path + "modules" + os.sep + "Oracle" + os.sep + "bin"

if bin_path not in os.environ['PATH']:
    os.environ["PATH"] += os.pathsep + bin_path

if cur_path not in sys.path:
    sys.path.append(cur_path)

import cx_Oracle

# Globals declared here
global mod_oracle_sessions
# Default declared here
SESSION_DEFAULT = "default"
# Initialize settings for the module here
try:
    if not mod_oracle_sessions:
        mod_oracle_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_oracle_sessions = {SESSION_DEFAULT: {}}


module = GetParams('module')

if module == "connect":
    user = GetParams('user')
    password = GetParams('password')
    dsn = GetParams('dsn')
    session = GetParams('session')
    result = GetParams('result')

    if not session:
        session = SESSION_DEFAULT

    con = cx_Oracle.connect(user, password, dsn)
    try:
        cursor = con.cursor()
        mod_oracle_sessions[session] = {
            "connection": con,
            "cursor": cursor
        }
        SetVar(result, True)
    except Exception as e:
        SetVar(result, False)
        PrintException()
        raise e

if module == "execute":
    query = GetParams('query')
    session = GetParams('session')
    result = GetParams('result')

    if not session:
        session = SESSION_DEFAULT

    cursor = mod_oracle_sessions[session]["cursor"]
    con = mod_oracle_sessions[session]["connection"]

    try:
        cursor.execute(query)
        if query.lower().startswith(("insert", "update", "delete", "alter")):
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

if module == "close":
    session = GetParams('session')

    if not session:
        session = SESSION_DEFAULT

    cursor = mod_oracle_sessions[session]["cursor"]
    con = mod_oracle_sessions[session]["connection"]

    try:
        cursor.close()
        con.close()
    except Exception as e:
        PrintException()
        raise e

