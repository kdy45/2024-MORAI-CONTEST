// Auto-generated. Do not edit!

// (in-package smarp_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class objInfo {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.deg = null;
      this.dist = null;
    }
    else {
      if (initObj.hasOwnProperty('deg')) {
        this.deg = initObj.deg
      }
      else {
        this.deg = [];
      }
      if (initObj.hasOwnProperty('dist')) {
        this.dist = initObj.dist
      }
      else {
        this.dist = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type objInfo
    // Serialize message field [deg]
    bufferOffset = _arraySerializer.int32(obj.deg, buffer, bufferOffset, null);
    // Serialize message field [dist]
    bufferOffset = _arraySerializer.float32(obj.dist, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type objInfo
    let len;
    let data = new objInfo(null);
    // Deserialize message field [deg]
    data.deg = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [dist]
    data.dist = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.deg.length;
    length += 4 * object.dist.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'smarp_msgs/objInfo';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '85eca806c10fa7a6bdccc3a57dc0154a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[]  deg
    float32[] dist
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new objInfo(null);
    if (msg.deg !== undefined) {
      resolved.deg = msg.deg;
    }
    else {
      resolved.deg = []
    }

    if (msg.dist !== undefined) {
      resolved.dist = msg.dist;
    }
    else {
      resolved.dist = []
    }

    return resolved;
    }
};

module.exports = objInfo;
