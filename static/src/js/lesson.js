/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {
    $('#save_lesson').on('click', function () {
        var _data = {
            'name': $('#id_name_lesson').val(),
            'place': $('#id_place_lesson').val(),
            'description': $('#id_description_lesson').val(),
            'timeout': $('#id_timeout_lesson').val()
        };
        $.ajax({
            type: "POST",
            url: '/',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            data: JSON.stringify(_data),
            async: false,
            success: function (_data) {
                console.log(_data);
            },
            error: function (_data) {
                console.log(_data);
            }
        });
    });
});
