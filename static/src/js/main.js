function del(id) {

    var _data = {
        'id': id,
        'name': name
    };
    $.ajax({
        type: "DELETE",
        url: "delete/",
        dataType: 'json',
        data: JSON.stringify(_data),
        success: function (response) {
            console.log(response);
        }


    });
}

function delete_group(id) {

    var _data = {
        'id': id,
        'name': name
    };
    $.ajax({
        type: "DELETE",
        url: "delete/",
        data: JSON.stringify(_data),
        success: function (response) {
            $("#group_" + id).remove();
            console.log(response);
        },
        error: function (err) {
            console.log(err);
        }
    });
}

$('.btn-default').on('click', function () {
    var _data = {
        'name': $('#id_name').val(),
        'captain': $('#id_captain').val(),
        'description': $('#id_description').val()

    };
    $.ajax({
        type: "POST",
        url: "create/",
        data: JSON.stringify(_data),
        success: function (response) {
            console.log(response);
        },
        error: function (err) {
            console.log(err);
        }
    });
});

/**
 * Created by Nazar on 02.02.2017.
 */
