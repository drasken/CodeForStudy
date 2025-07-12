#lang racket

(struct block
  (prev-hash current-hash transaction timestamp nonce)
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


