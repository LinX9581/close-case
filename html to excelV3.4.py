from bs4 import BeautifulSoup
import requests
import re
import time
import sys
import xlwt
import tkinter as tk
from dateutil import parser
import datetime

html=""
#######################getStr###################
f=open('html.txt','r',encoding='utf-8')

for line in f:
	html=html+line
f.close

sp = BeautifulSoup(html,'html.parser') 
datas=[]



######################title#########################
findTitleTd=sp.find_all("td",{"width":"41%" , "class":"text"})

count=0
for num in findTitleTd:
	print(num.text)
	datas.append(num.text)
	count+=1
print("firstTime########################")
#######################firstTime########################

#時間 td 標籤
findFirstTimeTd=sp.find_all("td",{"width":"15%" , "class":"text"})

#td標籤裡的標籤a
#<a href="JavaScript:openWin('pop_up_profile.asp?PF=303&FID=21','profile','toolbar=0,location=0,status=0,menubar=0,scrollbars=1,resizable=1,width=590,height=425')" title="這個主題最先發表於: 22/08/2018&nbsp;at&nbsp;15:31">linx9581</a>
arrFirstTimeTagA=[]		

#標籤a 的 title內容
arrFirstTime=[]

#搜尋時間  ex. 05/20/2018 at 12:40
arrRegexFirstTime=[]

for timeNum in findFirstTimeTd:
	arrFirstTimeTagA.append(timeNum.find("a"))

for timeCount in range(0,len(arrFirstTimeTagA)):	
	arrFirstTime.append(arrFirstTimeTagA[timeCount].get("title"))
	regexTime=re.search(r"(\d{1,2}/\d{1,2}/\d{4}\s[a-z][a-z]\s\d{1,2}:\d{1,2})",arrFirstTime[timeCount])
	arrRegexFirstTime.append(regexTime)
	print(parser.parse(arrRegexFirstTime[timeCount].group(0))) #時間正規化 ex.2018-05-20 12:40:00
	
print("lastTime##############")
#######################lastTime########################
	

arrLastTime=[]
arrRegexLastTime=[]
lastReplyTime=sp.find_all("td",{"class":"smText","align":"right"})

count=0  #lastTimeCount != int
#date2='2018/05/20 at 12:40' test
for lastTimeCount in lastReplyTime:
	arrLastTime.append(lastTimeCount.text)
	regexTime1=re.search(r"(\d{4}/\d{1,2}/\d{1,2}\s[a-z][a-z]\s\d{1,2}:\d{1,2})",arrLastTime[count])
	arrRegexLastTime.append(regexTime1)
	count+=1


for count in range(0,len(arrFirstTimeTagA)):
	print(parser.parse(arrRegexLastTime[count].group(0)))

######################lastTime-firstTime##########
finishDay=[]
finishHour=[]

for count in range(0,len(arrFirstTimeTagA)):

	#finishDay
	firstTime=parser.parse(arrRegexFirstTime[count].group(0))	#時間正規化
	lastTime=parser.parse(arrRegexLastTime[count].group(0))
	longDay=(lastTime-firstTime).days
	if longDay==0:
		longDay=1
	finishDay.append(longDay)
	#print(finishDay[count])
	
	#finishHour
	integer=int((lastTime-firstTime).seconds/3600)
	if integer==0:
		integer=1
	finishHour.append(integer)
	print(finishHour[count],finishDay[count])
	#print((parser.parse(arrRegexLastTime[count].group(0))-parser.parse(arrRegexFirstTime[count].group(0))).days)
	
	
#######################longDay###################
arrTitleA=[]
arrTitleHref=[]
arrlongDayNum=[]
longDaySite=[]
#findTitleTd=sp.find_all("td",{"width":"41%" , "class":"text"})
for aNum in findTitleTd:
	arrTitleA.append(aNum.find("a"))

for aCount in range(0,len(arrTitleA)):	
	arrTitleHref.append(arrTitleA[aCount].get("href"))
	if finishDay[aCount]>=5:
		arrlongDayNum.append(aCount)
		longDaySite.append("forum.shu.edu.tw/"+arrTitleHref[aCount])
		#print(longDaySite[1])
#if longDay>=5:

	# longDaySite.append("forum.shu.tw/"+arrTitleHref[longDayCount])
	

#######################excel#####################

filename = '123.xls'
book = xlwt.Workbook()
sheet_1 = book.add_sheet('hello')
sheet_1.col(0).width = 15000
sheet_1.col(4).width = 5000
sheet_1.col(5).width = 5000
sheet_1.col(6).width = 15000

sheet_1.write(0,0,"標題")
sheet_1.write(0,1,"天數")
sheet_1.write(0,2,"小時")
sheet_1.write(0,4,"發單時間")
sheet_1.write(0,5,"結單時間")
sheet_1.write(0,6,"網址")

for i in range(0,count+1):
	sheet_1.write(i+1,0,datas[i])
	sheet_1.write(i+1,1,finishDay[i])
	sheet_1.write(i+1,2,finishHour[i])
	sheet_1.write(i+1,4,arrRegexFirstTime[i].group(0))
	sheet_1.write(i+1,5,arrRegexLastTime[i].group(0))
	
count=0
for longDayCount in arrlongDayNum:
	sheet_1.write(longDayCount+1,6,longDaySite[count])
	print(longDaySite[count])
	count+=1
#sheet_1.write(5,1,'world')

book.save(filename)


######################tkinter####################

# a=parser.parse(arrRegexFirstTime[0].group(0))
# b=parser.parse(arrRegexLastTime[0].group(0))
# print(a,b)

# print((b-a).days)

# date1='2018/04/20 at 11:40'

# date2='2018/05/20 at 12:40'

# dt1 = parser.parse("%s" %(date1))
# dt2 = parser.parse("%s" %(date2))

# print((dt1-dt2).days)
'''
b.append(data3[0].text.split('/'))
print(b[0])
l=len(b)
print(l)
'''



