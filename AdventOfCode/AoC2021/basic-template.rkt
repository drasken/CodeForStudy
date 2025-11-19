;;;; Use as day template

#lang racket

;;;; READ INPUT
;;File path
(define *my-path* "file-path")

;; Read it
(define (read-my-input path)
  (file->lines path))

;; My input
(define *my-input* (read-myinput *my-path*))



