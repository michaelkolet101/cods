// javaScript Document

var product_1;
var product_2;
var product_3;
var product_4;


function init(){
    console.log("it is working");
    createProduct();
    // addProductToHtml();
}

function addProductToHtml(obg){

    var newSection = document.createElement("section");
    // var newimg = document.createEvent("img");
    newSection.className = "product";
    products.appendChild(newSection);

    newSection.innerHTML +="<h2>"+obg.name +"</h2> ";
    // newimg.src =  "images/"+obg.image;

    newSection.appendChild(newimg );

    newSection.innerHTML += "<div>"+obg.info+"</div>";
    newSection.innerHTML += "<div>price: "+obg.price+"</div>";

}

function createProduct(){
    product_1 = {
        name:"cola",
        image:"cola.jpg",
        info:"coca cola with ice",
        price:"10"
    }
    
    
    product_2 = {
        name:"sprite",
        image:"cola.jpg",
        info:"sprite with ice",
        price:"9"
    }

    product_3 = {
        name:"fanta",
        image:"cola.jpg",
        info:"fanta with ice",
        price:"8"
    }

    product_4 = {
        name:"pepsi",
        image:"cola.jpg",
        info:"pepsi cola with ice",
        price:"11"
    }
    addProductToHtml(product_1);
    addProductToHtml(product_2);
    addProductToHtml(product_3);
    addProductToHtml(product_4);
}