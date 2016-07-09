var languages = {
    "en-GB": "UK English Female",
    "de-DE": "Deutsch Female"
};

function Ariane(lang) {
    //this._rec = new webkitSpeechRecognition();
    this._rec = {
        start: function() {},
        stop: function() {}
    };
    this._rec.lang = lang;
    this.voice = languages[lang];
    this._rec.continuous = true;
    this._rec.interimResults = false;
    this.listening = false;

    this.start_recognition = function() {
        this.listening = true;
        this._rec.start();
    };

    this.stop_recognition = function() {
        this.listening = false;
        this._rec.stop();
    };

    this.say = function(text) {
        responsiveVoice.speak(
            text,
            this.voice,
            {
                onstart: this.stop_recognition,
                onend: this.start_recognition
            }
        );
        return true;
    };
}

//$(document).ready(function () {
//
//    var message_container = $('#messages');
//    var input = $('#input');
//
//    var socket = new WebSocket('ws://' + window.location.host + '/ws');
//    socket.onmessage = function(e) {
//
//    recognition.onresult = function(e) {
//        message = e.results[e.results.length -1];
//        socket.send(message[0].transcript);
//    };
//    startRecognition();
//});
