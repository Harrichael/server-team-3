
function register(username, password, email, options) {
    defaults = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        username_taken: function (data, textStatus, xhr) {}
    };
    
    callbacks = $.extend({}, defaults, options);

    $.ajax({
        type: "POST",
        url: "/api/users",
        contentType: "application/json",
        data: JSON.stringify({
            username: username,
            password: password,
            email: email
        }),
        success: callbacks.success,
        error: callbacks.error,
        statusCode: {
            409: callbacks.username_taken
        }
    });
}
