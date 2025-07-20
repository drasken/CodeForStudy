;;;; Problem 001

(defun my-last (lst)
  "Find last element in a list"
  (cond ((null lst) nil)
	((null (cdr lst)) lst)
	(t (my-last (cdr lst)))))

;; test
(my-last '(3 5 6 7))
(my-last '())
(my-last '(37))


(defun my-but-last (lst)
  "Find last two element in a list"
  (cond ((null lst) nil)
	((null (cdr lst)) nil)
	((null (cddr lst)) lst)
	(t (my-last (cdr lst)))))


;;test
(my-last '(3 5 6 7))
(my-last '())
(my-last '(37))

  
