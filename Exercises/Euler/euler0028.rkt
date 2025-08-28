#lang racket

;; Find sum of number on matrix diagonals
;; the matrix is created from center and spiraling counter clockwise
;; Ex given matrix 5 * 5 -> 101
;; Find result for a matrix 1001 * 1001


;; Idea: create first upper and lower rows and get sum

(define (aux-list side-len el res-list)
  (append (list (+ el side-len 1)
	      (+ el 2 (* 2 side-len))
	      (+ el 3 (* 3 side-len))
	      (+ el 4 (* 4 side-len)))
	res-list))

(define test-acc (list 3 5 7 9 1))
;; Test
;; (aux-list 3 9 test-acc)

;; Function to create list of list of desired number to sum
(define (create-matrix limit) ; limit is the matrix side dimension
  (define (helper-rec lim step last-el acc) ; step is starting matrix side dimension
    (cond [(= step limit) acc]
	  [else (helper-rec lim (+ 2 step) (+ (* 4 step) 4 last-el)
			    (aux-list step last-el acc))]))
  (helper-rec limit 1 1 '(1)))

;; Solution -> OK it works!
(define my-res (apply + (create-matrix 1001)))

