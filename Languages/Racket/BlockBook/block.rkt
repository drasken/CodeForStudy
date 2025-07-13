#lang racket

(provide (struct-out block) mine-block valid-block? mined-block?)

(require (only-in file/sha1 hex-string->bytes))
(require (only-in sha sha256))
(require (only-in sha bytes->hex-string))
(require racket/serialize)

(struct block
  (current-hash previous-hash transaction timestamp nonce)
  #:prefab)

(struct transaction
  (signature from to value)
  #:prefab)

;; test -> It works
;; (block "123456" "234" (transaction "BoroS" "Boro" "You"123) 1 1)


(define (calculate-block-hash previous-hash timestamp
			      transaction nonce)
  (bytes->hex-string (sha256 (bytes-append
			      (string->bytes/utf-8 previous-hash)
			      (string->bytes/utf-8 (number->string timestamp))
			      (string->bytes/utf-8 (~a (serialize transaction)))
			      (string->bytes/utf-8 (number->string nonce))))))


(define (valid-block? bl)
  (equal? (block-current-hash bl)
	  (calculate-block-hash (block-previous-hash bl)
				(block-timestamp bl)
				(block-transaction bl)
				(block-nonce bl))))


(define difficulty 2)
(define target (bytes->hex-string (make-bytes difficulty 32)))


(define (mined-block? block-hash)
  (equal? (subbytes (hex-string->bytes block-hash) 1 difficulty)
	  (subbytes (hex-string->bytes target) 1 difficulty)))


(define (make-and-mine-block previous-hash timestamp transaction nonce)
  (let ([current-hash (calculate-block-hash
		       previous-hash timestamp transaction nonce)])
    (if (mined-block? current-hash)
	(block current-hash previous-hash transaction timestamp nonce)
	(make-and-mine-block
	 previous-hash timestamp transaction (+ nonce 1)))))


(define (mine-block transaction previous-hash)
  (make-and-mine-block
   previous-hash (current-milliseconds) transaction 1)) ;; Nonce is 1 by default


;; exercise 3.4
(define test-block (block "26516" "6666" (transaction "abbabaa" "me" "you" 666) 1 1))

;; exercise 3.5 - first try nonce was 113
(define next-block (make-and-mine-block (block-previous-hash test-block)
                                        (block-timestamp test-block)
                                        (block-transaction test-block)
                                        (block-nonce test-block)))
