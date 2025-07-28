;;;; find if closing brackets are matching

(define open-char '(#\( #\[ #\{))
(define close-char-map (hash #\] #\[ #\} #\{ #\) #\())


(define (my-match? s)
  (define (my-helper st acc)
    (cond [(empty? st) acc] ; Comsumed all input list
	  [(member (car st) open-char) ; Consuming an open bracket
	   (my-helper (cdr st) (cons (car st) acc))]
	  [(and (not (empty? acc)) (char=? (hash-ref close-char-map (car st)) (car acc)))
	   (my-helper (cdr st) (cdr acc))]
	  [else #f]))
  (empty? (my-helper (string->list s) '())))

;; Test -> OK
(my-match? "]") ; "()[]{")
