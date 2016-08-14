var languages = {
    "en-GB": "UK English Female",
    "de-DE": "Deutsch Female"
};

function Ariane(lang) {
    self = this;

    self.active = ko.observable(false);
    self.listening = ko.observable(false);
    self.speaking = ko.observable(false);

    self.leftTemplate = ko.observable('empty');
    self.leftData = ko.observable();

    self.centerTemplate = ko.observable('empty');
    self.centerData = ko.observable();

    self.rightTemplate = ko.observable('empty');
    self.rightData = ko.observable();

    self.message = ko.observable('');

    self.start_recognition = function() {
        self.listening(true);
        self._rec.start();
    };

    self.stop_recognition = function() {
        self.listening(false);
        self._rec.stop();
    };

    self.start_speaking = function() {
        self.speaking(true);
        self.stop_recognition();
    };

    self.stop_speaking = function() {
        self.speaking(false);
        self.start_recognition();
    };

    self.say = function(text) {
        responsiveVoice.speak(
            text,
            self.voice,
            {
                onstart: self.start_speaking,
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
            self.message('Initializing user interface...');
            setTimeout(function() {
                $('.fourth_arc').removeClass('invis_arc');
                setTimeout(function() {
                    $('.fourth_arc').addClass('animated');
                    self._initialize.voice();
                }, initializationTimeout);
            }, initializationTimeout);
        },
        voice: function() {
            self.message('Initializing language...');
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
            self.message('Initializing speech recognition...');
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
            self.message('Establishing connection...');
            setTimeout(function() {
                $('.first_arc').removeClass('invis_arc');
                setTimeout(function() {
                    $('.first_arc').addClass('animated');
                    self.active(true);
                    self.message('Connection established. Ariane is now active.');
                }, initializationTimeout);
            }, initializationTimeout);
        }
    };
}
