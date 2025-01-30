;; To start

(require :uiop)
(require :str)

(defparameter *input-file* "./test003.txt")

;; Idea to solve problem:
;; first split integers str in single digit and than parse them
;; After that sum lists in parallel and collect in a lis of results
;; loop on the result list and check if num < half-length input:
;; than 0 more than 1
;; else more 1 than 0
;; use this info to calculate desird var


(defun read-my-input()
  "read the input and return a list of integers"
  ;; (mapcar #'parse-integer
  ;; 	  (uiop:read-file-lines *input-file*)))
  ;;(mapcar #'(lambda (x) (mapcar #'digit-char-p (coerce x 'list)))
  ;; (mapcar #'(lambda (x) (mapcar #'digit-char-p (coerce x 'list)))
  ;; (uiop:read-file-lines *input-file*)))
  ;;(mapcar #'(lambda (x) (coerce x 'list))
  (uiop:read-file-lines *input-file*))
  
(defun read-my-input()
  "read the input and return a list of integers"
   (mapcar #'(lambda (x) (mapcar #'digit-char-p (coerce x 'list)))
	   (uiop:read-file-lines *input-file*)))

(defun proviamolo (test-lis)
  (loop for l in test-lis

(defun count-bits (lis)
  "return a list of ????"
  (mapcar #'+ lis))


(defun sum-corresponding-elements (list-of-lists)
  "Sum corresponding elements of each list in list-of-lists."
  (apply #'mapcar #'reduce #'+ list-of-lists))

(defun test-loop (roba)
  (loop  for x in roba
	 do (loop for y in x
		  collect
    
    ;; (do* ((res '() (append res (round)) )
    ;; 	  (i 10) (* 10)
    ;; 	  (temp num (/ i)))
    ;; 	 (zerop num)
    ;;   ))



