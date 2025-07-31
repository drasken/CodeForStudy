#lang racket


(require (only-in sha sha256))
(require (only-in sha bytes->hex-string))
(require racket/serialize)

(provide (struct-out transaction-io)
	 make-transaction-io valid-transaction-io?)


(struct transaction-io
  (transaction-hash value owner timestamp)
  #:prefab)

(define (calculate-transaction-io-hash value owner timestamp)
  (bytes->hex-string (sha256 (bytes-append
			      (string->bytes/utf-8 (number->string value))
			      (string->bytes/utf-8 (~a (serialize owner)))
			      (string->bytes/utf-8 (number->string timestamp))))))
