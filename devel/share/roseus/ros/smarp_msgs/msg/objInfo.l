;; Auto-generated. Do not edit!


(when (boundp 'smarp_msgs::objInfo)
  (if (not (find-package "SMARP_MSGS"))
    (make-package "SMARP_MSGS"))
  (shadow 'objInfo (find-package "SMARP_MSGS")))
(unless (find-package "SMARP_MSGS::OBJINFO")
  (make-package "SMARP_MSGS::OBJINFO"))

(in-package "ROS")
;;//! \htmlinclude objInfo.msg.html


(defclass smarp_msgs::objInfo
  :super ros::object
  :slots (_deg _dist ))

(defmethod smarp_msgs::objInfo
  (:init
   (&key
    ((:deg __deg) (make-array 0 :initial-element 0 :element-type :integer))
    ((:dist __dist) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _deg __deg)
   (setq _dist __dist)
   self)
  (:deg
   (&optional __deg)
   (if __deg (setq _deg __deg)) _deg)
  (:dist
   (&optional __dist)
   (if __dist (setq _dist __dist)) _dist)
  (:serialization-length
   ()
   (+
    ;; int32[] _deg
    (* 4    (length _deg)) 4
    ;; float32[] _dist
    (* 4    (length _dist)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _deg
     (write-long (length _deg) s)
     (dotimes (i (length _deg))
       (write-long (elt _deg i) s)
       )
     ;; float32[] _dist
     (write-long (length _dist) s)
     (dotimes (i (length _dist))
       (sys::poke (elt _dist i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _deg
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _deg (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _deg i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; float32[] _dist
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _dist (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _dist i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get smarp_msgs::objInfo :md5sum-) "85eca806c10fa7a6bdccc3a57dc0154a")
(setf (get smarp_msgs::objInfo :datatype-) "smarp_msgs/objInfo")
(setf (get smarp_msgs::objInfo :definition-)
      "int32[]  deg
float32[] dist
")



(provide :smarp_msgs/objInfo "85eca806c10fa7a6bdccc3a57dc0154a")


