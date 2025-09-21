#! /usr/bin/env racket

#lang racket


;; Testing a simple word counter script in Racket


(define (main args)
  (if (= (vector-length args) 2)  ; Use vector-length instead of length
      (let ([input-value (vector-ref args 1)])  ; Use vector-ref instead of second
        (displayln (string-append "You entered: " input-value))
        (displayln (string-append "Processing input: " 
                                  (string-upcase input-value))))
      (displayln "Please provide exactly one argument when running the script")))

(main (current-command-line-arguments))
