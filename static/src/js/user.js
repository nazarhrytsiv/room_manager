/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {
    $('#save_user').on('click', function () {
        var _data = {
            'username': $('#id_username_user').val(),
            'name': $('#id_name_user').val(),
            'email': $('#id_email_user').val(),
            'password': $('#id_password_user').val()

        };
        $.ajax({
            type: "POST",
            url: '/',
            dataType: 'json',
            data: JSON.stringify(_data),
            success: function (_data) {
                console.log(_data);
            },
            error: function (_data) {
                console.log(_data);
            }
        });
    });
});