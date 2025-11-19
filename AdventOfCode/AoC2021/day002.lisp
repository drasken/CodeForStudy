;; (require :uiop)
;; (require :str)

;; (defparameter *input-file*  "./input002.txt")
;; (defparameter *h-dist* 0)
;; (defparameter *depth-dist* 0)

;; (defun read-my-input ()
;;   "My input read"
;;   (uiop:read-file-lines *input-file*)) 

;; (defun help-add (pair)
;;   (parse-integer (second pair)))

;; (defun sol-part1 (lis)
;;   (let ((tem-list
;;     (let ((my-input  (mapcar (lambda (line)
;; 	   (uiop:split-string line :separator " "))
;; 	   lis)))
;;       my-input))
;;   (loop for x in tem-list
;; 	do( cond
;; 	    ((string= (car x) "forward")
;; 	    (setf *h-dist* (+ *h-dist* (help-add x))))
;; 	    ((string= (car x) "up")
;; 	    (setf *depth-dist* (+ *depth-dist* (help-add x))))
;; 	    ((string= (car x) "down")
;; 	    (setf *depth-dist* (- *depth-dist* (help-add x)))))))



(require :uiop)
(require :str)

(defparameter *input-file* "./input002.txt")
(defparameter *h-dist* 0)
(defparameter *depth-dist* 0)

(defun read-my-input ()
  "My input read"
  (uiop:read-file-lines *input-file*))

(defun help-add (pair)
  (parse-integer (second pair)))

(defun parse-lis (lis)
  (let ((tem-list
	  (mapcar (lambda (line)
		    (uiop:split-string line :separator " "))
		  lis)))
    tem-list))

(defun sol-part1 (lis)
  (loop for x in lis
	do (cond ((string= "forward" (car x)) (setf *h-dist* (+ *h-dist* (help-add x))))
		 ((string= "up" (car x)) (setf *depth-dist* (- *depth-dist* (help-add x))))
		 (t (setf *depth-dist* (+ *depth-dist* (help-add x))))))
    (* *depth-dist* *h-dist*))

;; Answer01: -2039912 -> Wrong
;; Answer02: 2039912 -> OK! + and - inverted in the loop macro


(defparameter *aim* 0)

(defun sol-part2 (lis)
  (loop for x in lis
	do (cond ((string= "down" (car x)) (setf *aim* (+ *aim* (help-add x))))
		 ((string= "up" (car x)) (setf *aim* (- *aim* (help-add x))))
		 (t (progn
		      (setf *depth-dist* (+ *depth-dist* (* *aim* (help-add x))))
		      (setf *h-dist* (+ *h-dist* (help-add x)))))))
    (* *depth-dist* *h-dist*))

;;Answer 1942068080 -> OK!! slightly modified first function

