from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
company = []
job = []
job_html = []
company_html = []
content = []
ob_reqiured = {
    '身分條件':[],
    '具備駕照':[],
    '語文條件':[],
    '科系要求':[],
    '工作經歷':[],
    '薪資':[]
}
allSpeciality = []
each_Specialit = []

for page in range(1,3):
    url = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E5%B8%AB&expansionType=job&order=15&asc=0&page={}&mode=s&jobsource=2018indexpoc".format(str(page))
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"html.parser")
    # print(soup)
    title = soup.select('div[class="b-block__left"]')
    # print(title)
    jobhtmlforloop = []
    speciality_dict = dict()
    speciality_list = list()
    try:
        for each_work in title:
            for each_workname in each_work('h2'):
                for each_name in each_workname('a'):
                    # print('Job:','https:'+each_name['href'])
                    job_html.append('https:'+each_name['href'])
                    jobhtmlforloop.append('https:'+each_name['href'])
                    # print('Job:',each_name.text)
                    job.append(each_name.text)
            for each_workname in each_work('li'):
                for each_company in each_workname('a'):
                    # print('Company:',each_company.text)
                    company.append(each_company.text)
                    # print('Company:','https:'+each_company['href'])
                    company_html.append('https:'+each_company['href'])

    except:
        print('x')
    for i in jobhtmlforloop:
        id = i.split('/')[-1].split('?')[0]
        curl = "https://www.104.com.tw/job/ajax/content/{}".format(id)
        headers = {'Referer': "https://www.104.com.tw/job/ajax/content/{}".format(id),
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        cres = requests.get(curl,headers=headers)
        cj = json.loads(cres.text)
        content.append(''.join(''.join(cj['data']['jobDetail']['jobDescription'].split('\n')).split('\r')))
        # print(cj['data']['condition'])
        o = []
        for i in cj['data']['condition']['acceptRole']['role']:
            o.append(i['description'])
        # print(i['description'])
        ob_reqiured['身分條件'].append(o)
        ob_reqiured['具備駕照'].append(cj['data']['condition']['driverLicense'])
        if cj['data']['condition']['language'] == []:
            ob_reqiured['語文條件'].append(cj['data']['condition']['language'])
        else:
            ob_reqiured['語文條件'].append(cj['data']['condition']['language'][0]['language']+':'+cj['data']['condition']['language'][0]['ability'])
        ob_reqiured['科系要求'].append(cj['data']['condition']['major'])
        ob_reqiured['工作經歷'].append(cj['data']['condition']['workExp'])
        ob_reqiured['薪資'].append(cj['data']['jobDetail']['salary'])
        jobSpeciality = []
        for i in cj['data']['condition']['specialty']:
            allSpeciality.append(i['description'])
            jobSpeciality.append(i['description'])
        each_Specialit.append(jobSpeciality)
        cleanSpeciality = list(set(allSpeciality))
    # print(cleanSpeciality)
    # print(each_Specialit)
    for i in each_Specialit:
        x = dict()
        for k in range(0,len(i)):
            for h in range (0,len(cleanSpeciality)):
                if i[k] == cleanSpeciality[h]:
                    if cleanSpeciality[h] not in speciality_dict:
                        speciality_dict[cleanSpeciality[h]] = 1
                    else:
                        speciality_dict[cleanSpeciality[h]] += 1
                    if cleanSpeciality[h] not in x:
                        x[cleanSpeciality[h]] = 1
                    else:
                        x[cleanSpeciality[h]] += 1
                else:
                    if cleanSpeciality[h] not in speciality_dict:
                        speciality_dict[cleanSpeciality[h]] = 0
                        
                    else: 
                        speciality_dict[cleanSpeciality[h]] += 0
                    if cleanSpeciality[h] not in x:
                        x[cleanSpeciality[h]] = 0
                    else:
                        x[cleanSpeciality[h]] += 0
        speciality_list.append(x)
    # print(speciality_dict)
    specialframe = DataFrame(data = speciality_list ,columns=cleanSpeciality)
    specialframe = specialframe.fillna(0)
    # print(specialframe)

# print(ob_reqiured['身分條件'])


data = {"Company":company,"Company Html":company_html,"Opening Job":job,
        "Opening Job Html":job_html,"Job's Content":content}

data.update(ob_reqiured)
df = DataFrame(data)
dfs = pd.concat([df,specialframe],axis=1)
# print(df)
dfs.to_csv('104人力網.csv',encoding="utf-8-sig")
dfs.to_excel('104人力網.xlsx',encoding="utf-8-sig")


path = '擅長工具.txt'
f = open(path,'w',encoding='utf-8')
for key,value in speciality_dict.items():
    f.write(key+':'+str(value)+'\n')
f.close

print('Completed')





# ### 檢測用 ###
# def L(self):
#     return(len(self))
# print('company:',L(company))
# print('company_html:',L(company_html))
# print('job:',L(job))
# print('job_html:',L(job_html))
# print('content:',L(content))
# print(L(ob_reqiured['身分條件']))
# print(L(ob_reqiured['具備駕照']))
# print(L(ob_reqiured['語文條件']))
# print(L(ob_reqiured['科系要求']))
# print(L(ob_reqiured['工作經歷']))
# print(L(ob_reqiured['薪資']))
# print(L(speciality_list))