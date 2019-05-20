const puppeteer = require('puppeteer');
var cheerio = require("cheerio")

let getListData = async function(Category) {
    const browser = await puppeteer.launch({
        headless: true, //開啟網頁是否背景執行
        slowMo: 100, //每個指令間隔時間
    });
    const page = await browser.newPage();
    //await page.screenshot({ path: 'example.png' });

    await page.goto('http://forum.shu.edu.tw/default.asp');
    var content, $

    content = await page.content();

    // console.log(content)

    var $ = cheerio.load(content);
    var test = $('.text').text()
    console.log(test)
};

getListData()