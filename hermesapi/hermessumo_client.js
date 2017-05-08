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


    HermesSumo_move: function(speed, turn, cb){
        this.g('HermesSumo_move', speed, turn, cb);
    },
    HermesSumo_change_posture: function(posture_type, cb){
        this.g('HermesSumo_change_posture', posture_type, cb);
    },
    HermesSumo_jump: function(jump_type, cb){
        this.g('HermesSumo_jump', jump_type, cb);
    },
    HermesSumo_jump_load: function(cb){
        this.g('HermesSumo_jump_load', cb);
    },
    HermesSumo_jump_cancel: function(cb){
        this.g('HermesSumo_jump_cancel', cb);
    },
    HermesSumo_jump_stop: function(cb){
        this.g('HermesSumo_jump_stop', cb);
    },
    HermesSumo_simple_animation: function(animation_type, cb){
        this.g('HermesSumo_simple_animation', animation_type, cb);
    },
    HermesSumo_stop: function(cb){
        this.g('HermesSumo_stop', cb);
    }
};
