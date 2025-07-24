;;;; Main file

(ql:quickload :uiop)

(defpackage #:duplicate-files
  (:use :cl :uiop))

(in-package #:duplicate-files)

(defvar *test* 100)

(defun main (root-dir)
  "Starting from a root dir should inspect dir and all sub-directories recursively.
  Return a list with all files absolute path maybe(?)
  "
  (directory-files root-dir))

