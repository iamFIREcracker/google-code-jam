(defun solve (lydia)
  (map 'string (lambda (m) (if (char= m #\S) #\E #\S)) lydia))

(defun solution ()
  (loop
    :for i :from 1 :to (parse-integer (read-line))
    :for ignored = (read-line)
    :for lydia = (read-line)
    :for mine = (solve lydia)
    :do (format t "Case #~d: ~a~%" i mine)))
