;;;; Simple write and read from file in Racket
#lang racket
(require racket/file)

(define (test-write path)
  (call-with-output-file path
    (lambda (x)
      (write 'test x))
    #:exists 'replace))

(test-write "./test-to-delete.txt")

(define (test-read path)
  (file->lines path))

(define test (test-read "./input-file.txt"))  ;; "~/GitRepo/CodeForStudy/Languages/Racket/SecScript//input-file.txt"))
