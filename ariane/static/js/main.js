$(document).ready(function () {
    var message_container = $('#messages');
    var input = $('#input');

    var socket = new WebSocket('ws://' + window.location.host + '/ws');
    socket.onmessage = function(e) {
        message_container.append('<p>' + e.data + '</p>');
    };
    $('#websocket-test').on('submit', function(e) {
        e.preventDefault();
        socket.send(input.val());
        input.val('');
    });
});
