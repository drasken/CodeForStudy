#lang racket

(require test-engine/racket-tests)

;(provide collatz)

(define (collatz num)
  ;(error "Not implemented yet")
  (define (col num step)
    (cond
         [(= num 1) step]
         [(= (remainder num 2) 0) (col (/ num 2) (+ step 1))]
         [else (col (+ (* num 3) 1) (+ step 1))]))
  (col num 0))

(define (collatz2 num)
  ;(let ([step 0])
  (let ([step 0])
  (do ([num num (if (= (remainder num 2) 0)
                    (/ num 2)
                    (add1 (* num 3)))]
       [step step (add1 step)])
       ((= num 1) step))))



;;;; FUnctions to compare different iteration efficiency
(define (collatz-multiple upper-limit)
  (for ([i (in-range 1 upper-limit)])
    (collatz i))
  'end)


(define (collatz-multiple2 upper-limit)
  (for ([i (in-range 1 upper-limit)])
    (collatz2 i))
  'end)


;; (collatz 1)

;; (collatz-multiple 9)

(check-expect 9 (collatz 12))
(check-expect 152 (collatz 1000000))
(test)
