from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
def crew(keyword):
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
    keyword = keyword.encode('utf-8')
    for page in range(1,3):
        url = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword="+keyword+"&expansionType=job&order=15&asc=0&page={}&mode=s&jobsource=2018indexpoc".format(str(page))
        res = requests.get(url,headers=headers)
        soup = BeautifulSoup(res.text,"html.parser")
        title = soup.select('div[class="b-block__left"]')
        jobhtmlforloop = []
        speciality_dict = dict()
        speciality_list = list()    
        try:
            for each_work in title:
                for each_workname in each_work('h2'):
                    for each_name in each_workname('a'):
                        job_html.append('https:'+each_name['href'])
                        jobhtmlforloop.append('https:'+each_name['href'])
                        job.append(each_name.text)
                for each_workname in each_work('li'):
                    for each_company in each_workname('a'):
                        company.append(each_company.text)
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
            o = []              
            for i in cj['data']['condition']['acceptRole']['role']:
                o.append(i['description'])
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

        specialframe = DataFrame(data = speciality_list ,columns=cleanSpeciality)
        specialframe = specialframe.fillna(0)

    data = {"Company":company,"Company Html":company_html,"Opening Job":job,
            "Opening Job Html":job_html,"Job's Content":content}

    data.update(ob_reqiured)
    df = DataFrame(data)
    dfs = pd.concat([df,specialframe],axis=1)
    dfs.to_csv(keyword+'.csv',encoding="utf-8-sig")
    dfs.to_excel(keyword+'.xlsx',encoding="utf-8-sig")
    path = keyword+'_擅長工具.txt'
    f = open(path,'w',encoding='utf-8')
    for key,value in speciality_dict.items():
        f.write(key+':'+str(value)+'\n')
    f.close
    print('Completed')



