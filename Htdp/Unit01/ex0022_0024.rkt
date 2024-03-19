;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0022_0024) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;Exercise 22. Use DrRacket’s stepper on this program fragment:

(define (distance-to-origin x y)
  (sqrt (+ (sqr x) (sqr y))))

(distance-to-origin 3 4)

;Exercise 23. The first 1String in "hello world" is "h". How does the
;following function compute this result?

(define (string-first s)
  (substring s 0 1))

(string-first "Hello world"); print "H"

;Exercise 24. Here is the definition of ==>:

    (define (==> x y)
      (or (not x) y))

;Use the stepper to determine the value of (==> #true #false). 