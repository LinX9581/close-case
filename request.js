var request = require("request");

var options = {
    method: 'GET',
    url: 'http://forum.shu.edu.tw/forum_posts.asp',
}
request(options, function(error, response, body) {
    if (error) throw new Error(error);

    console.log(body);
});