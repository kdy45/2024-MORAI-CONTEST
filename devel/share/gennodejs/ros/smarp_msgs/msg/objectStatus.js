// Auto-generated. Do not edit!

// (in-package smarp_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let objInfo = require('./objInfo.js');

//-----------------------------------------------------------

class objectStatus {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.no_objects = null;
      this.objects = null;
    }
    else {
      if (initObj.hasOwnProperty('no_objects')) {
        this.no_objects = initObj.no_objects
      }
      else {
        this.no_objects = 0;
      }
      if (initObj.hasOwnProperty('objects')) {
        this.objects = initObj.objects
      }
      else {
        this.objects = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type objectStatus
    // Serialize message field [no_objects]
    bufferOffset = _serializer.int32(obj.no_objects, buffer, bufferOffset);
    // Serialize message field [objects]
    // Serialize the length for message field [objects]
    bufferOffset = _serializer.uint32(obj.objects.length, buffer, bufferOffset);
    obj.objects.forEach((val) => {
      bufferOffset = objInfo.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type objectStatus
    let len;
    let data = new objectStatus(null);
    // Deserialize message field [no_objects]
    data.no_objects = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [objects]
    // Deserialize array length for message field [objects]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.objects = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.objects[i] = objInfo.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.objects.forEach((val) => {
      length += objInfo.getMessageSize(val);
    });
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'smarp_msgs/objectStatus';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5a23f44a8ec703483381fef35d218672';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 no_objects
    objInfo[] objects
    
    ================================================================================
    MSG: smarp_msgs/objInfo
    int32[]  deg
    float32[] dist
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new objectStatus(null);
    if (msg.no_objects !== undefined) {
      resolved.no_objects = msg.no_objects;
    }
    else {
      resolved.no_objects = 0
    }

    if (msg.objects !== undefined) {
      resolved.objects = new Array(msg.objects.length);
      for (let i = 0; i < resolved.objects.length; ++i) {
        resolved.objects[i] = objInfo.Resolve(msg.objects[i]);
      }
    }
    else {
      resolved.objects = []
    }

    return resolved;
    }
};

module.exports = objectStatus;
