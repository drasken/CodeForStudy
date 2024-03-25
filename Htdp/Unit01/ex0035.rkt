;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0035) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;Exercise 35. Design the function string-last, which extracts the
;last character from a non-empty string.

;String -> String
;Given a String return the last character
;Eg. if provided "Bike" return "e"
(define (string-last str)
  (string-ith str (- (string-length str) 1)))
