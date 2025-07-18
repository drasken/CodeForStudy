#lang racket

;; Problem 005
(define (my-reverse lst)
  (define (aux-my-func l res)
    (cond [(empty? l) res]
	  [else (aux-my-func (cdr l) (cons (car l) res))]))
  (aux-my-func lst '()))

;; test -> OK
(my-reverse '(1 4 5 8 99))


;; Problem 006
;; using first naive approach
(define (is-pal lst)
  (let ([rev (reverse lst)])
    (if (equal? rev lst) #t #f)))

;; test -> OK
(is-pal '(a b c b a a))
(is-pal '(a b c b a)) 
(is-pal '())    


;; Problem 007 - flatten list
;; Example:
;; * (my-flatten '(a (b (c d) e)))
;; (A B C D E)
(define (my-flatten lst)
  'test )
;; TODO6
  

;; test
;;(my-flatten '(a (b (c d) e)))		    
		    

;; Problem 008
;; Eliminate consecutive duplicates of list elements.
;; If a list contains repeated elements they should be replaced
;; with a single copy of the element.
;; The order of the elements should not be changed.
;; Example:
;; * (pack '(a a a a b c c a a d e e e e))
;; ((A A A A) (B) (C C) (A A) (D) (E E E E))

;; Idea is to use an hash-map
(define (my-filter-dup lst)
  'test)




