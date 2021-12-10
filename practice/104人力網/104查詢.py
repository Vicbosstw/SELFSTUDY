from requests import get
from json import loads
from pandas import DataFrame,concat

job_name = list() #職位名稱
company_name = list() #公司名稱
company_address = list() #公司地址
short_content = list() #簡短工作內容
job_html =list() #工作網址
company_html = list() #公司網址
education = list() #教育程度
workexp = list() #工作經驗
salary = list() #薪水
for page in range (1,3):
    url = "https://www.104.com.tw/jobs/search/list?ro=0&kwop=7&keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=15&asc=0&page="+str(page)+"&mode=s&jobsource=2018indexpoc"
    headers = {"Referer":"https://www.104.com.tw/jobs/search/?keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E5%B8%AB&order=1&jobsource=2018indexpoc&ro=0",
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = get(url,headers=headers)
    json_string = loads(res.text)['data']['list']
    for i in json_string:
        job_name.append(i['jobName'])
        company_name.append(i['custName'])
        short_content.append(''.join(''.join(i['description'].split('\n')).split('\r')))
        company_address.append(i['jobAddrNoDesc']+i['jobAddress'])
        job_html.append('https:'+i['link']['job'])
        company_html.append('https:'+i['link']['cust'])
        education.append(i['optionEdu'])
        workexp.append(i['periodDesc'])
        salary.append(i['salaryDesc'])
####################=======================================############################
allSpecialty = list()
each_Specialty = list()
for i in job_html:
    id = i.split('/')[-1].split('?')[0]
    curl = "https://www.104.com.tw/job/ajax/content/{}".format(id)
    headers = {'Referer': "https://www.104.com.tw/job/ajax/content/{}".format(id),
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    cres = get(curl,headers=headers)
    cj = loads(cres.text)['data']['condition']['specialty']
    jobSpecialty = list()
    for k in cj:
        allSpecialty.append(k['description'])
        jobSpecialty.append(k['description'])
    each_Specialty.append(jobSpecialty)
cleanSpecialty = list(set(allSpecialty))
speciality_dict = dict()
specialty_list = list()
for i in each_Specialty:
        x = dict()
        for k in range(0,len(i)):
            for h in range (0,len(cleanSpecialty)):
                if i[k] == cleanSpecialty[h]:
                    if cleanSpecialty[h] not in speciality_dict:
                        speciality_dict[cleanSpecialty[h]] = 1
                    else:
                        speciality_dict[cleanSpecialty[h]] += 1
                    if cleanSpecialty[h] not in x:
                        x[cleanSpecialty[h]] = 1
                    else:
                        x[cleanSpecialty[h]] += 1
                else:
                    if cleanSpecialty[h] not in speciality_dict:
                        speciality_dict[cleanSpecialty[h]] = 0
                        
                    else: 
                        speciality_dict[cleanSpecialty[h]] += 0
                    if cleanSpecialty[h] not in x:
                        x[cleanSpecialty[h]] = 0
                    else:
                        x[cleanSpecialty[h]] += 0
        specialty_list.append(x)

specialframe = DataFrame(data = specialty_list ,columns=cleanSpecialty)
specialframe = specialframe.fillna(0)

data = {
        'company':company_name,
        'company_address':company_address,
        'company_html':company_html,
        'Opening_Job':job_name,
        'Job_html':job_html,
        'education':education,
        'workexp':workexp,
        'salary':salary,
        'short_content':short_content
}
df = DataFrame(data=data)
dfs = concat([df,specialframe],axis=1)
dfs.to_excel('嘗試.xlsx',encoding="utf-8-sig")


path = '擅長工具.txt'
f = open(path,'w',encoding='utf-8')
for key,value in speciality_dict.items():
    f.write(key+':'+str(value)+'\n')
f.close

print('Completed')
