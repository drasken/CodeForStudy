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

