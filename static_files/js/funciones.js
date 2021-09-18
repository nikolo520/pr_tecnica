
function consultar_usuario(id){

}

function guardar_usuario(id){
    
}

function eliminar_usuario(id){
    
}

$("button").click(function(){
    $.ajax({url: "demo_test.txt", success: function(result){
      $("#div1").html(result);
    }});
  });

  $("#crear_usuario").click(function(){
    var bool=confirm("Seguro de eliminar el dato?");
    if(bool){
      alert("se elimino correctamente");
    }else{
      alert("cancelo la solicitud");
    }
  });