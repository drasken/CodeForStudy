;; myscript.scm
(define mylib (dynamic-link "mylib.so"))

(define hello (foreign-lambda* void () mylib "hello"))
(define add (foreign-lambda* int (int int) mylib "add"))

(hello)  ;; Calls the C function
(display (add 5 7))  ;; Calls the C function and displays the result
