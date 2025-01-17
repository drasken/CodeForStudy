;; To start

(require :uiop)
(require :str)

(defparameter *input-file* "./input003.txt")

(defun read-my-input()
  (mapcar #'parse-integer
	  (uiop:read-file-lines *input-file*)))

