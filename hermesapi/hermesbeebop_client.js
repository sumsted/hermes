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
    HermesBeebop_take_off: function( cb){
        this.g('HermesBeebop_take_off', cb);
    },
    HermesBeebop_land: function( cb){
        this.g('HermesBeebop_land', cb);
    },
    HermesBeebop_emergency: function( cb){
        this.g('HermesBeebop_emergency', cb);
    },
    HermesBeebop_flat_trim: function( cb){
        this.g('HermesBeebop_flat_trim', cb);
    },
    HermesBeebop_navigate_home: function( cb){
        this.g('HermesBeebop_navigate_home', cb);
    },
    HermesBeebop_move_by: function(dx, dy, dz, dr, cb){
        this.g('HermesBeebop_move_by', dx, dy, dz, dr, cb);
    },
    HermesBeebop_max_altitude: function(m, cb){
        this.g('HermesBeebop_max_altitude', m, cb);
    },
    HermesBeebop_max_tilt: function(d, cb){
        this.g('HermesBeebop_max_tilt', d, cb);
    },
    HermesBeebop_max_distance: function(m, cb){
        this.g('HermesBeebop_max_distance', m, cb);
    },
    HermesBeebop_autonomous_flight_max_horizontal_speed: function(ms, cb){
        this.g('HermesBeebop_autonomous_flight_max_horizontal_speed', ms, cb);
    },
    HermesBeebop_autonomous_flight_max_vertical_speed: function(ms, cb){
        this.g('HermesBeebop_autonomous_flight_max_vertical_speed', ms, cb);
    },
    HermesBeebop_autonomous_flight_max_horizontal_acceleration: function(mss, cb){
        this.g('HermesBeebop_autonomous_flight_max_horizontal_acceleration', mss, cb);
    },
    HermesBeebop_autonomous_flight_max_vertical_acceleration: function(mss, cb){
        this.g('HermesBeebop_autonomous_flight_max_vertical_acceleration', mss, cb);
    },
    HermesBeebop_autonomous_flight_max_rotation_speed: function(ms, cb){
        this.g('HermesBeebop_autonomous_flight_max_rotation_speed', ms, cb);
    },
    HermesBeebop_max_vertical_speed: function(ms, cb){
        this.g('HermesBeebop_max_vertical_speed', ms, cb);
    },
    HermesBeebop_max_rotation_speed: function(ms, cb){
        this.g('HermesBeebop_max_rotation_speed', ms, cb);
    },
    HermesBeebop_set_home: function(lat, lon, alt, cb){
        this.g('HermesBeebop_set_home', lat, lon, alt, cb);
    },
    HermesBeebop_get_location: function( cb){
        this.g('HermesBeebop_get_location', cb);
    },
    HermesBeebop_get_state: function( cb){
        this.g('HermesBeebop_get_state', cb);
    }
};
