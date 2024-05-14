;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0058) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
(require 2htdp/image)
(require 2htdp/universe)

;Ex.58

;Definitions
(define LOW-PRICE 1000)
(define LOW-TAX 0.05)
(define LUXURY-PRICE 10000)
(define LUXURY-TAX 0.08)

; A Price falls into one of three intervals: 
; — 0 through 1000
; — 1000 through 10000
; — 10000 and above.
; interpretation the price of an item

(check-expect (sales-tax 537) 0)
(check-expect (sales-tax 1000) (* 0.05 1000))
(check-expect (sales-tax 12017) (* 0.08 12017))
(check-expect (sales-tax 10000)(* 0.08 10000))
(check-expect (sales-tax 1282) (* 0.05 1282))

; Price -> Number
; computes the amount of tax charged for p
(define (sales-tax p)
  (cond
    [(and (<= 0 p) (< p LOW-PRICE)) 0]
    [(and (<= LOW-PRICE p) (< p LUXURY-PRICE)) (* LOW-TAX p)]
    [(>= p LUXURY-PRICE) (* LUXURY-TAX p)]))
;DONE only zero left as "magic" number
