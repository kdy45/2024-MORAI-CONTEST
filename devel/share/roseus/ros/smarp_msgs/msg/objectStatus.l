;; Auto-generated. Do not edit!


(when (boundp 'smarp_msgs::objectStatus)
  (if (not (find-package "SMARP_MSGS"))
    (make-package "SMARP_MSGS"))
  (shadow 'objectStatus (find-package "SMARP_MSGS")))
(unless (find-package "SMARP_MSGS::OBJECTSTATUS")
  (make-package "SMARP_MSGS::OBJECTSTATUS"))

(in-package "ROS")
;;//! \htmlinclude objectStatus.msg.html


(defclass smarp_msgs::objectStatus
  :super ros::object
  :slots (_no_objects _objects ))

(defmethod smarp_msgs::objectStatus
  (:init
   (&key
    ((:no_objects __no_objects) 0)
    ((:objects __objects) ())
    )
   (send-super :init)
   (setq _no_objects (round __no_objects))
   (setq _objects __objects)
   self)
  (:no_objects
   (&optional __no_objects)
   (if __no_objects (setq _no_objects __no_objects)) _no_objects)
  (:objects
   (&rest __objects)
   (if (keywordp (car __objects))
       (send* _objects __objects)
     (progn
       (if __objects (setq _objects (car __objects)))
       _objects)))
  (:serialization-length
   ()
   (+
    ;; int32 _no_objects
    4
    ;; smarp_msgs/objInfo[] _objects
    (apply #'+ (send-all _objects :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _no_objects
       (write-long _no_objects s)
     ;; smarp_msgs/objInfo[] _objects
     (write-long (length _objects) s)
     (dolist (elem _objects)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _no_objects
     (setq _no_objects (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; smarp_msgs/objInfo[] _objects
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _objects (let (r) (dotimes (i n) (push (instance smarp_msgs::objInfo :init) r)) r))
     (dolist (elem- _objects)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get smarp_msgs::objectStatus :md5sum-) "5a23f44a8ec703483381fef35d218672")
(setf (get smarp_msgs::objectStatus :datatype-) "smarp_msgs/objectStatus")
(setf (get smarp_msgs::objectStatus :definition-)
      "int32 no_objects
objInfo[] objects

================================================================================
MSG: smarp_msgs/objInfo
int32[]  deg
float32[] dist
")



(provide :smarp_msgs/objectStatus "5a23f44a8ec703483381fef35d218672")


