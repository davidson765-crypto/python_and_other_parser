const rp = require('request-promise');
//const cheerio = require('cheerio');
const url = 'https://www.google.com';


rp(url)
	.then(function(html){
		console.log(html)
		//console.log(cheerio('a',html));
	})
	.catch(function(err) {
		console.log(err)
	})