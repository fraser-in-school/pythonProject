# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: baidu_realtime_bidding.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x62\x61idu_realtime_bidding.proto\x12\x04test\"\xbe\x39\n\nBidRequest\x12\n\n\x02id\x18\x01 \x02(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x12\n\nuser_agent\x18\x03 \x01(\t\x12\x15\n\rbaidu_user_id\x18\x04 \x01(\t\x12\x1d\n\x15\x62\x61idu_user_id_version\x18\x05 \x01(\x05\x12/\n\rbaidu_id_list\x18\x08 \x03(\x0b\x32\x18.test.BidRequest.BaiduId\x12\x15\n\rbuyer_user_id\x18  \x01(\t\x12\x15\n\ruser_category\x18\x06 \x03(\x03\x12?\n\x13\x63ustomized_user_tag\x18\x1f \x01(\x0b\x32\".test.BidRequest.CustomizedUserTag\x12\'\n\x06gender\x18\x07 \x01(\x0e\x32\x17.test.BidRequest.Gender\x12\x19\n\x11\x64\x65tected_language\x18\t \x01(\t\x12\x15\n\rflash_version\x18\n \x01(\t\x12+\n\ruser_geo_info\x18\x1c \x01(\x0b\x32\x14.test.BidRequest.Geo\x12\x0b\n\x03url\x18\x0b \x01(\t\x12\x0f\n\x07referer\x18\x0c \x01(\t\x12\x15\n\rsite_category\x18\r \x01(\x05\x12\x14\n\x0csite_quality\x18\x0e \x01(\x05\x12\x11\n\tpage_type\x18\x0f \x01(\x05\x12\x14\n\x0cpage_keyword\x18\x11 \x03(\t\x12\x14\n\x0cpage_quality\x18\x12 \x01(\x05\x12\x15\n\rpage_vertical\x18\x15 \x01(\x05\x12%\n\x19\x65xcluded_product_category\x18\x13 \x03(\x05\x42\x02\x10\x01\x12\'\n\x06mobile\x18\x1d \x01(\x0b\x32\x17.test.BidRequest.Mobile\x12%\n\x05video\x18\x1e \x01(\x0b\x32\x16.test.BidRequest.Video\x12\x32\n\x0c\x61rticle_info\x18! \x01(\x0b\x32\x1c.test.BidRequest.ArticleInfo\x12\'\n\x06\x61\x64slot\x18\x14 \x03(\x0b\x32\x17.test.BidRequest.AdSlot\x12\x0e\n\x06tag_id\x18\" \x03(\r\x12\x19\n\x11installed_app_ids\x18$ \x03(\x0c\x12\x19\n\x0e\x61ttribute_info\x18# \x01(\r:\x01\x30\x12\x16\n\x07is_test\x18\x1a \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07is_ping\x18\x1b \x01(\x08:\x05\x66\x61lse\x1a?\n\x07\x42\x61iduId\x12\x15\n\rbaidu_user_id\x18\x01 \x01(\t\x12\x1d\n\x15\x62\x61idu_user_id_version\x18\x02 \x01(\x05\x1a\xd7\x01\n\x11\x43ustomizedUserTag\x12?\n\x0c\x61ms_tag_list\x18\x01 \x03(\x0b\x32).test.BidRequest.CustomizedUserTag.AmsTag\x12K\n\x12installed_app_list\x18\x02 \x03(\x0b\x32/.test.BidRequest.CustomizedUserTag.InstalledApp\x1a\x18\n\x06\x41msTag\x12\x0e\n\x06tag_id\x18\x01 \x01(\x04\x1a\x1a\n\x0cInstalledApp\x12\n\n\x02id\x18\x01 \x02(\x04\x1a\xf8\x02\n\x03Geo\x12\x38\n\x0fuser_coordinate\x18\x01 \x03(\x0b\x32\x1f.test.BidRequest.Geo.Coordinate\x12\x38\n\ruser_location\x18\x02 \x01(\x0b\x32!.test.BidRequest.Geo.UserLocation\x1a\xaa\x01\n\nCoordinate\x12:\n\x08standard\x18\x01 \x01(\x0e\x32(.test.BidRequest.Geo.Coordinate.Standard\x12\x10\n\x08latitude\x18\x02 \x01(\x02\x12\x11\n\tlongitude\x18\x03 \x01(\x02\";\n\x08Standard\x12\t\n\x05\x42\x44_09\x10\x00\x12\n\n\x06GCJ_02\x10\x01\x12\n\n\x06WGS_84\x10\x02\x12\x0c\n\x08\x42\x44_09_LL\x10\x03\x1aP\n\x0cUserLocation\x12\x10\n\x08province\x18\x01 \x01(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\x12\x10\n\x08\x64istrict\x18\x03 \x01(\t\x12\x0e\n\x06street\x18\x04 \x01(\t\x1a\xd2\x0c\n\x06Mobile\x12\x1c\n\x14\x44\x45PRECATED_device_id\x18\x01 \x01(\t\x12,\n\x02id\x18\r \x03(\x0b\x32 .test.BidRequest.Mobile.MobileID\x12=\n\x0b\x64\x65vice_type\x18\x02 \x01(\x0e\x32(.test.BidRequest.Mobile.MobileDeviceType\x12\x38\n\x08platform\x18\x03 \x01(\x0e\x32\x1a.test.BidRequest.Mobile.OS:\nUNKNOWN_OS\x12;\n\nos_version\x18\x04 \x01(\x0b\x32\'.test.BidRequest.Mobile.DeviceOsVersion\x12\r\n\x05\x62rand\x18\x05 \x01(\t\x12\r\n\x05model\x18\x06 \x01(\t\x12\x14\n\x0cscreen_width\x18\x07 \x01(\x05\x12\x15\n\rscreen_height\x18\x08 \x01(\x05\x12\x16\n\x0escreen_density\x18\x0f \x01(\x02\x12\x12\n\ncarrier_id\x18\t \x01(\x03\x12J\n\x15wireless_network_type\x18\n \x01(\x0e\x32+.test.BidRequest.Mobile.WirelessNetworkType\x12%\n\x1d\x44\x45PRECATED_for_advertising_id\x18\x0b \x01(\t\x12\x44\n\x12\x66or_advertising_id\x18\x0e \x03(\x0b\x32(.test.BidRequest.Mobile.ForAdvertisingID\x12\x35\n\nmobile_app\x18\x0c \x01(\x0b\x32!.test.BidRequest.Mobile.MobileApp\x1a\xd2\x01\n\x08MobileID\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.test.BidRequest.Mobile.MobileID.IDType\x12\n\n\x02id\x18\x02 \x01(\t\x12\x1a\n\x12generate_timestamp\x18\x03 \x01(\x04\x12\x0f\n\x07version\x18\x04 \x01(\x0c\x12\x0e\n\x06vendor\x18\x05 \x01(\r\"F\n\x06IDType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04IMEI\x10\x01\x12\x07\n\x03MAC\x10\x02\x12\x08\n\x04\x43UID\x10\x03\x12\x08\n\x04OAID\x10\x04\x12\x08\n\x04\x43\x41ID\x10\x05\x1a_\n\x0f\x44\x65viceOsVersion\x12\x18\n\x10os_version_major\x18\x01 \x01(\x05\x12\x18\n\x10os_version_minor\x18\x02 \x01(\x05\x12\x18\n\x10os_version_micro\x18\x03 \x01(\x05\x1a\x8e\x01\n\x10\x46orAdvertisingID\x12=\n\x04type\x18\x01 \x01(\x0e\x32/.test.BidRequest.Mobile.ForAdvertisingID.IDType\x12\n\n\x02id\x18\x02 \x01(\t\"/\n\x06IDType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nANDROID_ID\x10\x04\x12\x08\n\x04IDFA\x10\x05\x1a\x8c\x02\n\tMobileApp\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x15\n\rapp_bundle_id\x18\x02 \x01(\t\x12\x14\n\x0c\x61pp_category\x18\x03 \x01(\x05\x12\x18\n\x10\x61pp_publisher_id\x18\x04 \x01(\x05\x12R\n\x14\x61pp_interaction_type\x18\x05 \x03(\x0e\x32\x34.test.BidRequest.Mobile.MobileApp.AppInteractionType\x12\x13\n\x0b\x61pp_version\x18\x06 \x01(\t\"?\n\x12\x41ppInteractionType\x12\r\n\tTELEPHONE\x10\x00\x12\x0c\n\x08\x44OWNLOAD\x10\x01\x12\x0c\n\x08\x44\x45\x45PLINK\x10\x02\"g\n\x10MobileDeviceType\x12\x12\n\x0eUNKNOWN_DEVICE\x10\x00\x12\x11\n\rHIGHEND_PHONE\x10\x01\x12\n\n\x06TABLET\x10\x02\x12\x0c\n\x08SMART_TV\x10\x04\x12\x12\n\x0eOUTDOOR_SCREEN\x10\x05\"=\n\x02OS\x12\x0e\n\nUNKNOWN_OS\x10\x00\x12\x07\n\x03IOS\x10\x01\x12\x0b\n\x07\x41NDROID\x10\x02\x12\x11\n\rWINDOWS_PHONE\x10\x03\"a\n\x13WirelessNetworkType\x12\x13\n\x0fUNKNOWN_NETWORK\x10\x00\x12\x08\n\x04WIFI\x10\x01\x12\r\n\tMOBILE_2G\x10\x02\x12\r\n\tMOBILE_3G\x10\x03\x12\r\n\tMOBILE_4G\x10\x04\x1aP\n\x05Video\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\x12\x16\n\x0e\x63ontent_length\x18\x03 \x01(\x05\x12\x12\n\nchannel_id\x18\x04 \x03(\x03\x1a\\\n\x0b\x41rticleInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\x0c\x12\x10\n\x08\x63\x61tegory\x18\x03 \x03(\x0c\x12\r\n\x05label\x18\x04 \x03(\x0c\x12\x11\n\tauthor_id\x18\x05 \x01(\x0c\x1a\xf2\x1e\n\x06\x41\x64Slot\x12\x14\n\x0c\x61\x64_block_key\x18\x01 \x01(\x04\x12\x13\n\x0b\x61\x64_block_id\x18\x1c \x01(\x0c\x12\x13\n\x0bsequence_id\x18\x02 \x01(\x05\x12\x0b\n\x02id\x18\xe9\x07 \x01(\t\x12\x13\n\x0b\x61\x64slot_type\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12\x14\n\x0c\x61\x63tual_width\x18\x12 \x01(\x05\x12\x15\n\ractual_height\x18\x13 \x01(\x05\x12\x17\n\x0fslot_visibility\x18\x06 \x01(\x05\x12\x19\n\rcreative_type\x18\x07 \x03(\x05\x42\x02\x10\x01\x12\x44\n\x12\x63reative_desc_type\x18\x16 \x03(\x0e\x32(.test.BidRequest.AdSlot.CreativeDescType\x12!\n\x19\x65xcluded_landing_page_url\x18\x08 \x03(\t\x12\"\n\x1apublisher_settings_list_id\x18\x0e \x03(\x06\x12\x13\n\x0bminimum_cpm\x18\t \x01(\x05\x12\x1a\n\x12max_video_duration\x18\n \x01(\x05\x12\x1a\n\x12min_video_duration\x18\x0b \x01(\x05\x12\x19\n\x11video_start_delay\x18\x0c \x01(\x05\x12\x35\n\nvideo_info\x18\x0f \x01(\x0b\x32!.test.BidRequest.AdSlot.VideoInfo\x12<\n\x0elink_unit_info\x18\x10 \x01(\x0b\x32$.test.BidRequest.AdSlot.LinkUnitInfo\x12H\n\x14preferred_order_info\x18\r \x01(\x0b\x32*.test.BidRequest.AdSlot.PreferredOrderInfo\x12\x42\n\x11guaranteed_orders\x18\x14 \x03(\x0b\x32\'.test.BidRequest.AdSlot.GuaranteedOrder\x12H\n\x14\x65xpand_creative_info\x18\x11 \x01(\x0b\x32*.test.BidRequest.AdSlot.ExpandCreativeInfo\x12L\n\x0c\x61\x64slot_level\x18\x15 \x01(\x0e\x32#.test.BidRequest.AdSlot.AdSlotLevel:\x11UNKNOWN_ADB_LEVEL\x12\"\n\x14\x61llowed_non_nativead\x18\x17 \x01(\x08:\x04true\x12=\n\x0enativead_param\x18\x18 \x01(\x0b\x32%.test.BidRequest.AdSlot.NativeAdParam\x12\x15\n\x06secure\x18\x19 \x01(\x08:\x05\x66\x61lse\x12\x35\n\nstyle_info\x18\x1a \x03(\x0b\x32!.test.BidRequest.AdSlot.StyleInfo\x12\x16\n\x0einventory_type\x18\x1b \x03(\x05\x12\x12\n\nmax_ad_num\x18\x1d \x01(\x05\x1a^\n\tVideoInfo\x12\x1a\n\x12max_video_duration\x18\x01 \x01(\x05\x12\x1a\n\x12min_video_duration\x18\x02 \x01(\x05\x12\x19\n\x11video_start_delay\x18\x03 \x01(\x05\x1a\xcd\x01\n\x0cLinkUnitInfo\x12\x12\n\nstyle_type\x18\x01 \x03(\x05\x12\x17\n\x0freq_keyword_num\x18\x02 \x01(\x05\x12\x18\n\x10proposed_keyword\x18\x03 \x03(\t\x12\x46\n\x08keywords\x18\x04 \x03(\x0b\x32\x34.test.BidRequest.AdSlot.LinkUnitInfo.ProposedKeyword\x1a.\n\x0fProposedKeyword\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05pctr1\x18\x02 \x01(\x02\x1a\xbd\x01\n\x12PreferredOrderInfo\x12S\n\x10preferred_orders\x18\x01 \x03(\x0b\x32\x39.test.BidRequest.AdSlot.PreferredOrderInfo.PreferredOrder\x12\x1b\n\rallow_auction\x18\x02 \x01(\x08:\x04true\x1a\x35\n\x0ePreferredOrder\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x11\n\tfixed_cpm\x18\x02 \x01(\x03\x1a\x90\x02\n\x0fGuaranteedOrder\x12\x10\n\x08order_id\x18\x01 \x01(\r\x12>\n\x06\x63harge\x18\x02 \x01(\x0b\x32..test.BidRequest.AdSlot.GuaranteedOrder.Charge\x1a\xaa\x01\n\x06\x43harge\x12\r\n\x05price\x18\x01 \x01(\x05\x12]\n\x0b\x63harge_mode\x18\x02 \x01(\x0e\x32\x39.test.BidRequest.AdSlot.GuaranteedOrder.Charge.ChargeType:\rCHARGE_GD_CPM\"2\n\nChargeType\x12\x11\n\rCHARGE_GD_CPM\x10\x02\x12\x11\n\rCHARGE_GD_CPT\x10\x03\x1a\xae\x03\n\x12\x45xpandCreativeInfo\x12Q\n\x12\x65xpand_action_type\x18\x01 \x03(\x0e\x32\x35.test.BidRequest.AdSlot.ExpandCreativeInfo.ActionType\x12N\n\x10\x65xpand_direction\x18\x02 \x01(\x0e\x32\x34.test.BidRequest.AdSlot.ExpandCreativeInfo.Direction\x12 \n\x14\x65xpand_creative_type\x18\x03 \x03(\x05\x42\x02\x10\x01\x12\x14\n\x0c\x65xpand_width\x18\x04 \x01(\x05\x12\x15\n\rexpand_height\x18\x05 \x01(\x05\x12\x17\n\x0f\x65xpand_duration\x18\x06 \x01(\x05\",\n\nActionType\x12\t\n\x05HOVER\x10\x01\x12\t\n\x05\x43LICK\x10\x02\x12\x08\n\x04LOAD\x10\x03\"_\n\tDirection\x12\x0f\n\x0b\x45XPAND_NONE\x10\x00\x12\r\n\tEXPAND_UP\x10\x01\x12\x0f\n\x0b\x45XPAND_DOWN\x10\x02\x12\x0f\n\x0b\x45XPAND_LEFT\x10\x03\x12\x10\n\x0c\x45XPAND_RIGHT\x10\x04\x1a\x8e\x03\n\rNativeAdParam\x12\x17\n\x0frequired_fields\x18\x01 \x03(\x03\x12\x18\n\x10title_max_length\x18\x02 \x01(\x05\x12\x17\n\x0f\x64\x65sc_max_length\x18\x03 \x01(\x05\x12\x41\n\tlogo_icon\x18\x04 \x01(\x0b\x32..test.BidRequest.AdSlot.NativeAdParam.ImageEle\x12=\n\x05image\x18\x05 \x01(\x0b\x32..test.BidRequest.AdSlot.NativeAdParam.ImageEle\x12\x11\n\timage_num\x18\x06 \x01(\x05\x1a;\n\x08ImageEle\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x10\n\x05shape\x18\x03 \x01(\x05:\x01\x30\"_\n\x06\x46ields\x12\t\n\x05TITLE\x10\x01\x12\x08\n\x04\x44\x45SC\x10\x02\x12\t\n\x05IMAGE\x10\x04\x12\x0c\n\x08LOGOICON\x10\x08\x12\x0b\n\x07\x41PPSIZE\x10\x10\x12\t\n\x05VIDEO\x10@\x12\x0f\n\nBRAND_NAME\x10\x80\x01\x1a\xc9\x08\n\tStyleInfo\x12\x12\n\nstyle_type\x18\x01 \x01(\x05\x12;\n\x08\x61\x64_style\x18\x02 \x01(\x0b\x32).test.BidRequest.AdSlot.StyleInfo.AdStyle\x1a\xea\x07\n\x07\x41\x64Style\x12R\n\x10meta_style_group\x18\x03 \x03(\x0b\x32\x38.test.BidRequest.AdSlot.StyleInfo.AdStyle.MetaStyleGroup\x1a.\n\nTxtElement\x12\x0f\n\x07min_len\x18\x01 \x01(\x05\x12\x0f\n\x07max_len\x18\x02 \x01(\x05\x1a-\n\x0cImageElement\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x1a\xa3\x01\n\x0cVideoElement\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x0c\n\x04size\x18\x03 \x01(\x05\x12\x10\n\x08\x65ncoding\x18\x04 \x03(\t\x12\x13\n\x0bmin_bitrate\x18\x05 \x01(\x05\x12\x13\n\x0bmax_bitrate\x18\x06 \x01(\x05\x12\x14\n\x0cmax_duration\x18\x07 \x01(\x05\x12\x14\n\x0cmin_duration\x18\x08 \x01(\x05\x1a\x97\x03\n\tMetaStyle\x12\x19\n\x11required_elements\x18\x01 \x01(\x03\x12G\n\ttitle_ele\x18\x02 \x03(\x0b\x32\x34.test.BidRequest.AdSlot.StyleInfo.AdStyle.TxtElement\x12\x46\n\x08\x64\x65sc_ele\x18\x03 \x03(\x0b\x32\x34.test.BidRequest.AdSlot.StyleInfo.AdStyle.TxtElement\x12H\n\x08icon_ele\x18\x04 \x03(\x0b\x32\x36.test.BidRequest.AdSlot.StyleInfo.AdStyle.ImageElement\x12I\n\timage_ele\x18\x05 \x03(\x0b\x32\x36.test.BidRequest.AdSlot.StyleInfo.AdStyle.ImageElement\x12I\n\tvideo_ele\x18\x06 \x03(\x0b\x32\x36.test.BidRequest.AdSlot.StyleInfo.AdStyle.VideoElement\x1a\x66\n\x0eMetaStyleGroup\x12\x0b\n\x03num\x18\x01 \x01(\x05\x12G\n\nmeta_style\x18\x02 \x01(\x0b\x32\x33.test.BidRequest.AdSlot.StyleInfo.AdStyle.MetaStyle\"\x83\x01\n\x0bMetaElement\x12\x12\n\x0eMETA_ELE_TITLE\x10\x01\x12\x11\n\rMETA_ELE_DESC\x10\x02\x12\x11\n\rMETA_ELE_ICON\x10\x04\x12\x12\n\x0eMETA_ELE_IMAGE\x10\x08\x12\x12\n\x0eMETA_ELE_BRAND\x10\x10\x12\x12\n\x0eMETA_ELE_VIDEO\x10 \"=\n\x10\x43reativeDescType\x12\x13\n\x0fSTATIC_CREATIVE\x10\x01\x12\x14\n\x10\x44YNAMIC_CREATIVE\x10\x02\"I\n\x0b\x41\x64SlotLevel\x12\x15\n\x11UNKNOWN_ADB_LEVEL\x10\x00\x12\x07\n\x03TOP\x10\x01\x12\x07\n\x03MED\x10\x02\x12\x08\n\x04TAIL\x10\x03\x12\x07\n\x03LOW\x10\x04\"+\n\x06Gender\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06\x46\x45MALE\x10\x02\"\xdf\x1d\n\x0b\x42idResponse\x12\n\n\x02id\x18\x01 \x02(\t\x12 \n\x02\x61\x64\x18\x02 \x03(\x0b\x32\x14.test.BidResponse.Ad\x12\x14\n\x0c\x64\x65\x62ug_string\x18\x03 \x01(\t\x12\x1a\n\x12processing_time_ms\x18\x04 \x01(\x05\x12\x15\n\rads_num_limit\x18\x05 \x01(\x05\x1a\xd8\x1c\n\x02\x41\x64\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x05\x12\x0e\n\x05impid\x18\xea\x07 \x01(\t\x12\x13\n\x0b\x63reative_id\x18\x02 \x01(\x03\x12\x14\n\x0chtml_snippet\x18\x07 \x01(\t\x12?\n\x11link_unit_keyword\x18\x12 \x01(\x0b\x32$.test.BidResponse.Ad.LinkUnitKeyword\x12\x45\n\x14\x65xpand_creative_info\x18\x13 \x01(\x0b\x32\'.test.BidResponse.Ad.ExpandCreativeInfo\x12\x15\n\radvertiser_id\x18\x08 \x01(\x04\x12\r\n\x05width\x18\t \x01(\x05\x12\x0e\n\x06height\x18\n \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x0b \x01(\x05\x12\x0c\n\x04type\x18\x0c \x01(\x05\x12\x14\n\x0clanding_page\x18\r \x01(\t\x12\x12\n\ntarget_url\x18\x0e \x03(\t\x12\x14\n\x0cmonitor_urls\x18\x11 \x03(\t\x12\x0c\n\x04nurl\x18  \x01(\t\x12\x0f\n\x07max_cpm\x18\x03 \x01(\x05\x12\x0f\n\x07\x65xtdata\x18\x05 \x01(\t\x12\x0c\n\x04\x65xt1\x18\x17 \x01(\t\x12\x0c\n\x04\x65xt2\x18\x18 \x01(\t\x12\x0c\n\x04\x65xt3\x18\x19 \x01(\t\x12\x1a\n\x12is_cookie_matching\x18\x06 \x01(\x08\x12\x1a\n\x12preferred_order_id\x18\x0f \x01(\t\x12\x1b\n\x13guaranteed_order_id\x18\x14 \x01(\r\x12\x38\n\rdeeplink_info\x18\x15 \x01(\x0b\x32!.test.BidResponse.Ad.DeeplinkInfo\x12\x30\n\tnative_ad\x18\x16 \x01(\x0b\x32\x1d.test.BidResponse.Ad.NativeAd\x12\x38\n\rmaterial_info\x18\x1a \x03(\x0b\x32!.test.BidResponse.Ad.MaterialInfo\x12;\n\x0fmeta_info_group\x18\x1b \x03(\x0b\x32\".test.BidResponse.Ad.MetaInfoGroup\x12\x38\n\rdownload_info\x18\x1c \x01(\x0b\x32!.test.BidResponse.Ad.DownloadInfo\x12\x18\n\x10\x63ustmer_ext_data\x18\x1d \x01(\x0c\x12\x16\n\x0b\x62udget_type\x18\x1e \x01(\x05:\x01\x30\x12\x0e\n\x03\x62id\x18\x1f \x01(\x05:\x01\x30\x12\x12\n\nstyle_type\x18! \x01(\x05\x12\x16\n\x0b\x63harge_type\x18\" \x01(\x05:\x01\x30\x1a?\n\x0fLinkUnitKeyword\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12\x1b\n\x13selected_style_type\x18\x02 \x03(\x05\x1a{\n\x12\x45xpandCreativeInfo\x12\x16\n\x0e\x63reative_width\x18\x01 \x01(\x05\x12\x17\n\x0f\x63reative_height\x18\x02 \x01(\x05\x12\x1d\n\x15\x63reative_landing_page\x18\x03 \x01(\t\x12\x15\n\rcreative_type\x18\x04 \x01(\x05\x1a\x82\x02\n\x0c\x44\x65\x65plinkInfo\x12\x14\n\x0c\x64\x65\x65plink_url\x18\x01 \x01(\t\x12\x13\n\x0b\x61pp_version\x18\x02 \x01(\r\x12\x14\n\x0c\x66\x61llback_url\x18\x03 \x01(\t\x12\x15\n\rfallback_type\x18\x04 \x01(\r\x12\x15\n\rapp_bundle_id\x18\x05 \x01(\x0c\x12\x11\n\tpublisher\x18\x06 \x01(\x0c\x12\x1c\n\x14\x64ownload_app_version\x18\x07 \x01(\x0c\x12\x14\n\x0cprivacy_link\x18\x08 \x01(\x0c\x12\x17\n\x0fpermission_link\x18\t \x01(\x0c\x12\x0f\n\x07ulk_url\x18\n \x01(\x0c\x12\x12\n\nulk_scheme\x18\x0b \x01(\x0c\x1a\xd5\x02\n\x08NativeAd\x12\r\n\x05title\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\x0c\x12\x32\n\x05image\x18\x03 \x03(\x0b\x32#.test.BidResponse.Ad.NativeAd.Image\x12\x36\n\tlogo_icon\x18\x04 \x01(\x0b\x32#.test.BidResponse.Ad.NativeAd.Image\x12\x10\n\x08\x61pp_size\x18\x05 \x01(\x05\x12\x12\n\nbrand_name\x18\x06 \x01(\x0c\x12\x0f\n\x07keyword\x18\x07 \x03(\x0c\x12\x11\n\tvideo_url\x18\x08 \x01(\t\x12\x13\n\x0bvideo_width\x18\t \x01(\x05\x12\x14\n\x0cvideo_height\x18\n \x01(\x05\x12\x16\n\x0evideo_duration\x18\x0b \x01(\x05\x1a\x33\n\x05Image\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x1a\xc8\x02\n\x0cMaterialInfo\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x14\n\x0cmaterial_url\x18\x03 \x01(\t\x12\x16\n\x0evideo_duration\x18\x04 \x01(\x05\x12K\n\x10material_pattern\x18\x05 \x01(\x0e\x32\x31.test.BidResponse.Ad.MaterialInfo.MaterialPattern\x12\"\n\x1amaterial_position_vertical\x18\x06 \x01(\x02\x12\x14\n\x0cmaterial_md5\x18\x07 \x01(\t\x12\x0f\n\x07keyword\x18\x08 \x03(\x0c\"U\n\x0fMaterialPattern\x12 \n\x1cMATERIAL_PATTERN_FULL_SCREEN\x10\x01\x12 \n\x1cMATERIAL_PATTERN_HALF_SCREEN\x10\x02\x1a\xae\n\n\x08MetaInfo\x12=\n\x0b\x61\x63tion_info\x18\x01 \x01(\x0b\x32(.test.BidResponse.Ad.MetaInfo.ActionInfo\x12\x38\n\x05title\x18\x02 \x03(\x0b\x32).test.BidResponse.Ad.MetaInfo.TxtMaterial\x12\x37\n\x04\x64\x65sc\x18\x03 \x03(\x0b\x32).test.BidResponse.Ad.MetaInfo.TxtMaterial\x12\x37\n\x04icon\x18\x04 \x03(\x0b\x32).test.BidResponse.Ad.MetaInfo.SrcMaterial\x12\x38\n\x05image\x18\x05 \x03(\x0b\x32).test.BidResponse.Ad.MetaInfo.SrcMaterial\x12;\n\nbrand_info\x18\x06 \x01(\x0b\x32\'.test.BidResponse.Ad.MetaInfo.BrandInfo\x12\x10\n\x08\x63\x61tegory\x18\x07 \x03(\x05\x12\x38\n\x05video\x18\t \x03(\x0b\x32).test.BidResponse.Ad.MetaInfo.SrcMaterial\x12\x37\n\x08\x61pp_info\x18\n \x01(\x0b\x32%.test.BidResponse.Ad.MetaInfo.AppInfo\x12\x38\n\rdeeplink_info\x18\x0b \x01(\x0b\x32!.test.BidResponse.Ad.DeeplinkInfo\x12\x39\n\x06\x62utton\x18\r \x03(\x0b\x32).test.BidResponse.Ad.MetaInfo.SrcMaterial\x12\x15\n\rcreative_type\x18\x0f \x01(\x05\x12\x0f\n\x07keyword\x18\x10 \x03(\x0c\x1a\xad\x01\n\nActionInfo\x12\x12\n\naction_url\x18\x01 \x01(\x0c\x12\x14\n\x0clanding_page\x18\x02 \x01(\x0c\x12\x13\n\x0b\x61\x63tion_type\x18\x04 \x01(\x05\x12\x19\n\x11\x63lick_monitor_url\x18\x06 \x03(\x0c\x12\x18\n\x10\x61pp_download_url\x18\x07 \x01(\x0c\x12\x16\n\x0e\x61pp_store_link\x18\x08 \x01(\x0c\x12\x13\n\x0b\x63harge_link\x18\t \x01(\x0c\x1a\x1a\n\x0bTxtMaterial\x12\x0b\n\x03txt\x18\x01 \x01(\x0c\x1a\xab\x01\n\x0bSrcMaterial\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0b\n\x03url\x18\x02 \x01(\x0c\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x16\n\x0evideo_duration\x18\x05 \x01(\x05\x12\x0c\n\x04size\x18\x06 \x01(\x05\x12\x0f\n\x07\x62itrate\x18\x07 \x01(\x05\x12\x10\n\x08\x65ncoding\x18\x08 \x01(\t\x12\x0b\n\x03md5\x18\t \x01(\t\x12\x0c\n\x04text\x18\n \x01(\x0c\x1a\x34\n\tBrandInfo\x12\x12\n\nbrand_name\x18\x01 \x01(\x0c\x12\x13\n\x0b\x62rand_level\x18\x02 \x01(\x05\x1a\xed\x01\n\x07\x41ppInfo\x12\x10\n\x08\x61pp_name\x18\x01 \x01(\x0c\x12\x14\n\x0cpackage_name\x18\x02 \x01(\x0c\x12\x10\n\x08\x61pk_name\x18\x03 \x01(\x0c\x12\x0c\n\x04size\x18\x04 \x01(\x05\x12\x11\n\tdownloads\x18\x05 \x01(\x05\x12\x0e\n\x06rating\x18\x06 \x01(\x02\x12\x10\n\x08\x63omments\x18\x07 \x01(\x05\x12\x0e\n\x06\x61pp_id\x18\x08 \x01(\x0c\x12\x11\n\tpublisher\x18\t \x01(\x0c\x12\x13\n\x0b\x61pp_version\x18\n \x01(\x0c\x12\x14\n\x0cprivacy_link\x18\x0b \x01(\x0c\x12\x17\n\x0fpermission_link\x18\x0c \x01(\x0c\x1a\x41\n\rMetaInfoGroup\x12\x30\n\tmeta_info\x18\x01 \x03(\x0b\x32\x1d.test.BidResponse.Ad.MetaInfo\x1a\xc8\x01\n\x0c\x44ownloadInfo\x12\x10\n\x08\x61pp_size\x18\x01 \x01(\x05\x12\x18\n\x10\x61pp_package_name\x18\x02 \x01(\t\x12\x0e\n\x06ios_id\x18\x07 \x01(\t\x12\x0e\n\x06\x64oc_id\x18\x08 \x01(\t\x12\x15\n\rdownload_desc\x18\t \x01(\t\x12\x11\n\tpublisher\x18\x03 \x01(\x0c\x12\x13\n\x0b\x61pp_version\x18\x04 \x01(\x0c\x12\x14\n\x0cprivacy_link\x18\x05 \x01(\x0c\x12\x17\n\x0fpermission_link\x18\x06 \x01(\x0c*\x05\x08\x64\x10\xc8\x01:\'\n\tad_status\x12\x14.test.BidResponse.Ad\x18\x65 \x01(\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'baidu_realtime_bidding_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _BIDREQUEST_ADSLOT_EXPANDCREATIVEINFO.fields_by_name['expand_creative_type']._options = None
  _BIDREQUEST_ADSLOT_EXPANDCREATIVEINFO.fields_by_name['expand_creative_type']._serialized_options = b'\020\001'
  _BIDREQUEST_ADSLOT.fields_by_name['creative_type']._options = None
  _BIDREQUEST_ADSLOT.fields_by_name['creative_type']._serialized_options = b'\020\001'
  _BIDREQUEST.fields_by_name['excluded_product_category']._options = None
  _BIDREQUEST.fields_by_name['excluded_product_category']._serialized_options = b'\020\001'
  _globals['_BIDREQUEST']._serialized_start=39
  _globals['_BIDREQUEST']._serialized_end=7397
  _globals['_BIDREQUEST_BAIDUID']._serialized_start=938
  _globals['_BIDREQUEST_BAIDUID']._serialized_end=1001
  _globals['_BIDREQUEST_CUSTOMIZEDUSERTAG']._serialized_start=1004
  _globals['_BIDREQUEST_CUSTOMIZEDUSERTAG']._serialized_end=1219
  _globals['_BIDREQUEST_CUSTOMIZEDUSERTAG_AMSTAG']._serialized_start=1167
  _globals['_BIDREQUEST_CUSTOMIZEDUSERTAG_AMSTAG']._serialized_end=1191
  _globals['_BIDREQUEST_CUSTOMIZEDUSERTAG_INSTALLEDAPP']._serialized_start=1193
  _globals['_BIDREQUEST_CUSTOMIZEDUSERTAG_INSTALLEDAPP']._serialized_end=1219
  _globals['_BIDREQUEST_GEO']._serialized_start=1222
  _globals['_BIDREQUEST_GEO']._serialized_end=1598
  _globals['_BIDREQUEST_GEO_COORDINATE']._serialized_start=1346
  _globals['_BIDREQUEST_GEO_COORDINATE']._serialized_end=1516
  _globals['_BIDREQUEST_GEO_COORDINATE_STANDARD']._serialized_start=1457
  _globals['_BIDREQUEST_GEO_COORDINATE_STANDARD']._serialized_end=1516
  _globals['_BIDREQUEST_GEO_USERLOCATION']._serialized_start=1518
  _globals['_BIDREQUEST_GEO_USERLOCATION']._serialized_end=1598
  _globals['_BIDREQUEST_MOBILE']._serialized_start=1601
  _globals['_BIDREQUEST_MOBILE']._serialized_end=3219
  _globals['_BIDREQUEST_MOBILE_MOBILEID']._serialized_start=2229
  _globals['_BIDREQUEST_MOBILE_MOBILEID']._serialized_end=2439
  _globals['_BIDREQUEST_MOBILE_MOBILEID_IDTYPE']._serialized_start=2369
  _globals['_BIDREQUEST_MOBILE_MOBILEID_IDTYPE']._serialized_end=2439
  _globals['_BIDREQUEST_MOBILE_DEVICEOSVERSION']._serialized_start=2441
  _globals['_BIDREQUEST_MOBILE_DEVICEOSVERSION']._serialized_end=2536
  _globals['_BIDREQUEST_MOBILE_FORADVERTISINGID']._serialized_start=2539
  _globals['_BIDREQUEST_MOBILE_FORADVERTISINGID']._serialized_end=2681
  _globals['_BIDREQUEST_MOBILE_FORADVERTISINGID_IDTYPE']._serialized_start=2634
  _globals['_BIDREQUEST_MOBILE_FORADVERTISINGID_IDTYPE']._serialized_end=2681
  _globals['_BIDREQUEST_MOBILE_MOBILEAPP']._serialized_start=2684
  _globals['_BIDREQUEST_MOBILE_MOBILEAPP']._serialized_end=2952
  _globals['_BIDREQUEST_MOBILE_MOBILEAPP_APPINTERACTIONTYPE']._serialized_start=2889
  _globals['_BIDREQUEST_MOBILE_MOBILEAPP_APPINTERACTIONTYPE']._serialized_end=2952
  _globals['_BIDREQUEST_MOBILE_MOBILEDEVICETYPE']._serialized_start=2954
  _globals['_BIDREQUEST_MOBILE_MOBILEDEVICETYPE']._serialized_end=3057
  _globals['_BIDREQUEST_MOBILE_OS']._serialized_start=3059
  _globals['_BIDREQUEST_MOBILE_OS']._serialized_end=3120
  _globals['_BIDREQUEST_MOBILE_WIRELESSNETWORKTYPE']._serialized_start=3122
  _globals['_BIDREQUEST_MOBILE_WIRELESSNETWORKTYPE']._serialized_end=3219
  _globals['_BIDREQUEST_VIDEO']._serialized_start=3221
  _globals['_BIDREQUEST_VIDEO']._serialized_end=3301
  _globals['_BIDREQUEST_ARTICLEINFO']._serialized_start=3303
  _globals['_BIDREQUEST_ARTICLEINFO']._serialized_end=3395
  _globals['_BIDREQUEST_ADSLOT']._serialized_start=3398
  _globals['_BIDREQUEST_ADSLOT']._serialized_end=7352
  _globals['_BIDREQUEST_ADSLOT_VIDEOINFO']._serialized_start=4511
  _globals['_BIDREQUEST_ADSLOT_VIDEOINFO']._serialized_end=4605
  _globals['_BIDREQUEST_ADSLOT_LINKUNITINFO']._serialized_start=4608
  _globals['_BIDREQUEST_ADSLOT_LINKUNITINFO']._serialized_end=4813
  _globals['_BIDREQUEST_ADSLOT_LINKUNITINFO_PROPOSEDKEYWORD']._serialized_start=4767
  _globals['_BIDREQUEST_ADSLOT_LINKUNITINFO_PROPOSEDKEYWORD']._serialized_end=4813
  _globals['_BIDREQUEST_ADSLOT_PREFERREDORDERINFO']._serialized_start=4816
  _globals['_BIDREQUEST_ADSLOT_PREFERREDORDERINFO']._serialized_end=5005
  _globals['_BIDREQUEST_ADSLOT_PREFERREDORDERINFO_PREFERREDORDER']._serialized_start=4952
  _globals['_BIDREQUEST_ADSLOT_PREFERREDORDERINFO_PREFERREDORDER']._serialized_end=5005
  _globals['_BIDREQUEST_ADSLOT_GUARANTEEDORDER']._serialized_start=5008
  _globals['_BIDREQUEST_ADSLOT_GUARANTEEDORDER']._serialized_end=5280
  _globals['_BIDREQUEST_ADSLOT_GUARANTEEDORDER_CHARGE']._serialized_start=5110
  _globals['_BIDREQUEST_ADSLOT_GUARANTEEDORDER_CHARGE']._serialized_end=5280
  _globals['_BIDREQUEST_ADSLOT_GUARANTEEDORDER_CHARGE_CHARGETYPE']._serialized_start=5230
  _globals['_BIDREQUEST_ADSLOT_GUARANTEEDORDER_CHARGE_CHARGETYPE']._serialized_end=5280
  _globals['_BIDREQUEST_ADSLOT_EXPANDCREATIVEINFO']._serialized_start=5283
  _globals['_BIDREQUEST_ADSLOT_EXPANDCREATIVEINFO']._serialized_end=5713
  _globals['_BIDREQUEST_ADSLOT_EXPANDCREATIVEINFO_ACTIONTYPE']._serialized_start=5572
  _globals['_BIDREQUEST_ADSLOT_EXPANDCREATIVEINFO_ACTIONTYPE']._serialized_end=5616
  _globals['_BIDREQUEST_ADSLOT_EXPANDCREATIVEINFO_DIRECTION']._serialized_start=5618
  _globals['_BIDREQUEST_ADSLOT_EXPANDCREATIVEINFO_DIRECTION']._serialized_end=5713
  _globals['_BIDREQUEST_ADSLOT_NATIVEADPARAM']._serialized_start=5716
  _globals['_BIDREQUEST_ADSLOT_NATIVEADPARAM']._serialized_end=6114
  _globals['_BIDREQUEST_ADSLOT_NATIVEADPARAM_IMAGEELE']._serialized_start=5958
  _globals['_BIDREQUEST_ADSLOT_NATIVEADPARAM_IMAGEELE']._serialized_end=6017
  _globals['_BIDREQUEST_ADSLOT_NATIVEADPARAM_FIELDS']._serialized_start=6019
  _globals['_BIDREQUEST_ADSLOT_NATIVEADPARAM_FIELDS']._serialized_end=6114
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO']._serialized_start=6117
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO']._serialized_end=7214
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE']._serialized_start=6212
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE']._serialized_end=7214
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_TXTELEMENT']._serialized_start=6307
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_TXTELEMENT']._serialized_end=6353
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_IMAGEELEMENT']._serialized_start=6355
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_IMAGEELEMENT']._serialized_end=6400
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_VIDEOELEMENT']._serialized_start=6403
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_VIDEOELEMENT']._serialized_end=6566
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_METASTYLE']._serialized_start=6569
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_METASTYLE']._serialized_end=6976
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_METASTYLEGROUP']._serialized_start=6978
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_METASTYLEGROUP']._serialized_end=7080
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_METAELEMENT']._serialized_start=7083
  _globals['_BIDREQUEST_ADSLOT_STYLEINFO_ADSTYLE_METAELEMENT']._serialized_end=7214
  _globals['_BIDREQUEST_ADSLOT_CREATIVEDESCTYPE']._serialized_start=7216
  _globals['_BIDREQUEST_ADSLOT_CREATIVEDESCTYPE']._serialized_end=7277
  _globals['_BIDREQUEST_ADSLOT_ADSLOTLEVEL']._serialized_start=7279
  _globals['_BIDREQUEST_ADSLOT_ADSLOTLEVEL']._serialized_end=7352
  _globals['_BIDREQUEST_GENDER']._serialized_start=7354
  _globals['_BIDREQUEST_GENDER']._serialized_end=7397
  _globals['_BIDRESPONSE']._serialized_start=7400
  _globals['_BIDRESPONSE']._serialized_end=11207
  _globals['_BIDRESPONSE_AD']._serialized_start=7535
  _globals['_BIDRESPONSE_AD']._serialized_end=11207
  _globals['_BIDRESPONSE_AD_LINKUNITKEYWORD']._serialized_start=8477
  _globals['_BIDRESPONSE_AD_LINKUNITKEYWORD']._serialized_end=8540
  _globals['_BIDRESPONSE_AD_EXPANDCREATIVEINFO']._serialized_start=8542
  _globals['_BIDRESPONSE_AD_EXPANDCREATIVEINFO']._serialized_end=8665
  _globals['_BIDRESPONSE_AD_DEEPLINKINFO']._serialized_start=8668
  _globals['_BIDRESPONSE_AD_DEEPLINKINFO']._serialized_end=8926
  _globals['_BIDRESPONSE_AD_NATIVEAD']._serialized_start=8929
  _globals['_BIDRESPONSE_AD_NATIVEAD']._serialized_end=9270
  _globals['_BIDRESPONSE_AD_NATIVEAD_IMAGE']._serialized_start=9219
  _globals['_BIDRESPONSE_AD_NATIVEAD_IMAGE']._serialized_end=9270
  _globals['_BIDRESPONSE_AD_MATERIALINFO']._serialized_start=9273
  _globals['_BIDRESPONSE_AD_MATERIALINFO']._serialized_end=9601
  _globals['_BIDRESPONSE_AD_MATERIALINFO_MATERIALPATTERN']._serialized_start=9516
  _globals['_BIDRESPONSE_AD_MATERIALINFO_MATERIALPATTERN']._serialized_end=9601
  _globals['_BIDRESPONSE_AD_METAINFO']._serialized_start=9604
  _globals['_BIDRESPONSE_AD_METAINFO']._serialized_end=10930
  _globals['_BIDRESPONSE_AD_METAINFO_ACTIONINFO']._serialized_start=10261
  _globals['_BIDRESPONSE_AD_METAINFO_ACTIONINFO']._serialized_end=10434
  _globals['_BIDRESPONSE_AD_METAINFO_TXTMATERIAL']._serialized_start=10436
  _globals['_BIDRESPONSE_AD_METAINFO_TXTMATERIAL']._serialized_end=10462
  _globals['_BIDRESPONSE_AD_METAINFO_SRCMATERIAL']._serialized_start=10465
  _globals['_BIDRESPONSE_AD_METAINFO_SRCMATERIAL']._serialized_end=10636
  _globals['_BIDRESPONSE_AD_METAINFO_BRANDINFO']._serialized_start=10638
  _globals['_BIDRESPONSE_AD_METAINFO_BRANDINFO']._serialized_end=10690
  _globals['_BIDRESPONSE_AD_METAINFO_APPINFO']._serialized_start=10693
  _globals['_BIDRESPONSE_AD_METAINFO_APPINFO']._serialized_end=10930
  _globals['_BIDRESPONSE_AD_METAINFOGROUP']._serialized_start=10932
  _globals['_BIDRESPONSE_AD_METAINFOGROUP']._serialized_end=10997
  _globals['_BIDRESPONSE_AD_DOWNLOADINFO']._serialized_start=11000
  _globals['_BIDRESPONSE_AD_DOWNLOADINFO']._serialized_end=11200
# @@protoc_insertion_point(module_scope)