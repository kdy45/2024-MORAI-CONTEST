; Auto-generated. Do not edit!


(cl:in-package smarp_msgs-msg)


;//! \htmlinclude camInfo.msg.html

(cl:defclass <camInfo> (roslisp-msg-protocol:ros-message)
  ((stopline
    :reader stopline
    :initarg :stopline
    :type cl:fixnum
    :initform 0)
   (crop_image_width
    :reader crop_image_width
    :initarg :crop_image_width
    :type cl:integer
    :initform 0)
   (crop_image_height
    :reader crop_image_height
    :initarg :crop_image_height
    :type cl:integer
    :initform 0)
   (m_lx
    :reader m_lx
    :initarg :m_lx
    :type cl:float
    :initform 0.0)
   (m_ly
    :reader m_ly
    :initarg :m_ly
    :type cl:float
    :initform 0.0)
   (m_rx
    :reader m_rx
    :initarg :m_rx
    :type cl:float
    :initform 0.0)
   (m_ry
    :reader m_ry
    :initarg :m_ry
    :type cl:float
    :initform 0.0))
)

(cl:defclass camInfo (<camInfo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <camInfo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'camInfo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name smarp_msgs-msg:<camInfo> is deprecated: use smarp_msgs-msg:camInfo instead.")))

(cl:ensure-generic-function 'stopline-val :lambda-list '(m))
(cl:defmethod stopline-val ((m <camInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:stopline-val is deprecated.  Use smarp_msgs-msg:stopline instead.")
  (stopline m))

(cl:ensure-generic-function 'crop_image_width-val :lambda-list '(m))
(cl:defmethod crop_image_width-val ((m <camInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:crop_image_width-val is deprecated.  Use smarp_msgs-msg:crop_image_width instead.")
  (crop_image_width m))

(cl:ensure-generic-function 'crop_image_height-val :lambda-list '(m))
(cl:defmethod crop_image_height-val ((m <camInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:crop_image_height-val is deprecated.  Use smarp_msgs-msg:crop_image_height instead.")
  (crop_image_height m))

(cl:ensure-generic-function 'm_lx-val :lambda-list '(m))
(cl:defmethod m_lx-val ((m <camInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:m_lx-val is deprecated.  Use smarp_msgs-msg:m_lx instead.")
  (m_lx m))

(cl:ensure-generic-function 'm_ly-val :lambda-list '(m))
(cl:defmethod m_ly-val ((m <camInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:m_ly-val is deprecated.  Use smarp_msgs-msg:m_ly instead.")
  (m_ly m))

(cl:ensure-generic-function 'm_rx-val :lambda-list '(m))
(cl:defmethod m_rx-val ((m <camInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:m_rx-val is deprecated.  Use smarp_msgs-msg:m_rx instead.")
  (m_rx m))

(cl:ensure-generic-function 'm_ry-val :lambda-list '(m))
(cl:defmethod m_ry-val ((m <camInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:m_ry-val is deprecated.  Use smarp_msgs-msg:m_ry instead.")
  (m_ry m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <camInfo>) ostream)
  "Serializes a message object of type '<camInfo>"
  (cl:let* ((signed (cl:slot-value msg 'stopline)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'crop_image_width)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'crop_image_height)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'm_lx))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'm_ly))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'm_rx))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'm_ry))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <camInfo>) istream)
  "Deserializes a message object of type '<camInfo>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'stopline) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'crop_image_width) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'crop_image_height) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'm_lx) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'm_ly) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'm_rx) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'm_ry) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<camInfo>)))
  "Returns string type for a message object of type '<camInfo>"
  "smarp_msgs/camInfo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'camInfo)))
  "Returns string type for a message object of type 'camInfo"
  "smarp_msgs/camInfo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<camInfo>)))
  "Returns md5sum for a message object of type '<camInfo>"
  "19f6dfc32cf501fc7832af28b4cc64e0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'camInfo)))
  "Returns md5sum for a message object of type 'camInfo"
  "19f6dfc32cf501fc7832af28b4cc64e0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<camInfo>)))
  "Returns full string definition for message of type '<camInfo>"
  (cl:format cl:nil "int16 stopline~%int32 crop_image_width~%int32 crop_image_height~%float32 m_lx~%float32 m_ly~%float32 m_rx~%float32 m_ry~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'camInfo)))
  "Returns full string definition for message of type 'camInfo"
  (cl:format cl:nil "int16 stopline~%int32 crop_image_width~%int32 crop_image_height~%float32 m_lx~%float32 m_ly~%float32 m_rx~%float32 m_ry~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <camInfo>))
  (cl:+ 0
     2
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <camInfo>))
  "Converts a ROS message object to a list"
  (cl:list 'camInfo
    (cl:cons ':stopline (stopline msg))
    (cl:cons ':crop_image_width (crop_image_width msg))
    (cl:cons ':crop_image_height (crop_image_height msg))
    (cl:cons ':m_lx (m_lx msg))
    (cl:cons ':m_ly (m_ly msg))
    (cl:cons ':m_rx (m_rx msg))
    (cl:cons ':m_ry (m_ry msg))
))
