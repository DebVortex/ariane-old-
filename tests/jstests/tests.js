QUnit.module("unrelated test", {
    before: function() {
        this.ariane =  new Ariane(userLanguage);
        ko.cleanNode(this.ariane);
        this.ariane.initialize();
        this.ariane._rec = new webkitSpeechRecognition();
        this.ariane.socket = new ReconnectingWebSocket('');
    }
});

QUnit.test("Test start/stop speech recognition", function( assert ) {
    assert.notOk(this.ariane.listening());
    this.ariane.start_recognition();
    assert.ok(this.ariane.listening());
    this.ariane.stop_recognition();
    assert.notOk(this.ariane.listening());
});

QUnit.test("Test start/stop speaking & speech recognition", function( assert ) {
    assert.notOk(this.ariane.listening());
    assert.notOk(this.ariane.speaking());

    this.ariane.start_recognition();
    assert.ok(this.ariane.listening());
    assert.notOk(this.ariane.speaking());

    this.ariane.start_speaking();
    assert.notOk(this.ariane.listening());
    assert.ok(this.ariane.speaking());

    this.ariane.stop_speaking();
    assert.notOk(this.ariane.speaking());
    assert.ok(this.ariane.listening());

    this.ariane.stop_recognition();
    assert.notOk(this.ariane.listening());
    assert.notOk(this.ariane.speaking());
});

QUnit.test("Test dispatch_message", function ( assert ) {
    window.testObj = new testObj();
    assert.notOk(testObj.called);
    test_data = {'data': '{"testObj.call": "foo", "info": "bar"}'};
    this.ariane.dispatch_message(test_data);
    assert.notOk(testObj.called);
});

QUnit.test("Test say of Ariane (using responsive voice internally)", function( assert ) {
    assert.expect(0);
    this.ariane.say("Hi there!");
});

QUnit.test("Test the handle_transcription function of ariane.", function( assert ) {
    assert.notOk(this.ariane.inactive());
    this.ariane.handle_transcription('sleep');
    assert.ok(this.ariane.inactive());
    this.ariane.handle_transcription('wakeup');
    assert.notOk(this.ariane.inactive());
    assert.notOk(this.ariane.socket.called);
    msg = 'Who was Nelson Mandela?';
    this.ariane.handle_transcription(msg);
    assert.ok(this.ariane.socket.called);
    assert.ok(this.ariane.socket.called_with.message === msg);
    assert.ok(this.ariane.socket.called_with.lang === userLanguage);
});
