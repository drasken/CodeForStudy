#lang racket

;;; PROBLEM
;; <p>Let $d(n)$ be defined as the sum of proper divisors of $n$
;; (numbers less than $n$ which divide evenly into $n$).<br>
;; If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$
;; are an amicable pair and each of $a$ and $b$ are called amicable numbers.</p>
;; <p>For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$
;; and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are
;; $1, 2, 4, 71$ and $142$; so $d(284) = 220$.</p>
;; <p>Evaluate the sum of all the amicable numbers under $10000$.</p>

;; My limit number, given by the problem
(define NUMBERS 10000)

;; Find the proper divisor for a number recursively
(define (find-proper-div num)
  (define (fpd-rec n test acc)
    (cond [(zero? test) (foldl + 0 acc)]  ; sum all accumulated values
          [(zero? (remainder n test)) (fpd-rec n (sub1 test) (cons test acc))]
          [else (fpd-rec n (sub1 test) acc)]))
  (fpd-rec num (floor (/ num 2)) '()))

;; create an hash table computing find-proper-divisor
;; for each number under limit make (mumber . val) pair
(define (ht-proper limit)
  (for/hash ([i (in-range limit)])
    (cond [(> (find-proper-div i) limit) (values i 0)]
          [else (values i (find-proper-div i))])))

;; test if 2 numbers are amicable
(define (amicable? a b ht)
  (and (not (= a b)) (= (hash-ref ht a) b) (= (hash-ref ht b) a)))

;; get the amicable keys from the hash table and sum them 
(define (get-res ht)
  (for/sum ([(i j) (in-hash ht)]
            #:when (amicable? i j ht))
    i))

;; variable to store my solution
(define res (get-res (ht-proper NUMBERS)))

