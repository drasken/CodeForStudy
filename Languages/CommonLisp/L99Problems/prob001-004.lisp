(defvar mylist1 '(1 6 8 4 22 55 67 46 158 351))
(defvar mylist2 '(6 351))
(defvar mylist3 '(46))
(defvar mylist4 '())

;; Problem 001

(defun my-last (lst)
  "Find last element in a list"
  (cond ((null lst) nil)
	((null (cdr lst)) lst)
	(t (my-last (cdr lst)))))

;; test
(my-last '(3 5 6 7))
(my-last '())
(my-last '(37))


;; Problem 002
(defun my-but-last (lst)
  "Find last two element in a list. If list elements <= 2 -> nil."
  (cond ((null lst) nil)
	((null (cdr lst)) nil)
	((null (cddr lst)) lst)
	(t (my-but-last (cdr lst)))))


;;test
(my-but-last '(3 5 6 7)) 
(my-but-last '())
(my-but-last '(37))


;; Problem 003
;; using loop
(defun my-find-el (lst pos)
  (loop for el in lst
	for n below (length lst)
		  when  (= n pos)
		      return el))

;; Test
(my-find-el '(3 5 6 7 55 7 1 874 55) 3) 
(my-find-el '() 5)
(my-find-el '(37) 0)

(defun my-find-rec (lst pos)
  (cond ((null lst) nil)
	((= 0 pos) (car lst))
	(t (my-find-rec (cdr lst) (1- pos))))))
	  
;; test
(my-find-rec '(3 5 6 7 55 7 1 874 55) 3) 
(my-find-rec '() 5)
(my-find-rec '(37) 0)


;; Problem 004
;; Find the number of elements in a list without built-in functions
;; (defun my-loop-num (lst)
;; (loop for x in lst count x))
(defun my-loop-num (lst)
 (loop for x in lst count x))

;; test -> OK
(my-loop-num mylist1)  ;; -> 10
(my-loop-num mylist2)  ;; -> 2
(my-loop-num mylist3)  ;; -> 1
(my-loop-num mylist4)  ;; -> nil

(defun my-rec-len (lst)
  (labels ((my-rec-helper (l acc)
	   (cond ((null l) nil)
		 ((null (cdr l)) acc)
		 (t (my-rec-helper (cdr l) (1+ acc))))))
  (my-rec-helper lst 1)))

;; test -> OK
(my-rec-len mylist1)  ;; -> 10
(my-rec-len mylist2)  ;; -> 2
(my-rec-len mylist3)  ;; -> 1
(my-rec-len mylist4)  ;; -> nil

