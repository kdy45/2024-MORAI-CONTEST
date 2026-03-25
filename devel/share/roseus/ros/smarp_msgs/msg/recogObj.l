;; Auto-generated. Do not edit!


(when (boundp 'smarp_msgs::recogObj)
  (if (not (find-package "SMARP_MSGS"))
    (make-package "SMARP_MSGS"))
  (shadow 'recogObj (find-package "SMARP_MSGS")))
(unless (find-package "SMARP_MSGS::RECOGOBJ")
  (make-package "SMARP_MSGS::RECOGOBJ"))

(in-package "ROS")
;;//! \htmlinclude recogObj.msg.html


(defclass smarp_msgs::recogObj
  :super ros::object
  :slots (_lines _light _stopline _object ))

(defmethod smarp_msgs::recogObj
  (:init
   (&key
    ((:lines __lines) nil)
    ((:light __light) nil)
    ((:stopline __stopline) nil)
    ((:object __object) nil)
    )
   (send-super :init)
   (setq _lines __lines)
   (setq _light __light)
   (setq _stopline __stopline)
   (setq _object __object)
   self)
  (:lines
   (&optional (__lines :null))
   (if (not (eq __lines :null)) (setq _lines __lines)) _lines)
  (:light
   (&optional (__light :null))
   (if (not (eq __light :null)) (setq _light __light)) _light)
  (:stopline
   (&optional (__stopline :null))
   (if (not (eq __stopline :null)) (setq _stopline __stopline)) _stopline)
  (:object
   (&optional (__object :null))
   (if (not (eq __object :null)) (setq _object __object)) _object)
  (:serialization-length
   ()
   (+
    ;; bool _lines
    1
    ;; bool _light
    1
    ;; bool _stopline
    1
    ;; bool _object
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _lines
       (if _lines (write-byte -1 s) (write-byte 0 s))
     ;; bool _light
       (if _light (write-byte -1 s) (write-byte 0 s))
     ;; bool _stopline
       (if _stopline (write-byte -1 s) (write-byte 0 s))
     ;; bool _object
       (if _object (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _lines
     (setq _lines (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _light
     (setq _light (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _stopline
     (setq _stopline (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _object
     (setq _object (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get smarp_msgs::recogObj :md5sum-) "4f3360b6f6ebe0d68e5b19307f35dc6c")
(setf (get smarp_msgs::recogObj :datatype-) "smarp_msgs/recogObj")
(setf (get smarp_msgs::recogObj :definition-)
      "bool lines
bool light
bool stopline
bool object
")



(provide :smarp_msgs/recogObj "4f3360b6f6ebe0d68e5b19307f35dc6c")


