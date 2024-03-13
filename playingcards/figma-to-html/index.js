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
// import { run } from './gemini_test.js'

// import { run } from "./gemini_test";

// run()
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
            movietitle: letterboxd.movie[x],
            year:letterboxd.year[x],
            review: letterboxd.review[x],
            timewatched: letterboxd.timewatched[x],
            rating: letterboxd.rating[x],
        };
        deck.push(movie)
      }
    let x_second = Math.floor(Math.random() *6);
    localStorage.setItem('movie-title', deck[x_second].movietitle)
    localStorage.setItem('year', deck[x_second].year)
    localStorage.setItem('review', deck[x_second].review)
    localStorage.setItem('rating', deck[x_second].rating)
    localStorage.setItem('timewatched', deck[x_second].timewatched)

    window.location.href="index.html";

}) //create random number that picks movie, create deck of card for movies, uploads card pictures onto trading card,