function draw() {
  var canvas = document.getElementById("my-canvas");
  var context = canvas.getContext("2d");

  /* lines are 2 pixels wide, so x = 0.5 = 1 pixel,
  * because the line is in the middle of the pixel.
  */
  for(var x=0.5; x<=801; x+=10)
  {
    context.moveTo(x, 0);
    context.lineTo(x, 600);
  }

  for(var y=0.5; y<=401; y+=10)
  {
    context.moveTo(0, y);
    context.lineTo(800, y);
  }

  context.strokeStyle = "#eee";
  context.stroke();

  var dislivello = [10, 80, 20, 100, 10];
  var lunghezze = [50, 100, 80, 120, 50];

  var dislivelloCorrente = 20;
  var lunghezzaCorrente = 20;
  context.beginPath();
  context.moveTo(lunghezzaCorrente, dislivelloCorrente);
  for(var x=0; x<lunghezze.length; x++)
  {
    dislivelloCorrente = dislivelloCorrente + dislivello[x];
    lunghezzaCorrente = lunghezzaCorrente + lunghezze[x];
    context.lineTo(lunghezzaCorrente, dislivelloCorrente);
    context.moveTo(lunghezzaCorrente, dislivelloCorrente);
    console.log(lunghezzaCorrente, dislivelloCorrente);
  }
  context.lineWidth = 2;
  context.strokeStyle = "purple";
  context.stroke();
  context.strokeStyle = "black";
  context.lineWidth = 1;
  context.font ="14px Arial";
  context.strokeText("Inizio", 20, 20);
  context.strokeText("Fine", lunghezzaCorrente, dislivelloCorrente);
}
