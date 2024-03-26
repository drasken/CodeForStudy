;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0039_0041) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;Exercise 39. Good programmers ensure that an image such as CAR can
;be enlarged or reduced via a single change to a constant definition.


;Good programmers establish a single point of control for all aspects
;of their programs, not just the graphical constants. Several
;chapters deal with this issue. We started the development of our car
;image with a single plain definition:

(require 2htdp/image)
(require 2htdp/universe)

;designing the car
(define WHEEL-RADIUS 10)
(define WHEEL-DISTANCE (* WHEEL-RADIUS 5))
(define CAR-LENGTH (* WHEEL-RADIUS 9))
(define CAR-HEIGHT (* WHEEL-RADIUS 2))
(define UPPER-CAR-LENGTH(* CAR-LENGTH 3/5))
(define UPPER-CAR-HEIGHT CAR-HEIGHT)
(define FIRST-WHEEL-Y (* WHEEL-RADIUS 3/2))
(define FIRST-WHEEL-X (- (+ UPPER-CAR-HEIGHT CAR-HEIGHT)(/ WHEEL-RADIUS 3/2) ))
(define SECOND-WHEEL-Y FIRST-WHEEL-Y)
(define SECOND-WHEEL-X (+ FIRST-WHEEL-X WHEEL-DISTANCE))

(define (auto num)          
  (overlay/xy;combine the 2
   ;under here creating the car
  (above (rectangle UPPER-CAR-LENGTH UPPER-CAR-HEIGHT  "solid" "red")
         (rectangle CAR-LENGTH CAR-HEIGHT "solid" "red"))
                FIRST-WHEEL-Y FIRST-WHEEL-X
          (overlay/xy ;creating the Wheels
          (circle WHEEL-RADIUS "solid" "black")
           WHEEL-DISTANCE 0
           (circle WHEEL-RADIUS "solid" "black")
           )))
  

(auto 0)
;Ex 39 ends here

;Exercise 40. Formulate the examples as BSL tests, that is, using the
;check-expect form. Introduce a mistake. Re-run the tests.

; WorldState -> WorldState 
; moves the car by 3 pixels for every clock tick
; examples: 
;   given: 20, expect 23
;   given: 78, expect 81

(define (tock cw)
  (+ cw 3))

;this below are tests added byt me

(check-expect (tock 20) 23)
(check-expect (tock 100) 103)
(check-expect (tock 0) 3)
(check-expect (tock -20) -17)
;all tests passed--> OK

;End of Ex 20

;Exercise 41. Finish the sample problem and get the program to run.
;That is, assuming that you have solved exercise 39, define the
;constants BACKGROUND and Y-CAR. Then assemble all the function
;definitions, including their tests. When your program runs to your
;satisfaction, add a tree to the scenery. We used
;
;    (define tree
;      (underlay/xy (circle 10 "solid" "green")
;                   9 15
;                   (rectangle 2 20 "solid" "brown")))
;
;to create a tree-like shape. Also add a clause to the big-bang
;expression that stops the animation when the car has disappeared on
;the right side.

;Defined by me
(define WORLD-HEIGHT (* WHEEL-RADIUS 10))
(define BACKGROUND (empty-scene (* WHEEL-RADIUS 40) WORLD-HEIGHT))
(define Y-CAR (- WORLD-HEIGHT(* WHEEL-RADIUS 11/4)))
(define CAR (auto 0))                         
; WorldState -> Image
; places the car into the BACKGROUND scene,
; according to the given world state 
 (define (render cw)
   (place-image CAR cw Y-CAR BACKGROUND))

; WorldState -> WorldState
; launches the program from some initial state 
(define (main ws)
   (big-bang ws
     [on-tick tock]
     [to-draw render]
     ;this is added by me
     [stop-when stop]))

;defined by me to call on stop-when
(define (stop ws)
  (>= ws (- (image-width BACKGROUND) (+ CAR-LENGTH 1))))