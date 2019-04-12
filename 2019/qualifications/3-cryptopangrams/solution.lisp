(defun read-cyphertext (length &aux (cyphertext (make-array length)))
  (dotimes (i length cyphertext)
    (setf (aref cyphertext i) (read))))
  
(defun split-sequence (string &optional (delimiter #\Space))
  (loop
    :for i = 0 :then (1+ j)
    :for j = (position delimiter string :start i)
    :collect (subseq string i j) :into parts
    :while j
    :finally (return (remove "" parts :test 'equal))))

(defun position-first-difference (cyphertext)
  (loop
    :for i = 0 :then (1+ i)
    :for j = (1+ i)
    :unless (= (aref cyphertext i) (aref cyphertext j)) :return i))

(defun divisors (cyphertext)
  (let* ((divisors (make-array (1+ (length cyphertext))))
         (pos (position-first-difference cyphertext)))
    (setf (aref divisors (1+ pos)) (gcd (aref cyphertext pos) (aref cyphertext (1+ pos))))
    (loop
      :for i :from pos :downto 0
      :do (setf (aref divisors i) (/ (aref cyphertext i) (aref divisors (1+ i))))) 
    (loop
      :for i :from (1+ pos) :below (length cyphertext)
      :do (setf (aref divisors (1+ i)) (/ (aref cyphertext i) (aref divisors i)))) 
    divisors))

(defun decypher-table (divisors &aux (table (make-hash-table)))
  (loop
    :for p :across (sort (remove-duplicates divisors) #'<)
    :for i = 0 :then (1+ i)
    :do (setf (gethash p table) (code-char (+ (char-code #\A) i))))
  table)

(defun solve (cyphertext)
  (loop
    :with divisors = (divisors cyphertext)
    :with table = (decypher-table divisors)
    :for d :across divisors
    :collect (gethash d table) :into plaintext
    :finally (return (coerce plaintext 'string))))

(defun solution ()
  (loop
    :for i :from 1 :to (parse-integer (read-line))
    :for ignored = (read)
    :for size = (read)
    :for cyphertext = (read-cyphertext size)
    :for plaintext = (solve (subseq cyphertext 0 size))
    :do (format t "Case #~d: ~a~%" i plaintext)))

(solution)
