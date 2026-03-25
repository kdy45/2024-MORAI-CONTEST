
(cl:in-package :asdf)

(defsystem "smarp_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "camInfo" :depends-on ("_package_camInfo"))
    (:file "_package_camInfo" :depends-on ("_package"))
    (:file "lidarStatus" :depends-on ("_package_lidarStatus"))
    (:file "_package_lidarStatus" :depends-on ("_package"))
    (:file "objInfo" :depends-on ("_package_objInfo"))
    (:file "_package_objInfo" :depends-on ("_package"))
    (:file "objectStatus" :depends-on ("_package_objectStatus"))
    (:file "_package_objectStatus" :depends-on ("_package"))
    (:file "recogObj" :depends-on ("_package_recogObj"))
    (:file "_package_recogObj" :depends-on ("_package"))
  ))