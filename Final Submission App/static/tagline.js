$(document).ready(function () {
	$("#submit_tagline_name").click(function () {
		addTagline()
	})
})



function addTagline(){
  let productTagline = $("#tagline_name").val()
  let data_to_save = {"product_tagline": productTagline}
  $.ajax({
            type: "POST",
            url: "save_producttagline",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),
            success: function (data, textStatus, jqXHR) {


							console.log("Succes saved tagline");
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
  window.location.href = "http://127.0.0.1:5000/paragraph";
}
