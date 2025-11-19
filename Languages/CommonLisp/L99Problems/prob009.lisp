"Solutions fom 009 to 012 for L99P"



;; (defun problem-009 (lst)
;;   "P009: Pack consecutive duplicates of list elements into sublists."
;;   (cond ()
;;   ))

(defparameter test009 ''(a a a a b c c a a d e e e e))
;; Solution ((A A A A) (B) (C C) (A A) (D) (E E E E))))



(defun test-fun (num)
  (defun aux-rec (n res)
    (cond ((zerop n) res)
	  (t (aux-rec (- n 1) (+ res n)))))
  (aux-rec num 0))


(test-fun 5)

