import json
import requests
import time
from bs4 import BeautifulSoup

#created by @ylasgamers @rhdx22
print("Auto Claim Oridron Tiap 60 Menit")
        
def claimeveryhours(username, sessionid):
    url = "https://oridron.com/airdrop/updateclaims.php"
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

def claimschedule():
    while True:
        with open('data.txt', 'r') as file:
            for line in file:
                username, sessionid = line.strip().split('|')
                claimeveryhours(username, sessionid)
                time.sleep(3600)

claimschedule()