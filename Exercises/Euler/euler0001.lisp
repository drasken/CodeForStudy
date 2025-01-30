;;;; First attempt with CL

;;;Using loop
(defun ex001 (limit)
  (loop for x from 1 below limit
	when  (or (= 0 (mod x 3)) (= 0 (mod x 5)))
	  sum x))


;;;Using do

(defun ex001B (limit)
  (do ((x 0 (1+ x))
       (sum 0))
      ((= x limit) sum)
    (if (or (= 0 (mod x 3)) (= 0 (mod x 5)))
	(setf sum (+ sum x)))))
    
