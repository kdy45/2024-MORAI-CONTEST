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

class recogObj {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.lines = null;
      this.light = null;
      this.stopline = null;
      this.object = null;
    }
    else {
      if (initObj.hasOwnProperty('lines')) {
        this.lines = initObj.lines
      }
      else {
        this.lines = false;
      }
      if (initObj.hasOwnProperty('light')) {
        this.light = initObj.light
      }
      else {
        this.light = false;
      }
      if (initObj.hasOwnProperty('stopline')) {
        this.stopline = initObj.stopline
      }
      else {
        this.stopline = false;
      }
      if (initObj.hasOwnProperty('object')) {
        this.object = initObj.object
      }
      else {
        this.object = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type recogObj
    // Serialize message field [lines]
    bufferOffset = _serializer.bool(obj.lines, buffer, bufferOffset);
    // Serialize message field [light]
    bufferOffset = _serializer.bool(obj.light, buffer, bufferOffset);
    // Serialize message field [stopline]
    bufferOffset = _serializer.bool(obj.stopline, buffer, bufferOffset);
    // Serialize message field [object]
    bufferOffset = _serializer.bool(obj.object, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type recogObj
    let len;
    let data = new recogObj(null);
    // Deserialize message field [lines]
    data.lines = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [light]
    data.light = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [stopline]
    data.stopline = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [object]
    data.object = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'smarp_msgs/recogObj';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4f3360b6f6ebe0d68e5b19307f35dc6c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool lines
    bool light
    bool stopline
    bool object
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new recogObj(null);
    if (msg.lines !== undefined) {
      resolved.lines = msg.lines;
    }
    else {
      resolved.lines = false
    }

    if (msg.light !== undefined) {
      resolved.light = msg.light;
    }
    else {
      resolved.light = false
    }

    if (msg.stopline !== undefined) {
      resolved.stopline = msg.stopline;
    }
    else {
      resolved.stopline = false
    }

    if (msg.object !== undefined) {
      resolved.object = msg.object;
    }
    else {
      resolved.object = false
    }

    return resolved;
    }
};

module.exports = recogObj;
