/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {
    $('#save_room').on('click', function () {
        var _data = {
            'name': $('#id_name_room').val(),
            'type': $('#id_type_room').val(),
            'description': $('#id_description_room').val(),
            'size': $('#id_size_room').val()
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
