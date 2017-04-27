   
function register(username, password, email, callbacks) {
    if (callbacks.hasOwnProperty("success"))
    {
        success_callback = callbacks.success;
    } else {
        success_callback = function (data, textStatus, xhr) {};
    }

    if (callbacks.hasOwnProperty("error"))
    {
        error_callback = callbacks.error;
    } else {
        error_callback = function (data, textStatus, xhr) {};
    }

    if (callbacks.hasOwnProperty("username_taken"))
    {
        username_taken_callback = callbacks.username_taken;
    } else {
        username_taken_callback = function (data, textStatus, xhr) {};
    }

    $.ajax({
        type: "POST",
        url: "/api/users",
        contentType: "application/json",
        data: JSON.stringify({
            username: username,
            password: password,
            email: email
        }),
        success: success_callback,
        error: error_callback,
        statusCode: {
            409: username_taken_callback
        }
    });
}
