#lang racket

;; Problem 005
(define (my-reverse lst)
  (define (aux-my-func l res)
    (cond [(empty? l) res]
	  [else (aux-my-func (cdr l) (cons (car l) res))]))
  (aux-my-func lst '()))

;; test -> OK
;; (my-reverse '(1 4 5 8 99))


;; Problem 006
;; using first naive approach
(define (is-pal lst)
  (let ([rev (reverse lst)])
    (if (equal? rev lst) #t #f)))

;; test -> OK
;; (is-pal '(a b c b a a))
;; (is-pal '(a b c b a)) 
;; (is-pal '())    

;; TODO --------------------
;; Problem 007 - flatten list
;; Example:
;; * (my-flatten '(a (b (c d) e)))
;; (A B C D E)
(define (my-flatten lst)
  (define (rec-flat l acc)
    (cond [(null? l) acc]
          [(pair? (car l))
           (append (rec-flat (car l) acc))]
          [else (append (rec-flat (cdr l) (cons (car l) acc)))]))
  (rec-flat lst '()))


(define (my-flatten2 lst)
  (define (rec-flat2 l acc)
    (cond [(null? l) acc]
          [(pair? l) (append (rec-flat2 

;; test
;;(my-flatten '(a (b (c d) e)))		    
		    

;; Problem 008
;; Eliminate consecutive duplicates of list elements.
;; If a list contains repeated elements they should be replaced
;; with a single copy of the element.

(define (my-compress lst)
  (define (my-com-help l acc)
    (cond [(empty? l) acc]
          [(equal? (car l) (car acc)) (my-com-help (cdr l) acc)]
          [else (my-com-help (cdr l) (cons (car l) acc))]))
  (reverse (my-com-help lst (list (car lst)))))


;; test -> OK!
;; (my-compress '(a a a  b c c c c c b b b b e d a a))
;; (my-compress '(a a a a b c c a a d e e e e))
	   




