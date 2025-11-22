;; minimum skeleton required to complete day puzzle

(defpackage :advent-<insertyear>
  (:use :cl)
  :depends-on ("alexandria" "trivia")
  :export :test-func-adv21)

(in-package :my-package)

(defparameter *input-file* "./input002.txt")


(defun test-func-adv2 ()
  (format t "Test for AoC2021"))

