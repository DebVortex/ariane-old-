QUnit.module("unrelated test", {
    before: function() {
        this.ariane =  new Ariane(userLanguage);
        ko.cleanNode(this.ariane);
        this.ariane.initialize();
        this.ariane._rec = new webkitSpeechRecognition();
    }
});

QUnit.test("Test start/stop speech recognition", function( assert ) {
    assert.notOk(this.ariane.listening());
    this.ariane.start_recognition();
    assert.ok(this.ariane.listening());
    this.ariane.stop_recognition();
    assert.notOk(this.ariane.listening());
});

QUnit.test("Test say of Ariane (using responsive voice internally)", function( assert ) {
    assert.expect(0);
    this.ariane.say("Hi there!");
});
