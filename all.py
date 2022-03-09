#made by wasreal.xyz
import os
try:
    import requests
except:
    os.system('pip install requests')
    import requests
try:
    import time
except:
    os.system('pip install time')
    import time

def num_amount(num):
    req=requests.post('http://info.nec.go.kr/m/electioninfo/electionInfo_report.json',data=data).json()
    result= req['jsonResult']['body'][0]
    return result[f'DUGSU0{num}'], result[f'DUGYUL0{num}'],result[f'HUBO0{num}']
def all_vote(num):
    result=''
    num=int(num)
    for i in range(1,num):
        result+=f'{i}번째 선거의 투표율은 {num_amount(i)[1]}% ({num_amount(i)[0]})\n'
    return result
data={
    'electionId': '0020220309',
    'secondMenuId': 'VCCP09',
    'electionCode': 1,
    'cityCode': 0,
    'statementId': 'VCCP09_#1'
}
os.system('cls')
while 1:
    all_vote,all_percent,name=num_amount(f'1')
    all_vote2,all_percent2,name2=num_amount(f'2')
    차이=abs(int(all_vote.replace(',',''))-int(all_vote2.replace(',','')))
    print(f'이재명: {all_percent}% ({all_vote}) l 윤석열: {all_percent2}% ({all_vote2}) 차이: {차이}',end='\r', flush=True) 
    os.system(f'title 이재명: {all_percent}% ({all_vote}) l 윤석열: {all_percent2}% ({all_vote2}) 차이: {차이}')
    time.sleep(1)
