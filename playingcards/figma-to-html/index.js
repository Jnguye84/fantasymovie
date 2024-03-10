/*
const movietitle
const year
const attack
const scandal
const clout
const review
const timewatched
const rating
const numbermovieswatched
*/
//letterboxd data needed: reviews.csv for year, movietitle, review, rating, timewatched  
const movietitlelist = [];
const reviewlist = [];
const ratinglist = [];
const timewatchedlist = [];
const yearlist = [];
const deck = [];
let letterboxd = {};

const uploadconfirm = document.getElementById('uploadconfirm').addEventListener('click', () => {
    Papa.parse(document.getElementById('upload file').files[0], {
        download: true,
        header: true,
        skipEmptyLines: true,
        complete: function(results) {
            
            for (let i = 0; i < results.data.length; i++) {
                movietitlelist.push(results.data[i].Name);
                reviewlist.push(results.data[i].Review);
                ratinglist.push(results.data[i].Rating);
                timewatchedlist.push(results.data[i].Date);
                yearlist.push(results.data[i].Year);
            }
            letterboxd = {
                movie : movietitlelist,
                review : reviewlist,
                rating : ratinglist,
                timewatched : timewatchedlist,
                year : yearlist
            }
            console.log(letterboxd)
        }
    });
});

const createcard = document.getElementById('createcard').addEventListener('click', () => {
    for (let i = 0; i < 6; i++) { //creates 5 different movies
        let x = Math.floor(Math.random() *movietitlelist.length); //generate random movie number index
        let movie = {
            movietitle: letterboxd.movie.movie[x].Name,
            year: letterboxd.year[x].Year,
            review:  letterboxd.review[x].Review,
            timewatched: letterboxd.timewatched[x].Date,
            rating: letterboxd.rating[x].Rating,
        };
        deck.push(movie)
        console.log(movie)
      }
}) //create random number that picks movie, create deck of card for movies

//document.getElementById("createcard").onclick = creatingmovie();

/*
let movie = {
    movietitle:,
    year:,
    attack:,
    scandal:,
    clout:,
    review:,
    timewatched:,
    rating:,
    power:
};

console.log(movie);

function creatingmovie(results){
    movietitle = document.getElementsByClassName("v3_5")
    year = document.getElementsByClassName("v4_2")
    attack = document.getElementsByClassName("v4_13")
    scandal = document.getElementsByClassName("v4_15")
    clout = document.getElementsByClassName("v4_16")
    review = document.getElementsByClassName("v4_18")
    rating = document.getElementsByClassName("v4_19")
    timewatched = document.getElementsByClassName("v4_20")
    power = document.getElementsByClassName("v4_14")
   

}
*/