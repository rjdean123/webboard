window.addEventListener('load', main);

function main() {
	get_and_draw_coordinates();

	// var canvas = document.getElementById('board');

	// var cwidth = canvas.width;
	// var cheight = canvas.height;

	// var context = canvas.getContext("2d");

	// for (var i = 0; i < 1000; i++) {
	// 	context.fillStyle = "#000000";
	// 	getContext.beginPath();
	// 	context.arc(i,i,2,0,Math.PI*2,true);
	// 	context.closePath();
	// 	context.fill();
	// }
}

function get_and_draw_coordinates() {
	var xhr = new XMLHttpRequest();

	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			handle_response(xhr.responseText);
		}
	};

	xhr.open('GET', "https://webboard-bitcamp.herokuapp.com/api", true);
	xhr.send();

}

function handle_response(s) {
	alert(s);
}