; Auto-generated. Do not edit!


(cl:in-package smarp_msgs-msg)


;//! \htmlinclude objectStatus.msg.html

(cl:defclass <objectStatus> (roslisp-msg-protocol:ros-message)
  ((no_objects
    :reader no_objects
    :initarg :no_objects
    :type cl:integer
    :initform 0)
   (objects
    :reader objects
    :initarg :objects
    :type (cl:vector smarp_msgs-msg:objInfo)
   :initform (cl:make-array 0 :element-type 'smarp_msgs-msg:objInfo :initial-element (cl:make-instance 'smarp_msgs-msg:objInfo))))
)

(cl:defclass objectStatus (<objectStatus>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <objectStatus>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'objectStatus)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name smarp_msgs-msg:<objectStatus> is deprecated: use smarp_msgs-msg:objectStatus instead.")))

(cl:ensure-generic-function 'no_objects-val :lambda-list '(m))
(cl:defmethod no_objects-val ((m <objectStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:no_objects-val is deprecated.  Use smarp_msgs-msg:no_objects instead.")
  (no_objects m))

(cl:ensure-generic-function 'objects-val :lambda-list '(m))
(cl:defmethod objects-val ((m <objectStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:objects-val is deprecated.  Use smarp_msgs-msg:objects instead.")
  (objects m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <objectStatus>) ostream)
  "Serializes a message object of type '<objectStatus>"
  (cl:let* ((signed (cl:slot-value msg 'no_objects)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'objects))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'objects))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <objectStatus>) istream)
  "Deserializes a message object of type '<objectStatus>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'no_objects) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'objects) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'objects)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'smarp_msgs-msg:objInfo))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<objectStatus>)))
  "Returns string type for a message object of type '<objectStatus>"
  "smarp_msgs/objectStatus")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'objectStatus)))
  "Returns string type for a message object of type 'objectStatus"
  "smarp_msgs/objectStatus")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<objectStatus>)))
  "Returns md5sum for a message object of type '<objectStatus>"
  "5a23f44a8ec703483381fef35d218672")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'objectStatus)))
  "Returns md5sum for a message object of type 'objectStatus"
  "5a23f44a8ec703483381fef35d218672")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<objectStatus>)))
  "Returns full string definition for message of type '<objectStatus>"
  (cl:format cl:nil "int32 no_objects~%objInfo[] objects~%~%================================================================================~%MSG: smarp_msgs/objInfo~%int32[]  deg~%float32[] dist~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'objectStatus)))
  "Returns full string definition for message of type 'objectStatus"
  (cl:format cl:nil "int32 no_objects~%objInfo[] objects~%~%================================================================================~%MSG: smarp_msgs/objInfo~%int32[]  deg~%float32[] dist~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <objectStatus>))
  (cl:+ 0
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'objects) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <objectStatus>))
  "Converts a ROS message object to a list"
  (cl:list 'objectStatus
    (cl:cons ':no_objects (no_objects msg))
    (cl:cons ':objects (objects msg))
))
