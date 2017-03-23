/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {

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
            error: function (_data) {
                console.log(_data);
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


function update_lecture(id) {

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
            url: '/lecture/'+ id +'/edit/',
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

// function delete_group(id) {
//
//     var _data = {
//         'id': id
//     };
//
//     $.ajax({
//         type: "DELETE",
//         url: '/group/delete/',
//         data: JSON.stringify(_data),
//         success: function (response) {
//             $("#hide_" + id).remove();
//             console.log(response);
//         },
//         error: function (err) {
//             console.log(err);
//         }
//     });
// }



