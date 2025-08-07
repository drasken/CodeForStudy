;;;; Problems from 021 to 024


;; Problem 021 insert element in a ginvel list at position k
(define (my-insert element lst k)
  (define (helper-rec el l i acc)
    (cond [(empty? l) acc]
	  [(= i 1) (helper-rec el l (- i 1) (cons el acc))]
	  [else (helper-rec el (cdr l) (- i 1) (cons (car l) acc))]))
  (reverse (helper-rec element lst k '())))

;; Test -> OK
;; (my-insert 'test '(1 2 3 4 5 6) 2) 
;; (my-insert 'test '(1 2 3 4 5 6) -2)
;; (my-insert 'test '(1 2 3 4 5 6) 22)
;; (my-insert 'test '(1 2 3 4 5 6) 0)
;; (my-insert 'test '(1 2 3 4 5 6) 5)



