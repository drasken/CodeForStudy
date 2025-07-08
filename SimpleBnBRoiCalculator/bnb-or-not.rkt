#lang racket


;;;; Doing simple calculation to understand if Bnb rent is convenient or not
;;;; The alternative considered is selling the house and investing in a risk-free asset

(define home-value 100000) ; Dummy value, change accordingly
(define yearly-depreciation 0.03) ; Found that 3% is standard government rate


(define (round-2-decimal num)
  

(define (compound-interest init-sum interest years)
    (* init-sum (expt (+ 1 interest) years)))

(compound-interest 1000 0.03 10)
