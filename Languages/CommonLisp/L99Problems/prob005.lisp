;;;; Problem from 05 to 08 in CommonLisp

;; Problem 05
(defun my-reverse (lst &optional acc)
  "Recursive version, not tail optimized"
  (cond ((null lst) acc)
	(t (my-reverse (cdr lst) (cons (car lst) acc)))))


(defun my-rev-iter (lst)
  (let ((res '())) (loop for x in lst
			 do (setf res (cons x res)))
    res))


;; ;; Test

;; (my-reverse '(1 2 4 6 7))
;; (my-reverse '(1 1 3 1 1))
;; (my-reverse '(1))
;; (my-reverse '()))

;; (my-rev-iter '(1 2 4 6 7))
;; (my-rev-iter '(1 1 3 1 1))
;; (my-rev-iter '(1))
;; (my-rev-iter '()))


;; Problem 06
(defun my-pal (lst)
  "First naive and trivial solution with reverse"
  (equalp lst (reverse lst)))


;; ;; Test
;; (my-pal '(1 2 4 6 7))
;; (my-pal '(11 11 4 11 11))
;; (my-pal '())


;; Problem 007
;; TODO: flatten a list of nested lists



;; TODO
;; Problem 008
;; Eliminate onsecutive dulicate in a list.
;; Mantain order of elements if possible
(defun my-compress (lst)
  (if (null lst)'()
      (reverse (help-acc lst '()))))

(defun help-acc (l res)
  ;; DELETE
  ;; Pseudocode:
  ;; if l empty -> res
  ;; else: if car res == car l recursion cdr l
  ;; else else recursion push new element
  (if (null l) res
      (if (equal (car l) (car res))
	  (help-acc (cdr l) res)
	  (progn (push (car l) res)
		 (help-acc (cdr l) res)))))))




;; (defun help-comp (lis acc)
;;   ((lambda (l1 l2) (when (not (equal (last l1) (car l2))) (push (car l1) l2)))
;;    lis acc)
;;   (cond ((null (cdr lis)) acc)
;; 	(t (help-comp (cdr lis) acc))))
	  
;; Test

(my-compress '(a a a a b b a e e e b b b a g r j d a a))

	 
  


