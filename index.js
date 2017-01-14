var exec = require('child_process').exec;
var login = require("facebook-chat-api");

// Create simple echo bot
login({email: USERNAME, password: PASSWORD}, function callback (err, api) {
    if(err) return console.error(err);

    api.listen(function callback(err, message) {
    	exec('python index.py '+message.threadID, function() {
    		console.log('Executing Python');
    	})
    });
});