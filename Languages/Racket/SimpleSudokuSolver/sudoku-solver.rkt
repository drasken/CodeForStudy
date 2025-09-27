;;;; Trying to implement it in Raket

;; Function to create an empty board
(define (make-empty-board n)
  (for/vector ([i (in-range n)])
    (for/vector ([j (in-range n)])
      0 )))

;; Test if is created
;; (define test-board (make-empty-board 9))


