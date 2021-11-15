// javaScript Document

var bmw;
var mazda;
var toyota;

function init()
{
createObgects();
}

function createObgects()
{
 bmw ={
     model:"x6",
     price:"150000",
     year:"2012",
     color:"black",
     showinfo:function(){
        id_h2.innerHTML = "the car model is: "+this.model+" and its color is: "+this.color;
     }

 }

 mazda ={
    model:"3",
    price:"6000",
    year:"2011",
    color:"blue",
    showinfo:function(){
        id_h2.innerHTML = "the car model is: "+this.model+" and its color is: "+this.color;
     }
}

toyota ={
    model:"corola",
    price:"75000",
    year:"2010",
    color:"red"

}
}
function onbmwclick()
{
   bmw.showinfo(); 
}

function onmazdaclick()
{
   mazda.showinfo(); 
}