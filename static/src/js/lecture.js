/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {
    $(".item").on('focus', function () {
        $(this).removeClass("invalid");
        $(this).next().addClass("invisible");
    });
    $('#save_lecture').on('click', function () {
        var _data = {
            'lesson': $('#id_lesson_lecture').val(),
            'group': $('#id_group_lecture').val(),
            'room': $('#id_room_lecture').val(),
            'teacher': $('#id_teacher_lecture').val(),
            'number_by_schedule': $('#id_number_by_schedule_lecture').val(),
            'date_time': $('#id_date_time_lecture').val(),
        };
        $.ajax({
            type: "POST",
            url: '/lecture/create/',
            data: JSON.stringify(_data),
            contentType: 'application/json; charset=utf-8',
            success: function (_data) {
                console.log(_data);
            },
            error: function (data) {
                errors = JSON.parse(data.responseText);
                for (let err in errors) {
                    $("#id_" + err + "_lecture").addClass("invalid");
                    $("#id_warning_" + err).text(errors[err]).removeClass("invisible");
                }
            }
        });
    });
});


function update_lecture(id) {
    $(".item").on('focus', function () {
        $(this).removeClass("invalid");
        $(this).next().addClass("invisible");
    });
    var _data = {
        'id': id,
        'lesson': $('#id_lesson_lecture').val(),
        'group': $('#id_group_lecture').val(),
        'room': $('#id_room_lecture').val(),
        'teacher': $('#id_teacher_lecture').val(),
        'number_by_schedule': $('#id_number_by_schedule_lecture').val(),
        'date_time': $('#id_date_time_lecture').val()
    };

    $.ajax({
        type: "PUT",
        url: '/lecture/' + id + '/edit/',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(_data),
        success: function (response) {
            console.log(response);
        },
        error: function (data) {
            errors = JSON.parse(data.responseText);
            for (let err in errors) {
                $("#id_" + err + "_lecture").addClass("invalid");
                $("#id_warning_" + err).text(errors[err]).removeClass("invisible");
            }
        }
    });
}

function delete_lecture(id) {

    var _data = {
        'id': id
    };

    $.ajax({
        type: "DELETE",
        url: '/lecture/delete/',
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



