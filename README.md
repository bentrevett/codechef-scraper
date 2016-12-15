# codechef-scraper

Given the problem name and programming language, this script will scrape codechef.com for all of the accepted solutions to that problem and write them to a CSV file.

Codechef replaces all submission languages with a number, i.e. Python 3.4 = 116, which is needed to scrape the correct language.

Codechef doesn't like being scraped so this code is tempermental and codechef will time-out a lot of the time, causing it to fail.

##To-Do
- Specify problem at command line instead of hard coding
- Option to scrape unaccepted submissions 
- Allow for scraping of multiple problems at once for a single language
- Abiltiy to scrape one problem in multiple languages at the same time
