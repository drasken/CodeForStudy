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


;; Annualize final investment return in percentage
;; This is the yearly version
;; Formula: AnnReturn = (1 + cumulativeReturn) ^ 1/n-years - 1
(define (calc-annual-return-y init-sum final-sum years)  ; This version we get our total return
  (let ([tot-return (- (/ final-sum init-sum) 1)])
    (- (expt (+ 1 tot-return) (/ 1 years)) 1)))


;; Annualize final investment return in percentage
;; This is the daily version
;; ; Formula: AnnReturn = (1 + cumulativeReturn) ^ 365/n-days - 1
(define (calc-annual-return-d init-sum final-sum days)  ; This version we get our total return
  (let ([tot-return (- (/ final-sum init-sum) 1)])
    (- (expt (+ 1 tot-return) (/ 365 days)) 1)))


;; Test
;; (calc-annual-return-d 100 115.75 650)  ; -> 0.0855 - OK


;;;; HERE IO USER'S INTERACTION LOGIC ---------------



;;;; HERE MY MAIN FUNCTION ---------------




