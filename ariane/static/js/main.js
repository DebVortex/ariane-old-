var languages = {
    "en-GB": "UK English Female",
    "de-DE": "Deutsch Female"
};

function Ariane(lang) {
    self = this;

    self.inactive = ko.observable(false);
    self.connected = ko.observable(false);
    self.listening = ko.observable(false);
    self.speaking = ko.observable(false);

    self.leftTemplate = ko.observable('empty');
    self.leftData = ko.observable();

    self.centerTemplate = ko.observable('empty');
    self.centerData = ko.observable();

    self.rightTemplate = ko.observable('empty');
    self.rightData = ko.observable();

    self.message = ko.observable('');

    self.first_connection = true;

    self.start_recognition = function() {
        /* Set listening to true and start speech recognition */
        self.listening(true);
        self._rec.start();
    };

    self.stop_recognition = function() {
        /* Set listening to false and stop speech recognition */
        self.listening(false);
        self._rec.stop();
    };

    self.start_speaking = function() {
        /* Set speaking boolean to true and then invoke stop_recognition */
        self.speaking(true);
        self.stop_recognition();
    };

    self.stop_speaking = function() {
        /* Set speaking boolean to false and then invoke start_recognition */
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

    self.dispatch_message = function(resp) {
        /* Parse provided data and invoke specified messages.
         *
         * Called as onmessage handler from the websocket. The JSON stored in the data attibute
         * of the resp keys and values. The keys represent the function names and the value the
         * data passed into the functions.
         *
         * The function names are provided as dotted strings. For example, the function name
         * "ariane.say" will invoke the function window.ariane.say
         */
        data = JSON.parse(resp.data);
        object_keys(data).forEach(function (key) {
            if (key !== 'info') {
                func = window;
                key.split('.').forEach(function (sub_key) {
                    func = func[sub_key];
                });
                func(data[key]);
            }
        });
    };

    self.handle_transcription = function(msg) {
        /* Handle transcripted message.
         *
         * If ariane is active and the message is 'sleep', set her to inactive.
         * If ariane is inactive and the message is 'wakeup', set her to active.
         * If the message is neither of the above cases, the message gets send
         * to the server via the websocket connection. The userLangue is is also
         * provided.
         */
        if ((msg == 'sleep') && !self.inactive()) {
            self.inactive(true);
        } else if ((msg == 'wakeup') && self.inactive()) {
            self.inactive(false);
        } else if (!self.inactive()) {
            self.socket.send(JSON.stringify({
                'message': msg,
                'lang': userLanguage
            }));
        }
    };

    self.initialize = function() {
        /* Start the initialization process.
         *
         * The intialization process follows the this order:
         * knockout -> voice -> speechRecognition -> websocket
         */
        self._initialize.knockout();
    };

    /* istanbul ignore next:
        * lack of coverage due to setTimeout
        * only UI specific sugar
        * speechRecognition & websocket will be faked in tests anyway.
    */
    self._initialize = {
        knockout: function() {
            /* Initialize knockout by applying the bindings.
             *
             * After a configureable delay, the inner most arc is displayed and after an
             * additional delay, the same arc start its animation. After that it starts the voice
             * initialization.
             */
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
            /* Initialize voice by setting the language.
             *
             * After a configureable delay, the second arc from the middle is displayed and after
             * an additional delay, the same most arc start its animation. It then starts the
             * speech recognition initialization.
             */
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
            /* Initialize speechRecognition instantiating and configuring the
             * webkitSpeechRecognition object.
             *
             * After a configureable delay, the second most outer arc is displayed and after an
             * additional delay, the same arc start its animation. It then starts the websocket
             * initialization process.
             */
            self.message('Initializing speech recognition...');
            setTimeout(function() {
                $('.second_arc').removeClass('invis_arc');
                self._rec = new webkitSpeechRecognition();
                self._rec.lang = lang;
                self._rec.continuous = true;
                self._rec.interimResults = false;
                self._rec.onresult = function(e) {
                    /* onresult handler for successful transcription. */
                    message = e.results[e.results.length -1];
                    transcript = message[0].transcript;
                    self.handle_transcription(transcript);
                };

                setTimeout(function() {
                    $('.second_arc').addClass('animated');
                    self._initialize.websocket();
                }, initializationTimeout);
            }, initializationTimeout);
        },
        websocket: function() {
            /* Initialize connection by initializing the websocket.
             *
             * After a configureable delay, the outer arc from the middle is displayed and after
             * an additional delay, the same arc start its animation. It then sets the connected
             * attribute to true.
             */
            self.message('Establishing connection...');
            setTimeout(function() {
                $('.first_arc').removeClass('invis_arc');
                setTimeout(function() {
                    $('.first_arc').addClass('animated');
                    self.socket = new ReconnectingWebSocket('ws://' + window.location.host + '/ws');
                    self.socket.onopen = function() {
                        /* onopen handler for websocket.
                         *
                         * Sets the connected state to true and shows a message. If it's the first
                         * time the connection gets established, another message is shown.
                         */
                        self.connected(true);
                        if (self.first_connection) {
                            self.message('Connection established. Ariane is now active.');
                            self.first_connection = false;
                        } else {
                            self.message('Successfully reconnected.');
                        }
                    };
                    self.socket.onclose = function() {
                        /* onclose handler for websocket.
                         *
                         * Sets the connected state to false and shows a message.
                         */
                        self.connected(false);
                        self.message('Connection lost. Trying to reconnect...');
                    };
                    self.socket.onmessage = self.dispatch_message;
                    self.start_recognition();
                }, initializationTimeout);
            }, initializationTimeout);
        }
    };
}
