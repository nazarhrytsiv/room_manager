$(document).ready(function () {
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,basicWeek,basicDay'
        },
        defaultDate: '2017-03-01',
        navLinks: true, // can click day/week names to navigate views
        editable: true,
        eventLimit: true, // allow "more" link when too many events
    });
    $('#get_group').on('click', function () {
        var _data = {
            'name': $('#group_name').val(),
        };
        $.ajax({
            type: "POST",
            url: '/schedule/group_schedule/',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            data: JSON.stringify(_data),

            success: function (data_from_server) {
                events = data_from_server;


                $('#calendar').fullCalendar('removeEvents');
                $('#calendar').fullCalendar('addEventSource', events);
                $('#calendar').fullCalendar('rerenderEvents');
            },
            error: function (data_from_server) {
                console.log(data_from_server);

            }
        });

    });


});