;;;; Use as day template

#lang racket

;;;; READ INPUT
;;File path
(define *my-path* "test003.txt")

;; Read it
(define (read-my-input path)
  (file->lines path))

;; My input
(define *my-input* (read-my-input *my-path*))

;; let's transpose the matrix
(define (transpose-matrix matrix)
  (for/list ([i (in-range (string-length (car matrix)))])
    (apply string
    (for/list ([j (in-range (length matrix))])
      (string-ref (list-ref matrix j) i)))))

;; Now use the transpose matrix to get the desired output
;; mub: most used bit
;; (define (find-mub lst)
;;   (
  



