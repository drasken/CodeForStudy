#lang racket


;;;; READ INPUT
;;File path
(define my-path "./input002.txt")

(define my-input (map string-split (file->lines my-path)))

  
(define (sol-p1 in)
  ;; the value to multiply at the end
  (let loop ([lst in]
             [hval 0]
             [dval 0])
    (cond [(null? lst) (* hval dval)]
          [(string=? (caar lst) "up") (loop (cdr lst) hval (- dval (string->number (cadar lst))))]
          [(string=? (caar lst) "down") (loop (cdr lst) hval (+ dval (string->number(cadar lst))))]
          [else (loop (cdr lst) (+ hval (string->number (cadar lst))) dval)])))

(define res-p1 (sol-p1 my-input))
;; 2039912 -> OK

  
(define (sol-p2 in)
  ;; the value to multiply at the end
  (let loop ([lst in]
             [aim 0]
             [dval 0]
             [hval 0])
    (cond [(null? lst) (* dval hval)]
          [(string=? (caar lst) "up")
           (loop (cdr lst) (- aim (string->number (cadar lst))) dval hval)]
          [(string=? (caar lst) "down")
           (loop (cdr lst) (+ aim (string->number(cadar lst))) dval hval)]
          [else (loop (cdr lst)
                      aim
                      (+ dval (* aim (string->number(cadar lst))))
                      (+ hval (string->number (cadar lst))))])))

(define res-p2 (sol-p2 my-input))
;; 1942068080 -> OK
