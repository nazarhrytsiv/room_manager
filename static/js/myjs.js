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
          success: function(respons){
            console.log(respons)
          },

    });
}
/**
 * Created by Nazar on 02.02.2017.
 */
