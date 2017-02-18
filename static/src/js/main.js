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
