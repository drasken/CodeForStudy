;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0047) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
(require 2htdp/image)
(require 2htdp/universe)

;Exercise 47. Design a world program that maintains and displays a
;“happiness gauge.” Let’s call it gauge-prog, and let’s agree that
;happiness is a number between 0 and 100 (inclusive).
;
;
;The gauge-prog program consumes the current level of happiness. With
;each clock tick, the happiness level decreases by 0.1, it never
;falls below 0 though. Every time the down arrow key is pressed,
;happiness decreases by 1/5, every time the up arrow is pressed,
;happiness jumps by 1/3.
;
;To show the level of happiness, we use a scene with a solid, red
;rectangle with a black frame. For a happiness level of 0, the red
;bar should be gone, for the maximum happiness level of H, the bar
;should go all the way across the scene.


;Here constant definitions
(define BACKGROUND-HEIGHT 20)
(define BACKGROUND-WIDTH (* 10 BACKGROUND-HEIGHT))
(define BACKGROUND (empty-scene BACKGROUND-WIDTH BACKGROUND-HEIGHT))

;Used to draw the rectangle
(define (draw-rect happy)
  (rectangle happy BACKGROUND-HEIGHT "solid" "red"))
  

;Number -> Number
;decrease the happiness constantly
(define (decrease-happiness state)
  (- state 0.1))

; Number -> Happiness
; draw the rectangle in the state bar
 (define (render happiness)
   (place-image (draw-rect happiness)
          (/ happiness 2)  (/ BACKGROUND-HEIGHT 2)
    BACKGROUND))

;Number -> Number
;On arrow key event increase or decrease happyness
(define (modify-happiness state ke)
  (cond
    [(string=? ke "up") (* state 4/3)]
    [(string=? ke "down") (* state 1/5)]))



;Number --> Happiness
;From the starting happiness given in input, calculate the happiness
;increeasing and decreasing with time and with arrow-key
(define (gauge-prog var)
  (big-bang var
    [to-draw render]
    [on-tick decrease-happiness]
    [on-key modify-happiness]
    ))

;test
(gauge-prog 60)

;it works, missing setting the limit of 100 for happiness
