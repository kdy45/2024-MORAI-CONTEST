; Auto-generated. Do not edit!


(cl:in-package smarp_msgs-msg)


;//! \htmlinclude objInfo.msg.html

(cl:defclass <objInfo> (roslisp-msg-protocol:ros-message)
  ((deg
    :reader deg
    :initarg :deg
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (dist
    :reader dist
    :initarg :dist
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass objInfo (<objInfo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <objInfo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'objInfo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name smarp_msgs-msg:<objInfo> is deprecated: use smarp_msgs-msg:objInfo instead.")))

(cl:ensure-generic-function 'deg-val :lambda-list '(m))
(cl:defmethod deg-val ((m <objInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:deg-val is deprecated.  Use smarp_msgs-msg:deg instead.")
  (deg m))

(cl:ensure-generic-function 'dist-val :lambda-list '(m))
(cl:defmethod dist-val ((m <objInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:dist-val is deprecated.  Use smarp_msgs-msg:dist instead.")
  (dist m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <objInfo>) ostream)
  "Serializes a message object of type '<objInfo>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'deg))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'deg))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'dist))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'dist))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <objInfo>) istream)
  "Deserializes a message object of type '<objInfo>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'deg) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'deg)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'dist) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'dist)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<objInfo>)))
  "Returns string type for a message object of type '<objInfo>"
  "smarp_msgs/objInfo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'objInfo)))
  "Returns string type for a message object of type 'objInfo"
  "smarp_msgs/objInfo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<objInfo>)))
  "Returns md5sum for a message object of type '<objInfo>"
  "85eca806c10fa7a6bdccc3a57dc0154a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'objInfo)))
  "Returns md5sum for a message object of type 'objInfo"
  "85eca806c10fa7a6bdccc3a57dc0154a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<objInfo>)))
  "Returns full string definition for message of type '<objInfo>"
  (cl:format cl:nil "int32[]  deg~%float32[] dist~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'objInfo)))
  "Returns full string definition for message of type 'objInfo"
  (cl:format cl:nil "int32[]  deg~%float32[] dist~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <objInfo>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'deg) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'dist) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <objInfo>))
  "Converts a ROS message object to a list"
  (cl:list 'objInfo
    (cl:cons ':deg (deg msg))
    (cl:cons ':dist (dist msg))
))
