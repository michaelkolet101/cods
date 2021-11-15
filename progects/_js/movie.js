function Movie(_image, _name)
{
    this.image = _image;
    this.name =_name;
}

Movie.prototype.addToHtml = function()
{
    this.newBox = document.createElement("div");
    this.newBox.className = "box_movie";
    id_left.appendChild(this.newBox);

    this.newimg = document.createElement("img");
    this.newimg.src = '_images/'+this.image;
    this.newBox.appendChild(this.newimg); 
    this.newBox.innerHTML += "<h2>"+this.name+"</h2>";
    this.newBox.innerHTML += "<button> --read more-- </button>";
}