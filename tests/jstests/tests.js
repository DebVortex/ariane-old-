QUnit.test("Test start/stop speech recognition", function( assert ) {
    ariane = new Ariane("en-GB");
    assert.notOk(ariane.listening);
    ariane.start_recognition();
    assert.ok(ariane.listening);
    ariane.stop_recognition();
    assert.notOk(ariane.listening);
});
