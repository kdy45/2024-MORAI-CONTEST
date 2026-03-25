;; Auto-generated. Do not edit!


(when (boundp 'smarp_msgs::camInfo)
  (if (not (find-package "SMARP_MSGS"))
    (make-package "SMARP_MSGS"))
  (shadow 'camInfo (find-package "SMARP_MSGS")))
(unless (find-package "SMARP_MSGS::CAMINFO")
  (make-package "SMARP_MSGS::CAMINFO"))

(in-package "ROS")
;;//! \htmlinclude camInfo.msg.html


(defclass smarp_msgs::camInfo
  :super ros::object
  :slots (_stopline _crop_image_width _crop_image_height _m_lx _m_ly _m_rx _m_ry ))

(defmethod smarp_msgs::camInfo
  (:init
   (&key
    ((:stopline __stopline) 0)
    ((:crop_image_width __crop_image_width) 0)
    ((:crop_image_height __crop_image_height) 0)
    ((:m_lx __m_lx) 0.0)
    ((:m_ly __m_ly) 0.0)
    ((:m_rx __m_rx) 0.0)
    ((:m_ry __m_ry) 0.0)
    )
   (send-super :init)
   (setq _stopline (round __stopline))
   (setq _crop_image_width (round __crop_image_width))
   (setq _crop_image_height (round __crop_image_height))
   (setq _m_lx (float __m_lx))
   (setq _m_ly (float __m_ly))
   (setq _m_rx (float __m_rx))
   (setq _m_ry (float __m_ry))
   self)
  (:stopline
   (&optional __stopline)
   (if __stopline (setq _stopline __stopline)) _stopline)
  (:crop_image_width
   (&optional __crop_image_width)
   (if __crop_image_width (setq _crop_image_width __crop_image_width)) _crop_image_width)
  (:crop_image_height
   (&optional __crop_image_height)
   (if __crop_image_height (setq _crop_image_height __crop_image_height)) _crop_image_height)
  (:m_lx
   (&optional __m_lx)
   (if __m_lx (setq _m_lx __m_lx)) _m_lx)
  (:m_ly
   (&optional __m_ly)
   (if __m_ly (setq _m_ly __m_ly)) _m_ly)
  (:m_rx
   (&optional __m_rx)
   (if __m_rx (setq _m_rx __m_rx)) _m_rx)
  (:m_ry
   (&optional __m_ry)
   (if __m_ry (setq _m_ry __m_ry)) _m_ry)
  (:serialization-length
   ()
   (+
    ;; int16 _stopline
    2
    ;; int32 _crop_image_width
    4
    ;; int32 _crop_image_height
    4
    ;; float32 _m_lx
    4
    ;; float32 _m_ly
    4
    ;; float32 _m_rx
    4
    ;; float32 _m_ry
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _stopline
       (write-word _stopline s)
     ;; int32 _crop_image_width
       (write-long _crop_image_width s)
     ;; int32 _crop_image_height
       (write-long _crop_image_height s)
     ;; float32 _m_lx
       (sys::poke _m_lx (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _m_ly
       (sys::poke _m_ly (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _m_rx
       (sys::poke _m_rx (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _m_ry
       (sys::poke _m_ry (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _stopline
     (setq _stopline (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int32 _crop_image_width
     (setq _crop_image_width (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _crop_image_height
     (setq _crop_image_height (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _m_lx
     (setq _m_lx (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _m_ly
     (setq _m_ly (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _m_rx
     (setq _m_rx (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _m_ry
     (setq _m_ry (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get smarp_msgs::camInfo :md5sum-) "19f6dfc32cf501fc7832af28b4cc64e0")
(setf (get smarp_msgs::camInfo :datatype-) "smarp_msgs/camInfo")
(setf (get smarp_msgs::camInfo :definition-)
      "int16 stopline
int32 crop_image_width
int32 crop_image_height
float32 m_lx
float32 m_ly
float32 m_rx
float32 m_ry
")



(provide :smarp_msgs/camInfo "19f6dfc32cf501fc7832af28b4cc64e0")


