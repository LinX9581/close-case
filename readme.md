爬取網頁元素到 excel
下面介紹套件和使用方法

##1.python -m pip install --upgrade pip <br>
更新 pip modules<br>

##2.pip install beautifulsoup4<br>
解析網頁原始碼<br>

##3.pip install requests<br>
解析網址<br>


##4.pip install xlwt<br>

filename = 'filemane.xls'<br>
book = xlwt.Workbook()<br>
sheet_1 = book.add_sheet('hello')   //工作表名稱<br>
sheet_1.col(0).width = 15000        //欄位寬度 <br>
<br>
sheet_1.write(0,0,"標題")           //欄位存放的值<br>
<br>
book.save(filename)                 //輸出excel  <br>
<br>
python轉輸出到excel<br>


##5.regex
從字串中 正規化時間<br>
ex.<br>
title="這個主題最先發表於: 2019/03/20&nbsp;at&nbsp;09:18"<br>
regexTime=re.search(r"(\d{4}/\d{1,2}/\d{1,2}\s[a-z][a-z]\s\d{1,2}:\d{1,2})",title)<br>
regexTime= "2018/05/20 at 12:40:00"<br>
<br>
##6.pip install python-dateutil<br>
可以使用parse方法<br>
<br>
parser.parse(regexTime)<br>
把時間表準格式化 方便之後時間相減<br>
2019/03/06 at 16:16 -> 2019-03-06 16:16:00<br>

 
