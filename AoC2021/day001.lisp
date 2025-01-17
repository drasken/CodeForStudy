;;(in-package #:AoC2021)

(require :uiop)

(defparameter *input-file* "./input001.txt")
(defparameter *input-lines* (uiop:read-file-lines *input-file*))

(defun read-sonar()
  (mapcar #'parse-integer
	  (uiop:read-file-lines *input-file*)))

(defun sol-part-1 (lis)
  (let ((acc 0))
  (loop for x from 0 below (1- (length lis))
			do (if (< (nth x lis) (nth (1+ x) lis))
			    (setf acc (1+ acc))))
    acc))

;;found online

(defun increasing-pairs (nums)
  (loop for (a b) on nums while b count (< a b))) ;;OK

;; First Part Solution: 1581 --> OK!!

(defun sol-part-2 (lis)
  (sol-part-1
    (loop for x from 1 to (- (length lis) 2)
	  collect (reduce #'+ (list (nth (1- x) lis)
				(nth x lis)
				(nth (1+ x) lis))))))

;;found online same as for part 1, same way using loop

(defun increasing-tri (nums)
  (loop for (a b c d) on nums while d count (< (+ a b c) (+ b c d))))

;; Second Part Solution: 1618 -> OK!!
    

