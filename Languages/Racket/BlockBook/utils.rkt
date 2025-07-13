#lang racket

(require racket/serialize)

(provide true-for-all? struct->file file->struct)

(define (true-for-all? pred list)
  (cond
   [(empty? list) #t]
   [(pred (car list)) (true-for-all? pred (cdr list))]
   [else #f]))


(define (struct->file object file)
  (let ([out (open-output-file file #:exists 'replace)])
    (write (serialize object) out)
    (close-output-port out)))


(define (file->struct file)
  (letrec ([in (open-input-file file)]
	   [result (read in)])
    (close-input-port in)
    (deserialize result)))
