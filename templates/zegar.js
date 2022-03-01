function start_timer()
{
const today = new Date();
let h = today.getHours();
if (h < 10) h = "0" + h;
let m = today.getMinutes();
if (m < 10) m = "0" + m;
let s = today.getSeconds();
if (s < 10) s = "0" + s;

document.getElementById('zegar').innerHTML = h + ":" + m + ":" + s;
setTimeout(start_timer, 1000);
}