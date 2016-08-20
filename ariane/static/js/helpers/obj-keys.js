var object_keys = function(obj) {
    var keys = [];
    for (var name in obj) {
        keys.push(name);
    }
    return keys;
};
