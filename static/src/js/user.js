/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {
    $(".item").on('focus', function () {
        $(this).removeClass("invalid");
        $(this).next().addClass("invisible");
    });
    $('#save_user').on('click', function () {
        var _data = {
            'username': $('#id_username_user').val(),
            'name': $('#id_name_user').val(),
            'email': $('#id_email_user').val(),
            'password': $('#id_password_user').val()

        };
        $.ajax({
            type: "POST",
            url: '/user/create/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(_data),
            success: function (_data) {
                console.log('created!');
            },
            error: function (data) {
                errors = JSON.parse(data.responseText);
                for (let err in errors) {
                    $("#id_" + err + "_user").addClass("invalid");
                    $("#id_warning_" + err).text(errors[err]).removeClass("invisible");
                }
            }
        });
    });
});


function update_user(id) {
    $(".item").on('focus', function () {
        $(this).removeClass("invalid");
        $(this).next().addClass("invisible");
    });
    var _data = {
        'id': id,
        'username': $('#id_username_user').val(),
        'name': $('#id_name_user').val(),
        'email': $('#id_email_user').val(),
        'password': $('#id_password_user').val()
    };

    $.ajax({
        type: "PUT",
        url: '/user/' + id + '/edit/',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(_data),
        success: function (respons) {
            console.log(respons);
        },
        error: function (data) {
            errors = JSON.parse(data.responseText);
            for (let err in errors) {
                $("#id_" + err + "_user").addClass("invalid");
                $("#id_warning_" + err).text(errors[err]).removeClass("invisible");
            }
        }
    });
}


function delete_user(id) {

    var _data = {
        'id': id
    };

    $.ajax({
        type: "DELETE",
        url: '/user/delete/',
        data: JSON.stringify(_data),
        success: function (response) {
            $("#hide_" + id).remove();
            console.log(response);
        },
        error: function (err) {
            console.log(err);
        }
    });
}