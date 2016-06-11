
var recognition = (function initializeRecognition() {
    var r = new webkitSpeechRecognition();
    r.lang = "en-GB";
    r.continuous = true;
    r.interimResults = false;
    return r;
})();

function startRecognition() {
    recognition.start();
}

function stopRecognition() {
    recognition.stop();
}


$(document).ready(function () {

    var message_container = $('#messages');
    var input = $('#input');

    var socket = new WebSocket('ws://' + window.location.host + '/ws');
    socket.onmessage = function(e) {
        responsiveVoice.speak(e.data, "UK English Female", {
            onstart: stopRecognition, onend: startRecognition});
    };
    recognition.onresult = function(e) {
        message = e.results[e.results.length -1];
        socket.send(message[0].transcript);
    };
    startRecognition();
});
