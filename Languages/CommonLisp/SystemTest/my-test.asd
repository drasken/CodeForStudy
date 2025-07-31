;;;; This works
;; Compile it in Slime with C-c C-k
;; Than load it with ql:quicklisp ...) should be in the completion list

(asdf:defsystem :my-test
  :description "Testing asdf"
  :depends-on ("uiop")
  :components ((:file "main")))
       
