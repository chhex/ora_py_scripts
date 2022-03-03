#!/usr/bin/env python
import cx_Oracle 
import argparse

def stmt_tester():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--pw', '-p',  required=True, help="User password")
    arg_parser.add_argument('--user', '-u', required=True, help="User") 
    arg_parser.add_argument('--stmt','-s',  required=True, help="Statement which will be executed")
    arg_parser.add_argument('--target', '-t', default='CHEI212', help='Target SID')
    args = arg_parser.parse_args()
    dsn = cx_Oracle.makedsn(f"%s.apgsga.ch" % args.target, 1521, sid=args.target)
    with cx_Oracle.connect(user=f"%s" % args.user, password=f"%s" % args.pw,  dsn=dsn,
            encoding="UTF-8") as connection:
        cur = connection.cursor()
        for row in cur.execute(f"%s" % (args.stmt)):
            print(row)


if __name__ == '__main__':
    stmt_tester()
