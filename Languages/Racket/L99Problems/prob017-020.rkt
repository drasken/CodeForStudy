;;;; Problems from 17 to 20


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
