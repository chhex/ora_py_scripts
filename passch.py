#!/usr/bin/env python
import cx_Oracle 
import argparse

def pass_change():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--pw', '-p',  required=True, help="Zo password")
    arg_parser.add_argument('--user', '-u', required=True, help="User to be changed") 
    arg_parser.add_argument('--to',  required=True, help="Target password")
    arg_parser.add_argument('--target', '-t', default='CHEI212', help='Target SID')
    args = arg_parser.parse_args()
    dsn = cx_Oracle.makedsn(f"%s.apgsga.ch" % args.target, 1521, sid=args.target)
    with cx_Oracle.connect(user="zo", password=f"%s" % args.pw,  dsn=dsn,
            encoding="UTF-8") as connection:
        cur = connection.cursor()
        cur.execute(f"alter user %s identified by %s" % (args.user, args.to)) 
        cur.execute(f"alter user %s account unlock" % (args.user))

if __name__ == '__main__':
    pass_change()
