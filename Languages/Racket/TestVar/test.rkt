#lang racket

(require "test-provide.rkt")

(displayln "ciao amore")
(displayln "ciao")

(define (my-require)
  (my-provide-test))

(my-require)



