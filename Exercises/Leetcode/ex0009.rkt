;; Trying this in Racket after Python

#lang racket

(define (is-pal num)
  (if (< num 0) #f 
      (string-join (reverse (string-split (number->string num)))))) 
      ;; (= num
      ;; 	 (string->number
      ;; 	  (string-join (reverse (string-split (number->string num))))))))


(define (test-fun num)
					;  (string-join (reverse
  (string-split
   (number->string num)))


(define (bho s)
  (for ([x s])
    (printf "\n ~a \n" x)))
      

