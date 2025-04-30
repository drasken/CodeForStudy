#lang racket


(define (compound-interest init-sum years interest)
  (/ (round (* 100(* init-sum (expt (+ 1 interest) years)))) 100 ))


(define (compound-rec init-sum years interest deposit)) ;;TODO
