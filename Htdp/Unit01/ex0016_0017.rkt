;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ex0016_0017) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
 (require 2htdp/image)

;Exercise 16. Define the function image-area, which counts
;the number of pixels in a given image. See exercise 6 for
;ideas.

(define (ex16 img)
  (* (image-width img)
     (image-height img)))

;Exercise 17. Define the function image-classify, which
;consumes an image and conditionally produces "tall" if the
;image is taller than wide, "wide" if it is wider than tall,
;or "square" if its width and height are the same. See
;exercise 8 for ideas.

(define (image-classify img)
  (if (< (image-width img) (image-height img))
      "wide"
      "tall"))
         