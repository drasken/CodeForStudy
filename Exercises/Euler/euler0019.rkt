#lang racket

;;;; Trying to solve problem 0019 from Project Euler

;; The problem state this:
;; Start date: 1 Jenuary 1900 Sunday
;; Final date: 31 December 2000 
;; Find the number or times a month start with a sunday
;; First try;
;; Using this algorithm https://it.wikipedia.org/wiki/Calendario_perpetuo

;; Utility function for leap years
;; (define (is-leap? num)
;;   (cond [(and (zero? (remainder num 100)) (not (zero? (remainder num 400)))) #f]
;; 	[(zero? (remainder num 4)) #t]
;; 	[else #f]))


;; Try 001: using matrix and checking with offset modulo 7

(define (init-matrix years elements)
  (lambda (x)
    (for/vector ([i (in-range x)])
      (for/vector ([j (in-range elements)])
	-1))))

(define (init-calendar years)
  (let ([my-calendar (init-matrix years 13)])
    (my-calendar years)))


(define (set-calendar-init-state calendar year)
  (let ([val year]
	[first #t])
    (for ([i calendar])
      (vector-set! i 0 val)
      (set! val (add1 val)))
    (vector-set! (vector-ref calendar 0) 1 0))) ; hardcoded firt day is a sunday

(define (set-calendar-first-days calendar)
  (for* ([i (in-range (vector-length calendar))]
	 [j (in-range 1 13)] ; iterate on all matrix
	 #:unless (and (zero? i)(zero? j)))
    (printf  "test ~a ~a \t" i j)))
;; TODO finish to implement calculation based on previous index
;; add auxiliary function


;; This will be maybe my main funciton
;; (define my-calendar (for/vector ([i (in-range 1900 2001)])
;; 		      (build-vector

