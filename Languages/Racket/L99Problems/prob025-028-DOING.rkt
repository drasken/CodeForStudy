#lang racket

;;;; Problems frmo 025 to 028 L99P


;; Problem 025 random permutation of list elements
(define (my-rnd-permutation lst)
  (for/list ([ind (shuffle (range (length lst)))])
    (list-ref lst ind)))

;; Test
;; (my-rnd-permutation '(a b c d e f g h))


;; Problem 026
;; All combinations calculated from a list of elements
;; according to a binomial coefficient calculation
;; Pseudocode recursion:
;; Base case: using counter, IF counter 0 append temp list to acc list
;; Recursive case: if Index < (length list) recursive with index
;; Return case: diminish index and extends temp list

;; TODO: try better implementation, maybe rucksack?

;; Test -> OK
;; (my-combination '(1 2 3 4) 2)


;; Problem 027 Grouping elements of a set into disjoint subset
;; A - How many ways can a group of 9 people work in 3 disjoint subgroups of 2,3 and 4 people?
;; B - Generalize function at point A so that a list of group size can be passed as input


;; Problem 028 Sorting a list of list by length
;; A - Elements of a list are lists, order them by length
;; B - This time sort by the length frequency. Rare first more common last


