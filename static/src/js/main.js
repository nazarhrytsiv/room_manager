function delete_object(id) {

    var _data = {
        'id': id

    };
    $.ajax({
        type: "DELETE",
        url: "delete/",
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
// Create a group and edit
$(document).ready(function () {
    $('#save_group').on('click', function () {
        var _data = {
            'name': $('#id_name_group').val(),
            'description': $('#id_description_group').val()
        };
        $.ajax({
            type: "POST",
            url: '/',
            contentType: 'application/json; charset=utf-8',
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


// Create a room and edit
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


// Create a lesson and edit
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


// Create a user and edit
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
//
//
// $(document).ready(function (id) {
//     $('#update_user').on('click', function () {
//         var _data = {
//             'username': $('#id_username').val(),
//             'name': $('#id_name').val(),
//             'email': $('#id_email').val(),
//             'password': $('#id_password').val()
//
//         };
//         $.ajax({
//             type: "PUT",
//             url: '/',
//             dataType: 'json',
//             data: JSON.stringify(_data),
//             success: function (_data) {
//                 console.log(_data);
//             },
//             error: function (_data) {
//                 console.log(_data);
//             }
//         });
//     });
// });
 /**
 * Created by Nazar on 02.02.2017.
 */
