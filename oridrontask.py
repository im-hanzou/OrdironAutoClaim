import json
import requests
import time
from bs4 import BeautifulSoup

#created by @ylasgamers @rhdx22
print("\n>>>>>>>>>> Auto Clear Task <<<<<<<<<<\n")
username = input("= Username mu \t: ")
sessionid = input("= cookie\t: ")
print("\n>>>>>>>>>> Jangan Lupa Join AirdropFamilyIDN <<<<<<<<<<")

def get_profile(sessionid):
    url = "https://oridron.com/airdrop/profile"
    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "origin": "https://oridron.com",
        "referer": "https://oridron.com/airdrop/profile"
    }

    # Menambahkan sessionid ke header
    headers["cookie"] = sessionid

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        #print("Claim Berhasil!")
        print("")
        soup = BeautifulSoup(response.text, "html.parser")
        getbalance = str(soup.find_all('span', { 'id': 'balanceContainer'}))
        getname = str(soup.find_all('h5', { 'class': 'mb-0 d-sm-block navbar-profile-name'}))
        soup2 = BeautifulSoup(getbalance, "html.parser")
        soup3 = BeautifulSoup(getname, "html.parser")
        balance = ''.join(filter(str.isdigit, soup2.get_text().strip()))
        print("= Username \t: ",soup3.get_text().strip())
        print("= Balance \t: ",balance)
        print("")
    elif response.status_code == 401:
        print("Tidak diotorisasi. Mohon periksa sessionid Anda.")
    else:
        print("Terjadi kesalahan. Kode status:", response.status_code)
        print("Respon:", response.text)
        
def claimtask(username, sessionid):
    get_profile(sessionid)    
    for quests in range(5, 9):
        url = "https://oridron.com/airdrop/updatequests"+str(quests)+".php"
        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "origin": "https://oridron.com",
            "referer": "https://oridron.com/airdrop/profile"
        }

        # Menambahkan sessionid ke header
        headers["cookie"] = sessionid
        
        data = {
            "usernameplayer": username
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            #print("Claim Berhasil!")
            print("")
            soup = BeautifulSoup(response.text, "html.parser")
            print(soup.get_text().strip())
        elif response.status_code == 401:
            print("Tidak diotorisasi. Mohon periksa sessionid Anda.")
        else:
            print("Terjadi kesalahan. Kode status:", response.status_code)
            print("Respon:", response.text)
def claims():
            claimtask(username, sessionid)
            get_profile(sessionid)

claims()