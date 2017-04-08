window.addEventListener('load', main);

function main() {
	get_and_draw_coordinates();
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

function handle_response(raw_coordinates_str) {
	var raw_coordinates = raw_coordinates_str.split(";");

	var xcoords = [];
	var ycoords = [];

	for (var i = 0; i < raw_coordinates.length; i++) {
		var rc = raw_coordinates[i];

		if (rc.length <= 3) {
			continue;
		}

		rc = rc.substring(1, rc.length - 1);

		coords = rc.split(",");

		xcoords.push(parseInt(coords[0]));
		ycoords.push(parseInt(coords[1]));
	}

	draw_coords(xcoords, ycoords);
}

function draw_coords(xcoords, ycoords) {
	var canvas = document.getElementById('board');

	var cwidth = canvas.width;
	var cheight = canvas.height;

	var context = canvas.getContext("2d");

	for (var i = 0; i < xcoords.length && i < ycoords.length; i++) {
		var x = xcoords[i];
		var y = cheight - ycoords[i];
		var r = 2;

		context.fillStyle = "#000000";
		context.beginPath();
		context.arc(x,y,r,0,Math.PI*2,true);
		context.closePath();
		context.fill();
	}	
}