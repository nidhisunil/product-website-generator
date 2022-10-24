$(document).ready(function () {


	//or, when you click the button directly
	$("#submit-product_id").click(function () {
		addName()
	})
})

function addName(){
  let productID = $("#product_id").val()
  let data_to_save = {"product_id": productID}
  $.ajax({
            type: "POST",
            url: "save_product",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),
            success: function (data, textStatus, jqXHR) {


               let itemAddedByServer = data['product_id']
               console.log(itemAddedByServer)
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
  window.location.href = "http://127.0.0.1:5000/name";
}
