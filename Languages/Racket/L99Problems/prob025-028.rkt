#lang racket

;;;; Problems frmo 025 to 028 L99P


;; Problem 025 random permutation of list elements
(define (my-rnd-permutation lst)
  (for/list ([ind (shuffle (range (length lst)))])
    (list-ref lst ind)))

;; Test
;; (my-rnd-permutation '(a b c d e f g h))


