;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0036) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;Exercise 36. Design the function image-area, which counts the number
;of pixels in a given image.

;Image -> Number
;Takes an Image in input and return the number of pixels
;E.g. An image of 100*100 return 10000
(define (image-area img)
  (* (image-width img)
     (image-height)))