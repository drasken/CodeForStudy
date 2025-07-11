#lang racket

(struct block
  (prev-hash current-hash transaction timestamp nonce)
  #:prefab)

(struct transaction
  (signature from to value)
  #:prefab)


(block "123456" "234" (transaction "BoroS" "Boro" "You"123) 1 1)
