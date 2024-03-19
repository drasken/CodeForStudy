;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0025) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;Exercise 25. Take a look at this attempt to solve exercise 17:
;
;    (define (image-classify img)
;      (cond
;        [(>= (image-height img) (image-width img)) "tall"]
;        [(= (image-height img) (image-width img)) "square"]
;        [(<= (image-height img) (image-width img)) "wide"]))

;Fix: last cond can be evaluated directly as else

(define (image-classify img)
      (cond
        [(>= (image-height img) (image-width img)) "tall"]
        [(= (image-height img) (image-width img)) "square"]
        [else "wide"]))