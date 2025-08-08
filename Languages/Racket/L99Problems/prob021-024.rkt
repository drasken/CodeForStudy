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


;; Problem 022 Create list of integers in a given range
;; If first number limit is greater than secons the order is descending
;; First easy solution with racket for/list
(define (my-range1 val-1 val-2)
;  (define descending (if (> val-1 val-2) #t #f)
  (for/list ([i (if (> val-1 val-2)
		    (in-range val-1 (- val-2 1) -1)
		    (in-range val-1 (add1 val-2)))])
    i))

;; Test
(my-range1 21 10) 
		    
