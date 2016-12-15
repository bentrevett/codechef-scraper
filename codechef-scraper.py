import requests, bs4, csv

#dicts to hold submission ids
submission_ids = []

PROBLEM_NAME = 'TEST'
SUBMISSION_LANGUAGE = 'Python3'
SUBMISSION_LANGUAGE_NUMBER = '116'

#gets data from page
#language=116 = PYTHON 3.4
res = requests.get('https://www.codechef.com/status/'+PROBLEM_NAME+'?page=0&sort_by=All&sorting_order=asc&language='+SUBMISSION_LANGUAGE_NUMBER+'&status=15&handle=&Submit=GO')
 
#check if the download succeeded 
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: {}'.format(exc))

#turn the context (res.text) into a BeautifulSoup object
site_content = bs4.BeautifulSoup(res.text, "html.parser")

#gets the number of the last page, used for looping through
elems = site_content.select('div[class=pageinfo]')

num_pages = int(elems[0].getText().split(' ')[2])

for i in range(num_pages+1):
    
    res = requests.get('https://www.codechef.com/status/'+PROBLEM_NAME+'?page='+str(i)+'&sort_by=All&sorting_order=asc&language='+SUBMISSION_LANGUAGE_NUMBER+'&status=15&handle=&Submit=GO')
    
    #check if the download succeeded 
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: {}'.format(exc))
        
    #turn the context (res.text) into a BeautifulSoup object
    site_content = bs4.BeautifulSoup(res.text, "html.parser")
    
    #want every submission ids are in td with width 60
    elems = site_content.select('td[width=60]')
 
    for j in range(len(elems)):
        submission_ids.append(elems[j].getText())
 
    print("page {}/{}, total submissions found: {}".format(i,num_pages,len(submission_ids)))
 
 #opening a csv file for submissions to be written to
csvfile = open('codechef/submissions'+PROBLEM_NAME+SUBMISSION_LANGUAGE+'.csv','w+',encoding='utf-8',newline='')
csvwriter = csv.writer(csvfile)
 
for i in range(len(submission_ids)):
    
    #open submission page
    res = requests.get('https://www.codechef.com/viewplaintext/'+str(submission_ids[i]))
    
    #check if the download succeeded 
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: {}'.format(exc))
        
    #turn the context (res.text) into a BeautifulSoup object
    site_content = bs4.BeautifulSoup(res.text, "html.parser")
    
    #code is simply within a <pre> tag
    elems = site_content.select('pre')
    
    print("writing submission {}/{}, submission_id = {}".format(i+1,len(submission_ids),submission_ids[i]))
    
    #write to csv file with start and end markers
    csvwriter.writerow(["~~start~~"+elems[0].getText()+"~~end~~"])
    

#close the csv file
csvfile.close()
