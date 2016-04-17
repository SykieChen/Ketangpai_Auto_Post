# coding=utf-8
import requests
import userinfo

#auto login


def login(session):
    h_url="http://www.ketangpai.com/UserApi/login"
    h_val={
        "email" : userinfo.usr,
        "password" : userinfo.pwd
    }
    r = session.post(h_url, data=h_val)
    if r.json()["info"] == "success" : return 1
    else: return 0

def upload(session):
    h_url=""


if __name__ == '__main__':
    # open session
    session = requests.Session()
    if (login(session)):
        # login success
        print(1)

