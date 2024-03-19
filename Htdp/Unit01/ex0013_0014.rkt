;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0013_0014) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;Exercise 13. Define the function string-first, which
;extracts the first 1String from a non-empty string.

(define (string-first word)
  (if
     (>= (string-length word) 1)
        (string-ith word 0)
         #false))

;Exercise 14. Define the function string-last, which
;extracts the last 1String from a non-empty string.

(define (string-last word)
  (string-ith word
     (- (string-length word) 1)
     ))