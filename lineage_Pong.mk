#
# Copyright (C) 2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from Pong device
$(call inherit-product, device/nothing/Pong/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_Pong
PRODUCT_DEVICE := Pong
PRODUCT_MANUFACTURER := Nothing
PRODUCT_BRAND := Nothing
PRODUCT_MODEL := A065

DESCARTES_MAINTAINER := ediwq14
DESCARTES_PROCESSOR := Snapdragon_8_Plus_Gen_1
DESCARTES_BATTERY := 4700_mAh
DESCARTES_DISPLAY := 6.7_LTPO_OLED_120Hz
DESCARTES_CAMERA_REAR_INFO := 50,50
DESCARTES_CAMERA_FRONT_INFO := 32
DESCARTES_BUILD_TYPE := UNOFFICIAL
TARGET_FACE_UNLOCK_SUPPORTED := true
TARGET_BUILD_DEVICE_AS_WEBCAM := true
TARGET_SUPPORTS_QUICK_TAP := true
TARGET_ENABLE_BLUR := true
TARGET_DISABLE_MATLOG := true

PRODUCT_CHARACTERISTICS := nosdcard

PRODUCT_GMS_CLIENTID_BASE := android-nothing

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildFingerprint=Nothing/Pong/Pong:12/SKQ1.250415.001/2604141749:user/release-keys \
    DeviceName=Pong \
    DeviceProduct=Pong \
    SystemDevice=Pong \
    SystemName=Pong
