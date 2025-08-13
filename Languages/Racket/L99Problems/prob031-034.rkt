#lang racket
(require racket/trace) ; testing recursive calls

;;;; Problems from 031 to 034 Arithmetic


;; Problem 031 - Determine if an input number is prime
(define (my-is-prime? num)
  (define (helper-rec n step)
    (cond [(<= n 1) #f]
	  [(> step (sqrt num)) #t]
	  [(zero? (remainder n step)) #f]
	  [else (helper-rec n (add1 step))]))
  (helper-rec num 2))

;; Test -> OK
;; (my-is-prime? 17)
;; (define prime-list '(2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97))
;; (map my-is-prime? prime-list) ; expected all true -> OK


;; Problem 032 - Find GCD
;; Using Euclid's algo
(define (my-gcd num1 num2)
  (cond [(zero? num1) num2]
	[else (my-gcd (remainder num2 num1) num1)]))

;; Test -> OK
;; (my-gcd 35 15)
;; (my-gcd 101 17)


;; Problem 033 find if 2 numbers are coprime
(define (my-coprime? num1 num2)
  (if (= (my-gcd num1 num2) 1) #t #f))

;; Test -> OK
;; (my-coprime? 35 64)
;; (my-coprime? 35 65)
