;;;; Problem 0021
;; Merge 2 sorted lists

;; (define (helper-rec l1 l2 acc)
;;   (cond [(and (empty? l2) (empty? l1)) acc]
;; 	[(empty? l1) (append acc l2)]
;; 	[(empty? l2) (append acc l1)]
;; 	[(> (car l1) (car l2)) (helper-rec l1 (cdr l2) (append acc (list (car l2))))]
;; 	[else (helper-rec (cdr l1) l2 (append acc (list (car l1))))]))


;; (define/contract (merge-two-lists list1 list2)
;;   (-> (or/c list-node? #f) (or/c list-node? #f) (or/c list-node? #f))
;;   (cond 
;;     [(not list1) list2]
;;     [(not list2) list1]
;;     [(< (list-node-val list1) (list-node-val list2)) (list-node (list-node-val list1) (merge-two-lists (list-node-next list1) list2))]
;;     [else (list-node (list-node-val list2) (merge-two-lists (list-node-next list2) list1))]
;;   )
;;   )


;; (define (my-merge list1 list2)
;;   (helper-rec list1 list2 '()))

;; (my-merge '(1 4 6) '(1 2 5 8))



(struct list-node
  (val next) #:mutable #:transparent)

; constructor
(define (make-list-node [val 0])
  (list-node val #f))

(define (helper-rec l1 l2)
  (cond [(not l1) l2]
	[(not l2) l1]
	[(< (list-node-val l1)(list-node-val l2)) 
	 (list-node (list-node-val l1) (helper-rec (list-node-next l1) l2))]
	[else (list-node (list-node-val l2) (helper-rec (list-node-next l2) l1))]))


(define m-l-n (list-node 3 66))
