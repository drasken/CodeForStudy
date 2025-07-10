#lang racket

(require plot) ;; Used to plot returns
(plot-new-window? #t)

;; How to procede:
;; - Take a number of N time periods T-n
;; - Create a list of length N + 1
;; - The first element at time T-0 is the starting capital
;; - The function should compute the resulting value at each time T-x
;; - Let's use recursion and memoization to compare performance


;;; Global Variables
;; the time period of interest
(define periods (range 30))
(define my-rate 0.07)
(define my-sum 10000)


;; Just to test
(define (simple-interest val rate)
  (/ (round (* (+ val (* val rate)) 100)) 100))


;; Funtion to calculate compound interest
(define (calc-int val rate per)
  (map (lambda (num)
	 (/ (round (* (* (expt (add1 rate) num) val) 100)) 100))
       per))


(define my-inv (calc-int my-sum  my-rate periods)) ; Simple implementation, it works


;; Create a list of points for plotting with lines function
(define points (map (lambda (x y) (list x y)) periods my-inv))


;; test plot library
;; (plot (function sqr -2 2) #:title "Test") ;;this works

;; plot with my-inv var
(plot (lines points  #:color "red")
      #:title "Test")





;; (plot (list
;;        (lines my-inv
;; 	      #:color "yellow")
;;        (points my-inv
;; 	       #:fill-color "red")
;;       #:x-min 0 #:x-max 20 #:title "Expected return"))

