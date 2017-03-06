import requests, bs4, csv

#dicts to hold submission ids
submission_ids = []

PROBLEM_NAME = 'HOLES'
SUBMISSION_LANGUAGE = 'C'
SUBMISSION_LANGUAGE_NUMBER = '11'

#gets data from page
#language=116 = PYTHON 3.4
res = requests.get('https://www.codechef.com/status/'+PROBLEM_NAME+'?page=0&sort_by=All&sorting_order=asc&language='+SUBMISSION_LANGUAGE_NUMBER+'&status=11&handle=&Submit=GO')
 
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

total_submissions = 0

#num_pages+1
for i in range(num_pages+1):

    #status:
    # 15 = AC
    # 14 = WA
    res = requests.get('https://www.codechef.com/status/'+PROBLEM_NAME+'?page='+str(i)+'&sort_by=All&sorting_order=asc&language='+SUBMISSION_LANGUAGE_NUMBER+'&status=11&handle=&Submit=GO')
    
    #check if the download succeeded
    #while True:
    try:
        res.raise_for_status()
            #break
    except Exception as exc:
        print('There was a problem: {}'.format(exc))
        
    #turn the context (res.text) into a BeautifulSoup object
    site_content = bs4.BeautifulSoup(res.text, "html.parser")
    
    #want every submission ids are in td with width 60
    elems = site_content.select('td[width=60]')
 
    for j in range(len(elems)):
        submission_ids.append(elems[j].getText())

    total_submissions += len(submission_ids) 
    print("page {}/{}, total submissions found: {}".format(i,num_pages,total_submissions))

    csvfile = open('codechef/all_CTE_submission_ids_'+PROBLEM_NAME+'_'+SUBMISSION_LANGUAGE+'.csv', 'a', encoding='utf-8', newline='')
    csvwriter = csv.writer(csvfile)

    for id in submission_ids:
        csvwriter.writerow(id)

    submission_ids = []

print("GOT ALL SUBMISSION IDS")
