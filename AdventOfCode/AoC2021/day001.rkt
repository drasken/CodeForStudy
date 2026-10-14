;;;; Use as day template

#lang racket

;;;; READ INPUT
;;File path
(define my-path "./input001.txt")

;; Read it
(define (read-my-input path)
    (file->lines path))

;; My input
(define my-input (map string->number (read-my-input my-path)))

(define (sol-p1 lst)
  (for/sum ([i (in-list lst)]
            [j (in-list (cdr lst))])
    (if (< i j) 1 0)))

(define sole-p1 (sol-p1 my-input))
;; 1581 -> OK

;; Improve on solution 1, using method from the CL version
(define (sol-p2 lst)
  (for/sum ([i (in-list lst)]
            [j (in-list (cdr lst))]
            [k (in-list (cddr lst))]
            [l (in-list (cdddr lst))])
    (if (< (+ i j k) (+ j k l)) 1 0)))

(define sole-p2 (sol-p1 my-input))
;; 1618 -> OK

