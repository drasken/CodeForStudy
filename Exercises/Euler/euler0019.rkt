#lang racket

;;;; Trying to solve problem 0019 from Project Euler

;; The problem state this:
;; Start date: 1 Jenuary 1900 Sunday
;; Final date: 31 December 2000 
;; Find the number or times a month start with a sunday
;; First try;
;; Using this algorithm https://it.wikipedia.org/wiki/Calendario_perpetuo

;; Utility function for leap years
(define (is-leap? num)
  (cond [(and (zero? (remainder num 100)) (not (zero? (remainder num 400)))) #f]
	[(zero? (remainder num 4)) #t]
	[else #f]))


(define (aux-get-day month-days old-val)
  (remainder (+ old-val month-days) 7))


;; Try 03 using Dynamic programming recursively

; Create the array needed to compute 
(define my-year1 1901)
(define my-year2 1902)
(define my-years (* 12 (add1 (- my-year2 my-year1))))
(define my-calendar (for/vector ([i (in-range my-years)]) -1))
(vector-set! my-calendar 0 1)

(define (set-calendar calendar start-year end-year) ; end year included
  (for ([i (in-range 1 (vector-length calendar))]
	[year start-year])
    ;[(> (+ start-year (quotient i 12)) end-year) (void)]
    (cond [(member (remainder i 12) '(4 6 9 11)) 
	   (vector-set! calendar i (aux-get-day 30 (vector-ref calendar (- i 1))))] ; TODO 31 days
	  ; [(= (remainder i 12) 11) ] ; TODO: december
	  [(member (remainder i 12) '(0 1 3 5 7 8 10))
	   (vector-set! calendar i (aux-get-day 31 (vector-ref calendar (- i 1))))] ; TODO 30 days ex. feb
	  [(is-leap? (+ (quotient i 12) start-year))
	   (vector-set! calendar i (aux-get-day 29 (vector-ref calendar (- i 1))))] ; leap year
	  [else (vector-set! calendar i (aux-get-day 28 (vector-ref calendar (- i 1))))]))) ; normal febraury

; Calc calendar
(set-calendar my-calendar my-year1 my-year2)



(define (my-solution calendar)
  (for/sum ([i calendar])
    (if (= i 0) 1 0)))

(define my-result (my-solution my-calendar)) ; use this var to count sundays


;;;; Code from thread ProjectEuler
;; CommonLisp
;; (defun day-of-week-for-date (day month year)
;;   (nth 6 (multiple-value-list
;;           (decode-universal-time
;;            (encode-universal-time 0 0 8 day month year)))))

;; (defun sundayp (day month year)
;;   (= (day-of-week-for-date day month year) 6))

;; (defun euler19 ()
;;   (loop for year from 1901 to 2000
;;         sum (loop for month from 1 to 12
;;                   if (sundayp 1 month year)
;;                      count month)))

;; Converted in Racket by ChatGPT
;; #lang racket
;; (require srfi/19) ; for date/time conversion utilities

;; (define (day-of-week-for-date day month year)
;; ;; Racket's date-day-of-week returns 0 = Sunday .. 6 = Saturday
;; (let* ([secs (date->seconds (make-date year month day 8 0 0 0 #f))] ; 08:00 like CL code
;; [dt (seconds->date secs)])
;; (date-day-of-week dt)))

;; (define (sunday? day month year)
;; (= (day-of-week-for-date day month year) 0)) ; 0 == Sunday in Racket

;; (define (euler19)
;; (for/sum ([year (in-range 1901 2001)]) ; 1901..2000 inclusive
;; (for/sum ([month (in-range 1 13)])   ; 1..12
;; (if (sunday? 1 month year) 1 0))))

;; ;; Example: compute the Project Euler answer
;; (euler19) ; => 171

;; Notes:

;; srfi/19 date functions use date-day-of-week with 0 = Sunday.
;; I created the date at 08:00 to match the Common Lisp code's use of 8 for the hour.
;; euler19 uses for/sum to sum counts of months whose 1st is a Sunday.


;; ;; Try 02 with list

;; ;; Algo: add to alist of number modulo 7 depending on
;; ;; the previous added value and the step counter for moths
;; ;; using a second counter for year and lep year count

;; (define (aux-get-day month-days old-val)
;;   (remainder (+ old-val month-days) 7))

;; ;; (aux-get-day 31 0) 

;; ;; create a list with index and populate it until year is surpassed
;; (define (my-calendar start-year end-year)
;;   (define (helper-rec year1 year2 month acc) ; month represent last month
;;     ;; (displayln month)
;;     ;; (displayln acc)
;;     (cond [(> year1 year2) acc]
;; 	  [(member (remainder month 12) '(0 2 4 6 7 9)) ; pick month in this list
;; 	   (helper-rec year1 year2 (add1 month) (cons (aux-get-day 31 (car acc)) acc))]
;; 	  [(= (remainder month 12) 11)
;; 	   (helper-rec (add1 year1) year2 (add1 month) (cons (aux-get-day 31 (car acc)) acc))]
;; 	  [(member (remainder month 12) '(3 5 8 10))
;; 	   (helper-rec year1 year2 (add1 month) (cons (aux-get-day 30 (car acc)) acc))]
;; 	  [(is-leap? year1)
;; 	   (helper-rec year1 year2 (add1 month) (cons (aux-get-day 29 (car acc)) acc))]
;; 	  [else (helper-rec year1 year2 (add1 month) (cons (aux-get-day 28 (car acc)) acc))]))
;;   (helper-rec start-year end-year 0 '(0)))

;; ;; (my-calendar 1901 1901)
;;   ;; (define (helper-rec year1 year2 month last-element acc)
;;   ;;   (cond [(> year1 year2) acc]
;;   ;; 	  [(member (remainder month 12) '(1 3 5 7 8 10)) ; pick month
;;   ;; 	   (helper-rec year1 year2 (add1 month) (aux-get-day 31 element) (cons element acc))]
;;   ;; 	  [(= 12 (remainder month 12))
;;   ;; 	   (helper-rec (add1 year1) year2 (add1 month) (aux-get-day 31 element) (cons element acc))]
;;   ;; 	  [(member (remainder month 12) '(4 6 9 11))
;;   ;; 	   (helper-rec year1 year2 (add1 month) (aux-get-day 30 element) (cons element acc))]
;;   ;; 	  [(is-leap? year1)
;;   ;; 	   (helper-rec year1 year2 (add1 month) (aux-get-day 29 element) (cons element acc))]
;;   ;; 	  [else (helper-rec year1 year2 (add1 month) (aux-get-day 28 element) (cons element acc))]))
;;   ;; (helper-rec start-year end-year 1 0 '()))

;; (define res-list (my-calendar 1900 2000))
;; ;res-list
;; (for/sum ([i res-list])
;;   (if (= i 0) 1 0))
;;(define res-list (filter (lambda (x) (= x 0)) (cdr (my-calendar 1900 1900))))  ; list of all my calculated values

;; res-list
;; Here get the desired result, count all the sundays -> 0 values
;; (for/sum ([i res-list])
;;   (if (= i 0) 1 0))


;; ;; Try 001: using matrix and checking with offset modulo 7

;; (define (init-matrix years elements)
;;   (lambda (x)
;;     (for/vector ([i (in-range x)])
;;       (for/vector ([j (in-range elements)])
;; 	-1))))

;; (define (init-calendar years)
;;   (let ([my-calendar (init-matrix years 13)])
;;     (my-calendar years)))


;; (define (set-calendar-init-state calendar year)
;;   (let ([val year]
;; 	[first #t])
;;     (for ([i calendar])
;;       (vector-set! i 0 val)
;;       (set! val (add1 val)))
;;     (vector-set! (vector-ref calendar 0) 1 0))) ; hardcoded firt day is a sunday

;; (define (set-calendar-first-days calendar)
;;   (for* ([i (in-range (vector-length calendar))]
;; 	 [j (in-range 1 13)] ; iterate on all matrix
;; 	 #:unless (and (zero? i)(zero? j)))
;;     (vector-m
;;     ))
;; ;    (printf  "test ~a ~a \t" i j)))
    
;; ;; TODO finish to implement calculation based on previous index
;; ;; add auxiliary function

;; ;; Calc day value starting from Sunday as zero
;; (define (calculate-day array-year index-month)
;;   (define my-calc (lambda (x) (remainder x 7)))
;;   (let ([year (vector-ref array-year 0)]
;; 	[day (vector-ref array-year index-month)])
;;     (cond [(member day '(1 3 5 7 8 10 12)) (my-calc 31)]
;; 	  [(member day '(4 6 9 11)) (my-calc 30)]
;; 	  [(is-leap? year) (my-calc 29)]
;; 	  [else (my-calc 28)])))



;; ;; This will be maybe my main funciton to get problem solution
;; (define (main year1 year2)
;;   (let ([calendar (init-calendar (add1 (- year2 year1)))])
;;     (set-calendar-init-state calendar year1)
;;     calendar))


;; (main 1900 1902)
