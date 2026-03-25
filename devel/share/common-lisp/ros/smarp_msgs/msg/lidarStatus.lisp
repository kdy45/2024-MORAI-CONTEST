; Auto-generated. Do not edit!


(cl:in-package smarp_msgs-msg)


;//! \htmlinclude lidarStatus.msg.html

(cl:defclass <lidarStatus> (roslisp-msg-protocol:ros-message)
  ((range
    :reader range
    :initarg :range
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (dist
    :reader dist
    :initarg :dist
    :type cl:float
    :initform 0.0))
)

(cl:defclass lidarStatus (<lidarStatus>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <lidarStatus>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'lidarStatus)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name smarp_msgs-msg:<lidarStatus> is deprecated: use smarp_msgs-msg:lidarStatus instead.")))

(cl:ensure-generic-function 'range-val :lambda-list '(m))
(cl:defmethod range-val ((m <lidarStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:range-val is deprecated.  Use smarp_msgs-msg:range instead.")
  (range m))

(cl:ensure-generic-function 'dist-val :lambda-list '(m))
(cl:defmethod dist-val ((m <lidarStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:dist-val is deprecated.  Use smarp_msgs-msg:dist instead.")
  (dist m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <lidarStatus>) ostream)
  "Serializes a message object of type '<lidarStatus>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'range))))
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
   (cl:slot-value msg 'range))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dist))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <lidarStatus>) istream)
  "Deserializes a message object of type '<lidarStatus>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'range) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'range)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dist) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<lidarStatus>)))
  "Returns string type for a message object of type '<lidarStatus>"
  "smarp_msgs/lidarStatus")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'lidarStatus)))
  "Returns string type for a message object of type 'lidarStatus"
  "smarp_msgs/lidarStatus")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<lidarStatus>)))
  "Returns md5sum for a message object of type '<lidarStatus>"
  "9851517ab1c233d16dff1313b91ad130")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'lidarStatus)))
  "Returns md5sum for a message object of type 'lidarStatus"
  "9851517ab1c233d16dff1313b91ad130")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<lidarStatus>)))
  "Returns full string definition for message of type '<lidarStatus>"
  (cl:format cl:nil "int32[] range~%float32 dist~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'lidarStatus)))
  "Returns full string definition for message of type 'lidarStatus"
  (cl:format cl:nil "int32[] range~%float32 dist~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <lidarStatus>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'range) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <lidarStatus>))
  "Converts a ROS message object to a list"
  (cl:list 'lidarStatus
    (cl:cons ':range (range msg))
    (cl:cons ':dist (dist msg))
))
