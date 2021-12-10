from requests import get
from json import loads
from pandas import DataFrame,concat
from urllib.parse import quote


def crew(keyword,pages):
    job_name = list() #職位名稱
    company_name = list() #公司名稱
    company_address = list() #公司地址
    short_content = list() #簡短工作內容
    job_html =list() #工作網址
    company_html = list() #公司網址
    education = list() #教育程度
    workexp = list() #工作經驗
    salary = list() #薪水
    keyword_quote = quote(keyword)
    for page in range (1,int(pages)+1):
        url = "https://www.104.com.tw/jobs/search/list?ro=0&kwop=7&keyword="+keyword_quote+"&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=15&asc=0&page="+str(page)+"&mode=s&jobsource=2018indexpoc"
        headers = {"Referer":"https://www.104.com.tw/jobs/search/?keyword="+keyword_quote+"&order=1&jobsource=2018indexpoc&ro=0",
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

    dfs.to_excel(keyword+'.xlsx', encoding="utf-8-sig")
    # dfs.to_csv(keyword+'.csv', encoding="utf-8-sig")
    print('Completed')

crew(input("請輸入您想查詢的職業："),input("請輸入您想查詢總頁面數："))

input("Press Enter to exit")