# Fetcher 

Automated fetching and analysis of exam results for Delhi University. 

## Motivation

**Individual Results**
At the time of announcement of exam results, [DU exam result portal](http://duexam2.du.ac.in/RSLT_ND2017/Students/Home.aspx) often crashes due to the load. As a consequence, it takes too much time for a student to get his own result, the response just keeps crashing again and again, and re filling of the time is a time consuming process. So why not automate the process ? Let's fetch our results with freedom. :star:

**Bulk fetch**
Final year students are often concerned about where they stand in the university rank. 
Manually downloading the result of 1000 students and then comparing them is not feasible.
This can again be automated with same logic. Bulk fetch marks statements with freedom and get comparisons and rankings with scripts. :fire:

## Todo

- [X] proof of concept
- [X] fetch specific college : computer science 
- [X] fetch all DU colleges  : computer science
- [X] Results saved
	- [X] To html
	- [X] consolidated text file
	- [X] array for any other processing	
- [X] Retry failed responses ( as site crashes often ) 
- [ ] any course : fetch students and marks  
- [ ] Deployment, if any, with menu selection : course, college, individual

## Dev

- Make sure you have [pipenv](https://docs.pipenv.org/) installed.

```shell
git clone https://github.com/jatin69/fetcher.git
cd fetcher
pipenv shell
pipenv install
```

## Note 

- The script currently has a lot of moving parts and variables.
- A generic script with variable configurations would be more clean.
- Contributions are welcome.