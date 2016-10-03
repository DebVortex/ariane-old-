responsiveVoice = {
    speak: function () {}
};

function webkitSpeechRecognition() {
    this.start = function () {};
    this.stop = function () {};
}

function ReconnectingWebSocket(location) {
    this.location = location;
}

function testObj() {
    this.called = false;
    this.call = function() {
        this.called = true;
    };
}
