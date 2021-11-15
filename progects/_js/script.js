var movies_arr;
var movie1;

function init()
{
    creatMovies()
}

function creatMovies()
{
    for(var i=0; i<json_ar.length; i++)
    { 
        movie = new Movie(json_ar[i]. image, json_ar[i].name);
        movie.addToHtml();
    }
 
}