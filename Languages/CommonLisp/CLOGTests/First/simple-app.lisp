(ql:quickload :clog)
(in-package :clog-user)
(initialize (lambda (body) (create-div body :content "Hello World")))
(open-browser)
