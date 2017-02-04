 function del(id){
   $( "#rooms" ).hide( "#rooms" );
   var _data = {
        'id': id,
        'name': name
   };
    $.ajax({
          type: "DELETE",
          url: "delete/",
          dataType: 'json',
          data: JSON.stringify(_data),
          success:
          function(response){
            console.log(response);
          }


    });
}



/**
 * Created by Nazar on 02.02.2017.
 */
