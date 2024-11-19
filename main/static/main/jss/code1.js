button.onclick = function()
{var alpha = 0;
 var X;
 var Y;
 var EartX;
 var EartY;
var timerId = setInterval(function()
{
	 X=150*Math.sin(alpha)+275;
     Y=150-150*Math.cos(alpha);
     document.getElementById("Earth").style.left = ( X  + 'px');
     document.getElementById("Earth").style.top = ( Y  + 'px');
     document.getElementById('X').value = X;
     document.getElementById('Y').value = Y;
     alpha = alpha + 0.01;
}, 50);

};

button1.onclick = function()
{
var X = new Array();
var X =[];
var i;
X[0]=Math.floor(Math.random() * (240 - 0 + 1)) + 0;
for (i=1; i <= 9; i++)
{X[i]=Math.floor(Math.random() * ((240 + i*40) - X[i-1] + 1)) + X[i-1];};
document.getElementById('Text1').value = X;
var Y = new Array();
var Y =[];
for (i=0; i <= 10; i++)
{Y[i]=Math.floor(Math.random() * (300 - 1 + 1)) + 1;};
document.getElementById('Text2').value = Y;

button2.onclick = function()
{
var b;
var b_canvas = document.getElementById("Ris");
var b_context = b_canvas.getContext("2d");
b_context.fillStyle="white";
b_context.fillRect(0, 0, 600, 300);
b_context.beginPath();
for (b = 1; b <= 12; b++)
{
b_context.moveTo(X[b-1],(300-Y[b-1]));
b_context.lineTo((X[b]),(300-Y[b]));
b_context.closePath();
b_context.stroke();
};
};
};

