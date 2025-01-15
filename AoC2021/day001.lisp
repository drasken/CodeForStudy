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

; First Part Solution: 1581 --> OK!!
