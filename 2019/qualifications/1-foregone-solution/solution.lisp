(defun solve (string)
  (loop
    :with a = 0 :and b = 0
    :for c :across string
    :for d = (- (char-code c) (char-code #\0))
    :do (if (= d 4)
          (setf a (+ (* a 10) 2)
                b (+ (* b 10) 2))
          (setf a (+ (* a 10) d)
                b (+ (* b 10) 0)))
    :finally (return (list a b))))

(defun solution ()
  (loop
    :for i :from 1 :to (parse-integer (read-line))
    :for n = (read-line)
    :for (a b) = (solve n)
    :do (format t "Case #~d: ~d ~d~%" i a b)))
