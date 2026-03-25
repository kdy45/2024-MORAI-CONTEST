;; Auto-generated. Do not edit!


(when (boundp 'smarp_msgs::lidarStatus)
  (if (not (find-package "SMARP_MSGS"))
    (make-package "SMARP_MSGS"))
  (shadow 'lidarStatus (find-package "SMARP_MSGS")))
(unless (find-package "SMARP_MSGS::LIDARSTATUS")
  (make-package "SMARP_MSGS::LIDARSTATUS"))

(in-package "ROS")
;;//! \htmlinclude lidarStatus.msg.html


(defclass smarp_msgs::lidarStatus
  :super ros::object
  :slots (_range _dist ))

(defmethod smarp_msgs::lidarStatus
  (:init
   (&key
    ((:range __range) (make-array 0 :initial-element 0 :element-type :integer))
    ((:dist __dist) 0.0)
    )
   (send-super :init)
   (setq _range __range)
   (setq _dist (float __dist))
   self)
  (:range
   (&optional __range)
   (if __range (setq _range __range)) _range)
  (:dist
   (&optional __dist)
   (if __dist (setq _dist __dist)) _dist)
  (:serialization-length
   ()
   (+
    ;; int32[] _range
    (* 4    (length _range)) 4
    ;; float32 _dist
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _range
     (write-long (length _range) s)
     (dotimes (i (length _range))
       (write-long (elt _range i) s)
       )
     ;; float32 _dist
       (sys::poke _dist (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _range
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _range (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _range i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; float32 _dist
     (setq _dist (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get smarp_msgs::lidarStatus :md5sum-) "9851517ab1c233d16dff1313b91ad130")
(setf (get smarp_msgs::lidarStatus :datatype-) "smarp_msgs/lidarStatus")
(setf (get smarp_msgs::lidarStatus :definition-)
      "int32[] range
float32 dist
")



(provide :smarp_msgs/lidarStatus "9851517ab1c233d16dff1313b91ad130")


