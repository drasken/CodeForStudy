#lang racket
(require "./prob021-024-DONE.rkt")
;;;; Problems frmo 025 to 028 L99P

(define (my-rnd-select1 lst num) ; from problem 023
  (define (helper-re l n acc)
    (cond [(empty? l) acc]
	  [(zero? n) acc]
	  [else (helper-re (cdr l) (- n 1) (cons (car l) acc))]))
  (helper-re (shuffle lst) num '()))



