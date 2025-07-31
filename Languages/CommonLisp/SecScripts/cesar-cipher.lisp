(defpackage #:cesar-cipher
  (:use :cl)
  (:documentation "Encrypt a plain text file giving a number as a key")
  (:export #:cesar-encrypt))

(in-package #:cesar-cipher)

(defun cesar-encrypt (x)
  (length (uiop:read-file-lines x)))
  
