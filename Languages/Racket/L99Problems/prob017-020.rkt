;;;; Problems from 17 to 20

#lang racket

;; Problem 017 Split a list in two
;; the length of the first one is given as input
(define (my-split lst len)
;  (if (< len 0)
  (define (helper-rec l acc counter)
    (cond [(zero? counter) (list (reverse acc) l)]
	  [else (helper-rec (cdr l) (cons (car l) acc) (- counter 1))]))
  (if (< len 0) (error "Not valid len input")
      (helper-rec lst '() len)))

;; Test
;; (my-split '(a b c d e f g h i k) 3)


;; Prob 018 extract a slice from a list 
;; Return slice of list from i to k included
;; Count elements from 1 in list
(define (my-slice lst index1 index2)
  (define (help-rec l i1 i2 acc)
    (cond [(and (zero? i1) (zero? i2)) acc]
	  [(> i1 1) (help-rec (cdr l) (- i1 1) (- i2 1) acc)]
	  [(zero? i1) (help-rec (cdr l) i1 (- i2 1) (cons (car l) acc))]
	  [else (help-rec (cdr l) (- i1 1) (- i2 1) (cons (car l) acc))]))
  (if (or (<= index1 0) (>= index2 (length lst)))
      (displayln "Index error")
      (reverse (help-rec lst index1 index2 '()))))

;; Test -> OK
;; (my-slice '(a b c d e f g h i k) 3 7)

		     
		     
