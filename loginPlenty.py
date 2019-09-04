import getpass
import requests
import json
import time

def loginInput():
    print("Please enter your PM login data and press Enter button")
    time.sleep(0.5)
    username = input("username: ")
    time.sleep(0.5)
    password = getpass.getpass("password: ")
    return username, password

def loginPost(sellerUrl, username, password):
    sellerUrl = sellerUrl
    username, password = loginInput()
    route = "/rest/login"
    paras = f"?username={username}&password={password}"
    loginUrl = sellerUrl + route + paras  
    r = requests.post(loginUrl)
    return r

def loginTries(sellerUrl):
    sellerUrl = sellerUrl
    username = ""
    password = ""
    count = 0
    while count < 3:
        count += 1
        r = loginPost(sellerUrl, username, password)
        if r.status_code == 200:
            print ("login successful")
            login_r_js = r.json()
            token_type = login_r_js['token_type']
            access_token = login_r_js['access_token']
            refresh_token = login_r_js['refresh_token']
            head = {'Authorization': token_type + " " + access_token}
            
            return token_type, access_token, refresh_token, head
            break
        else:
            print ("Your " + str(count) + ". login failed, please try again! (max. 3 tries)")
    else:
        print ("Your 3 tries all failed, please contact admin!")

	
if __name__== "__main__":
    loginTries(sellerUrl)
