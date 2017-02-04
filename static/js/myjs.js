 function del(id){
   var _data = {
        'id': id,
        'name': 'test'
   };
    $.ajax({
          type: "DELETE",
          url: "delete/",
          dataType: 'json',
          data: JSON.stringify(_data),
          success: function(response){
            console.log(response);
          }

    });
}

 function create(id){
   var _data = {
        'id': id
   };
    $.ajax({
          type: "POST",
          url: "create/",
          dataType: 'json',
          data: JSON.stringify(_data),
          success: alert("hi")

    });
}

/**
 * Created by Nazar on 02.02.2017.
 */
