function testObj() {
    this.called = false;
    this.call = function() {
        this.called = true;
    };
}
