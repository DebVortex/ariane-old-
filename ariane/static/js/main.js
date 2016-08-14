var languages = {
    "en-GB": "UK English Female",
    "de-DE": "Deutsch Female"
};

function Ariane(lang) {
    self = this;
    self.listening = ko.observable(false);

    self.leftTemplate = ko.observable('empty');
    self.leftData = ko.observable();
    self.centerTopTemplate = ko.observable('empty');
    self.centerTopData = ko.observable();
    self.centerBottomTemplate = ko.observable('empty');
    self.centerBottomData = ko.observable();
    self.rightTemplate = ko.observable('empty');
    self.rightData = ko.observable();
    self.active = ko.observable(false);

    self.message = ko.observable('');

    self.start_recognition = function() {
        self.listening(true);
        self._rec.start();
    };

    self.stop_recognition = function() {
        self.listening(false);
        self._rec.stop();
    };

    self.say = function(text) {
        responsiveVoice.speak(
            text,
            self.voice,
            {
                onstart: self.stop_recognition,
                onend: self.start_recognition
            }
        );
        return true;
    };

    self.initialize = function() {self._initialize.knockout();};

    /* istanbul ignore next:
        * lack of coverage due to setTimeout
        * only UI specific sugar
        * speechRecognition & websocket will be faked in tests anyway.
    */
    self._initialize = {
        knockout: function() {
            ko.applyBindings(self);
            self.centerTopData({'text': 'Initializing user interface...'});
            self.centerTopTemplate('infoText');
            setTimeout(function() {
                $('.fourth_arc').removeClass('invis_arc');
                setTimeout(function() {
                    $('.fourth_arc').addClass('animated');
                    self._initialize.voice();
                }, initializationTimeout);
            }, initializationTimeout);
        },
        voice: function() {
            self.centerTopData({'text': 'Initializing language...'});
            setTimeout(function() {
                $('.third_arc').removeClass('invis_arc');
                self.voice = languages[lang];
                setTimeout(function() {
                    $('.third_arc').addClass('animated');
                    self._initialize.speechRecognition();
                }, initializationTimeout);
            }, initializationTimeout);
        },
        speechRecognition: function() {
            self.centerTopData({'text': 'Initializing speech recognition...'});
            setTimeout(function() {
                $('.second_arc').removeClass('invis_arc');
                self._rec = new webkitSpeechRecognition();
                self._rec.lang = lang;
                self._rec.continuous = true;
                self._rec.interimResults = false;
                setTimeout(function() {
                    $('.second_arc').addClass('animated');
                    self._initialize.websocket();
                }, initializationTimeout);
            }, initializationTimeout);
        },
        websocket: function() {
            self.centerTopData({'text': 'Establishing connection...'});
            setTimeout(function() {
                $('.first_arc').removeClass('invis_arc');
                setTimeout(function() {
                    $('.first_arc').addClass('animated');
                    self.active(true);
                    self.centerTopTemplate('empty');
                    self.centerTopData({});
                }, initializationTimeout);
            }, initializationTimeout);
        }
    };
}
