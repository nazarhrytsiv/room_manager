/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {
    $(".item").on('focus', function () {
        $(this).removeClass("invalid");
        $(this).next().addClass("invisible");
    });

    errors_input = new Object();


    $(".item").on('input', function () {
        if ($(this).hasClass("string")) {
            if (!validate_input_string(this)) {
                errors_input[this["id"]] = false;
            }
            else
            {
                delete errors_input[this["id"]];
            }
        }
        else if ($(this).hasClass("integer")) {
            if (!validate_input_integer(this)) {
                errors_input[this["id"]] = false;
            }
            else
            {
                delete errors_input[this["id"]];
            }
        }
    });

    if (jQuery.isEmptyObject(errors_input)) {

        $('#save_lesson').on('click', function () {
            var _data = {
                'name': $('#id_name_lesson').val(),
                'place': $('#id_place_lesson').val(),
                'description': $('#id_description_lesson').val(),
            };
            $.ajax({
                type: "POST",
                url: '/lesson/create/',
                contentType: 'application/json; charset=utf-8',
                data: JSON.stringify(_data),
                success: function (_data) {
                    console.log(_data);
                },
                error: function (data) {
                    errors = JSON.parse(data.responseText);
                    for (let err in errors) {
                        $("#id_" + err + "_lesson").addClass("invalid");
                        $("#id_warning_" + err).text(errors[err]).removeClass("invisible");
                    }
                }
            });
        });
    }
});

function update_lesson(id) {
    $(".item").on('focus', function () {
        $(this).removeClass("invalid");
        $(this).next().addClass("invisible");
    });
    var _data = {
        'id': id,
        'name': $('#id_name_lesson').val(),
        'description': $('#id_description_lesson').val(),
        'place': $('#id_place_lesson').val(),
    };

    $.ajax({
        type: "PUT",
        url: '/lesson/' + id + '/edit/',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(_data),
        success: function (response) {
            console.log('edited!');
        },
        error: function (data) {
            errors = JSON.parse(data.responseText);
            for (let err in errors) {
                $("#id_" + err + "_lesson").addClass("invalid");
                $("#id_warning_" + err).text(errors[err]).removeClass("invisible");
            }
        }
    });
}

function delete_lesson(id) {

    var _data = {
        'id': id
    };

    $.ajax({
        type: "DELETE",
        url: '/lesson/delete/',
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
