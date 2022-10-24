$(document).ready(function () {

//	for (const [key, value] of Object.entries(data)) {
//	  console.log(key, value);

//  })

	$("#final_website").click(function () {
		renderFinal()
	})

})

function renderFinal(){
  window.location.href = "http://127.0.0.1:5000/test_website";
}
