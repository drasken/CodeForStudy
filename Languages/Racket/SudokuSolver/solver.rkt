;;;; Solver inspired by Norvig's solution

;; Norvig's definitions:
;; Peers: all cells that share a unit
;; Unit: all cells on the same square OR column OR box
;; nil: If a puzzle has no solution, we represent that with nil
;; Picture: for input and output, a string is used to describe the grid (details described below).

;; This is using the Python solution

#lang racket

(define Digit "")  ; ex. "1"
(define digits "123456789")
(define DigitSet "")  ; Ex "123"
(define rows "ABCDEFGHI")
(define cols "")  ; digits
(define Square "")  ; Ex "A9"
(define squares '())  ; (cross rows cols)
(define Grid (make-hash))  ; Dict[Square, DigitSet] # E.g. {'A9': '123', ...}
;; Python code:
;; all_boxes = [cross(rs, cs)  for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
;; all-boxes defined later, under cross function
;; Unit: a unit is a row, column, or box; each unit is a tuple of 9 squares.
;; all_units is a list of all 27 units.
;; all_units = [cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + all_boxes
;; units is a dict such that units[s] is a tuple of the 3 units that square s is a part of.
;; NOTE: so I can use it to validate input on a square
;; Peers: the squares that share a unit are called peers.
;; peers is a dict such that peers[s] is a set of 20 squares that are in some unit with s.



;; Utility function to use in cross function
(define (util-str-app s1 s2 n1 n2)
  (list->string (list (string-ref s1 n1) (string-ref s2 n2))))

;; TODO: trying in a more Schemish and recursive way
;; (define (cross a b)
;;   (define (rec-cross a b ra rb res))
;;   (cond [(and (< ra 0) (< rb 0)) res]
;; 	[(< ra 0) (rec-cross (string-length a) (- rb 1) res)]
;;         [else (rec-cross a b (- ra 1) (- rb 1) (cons (util-str-app a b ra rb ) res))])
;;   (rec-cross a b (string-length a) (string-length b) '()))

;; DEPRECATED
;; Racketish style using for and mutation
;; (define (cross s1 s2)
;;   (let ([res '()])
;;     (for ([i (in-range (string-length s1))])
;;       (for ([j (in-range (string-length s2))])
;;         (set! res (cons (util-str-app s1 s2 i j) res))))
;;     res))


(define (cross2 s1 s2)
  (for*/list ([i (in-string s1)]
              [j (in-string s2)])
    (apply string (list i j))))

;; OLD: implementation is not good anymore
;; (define all-boxes  (foldl append '()
;;                           (for*/list
;;                               ([i (list "ABC" "DEF" "GHI")]
;;                                [j (list "123" "456" "789")])
;;                             (cross i j))))


(define all-boxes (cross2 rows digits))
(define all-units (

;(define all-units ())
  
