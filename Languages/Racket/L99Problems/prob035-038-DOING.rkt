#lang racket
(require "./prob031-034-DONE.rkt") ; importing my-is-prime? 
(require racket/trace)

;;;; Problems from 035 to 038
;; Hekper funciton to find all primes in a given range
(define (find-primes num)
  (define (helper-rec num step acc)
    (cond [(= step (add1 num)) acc]
	  [(my-is-prime? step)
	   (helper-rec num  (add1 step) (cons step acc))]
	  [else (helper-rec num (add1 step) acc)]))
  (reverse (helper-rec num 2 '())))

;; Test
;; (find-primes 19)


;; Effective main funciton
(define (my-prime-factors n)
  (let loop  ([test-list (find-primes n)] ; generate all primes
	      [acc '()] ; save find values
	      [temp n]) ; temp var to check factors
    (cond [(or (empty? test-list) (= temp 1)) (reverse acc)] ; base case
	  [(zero? (remainder temp (car test-list))) ; factor found
	   (loop test-list (cons (car test-list) acc) (/ temp (car test-list)))]
	  [else (loop (cdr test-list) acc temp)])))

;; Test -> OK
;; (my-prime-factors 315)
;; (my-prime-factors 15)
;; (my-prime-factors 17)


;; Problem 036 - express factor with a multiplicity pair instead of listing flat
;; Solving it using an hash table
(define (my-factors-new num)
  (define my-res (make-hash))
  (define my-factors (my-prime-factors num))
  (for ([i my-factors])
    (if (hash-has-key? my-res i)
	(hash-update! my-res i add1)
	(hash-set! my-res i 1)))
  (hash-map my-res (lambda (k v) (list k ))))

;; Test
;; (my-factors-new 315)
;; (my-factors-new 15)



