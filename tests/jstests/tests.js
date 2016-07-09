QUnit.test("Test start/stop speech recognition", function( assert ) {
    ariane = new Ariane("en-GB");
    assert.notOk(ariane.listening);
    ariane.start_recognition();
    assert.ok(ariane.listening);
    ariane.stop_recognition();
    assert.notOk(ariane.listening);
});

QUnit.test("Test say of Ariane (using responsive voice internally)", function( assert ) {
    assert.expect(0);
    ariane = new Ariane("en-GB");
    ariane.say("Hi there!");
});
