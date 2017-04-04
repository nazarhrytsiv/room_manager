/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {
    $(".item").on('focus', function () {
        $(this).removeClass("invalid");
        $(this).next().addClass("invisible");
    });
    $('#save_room').on('click', function () {
        var _data = {
            'name': $('#id_name_room').val(),
            'type': $('#id_type_room').val(),
            'description': $('#id_description_room').val(),
            'size': $('#id_size_room').val()
        };
        $.ajax({
            type: "POST",
            url: '/room/create/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(_data),
            async: false,
            success: function (_data) {
                console.log('created!');
            },
            error: function (data) {
                errors = JSON.parse(data.responseText);
                for (let err in errors) {
                    $("#id_" + err + "_room").addClass("invalid");
                    $("#id_warning_" + err).text(errors[err]).removeClass("invisible");
                }
            }
        });
    });
});


function update_room(id) {
    $(".item").on('focus', function () {
        $(this).removeClass("invalid");
        $(this).next().addClass("invisible");
    });
    var _data = {
        'id': id,
        'name': $('#id_name_room').val(),
        'type': $('#id_type_room').val(),
        'description': $('#id_description_room').val(),
        'size': $('#id_size_room').val()
    };

    $.ajax({
        type: "PUT",
        url: '/room/' + id + '/edit/',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(_data),
        success: function (response) {
            console.log('edited');
        },
        error: function (data) {
            errors = JSON.parse(data.responseText);
            for (let err in errors) {
                $("#id_" + err + "_room").addClass("invalid");
                $("#id_warning_" + err).text(errors[err]).removeClass("invisible");
            }
        }
    });
}

function delete_room(id) {

    var _data = {
        'id': id
    };

    $.ajax({
        type: "DELETE",
        url: '/room/delete/',
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

