#lang racket/gui

(define frame
  (new frame%
       [label "I'm a GUI!"]
       [width 300]
       [height 200]))

(send frame show #t)
