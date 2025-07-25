;;;; Problem from 05 to 08 in CommonLisp

;; Problem 05
(defun my-reverse (lst &optional acc)
  (cond ((null lst) acc)
	(t (my-reverse (cdr lst) (cons (car lst) acc)))))


;; Test
#+nil
(progn
  (my-reverse '(1 2 4 6 7))
  (my-reverse '(1 1 3 1 1))
  (my-reverse '(1))
  (my-reverse '()))

