;; Trying to implement a script that inspect directory tree
;; and find find duplicate files comparing their difest.
;; Stll not decided which actual implementation to check the file

;; First rough idea:
;; - user set a starting point in the filesystem
;; - the script chech for all files in tht directory
;; - get all the result of the checksum or whatever ad store them (hash ?)
;; - using the hash as key map the files with complete filepath
;; - recursively do the same on all subdirectories
;; - at the end of the inspection filter and get all duplicates
;; - + Simple method: check if for key more than 1 element
;; - log in a txt file the result of the inspection
