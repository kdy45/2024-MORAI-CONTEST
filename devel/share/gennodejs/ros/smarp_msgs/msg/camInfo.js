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

class camInfo {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.stopline = null;
      this.crop_image_width = null;
      this.crop_image_height = null;
      this.m_lx = null;
      this.m_ly = null;
      this.m_rx = null;
      this.m_ry = null;
    }
    else {
      if (initObj.hasOwnProperty('stopline')) {
        this.stopline = initObj.stopline
      }
      else {
        this.stopline = 0;
      }
      if (initObj.hasOwnProperty('crop_image_width')) {
        this.crop_image_width = initObj.crop_image_width
      }
      else {
        this.crop_image_width = 0;
      }
      if (initObj.hasOwnProperty('crop_image_height')) {
        this.crop_image_height = initObj.crop_image_height
      }
      else {
        this.crop_image_height = 0;
      }
      if (initObj.hasOwnProperty('m_lx')) {
        this.m_lx = initObj.m_lx
      }
      else {
        this.m_lx = 0.0;
      }
      if (initObj.hasOwnProperty('m_ly')) {
        this.m_ly = initObj.m_ly
      }
      else {
        this.m_ly = 0.0;
      }
      if (initObj.hasOwnProperty('m_rx')) {
        this.m_rx = initObj.m_rx
      }
      else {
        this.m_rx = 0.0;
      }
      if (initObj.hasOwnProperty('m_ry')) {
        this.m_ry = initObj.m_ry
      }
      else {
        this.m_ry = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type camInfo
    // Serialize message field [stopline]
    bufferOffset = _serializer.int16(obj.stopline, buffer, bufferOffset);
    // Serialize message field [crop_image_width]
    bufferOffset = _serializer.int32(obj.crop_image_width, buffer, bufferOffset);
    // Serialize message field [crop_image_height]
    bufferOffset = _serializer.int32(obj.crop_image_height, buffer, bufferOffset);
    // Serialize message field [m_lx]
    bufferOffset = _serializer.float32(obj.m_lx, buffer, bufferOffset);
    // Serialize message field [m_ly]
    bufferOffset = _serializer.float32(obj.m_ly, buffer, bufferOffset);
    // Serialize message field [m_rx]
    bufferOffset = _serializer.float32(obj.m_rx, buffer, bufferOffset);
    // Serialize message field [m_ry]
    bufferOffset = _serializer.float32(obj.m_ry, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type camInfo
    let len;
    let data = new camInfo(null);
    // Deserialize message field [stopline]
    data.stopline = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [crop_image_width]
    data.crop_image_width = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [crop_image_height]
    data.crop_image_height = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [m_lx]
    data.m_lx = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [m_ly]
    data.m_ly = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [m_rx]
    data.m_rx = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [m_ry]
    data.m_ry = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 26;
  }

  static datatype() {
    // Returns string type for a message object
    return 'smarp_msgs/camInfo';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '19f6dfc32cf501fc7832af28b4cc64e0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 stopline
    int32 crop_image_width
    int32 crop_image_height
    float32 m_lx
    float32 m_ly
    float32 m_rx
    float32 m_ry
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new camInfo(null);
    if (msg.stopline !== undefined) {
      resolved.stopline = msg.stopline;
    }
    else {
      resolved.stopline = 0
    }

    if (msg.crop_image_width !== undefined) {
      resolved.crop_image_width = msg.crop_image_width;
    }
    else {
      resolved.crop_image_width = 0
    }

    if (msg.crop_image_height !== undefined) {
      resolved.crop_image_height = msg.crop_image_height;
    }
    else {
      resolved.crop_image_height = 0
    }

    if (msg.m_lx !== undefined) {
      resolved.m_lx = msg.m_lx;
    }
    else {
      resolved.m_lx = 0.0
    }

    if (msg.m_ly !== undefined) {
      resolved.m_ly = msg.m_ly;
    }
    else {
      resolved.m_ly = 0.0
    }

    if (msg.m_rx !== undefined) {
      resolved.m_rx = msg.m_rx;
    }
    else {
      resolved.m_rx = 0.0
    }

    if (msg.m_ry !== undefined) {
      resolved.m_ry = msg.m_ry;
    }
    else {
      resolved.m_ry = 0.0
    }

    return resolved;
    }
};

module.exports = camInfo;
