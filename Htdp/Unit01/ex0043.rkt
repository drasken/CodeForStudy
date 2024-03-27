;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0043) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;Exercise 43. Let’s work through the same problem statement with a
;time-based data definition:
;
;    ; An AnimationState is a Number.
;    ; interpretation the number of clock ticks 
;    ; since the animation started
;
;Like the original data definition, this one also equates the states
;of the world with the class of numbers. Its interpretation, however,
;explains that the number means something entirely different.
;
;Design the functions tock and render. Then develop a big-bang
;expression so that once again you get an animation of a car
;traveling from left to right across the world’s canvas.
;
;
;How do you think this program relates to animate from Prologue: How
;to Program?
;
;Use the data definition to design a program that moves the car
;according to a sine wave. (Don’t try to drive like that.)

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


; WorldState -> WorldState 
; moves the car by 3 pixels for every clock tick
; examples: 
;   given: 20, expect 23
;   given: 78, expect 81

(define (tock cw)
  (+ cw 3))


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

;; The idea is to use the sine function and to convert something
;like degree to sine and using this we move the car but it's too
;much of work for a simple exercise

;EX 43 B Mouse Event

; Number -> WorldState.
; stop the car when on the right edge of the world
(define (stop ws)
  (>= ws (- (image-width BACKGROUND) (/ CAR-LENGTH 2))))

; WorldState -> WorldState
; launches the program from some initial state 
(define (main ws)
   (big-bang ws
     [on-tick tock]
     [on-mouse hyper]
     [to-draw render]
     ;this is added by me
     [stop-when stop]))


; WorldState Number Number String -> WorldState
; places the car at x-mouse
; if the given me is "button-down" 
(define (hyper x-position-of-car x-mouse y-mouse me)
  x-position-of-car)