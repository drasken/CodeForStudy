;;;; Main file for my project


(defpackage #:todo-main
  (:use #:cl))

(in-package #:todo-main)

(defclass <my-to-do> ()
  ((description
    :initarg :description
    :accessor todo-description)
   (state
    :initarg :state
    :initform nil
    :accessor todo-state)))

(defvar test-todo (make-instance '<MY-TO-DO> :description "cambiare lampadina al tetto"))



