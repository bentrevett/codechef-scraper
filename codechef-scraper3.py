import requests, bs4, csv, time

#dicts to hold submission ids
submission_ids = []

PROBLEM_NAME = 'HOLES'
SUBMISSION_LANGUAGE = 'C'
SUBMISSION_LANGUAGE_NUMBER = '11'

i = 0
skip = False
skipped = 0

with open('codechef/all_TLE_submission_ids_'+PROBLEM_NAME+'_'+SUBMISSION_LANGUAGE+'.csv', 'r', encoding='utf-8', newline='') as read:
    reader = csv.reader(read)

    with open('codechef/all_TLE_submissions_'+PROBLEM_NAME+'_'+SUBMISSION_LANGUAGE+'.csv', 'w', encoding='utf-8', newline='') as write:
        writer = csv.writer(write)

        for row in reader:
            submission_id = ''.join(row)

            res = requests.get('https://www.codechef.com/viewplaintext/{}'.format(submission_id))

            skip = False
            try:
                res.raise_for_status()
            except Exception as exc:
                print('There was a problem: {}'.format(exc))
                skip = True
                skipped += 1
            
            if skip == False:
                #turn the context (res.text) into a BeautifulSoup object
                site_content = bs4.BeautifulSoup(res.text, "html.parser")
            
                #code is simply within a <pre> tag
                elems = site_content.select('pre')
    
                print("writing TLE submission no:{}, submission_id = {}, skipped = {}".format(i,submission_id,skipped))
                i+=1
            
                #write to csv file with start and end markers
                writer.writerow(["<START> "+elems[0].getText()+" <END>"])

print("DONE")
