;;;; Problems [13, 16] in Racket

;; Problem 013 -> it's a repetition of the previous 2 problems


;; Problem 014
;; Duplicate elements of a list

(define (my-dupli lst)
  (define (help-rec l acc)
    (cond [(empty? l) acc]
	  [else (help-rec (cdr l) (cons (car l) (cons (car l) acc)))]))
  (reverse (help-rec lst '())))

;; Test -> OK
;; (my-dupli '(a b c c d))
;; (my-dupli '(1 3 5 5 6 6 7))


;; Problem 015
;; Replicate element of a list given number of times
(define (my-dupli-n lst num)
  (let ([res '()])
    (for ([i lst])
      (set! res (append res (build-list num (lambda (x) i)))))
    res))

;; Test -> OK
;; (my-dupli-n '(a b c) 3)
;; (my-dupli-n (in-range 10)  2)


;; Problem 016
;; Drop every nth element from list
(define (my-drop lst num-filter)
  (define (helper-rec l acc counter)
    (cond [(empty? l) acc]
	  [(= (modulo counter num-filter) 0)
	   (helper-rec (cdr l) acc (add1 counter))]
	  [else (helper-rec (cdr l) (cons (car l) acc) (add1 counter))]))
  (reverse (helper-rec lst '() 1)))


;; Test -> OK
;; (my-drop '(a b c d e f g h i l) 3)
