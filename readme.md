<pre>
爬取網頁元素到 excel
下面介紹套件和使用方法

<h2> python -m pip install --upgrade pip 
更新 pip modules

<h2> pip install beautifulsoup4
解析網頁原始碼

<h2> pip install requests
解析網址

<h2> pip install xlwt

filename = 'filemane.xls'
book = xlwt.Workbook()
sheet_1 = book.add_sheet('hello')   //工作表名稱
sheet_1.col(0).width = 15000        //欄位寬度 

sheet_1.write(0,0,"標題")           //欄位存放的值

book.save(filename)                 //輸出excel  

python轉輸出到excel


<h2> regex
從字串中 正規化時間
ex.
title="這個主題最先發表於: 2019/03/20&nbsp;at&nbsp;09:18"
regexTime=re.search(r"(\d{4}/\d{1,2}/\d{1,2}\s[a-z][a-z]\s\d{1,2}:\d{1,2})",title)
regexTime= "2018/05/20 at 12:40:00"

<h2> pip install python-dateutil
可以使用parse方法

parser.parse(regexTime)
把時間表準格式化 方便之後時間相減
2019/03/06 at 16:16 -> 2019-03-06 16:16:00

 </pre>
