/* Shapes */
var svgContainer = document.getElementById('svgContainer2');
var animItem2 = bodymovin.loadAnimation({
  wrapper: svgContainer,
  animType: 'canvas',
  loop: true,
  path: 'static/errors/js/parents.json'
});
animItem2.setSubframe(false);
animItem2.setSpeed(0.8)
window.onresize = function(){
  animItem2.resize()
}