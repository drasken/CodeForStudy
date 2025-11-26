#lang racket

(require racket/trace)

;;;; Trying to do L-99: 99 problems in Lisp

;; Problem 001
(define (my-last lst)
  (last lst))

;; test
;; (my-last '(a b c d))  ; OK


;; Problem 002
(define (my-but-last lst)
  (cond [(< (length lst) 2) "error"]
	[(= (length lst) 2) lst]
	[else (my-but-last (cdr lst))]))

;; (my-but-last '(1 2 3 4))  ; OK


;; Problem 003
; trying not to use a bult-in function
(define (element-at lst k)
  (cond [(empty? lst) "Errore"]
	[(zero? k) (car lst)]
	[else (element-at (cdr lst) (- k 1))]))

;tests --> OK
;; (element-at '(1 4 6 8 9) 3)
;; (element-at '(1 4 6 8 9) 13)
;; (element-at '(1 4 6 8 9) 0)


;; Problem 004
;; Find the number of elements in a list
;; DONE, don't know if this is TCO or not
(define (my-len lst)
  (cond [(null? lst) 0]
        [else (add1 (my-len (cdr lst)))]))   


   
