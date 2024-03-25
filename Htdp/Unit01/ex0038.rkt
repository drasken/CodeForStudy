;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0038) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;Exercise 38. Design the function string-remove-last, which produces
;a string like the given one with the last character removed.

;String -> String
;Given a String return the string without the last char
;E.g. "Cat" return "Ca"
(define (string-remove-last str)
  (substring str 0 (- (string-length str) 1)))