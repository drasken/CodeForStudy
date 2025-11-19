;;;; Use as day template

#lang racket

;;;; READ INPUT
;;File path
(define my-path "./test001.txt")

;; Read it
(define (read-my-input path)
    (file->lines path))

;; My input
(define my-input (read-my-input my-path))


