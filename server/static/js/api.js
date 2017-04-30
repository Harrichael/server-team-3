

function login(username, password, options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_username: function (data, textStatus, xhr) {},
        invalid_password: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    $.ajax({
        type: "POST",
        url: "/api/session",
        headers: {
            "Content-Type": "application/json"
        },
        data: JSON.stringify({
            username: username,
            password: password
        }),
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_username,
            409: callbacks.invalid_password
        }
    });
}

function logout(options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {}
    };

    callbacks = $.extend({}, defaults, options);

    $.ajax({
        type: "DELETE",
        url: "/api/session",
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete
    });
}

function get_online_users(options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {}
    };

    callbacks = $.extend({}, defaults, options);

    $.ajax({
        type: "GET",
        url: "/api/session/users",
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete
    });
}

function register_user(username, password, email, options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        username_taken: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    $.ajax({
        type: "POST",
        url: "/api/users",
        headers: {
            "Content-Type": "application/json"
        },
        data: JSON.stringify({
            username: username,
            password: password,
            email: email
        }),
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.username_taken
        }
    });
}

function change_password(session_key, password, options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        same_as_old: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/users/" + username + "/password";

    $.ajax({
        type: "PUT",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        data: JSON.stringify({
            session-key: session_key,
            password: password
        }),
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.same_as_old
        }
    });
}

function verify_email(email, email_code, username, options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_code: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/users/" + username + "/emails";

    $.ajax({
        type: "PUT",
        url: str_url,
        headers: {
            "Content-Type": "application/json"
        },
        data: JSON.stringify({
            email: email,
            email_coed: email_code
        }),
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_code
        }
    });
}

function get_user_config(username, options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/users/" + username + "/config";

    $.ajax({
        type: "GET",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete
    });
}


function update_user_config(username, data_options, options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    data = {
        username: username /*required argument */
    };

    data = $.extend({}, data_options, data);

    var str_url = "/api/users/" + username + "/config";

    $.ajax({
        type: "PUT",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        data: data,
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete
    });
}


function get_user_profile(user, options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_user: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/users/" + user + "/profile";

    $.ajax({
        type: "GET",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_user
        }
    });
}

function update_user_profile(username, data_option, options){
	defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    data = $.extend({}, data_options, data);

    var str_url = "/api/users/" + username + "/profile";

    $.ajax({
        type: "PUT",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        data: data,
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete
    });
}


function get_pm_history(username, user, options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_user: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/users/" + username + "/pm/" + user;

    $.ajax({
        type: "GET",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_user
        }
    });
}


function send_pm(message, username, user, options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_user: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/users/" + username + "/pm/" + user;

    $.ajax({
        type: "POST",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        data: JSON.stringify({
            message: message
        }),
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_user
        }
    });
}

// message ID ?????
function delete_pm(username, user, id, options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_user: function (data, textStatus, xhr) {}
    };

    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/users/" + username + "/pm/" + user + id;

    $.ajax({
        type: "DELETE",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete
        statusCode: {
            409: callbacks.invalid_user
        }
    });
}

function get_channel_list(options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        no_channels: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    $.ajax({
        type: "GET",
        url: "/api/channels",
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.no_channels
        }
    });
}

function create_channel(channel_name, options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        channel_name_taken: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    $.ajax({
        type: "POST",
        url: "/api/channels",
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        data: JSON.stringify({
            channel_name: channel_name
        }),
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.channel_name_taken
        }
    });
}

function delete_channel(channel, options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_channel: function (data, textStatus, xhr) {}
    };

    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/channels/" + channel;

    $.ajax({
        type: "DELETE",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete
        statusCode: {
            409: callbacks.invalid_channel
        }
    });
}

function get_channel_admins(channel, options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_channel: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/channels/" + channel + "/admins";

    $.ajax({
        type: "GET",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_channel
        }
    });
}

function adjust_admin_level (admins, chiefAdmin, channel, options){
	defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    data = $.extend({}, data_options, data);

    var str_url = "/api/users/" + username + "/admins";

    $.ajax({
        type: "PUT",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        data: data,
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete
    });
}

function get_channel_subscribers(channel){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_channel: function (data, textStatus, xhr) {},
        no_subscribers: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/channels/" + channel + "/subscriptions";

    $.ajax({
        type: "GET",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_channel
            409: callbacks.no_subscribers
        }
    });
}

function subscribe_to_channel (channel, options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_channel: function (data, textStatus, xhr) {},
        already_subscribed: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/channels/" + channel + "/subscriptions";

    $.ajax({
        type: "POST",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_channel,
            409: callbacks.already_subscribed
        }
    });
}

function unsubscribe_from_channel(channel, options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_channel: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/channels/" + channel + "/subscriptions";

    $.ajax({
        type: "DELETE",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_channel
        } 
    });
}

function get_blocked_users(channel, options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_channel: function (data, textStatus, xhr) {},
        no_blocked_users: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/channels/" + channel + "/black-list";

    $.ajax({
        type: "GET",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.no_blocked_users,
            409: callbacks.invalid_channel
        }
    });    
}

function block_user_channel(username, time, channel, options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_channel: function (data, textStatus, xhr) {},
        invalid_username: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/channels/" + channel + "/black-list";

    $.ajax({
        type: "POST",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        data: JSON.stringify({
            username: username,
            time: time
        }),
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_channel,
            409: callbacks.invalid_username
        }
    });
}

function get_channel_history(channel, options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_channel: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/channels/" + channel + "/chat";

    $.ajax({
        type: "GET",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_channel
        }
    });    
}

function send_message(message, channel, options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_channel: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/channels/" + channel + "/chat";

    $.ajax({
        type: "POST",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        data: JSON.stringify({
            message: message
        }),
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_channel
        }
    });
}

function delete_message(channel, id, options){
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        complete: function (data, textStatus, xhr) {},
        invalid_channel: function (data, textStatus, xhr) {},
        invalid_message_id: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    var str_url = "/api/channels/" + channel + "/chat" + id;

    $.ajax({
        type: "DELETE",
        url: str_url,
        headers: {
            "session-key": session_key,
            "Content-Type": "application/json"
        },
        success: callbacks.success,
        error: callbacks.error,
        complete: callbacks.complete,
        statusCode: {
            409: callbacks.invalid_channel,
            409: callbacks.invalid_message_id
        } 
    });
}





