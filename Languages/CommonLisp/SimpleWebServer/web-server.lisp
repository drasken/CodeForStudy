;;;; My first attempt

(ql:quickload "hunchentoot")

(defvar *acceptor* (make-instance 'hunchentoot:easy-acceptor
				  :port 4242))

(setf (hunchentoot:acceptor-document-root *acceptor*)
      #p"./www")

(hunchentoot:start *acceptor*)

