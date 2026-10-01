#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    "vendor/qcom/common/vendor/display",
    "vendor/qcom/common/vendor/perf",
    "vendor/qcom/common/vendor/qseecomd",
    "vendor/qcom/common/vendor/wlan",
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'vendor.qti.diaghal@1.0',
        'vendor.qti.hardware.dpmservice@1.0',
        'vendor.qti.hardware.qccsyshal@1.0',
        'vendor.qti.hardware.qccsyshal@1.1',
        'vendor.qti.hardware.qccvndhal@1.0',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.imsrtpservice@3.0',
        'vendor.qti.latency@*',
        'vendor.display.color@1.0',
        'vendor.display.color@1.1',
        'vendor.display.color@1.2',
        'vendor.display.color@1.3',
        'vendor.display.color@1.4',
        'vendor.display.color@1.5',
        'vendor.display.postproc@1.0',
        'vendor.qti.hardware.iop@2.0',
        'vendor.qti.hardware.perf@2.0',
        'vendor.qti.hardware.perf@2.1',
        'vendor.qti.hardware.perf@2.2',
        'vendor.qti.hardware.perf2-V1-ndk',
        'vendor.qti.qspmhal-V1-ndk',
    ): lib_fixup_vendor_suffix,
    (
        'libthermalclient',
        'libwpa_client',
        'vendor.qti.memory.pasrmanager-V1-ndk',
        'vendor.qti.snapdragonServices-V2-ndk',
        'vendor.qti.snapdragonServices.qape-V1-ndk',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/etc/seccomp_policy/perfservice.policy': blob_fixup()
        .add_line_if_missing('lseek: 1'),
    'vendor/etc/audio/sku_cape/resourcemanager_waipio_qrd.xml': blob_fixup()
        .regex_replace('<speaker_protection_enabled>1<', '<speaker_protection_enabled>0<'),
    'vendor/bin/hw/android.hardware.power.stats-service': blob_fixup()
        .replace_needed('android.hardware.power.stats-V1-ndk_platform.so', 'android.hardware.power.stats-V1-ndk.so'),
    ('vendor/bin/hw/android.hardware.security.keymint-service-qti', 'vendor/lib64/libqtikeymint.so'): blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V1-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
        .add_needed('android.hardware.security.rkp-V1-ndk.so'),
    'vendor/etc/init/vendor.qti.media.c2@1.0-service.rc': blob_fixup()
        .regex_replace(r'writepid\s+/dev/cpuset/foreground/tasks', 'task_profiles ProcessCapacityHigh HighPerformance'),
    ('vendor/etc/media_codecs_cape.xml', 'vendor/etc/media_codecs_cape_vendor.xml'): blob_fixup()
        .regex_replace('.*media_codecs_(google_audio|google_c2|google_telephony|google_video|vendor_audio).*\n', ''),
    ('vendor/lib64/libarcsoft_dark_vision_raw.so'): blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open')
        .clear_symbol_version('remote_register_buf_attr')
        .clear_symbol_version('remote_register_buf'),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup()
        .replace_needed('vendor.qti.hardware.display.config-V2-ndk_platform.so', 'vendor.qti.hardware.display.config-V2-ndk.so'),
    'vendor/lib64/vendor.libdpmframework.so': blob_fixup()
        .add_needed('libhidlbase_shim.so'),
    'vendor/lib64/libmorpho_video_stabilizer.so': blob_fixup()
        .add_needed('libutils.so'),
    'vendor/lib64/libqcodec2_core.so': blob_fixup()
        .add_needed('libcodec2_shim.so'),
    ('vendor/lib64/libqcrilNr.so', 'vendor/lib64/libril-db.so'): blob_fixup()
        .binary_regex_replace(rb'persist\.vendor\.radio\.poweron_opt', b'persist.vendor.radio.poweron_ign'),
    ('vendor/lib64/libntcamallocator.so', 'vendor/lib64/vendor.noth.hardware.camera-service-impl.so'): blob_fixup()
        .add_needed('libui_shim.so'),
    'system_ext/lib64/vendor.qti.hardware.qccsyshal@1.2-halimpl.so': blob_fixup()
        .replace_needed('libprotobuf-cpp-full.so', 'libprotobuf-cpp-full-21.7.so'),
    (
        'vendor/bin/hw/vendor.qti.camera.provider@2.7-service_64',
        'vendor/lib64/camx.device@3.4-ext-impl.so',
        'vendor/lib64/camx.device@3.5-ext-impl.so',
        'vendor/lib64/camx.device@3.6-ext-impl.so',
        'vendor/lib64/camx.provider@2.4-external.so',
        'vendor/lib64/camx.provider@2.4-impl.so',
        'vendor/lib64/camx.provider@2.4-legacy.so',
        'vendor/lib64/camx.provider@2.5-external.so',
        'vendor/lib64/camx.provider@2.5-legacy.so',
        'vendor/lib64/camx.provider@2.6-legacy.so',
        'vendor/lib64/camx.provider@2.7-legacy.so',
        'vendor/lib64/libdpps.so',
        'vendor/lib64/libsnapdragoncolor-manager.so',
    ): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'Pong',
    'nothing',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
