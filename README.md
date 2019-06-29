# DU Result Fetcher 

Bulk fetching marks statements for Delhi University Students and more. 🚀

## Motivation

**Individual Results**

At the time of announcement of exam results, ~~[DU exam result portal](http://duexam2.du.ac.in/RSLT_ND2017/Students/Home.aspx)~~ [New DU Result Portal](http://duresult.in/students/Combine_GradeCard.aspx) often crashes due to the load. As a consequence, it takes too much time for a student to get his result, the response tab just keeps crashing again and again, and re filling of the time is a time consuming process. So why not automate the process ? Let's fetch our results with freedom. :star:

**Bulk fetch**

Final year students are often concerned about where they stand in the university rank. 
Manually downloading the result of 800 students and then comparing them is not feasible.
This can again be automated with same logic. Bulk fetching marks statements and getting rankings with scripts. :fire:

**Update :** 

It's been almost 2 years i've been doing this. During this time, the du result portal has changed its structure twice. The recent release is up to date with the current portal.

The project turned out to be even more useful than i initially thought. The project has served several purposes.

- getting marks statements  
  + for a single student
  + for all students of a course of a college
  + for all students of a course of DU
  + for PG courses
- getting rankings
  + for a college
  + for PG courses merit list ( based on rankings of all DU results)
- keeping long term records
- tracking the history of changes in the portal structure
- teaching that no system is scrap proof. You just have to try harder.

## Features (v2.0)

- Bypasses captcha to get results
- sorts them and puts them in txt, csv formats
- downloads entire html result pages (kept on local system only for privacy reasons)
- The new release is based on rollnumbers, so it'll work for any course.

## Dev

- clone the repo
- Make sure you have python, pip and [pipenv](https://docs.pipenv.org/) installed.
- start a virtual env with `pipenv shell`
- install dependencies `pipenv install`

## How does this work? Did you hack anything?

No. I just used what was publically available, and came out with a logic based on simple observations. I do not have any inside access. It's straight through the web portal.

## Disclaimer

- This is only for educational purposes.
- If you use it with malicious intent, you and only you are responsible for the consequences.