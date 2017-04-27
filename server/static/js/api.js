
function register(username, password, email, callbacks) {
    default_callbacks = {
        success: function (data, textStatus, xhr) {},
        error: function (data, textStatus, xhr) {},
        username_taken: function (data, textStatus, xhr) {}
    };

    $.ajax({
        type: "POST",
        url: "/api/users",
        contentType: "application/json",
        data: JSON.stringify({
            username: username,
            password: password,
            email: email
        }),
        success: (callbacks.hasOwnProperty("success")) ? callbacks.success : default_callbacks.success,
        error: (callbacks.hasOwnProperty("error")) ? callbacks.error : default_callbacks.error,
        statusCode: {
            409: (callbacks.hasOwnProperty("username_taken")) ? callbacks.username_taken : default_callbacks.username_taken
        }
    });
}
