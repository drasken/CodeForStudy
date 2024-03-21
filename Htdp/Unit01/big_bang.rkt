;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname big_bang) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
(require 2htdp/batch-io)
(require 2htdp/universe)

(define (C f)
  (* 5/9 (- f 32)))

(define (convert in out)
  (write-file out
    (string-append
      (number->string
        (C
          (string->number
            (read-file in))))
      "\n")))

(define (number->square s)
  (square s "solid" "red"))

(define (reset s ke)
  100)


(define BACKGROUND (empty-scene 200 200))
(define DOT (circle 10 "solid" "red"))
 
(define (main y)
  (big-bang y
    [on-tick sub1]
    [stop-when zero?]
    [to-draw place-dot-at]
    [on-key stop]))
 
(define (place-dot-at y)
  (place-image DOT 50 y BACKGROUND))
 
(define (stop y ke)
  0)