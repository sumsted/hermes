var request = require('request');

var clientApi = {
    host : 'http://0.0.0.0:8080',
    g : function(action, args){
        if(arguments.length < 2) {
            return {};
        } else {
            var options = {
                'url': this.host,
                'method': 'GET'
            };
            var callback = arguments[arguments.length - 1];
            for(var i = 0; i < arguments.length - 1; i++) {
                options['url'] += '/' + arguments[i];
            }
            request(options, function(err, res, body) {
                callback(err, res, body);
            });
        }
    },
    Hermes___init__: function(, cb){
        this.g('Hermes___init__', , cb);
    },
    Hermes_connect: function(, cb){
        this.g('Hermes_connect', , cb);
    },
    Hermes_disconnect: function(, cb){
        this.g('Hermes_disconnect', , cb);
    },
    Hermes_move: function(speed, turn, cb){
        this.g('Hermes_move', speed, turn, cb);
    },
    Hermes_change_posture: function(posture_type, cb){
        this.g('Hermes_change_posture', posture_type, cb);
    },
    Hermes_jump: function(jump_type, cb){
        this.g('Hermes_jump', jump_type, cb);
    },
    Hermes_jump_load: function(, cb){
        this.g('Hermes_jump_load', , cb);
    },
    Hermes_jump_cancel: function(, cb){
        this.g('Hermes_jump_cancel', , cb);
    },
    Hermes_jump_stop: function(, cb){
        this.g('Hermes_jump_stop', , cb);
    },
    Hermes_simple_animation: function(animation_type, cb){
        this.g('Hermes_simple_animation', animation_type, cb);
    },
    Hermes_stop: function(, cb){
        this.g('Hermes_stop', , cb);
    }
};
