;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0020) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;Exercise 20. Define the function string-delete, which consumes a
;string plus a number i and deletes the ith position from str. Assume i
;is a number between 0 (inclusive) and the length of the given string
;(exclusive). See exercise 4 for ideas. Can string-delete deal with
;empty strings?


;Not implemented use case for emptylist 
(define (string-delete word i)
  (string-append (substring word 0 i)
                 (substring word (+ 1 i) (string-length word))))
