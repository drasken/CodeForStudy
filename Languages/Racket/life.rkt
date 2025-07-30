#lang racket

;;;; Here is the planning on this project
;; - Inite board
;; - helper function to init some cells
;; - maybe a wrapper to randomize all board state
;; - mini function to calc next cell state
;; - function to calc all next board state


;;; Constants

(define BOARD-WIDTH 4)
(define BOARD-HEIGHT 4)
(define ALIVE "O")
(define DEAD ".")
(define RATIO-INIT-CELLS 0.75)

;;;; Functions to init board

;; First attempt, not good and return a single vector -> Not good		     
;; (define (init-py)
;;   (let ([res (make-vector 0 0)])
;;     (for ([i (in-range BOARD-HEIGHT)])
;;       (set! res
;; 	    (vector-append res (make-vector BOARD-WIDTH 0))))
;;     res))

;; (define my-board-3 (init-py))
	      		       
;; ;; Second version, this one works
;; ;; Not working correctly, multiple vectors same pointers so can't modify
;; ;; modification in one is on all vectors
;; (define (init-board)
;;   (define (make-row)
;;     (make-vector BOARD-WIDTH 0))
;;   (let ([matrix (make-vector BOARD-HEIGHT (make-row))])
;;     matrix))

;; (define my-board (init-board))


;; Third version more Racky
(define (init-my-board height width)
  (for/vector ([y (in-range height)])
    (for/vector ([x (in-range width)])
      0)))


;; It works
(define my-board-def (init-my-board BOARD-HEIGHT BOARD-WIDTH))
;; my-board

;;; TODO: finish recursive implementation
;; (define (init-board2)
;;   (define (init-rec vec num)
;;     (cond [(zero? num) vec]
;; 	  [else (init-rec () (- num 1))])
;;     )
;;   (init-rec (make-vector 00) BOARD-HEIGHT))

;; (define matrix (init-board))


;;;; Helper access function to get and to set elements in a board

(define (get-matrix-el matrix y-index x-index)
  (vector-ref (vector-ref matrix y-index) x-index))

(define (set-matrix-el matrix y-index x-index new-el)
  (vector-set! (vector-ref matrix y-index) x-index new-el))

;; test
;; (set-matrix-el my-board 2 3 66)
;; (set-matrix-el my-board 3 3 66)
;; (display my-board)
;; (newline)

;;;; Third part

;; Here function to randomize board initial state
(define (randomize-board board)
  (for ([y (in-range BOARD-HEIGHT)])
    (for ([x (in-range BOARD-WIDTH)])
      (when (> (random) RATIO-INIT-CELLS)
	(set-matrix-el board y x 1)))))

;; Test -> it work
;; (randomize-board my-board)
;; (display my-board)


;;;; Fourth part, function to calc board next state

(define (normalize-y-index index)
  (modulo (+ index BOARD-HEIGHT) BOARD-HEIGHT))

(define (normalize-x-index index)
  (modulo (+ index BOARD-WIDTH) BOARD-HEIGHT))


;;;; TODO: it sum but return a wring value
;; Count cell neighbours
;; (define (count-neig board y-index x-index)
;;   ;; Input the board and the indexes of cell of interest
;;   (for/sum ([res
;;     (for/vector ([y (in-range (- y-index 1) (+ 2 y-index))]
;; 		 [x (in-range (- x-index 1) (+ 2 x-index))])
;;       (get-matrix-el board
;; 		     (normalize-y-index y)
;; 		     (normalize-x-index x)))])
;;     res))



