#lang racket

;;;; Trying to solve problem 0019 from Project Euler

;; The problem state this:
;; Start date: 1 Jenuary 1900 Sunday
;; Final date: 31 December 2000 
;; Find the number or times a month start with a sunday
;; First try;
;; Using this algorithm https://it.wikipedia.org/wiki/Calendario_perpetuo

;; Utility function for leap years
(define (is-leap? num)
  (cond [(and (zero? (remainder num 100)) (not (zero? (remainder num 400)))) #f]
	[(zero? (remainder num 4)) #t]
	[else #f]))



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
    (vector-m
    ))
;    (printf  "test ~a ~a \t" i j)))
    
;; TODO finish to implement calculation based on previous index
;; add auxiliary function

;; Calc day value starting from Sunday as zero
(define (calculate-day array-year index-month)
  (define my-calc (lambda (x) (remainder x 7)))
  (let ([year (vector-ref array-year 0)]
	[day (vector-ref array-year index-month)])
    (cond [(member day '(1 3 5 7 8 10 12)) (my-calc 31)]
	  [(member day '(4 6 9 11)) (my-calc 30)]
	  [(is-leap? year) (my-calc 29)]
	  [else (my-calc 28)])))



;; This will be maybe my main funciton to get problem solution
(define (main year1 year2)
  (let ([calendar (init-calendar (add1 (- year2 year1)))])
    (set-calendar-init-state calendar year1)
    calendar))


(main 1900 1902)
