$.fn.lbyl = function( options ) {
    var s = $.extend({
        content: '',
        speed: 10,
    }, options );

    var elem = $(this),
        letterArray = [],
        lbylContent = s.content,
        count = $(this).length;

    elem.empty();
    elem.attr('data-time', lbylContent.length * s.speed);

    for (var i = 0; i < lbylContent.length; i++) {
        letterArray.push(lbylContent[i]);
    }

    $.each(letterArray, function(index, value) {
        elem.append('<span style="display: none;">' + value + '</span>');
        setTimeout(function(){
            $(elem.find('span')[index]).show();
        }, index * s.speed);
    });
};


ko.bindingHandlers.lbylText = {
    init: function(element, valueAccessor, allBindings, viewModel, bindingContext) {
        // This will be called when the binding is first applied to an element
        // Set up any initial state, event handlers, etc. here
        value = valueAccessor();
        $(element).lbyl({
            content: value(),
        });

    },
    update: function(element, valueAccessor, allBindings, viewModel, bindingContext) {
        // This will be called once when the binding is first applied to an element,
        // and again whenever any observables/computeds that are accessed change
        // Update the DOM element based on the supplied values here.
        value = valueAccessor();
        $(element).lbyl({
            content: value(),
        });
    }
};
