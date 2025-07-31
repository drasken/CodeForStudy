(defpackage :my-test
  (:use :cl :uiop)
  (:export #:my-main))

(in-package :my-test)
 
(defun my-main (x)
  (format t "My main print is: ~a " x))
