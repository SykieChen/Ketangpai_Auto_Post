# coding=utf-8
import requests
import userinfo
import sys
import time
import os

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

def upload(session,filename):
    h_url="http://www.ketangpai.com/UploadApi/upload"
    print(filename)
    h_dat={
        'file' : (os.path.basename(filename),open(filename,'rb'))
    }
    r = session.post(h_url, files=h_dat)
    # print(h_dat)
    if r.json()['status'] == 1 : return r.json()['fileid']
    else :
        print(r.json())
        return -1

def get_course_id(session, index):
    h_url="http://www.ketangpai.com/CourseApi/lists"
    r = session.get(h_url)
    return r.json()['lists'][index]['id']

def post_noti(session, title, info, fileid, courseid):
    h_url="http://www.ketangpai.com/NotifyApi/addNotify"
    h_val={
        "courseid" : courseid,
        "title" : title,
        "content" : info,
        "attachment" : fileid+'|'
    }
    r = session.post(h_url, data=h_val)
    return r.json()['status']

if __name__ == '__main__':
    print("Useage: autopost.py filename course_index")
    print("\tif course_index is not given, it will be posted to the first class.")
    if len(sys.argv)>=2 :
        if len(sys.argv)==2 : course_index=0
        else: course_index=int(sys.argv[2])
        # open session
        print("[info] Opening session...")
        session = requests.Session()
        if (login(session)):
            # login success
            print("[okay] Session started.")
            print("[info] Uploading file...")
            file_id = upload(session,sys.argv[1])
            if file_id==-1:
                print("[error] Upload failed!")
                sys.exit()
            else:
                print("[okay] File uploaded.")
                print("[info] Course index", course_index)
                print("[info] Getting course ID...")
                course_id = get_course_id(session, course_index)
                print("[okay] Course ID is", course_id)
                print("[info] Publishing notification...")
                if post_noti(session,time.asctime(time.localtime(time.time())),sys.argv[1],file_id,course_id):
                    print("[okay] Post succeeded.")
                else:
                    print("[error] Post failed.")
                    sys.exit()


        else:
            print("[error] Session could not be established.")
    else :
        print("[error] Parameters error!")