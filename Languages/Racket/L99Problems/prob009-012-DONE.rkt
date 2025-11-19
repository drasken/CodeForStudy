;;;; File for test from 09 to 12


;; Problem 009
;; Using an ausiliary function whit a temp list and acc list
(define (my-pack lst)

  (when (empty? lst) '())
  (define (help-my-pack l acc temp)
    (cond [(empty? l) (append acc (list temp))]
	  [(or (empty? temp) (equal? (car l) (car temp)))
	   (help-my-pack (cdr l) acc (cons (car l) temp))]
	  [else (help-my-pack (cdr l) (append acc (list temp)) (list (car l)))]))
  (help-my-pack lst (list) (list)))

;; Test -> OK
;; (my-pack '(a a a a b c c a a d e e e))
;; Expected ((A A A)(B)(C C)(A A)(D)(E E E))


;; Problem 010
(define (my-len-encode lst)
  (let ([res (my-pack lst)])
    (map (lambda (l)
	   (list (length l) (car l)))
	 res)))

;; Test -> OK
;; (my-len-encode '(a a a a b c c a a d e e e))



;; Problem 011
(define (my-len-encode-bis lst)
  (let ([res (my-len-encode lst)])
    (for/list ([el res])
      (if (= (car el) 1)
	  (cadr el)
	  el))))
	  
;; Test -> OK
;; (my-len-encode-bis '(a a a a b c c a a d e e e))


;; Problem 012
(define (my-decode lst)
  (for/list ([el lst])
    (make-list (car el)(cadr el))))

;; Test -> OK
;; (define my-test-to-decode (my-len-encode '(a a a a b c c a a d e e e)))
;; (my-decode my-test-to-decode)
