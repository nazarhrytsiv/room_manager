/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {

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
            success: function (respons) {
                console.log(respons);
            },
            error: function (err) {
                console.log(err);
            }
        });
    });
});

// $(document).ready(function () {
//
//     $('#update_group').on('click', function () {
//         var _data = {
//             'id':  ,
//             'name': $('#id_name_group').val(),
//             'description': $('#id_description_group').val()
//         };
//         $.ajax({
//             type: "PUT",
//             url: '/group/'+ id +'/edit/',
//             contentType: 'application/json; charset=utf-8',
//             data: JSON.stringify(_data),
//             success: function (respons) {
//                 console.log(respons);
//             },
//             error: function (err) {
//                 console.log(err);
//             }
//         });
//     });
// });


function update_group(id) {

    var _data = {
            'id': id ,
            'name': $('#id_name_group').val(),
            'description': $('#id_description_group').val()
        };

    $.ajax({
            type: "PUT",
            url: '/group/'+ id +'/edit/',
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

function add_member_to_group(user_id,group_id) {

    var _data = {
            'id': user_id
        };

    $.ajax({
            type: "POST",
            url: '/group/'+ group_id +'/add_member/',
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


