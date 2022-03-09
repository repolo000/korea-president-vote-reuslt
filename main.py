#made by wasreal.xyz
import os
try:
    import requests
except:
    os.system('pip install requests')
    import requests
try:
    import json
except:
    os.system('pip install json')
    import json
try:
    import time
except:
    os.system('pip install time')
    import time

def num_amount(num):
    req=requests.post('http://info.nec.go.kr/m/electioninfo/electionInfo_report.json',data=data).json()
    result= req['jsonResult']['body'][0]
    return result[f'DUGSU0{num}'], result[f'DUGYUL0{num}'],result[f'HUBO0{num}']

data={
    'electionId': '0020220309',
    'secondMenuId': 'VCCP09',
    'electionCode': 1,
    'cityCode': 0,
    'statementId': 'VCCP09_#1'
}
os.system('cls')
num=input(f'[?] 선거번호를 입력하세요: ')
os.system('cls')
while 1:
    all_vote,all_percent,name=num_amount(f'{num}')
    os.system(f'title {name}({num}) 선거 - {all_percent}% ({all_vote})')
    print(f'{name}의 전국 투표율은 {all_percent}% ({all_vote})입니다.',end='\r', flush=True) 
    time.sleep(1)
