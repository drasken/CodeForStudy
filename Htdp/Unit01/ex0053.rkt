;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0053) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
(require 2htdp/image)
(require 2htdp/universe)

;Ex 53

;Constants
(define HEIGHT 400)
(define WIDTH 300)
(define CENTER-X (/ WIDTH 2))

;Draw the rocket
(define SCENE  (empty-scene WIDTH HEIGHT))
(define ROCKET (bitmap "rocket.png"))
(define HALF-ROCKET (/ (image-height ROCKET) 2))
(define MAX-Y (- HEIGHT HALF-ROCKET))


; An LR (short for launching rocket) is one of:
; – "resting"
; – NonnegativeNumber
; interpretation "resting" represents a grounded rocket
; a number denotes the height of a rocket in flight
;(check-expect (LR 29) 
(define (LR y)
  (place-image ROCKET
               CENTER-X
               (cond
                 [(equal? y "resting") HALF-ROCKET]
                 [(string? y) HALF-ROCKET]
                 [(= y 0) HALF-ROCKET]
                 [(and (> y 0) (< y MAX-Y)) y]
                 [else MAX-Y])
                SCENE))

(LR 200)
(LR 0)
(LR 20)
(LR "resting")
(LR "asd")
(LR 300)
(LR 800)



                       