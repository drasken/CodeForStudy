;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0051) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
(require 2htdp/image)
(require 2htdp/universe)

;Exercise 51. Design a big-bang program that simulates a traffic
;light for a given duration. The program renders the state of a
;traffic light as a solid circle of the appropriate color, and it
;changes state on every clock tick. Hint Read the documentation
;for big-bang; there is a reason all these “words” are linked to
;their documentation. What is the most appropriate initial state?
;Ask your engineering friends.


; TrafficLight -> TrafficLight
; yields the next state given current state s
(check-expect (traffic-light-next "red") "green")
(check-expect (traffic-light-next "green") "yellow")
(check-expect (traffic-light-next "yellow") "red")
(define (traffic-light-next s)
  (cond
    [(string=? "red" s) "green"]
    [(string=? "green" s) "yellow"]
    [(string=? "yellow" s) "red"]))

(define LIGHT-SIDE 50)
;String -> Image
;Given the color render the square representing
;traffic-lights
(define (render color)
  (place-image (square LIGHT-SIDE "solid" color)
               (/ LIGHT-SIDE 2) (/ LIGHT-SIDE 2)
               (empty-scene LIGHT-SIDE LIGHT-SIDE)))

;TrafficLight -> TrafficLight
;Draws the TL depending on the state, changing on tick 
(define (main color)
  (big-bang color
       [to-draw render]
       [on-tick traffic-light-next]))

(main "red")
