function draw() {
  var canvas = document.getElementById("my-canvas");
  var context = canvas.getContext("2d");

  /* lines are 2 pixels wide, so x = 0.5 = 1 pixel,
  * because the line is in the middle of the pixel.
  */
  for(var x=0.5; x<=801; x+=10) {
    context.moveTo(x, 0);
    context.lineTo(x, 600);
  }

  for(var y=0.5; y<=401; y+=10) {
    context.moveTo(0, y);
    context.lineTo(800, y);
  }

  context.strokeStyle = "#eee";
  context.stroke();

  // Draw a circle

  var segments = 64, radius = 100;
  var cx = 400, cy = 200;

  context.moveTo(cx + radius, cy + radius);

  context.beginPath();

  for(var i=0; i<=segments; i++) {
    var alpha = (i/segments) * 2 * Math.PI;
    context.lineTo(cx + radius * Math.cos(alpha), cy + radius * Math.sin(alpha));
  }

  context.lineWidth=1;
  context.strokeStyle = "#000";
  context.stroke();
}
