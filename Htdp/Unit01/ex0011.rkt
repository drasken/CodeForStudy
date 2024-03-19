;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0011) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;;Exercise 11. Define a function that consumes two numbers,
;;x and y, and that computes the distance of point (x,y) to the origin.

(define (ex11 x y)
  (sqrt
   (+ (expt x 2)
     (expt y 2))))
  
