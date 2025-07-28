(defpackage #:agui
  (:use #:cl #:clog)
  (:export start-app))

(in-package :agui)

(defun on-new-window (body)
  (create-div body :content "Hello World"))

(defun start-app ()
  (initialize 'on-new-window)
  (open-browser))
