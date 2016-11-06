responsiveVoice = {
    speak: function () {}
};

function webkitSpeechRecognition() {
    this.start = function () {};
    this.stop = function () {};
}

function ReconnectingWebSocket(location) {
    this.location = location;
    this.called = false;
    this.called_with = '';
    this.send = function (msg) {
        this.called = true;
        this.called_with = JSON.parse(msg);
    };
}

function testObj() {
    this.called = false;
    this.call = function() {
        this.called = true;
    };
}
