$(document).ready(function () {

//	for (const [key, value] of Object.entries(data)) {
//	  console.log(key, value);

//  })

	$("#submit_product_colour").click(function () {
		addColour()
	})

})



function addColour(){
  let productColour = $("#product_colour").val()
  let data_to_save = {"product_colour": productColour}
  $.ajax({
            type: "POST",
            url: "save_productcolour",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),
            success: function (data, textStatus, jqXHR) {


							console.log("Succes saved primary colour");
               getToNamePage();


            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
}

function getToNamePage(){
  window.location.href = "http://127.0.0.1:5000/secondarycolour";
}
