;;;; Here define function that can be used across different test

#lang racket

(provide get-file)  ; TODO:  parse DELATED get-test


;;Just testingg
;; (define (get-test strg)
;;   (displayln strg))

;; The path is constructed assuming the file is int the same directory
(define (my-get-file num)
  (file->lines (string-append "input" num "txt")))




