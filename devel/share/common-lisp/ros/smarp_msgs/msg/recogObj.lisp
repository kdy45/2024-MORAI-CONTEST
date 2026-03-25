; Auto-generated. Do not edit!


(cl:in-package smarp_msgs-msg)


;//! \htmlinclude recogObj.msg.html

(cl:defclass <recogObj> (roslisp-msg-protocol:ros-message)
  ((lines
    :reader lines
    :initarg :lines
    :type cl:boolean
    :initform cl:nil)
   (light
    :reader light
    :initarg :light
    :type cl:boolean
    :initform cl:nil)
   (stopline
    :reader stopline
    :initarg :stopline
    :type cl:boolean
    :initform cl:nil)
   (object
    :reader object
    :initarg :object
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass recogObj (<recogObj>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <recogObj>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'recogObj)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name smarp_msgs-msg:<recogObj> is deprecated: use smarp_msgs-msg:recogObj instead.")))

(cl:ensure-generic-function 'lines-val :lambda-list '(m))
(cl:defmethod lines-val ((m <recogObj>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:lines-val is deprecated.  Use smarp_msgs-msg:lines instead.")
  (lines m))

(cl:ensure-generic-function 'light-val :lambda-list '(m))
(cl:defmethod light-val ((m <recogObj>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:light-val is deprecated.  Use smarp_msgs-msg:light instead.")
  (light m))

(cl:ensure-generic-function 'stopline-val :lambda-list '(m))
(cl:defmethod stopline-val ((m <recogObj>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:stopline-val is deprecated.  Use smarp_msgs-msg:stopline instead.")
  (stopline m))

(cl:ensure-generic-function 'object-val :lambda-list '(m))
(cl:defmethod object-val ((m <recogObj>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smarp_msgs-msg:object-val is deprecated.  Use smarp_msgs-msg:object instead.")
  (object m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <recogObj>) ostream)
  "Serializes a message object of type '<recogObj>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'lines) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'light) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'stopline) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'object) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <recogObj>) istream)
  "Deserializes a message object of type '<recogObj>"
    (cl:setf (cl:slot-value msg 'lines) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'light) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'stopline) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'object) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<recogObj>)))
  "Returns string type for a message object of type '<recogObj>"
  "smarp_msgs/recogObj")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'recogObj)))
  "Returns string type for a message object of type 'recogObj"
  "smarp_msgs/recogObj")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<recogObj>)))
  "Returns md5sum for a message object of type '<recogObj>"
  "4f3360b6f6ebe0d68e5b19307f35dc6c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'recogObj)))
  "Returns md5sum for a message object of type 'recogObj"
  "4f3360b6f6ebe0d68e5b19307f35dc6c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<recogObj>)))
  "Returns full string definition for message of type '<recogObj>"
  (cl:format cl:nil "bool lines~%bool light~%bool stopline~%bool object~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'recogObj)))
  "Returns full string definition for message of type 'recogObj"
  (cl:format cl:nil "bool lines~%bool light~%bool stopline~%bool object~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <recogObj>))
  (cl:+ 0
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <recogObj>))
  "Converts a ROS message object to a list"
  (cl:list 'recogObj
    (cl:cons ':lines (lines msg))
    (cl:cons ':light (light msg))
    (cl:cons ':stopline (stopline msg))
    (cl:cons ':object (object msg))
))
