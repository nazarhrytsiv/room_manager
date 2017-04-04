/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {
    $(".item").on('focus', function () {
        $(this).removeClass("invalid");
        $(this).next().addClass("invisible");
    });
    $('#save_group').on('click', function () {
        var _data = {
            'name': $('#id_name_group').val(),
            'description': $('#id_description_group').val()
        };
        $.ajax({
            type: "POST",
            url: '/group/create/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(_data),
            success: function (response) {
                console.log('created!');
            },
            error: function (data) {
                errors = JSON.parse(data.responseText);
                for (let err in errors) {
                    $("#id_" + err + "_group").addClass("invalid");
                    $("#id_warning_" + err).text(errors[err]).removeClass("invisible");
                }
            }
        });
    });
});


function update_group(id) {
    $(".item").on('focus', function () {
        $(this).removeClass("invalid");
        $(this).next().addClass("invisible");
    });
    var _data = {
        'id': id,
        'name': $('#id_name_group').val(),
        'description': $('#id_description_group').val()
    };

    $.ajax({
        type: "PUT",
        url: '/group/' + id + '/edit/',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(_data),
        success: function (response) {
            console.log('edited!');
        },
        error: function (data) {
            errors = JSON.parse(data.responseText);
            for (let err in errors) {
                $("#id_" + err + "_group").addClass("invalid");
                $("#id_warning_" + err).text(errors[err]).removeClass("invisible");
            }
        }
    });
}

function delete_group(id) {

    var _data = {
        'id': id
    };

    $.ajax({
        type: "DELETE",
        url: '/group/delete/',
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

function add_member_to_group(user_id, group_id) {

    var _data = {
        'id': user_id
    };

    $.ajax({
        type: "POST",
        url: '/group/' + group_id + '/add_member/',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(_data),
        success: function (respons) {
            console.log(respons);
        },
        error: function (err) {
            console.log(err);
        }
    });
}


