#lang racket

;;;; HERE GLOBAL VARIABLES ---------------


;;;; HERE FUNCTIONS DEFINITIONS ---------------

;; Simple interest calculator
;; rate must be a float (0.0, N)
(define (calc-simple-interest init-sum rate periods)
  (+ init-sum (* periods (* init-sum rate))))

;; Test
;; (simple-interest 100 0.10 6) ; -> 160 - OK


;; Compound interest calculator
;; This function compute to get only a final result
(define (calc-compond-interest init-sum rate periods)
  ;; Add a rounding to the result
  (/ (round (* 100  ; This do the rounding
		   (* init-sum (expt (+ 1 rate) periods)))) 100))  ; this do the calc

;; Test
;; (calc-compond-interest 100 0.05 10)  ; -> 162.89 - OK
 

;;;; HERE IO USER'S INTERACTION LOGIC ---------------



;;;; HERE MY MAIN FUNCTION ---------------




