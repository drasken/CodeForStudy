#lang racket

;; 
;; (define (mult num mul)
;;   (lambda (x y) (* x y)
;;     num mul))
;; 
;; (define (double num)
;;   (let ()
;;     (mult num 2)))


(define (mult num mul)
  (lambda (x) (* x mul))) ; Create a closure that multiplies x by mul

(define (double num)
  (let ((multiplier (mult num 2))) ; Create a closure with num and 2
    (multiplier num))) ; Call the closure with num
(double 6)

(define (add-suffix str suff)
  (lambda (x) (string-append x suff)))

(define (add-devil my-str)
  (let ([devilize (add-suffix my-str " 666!")]) 
  (devilize my-str)))

(define (add-exclamation str)
  (let ([exclamation (add-suffix str "!!!")])
    (exclamation str)))

((let ([bhoo ""])
  (add-suffix bhoo " test "))
 " mio test")
 
((lambda (x y) (+ x y)) 30 12)