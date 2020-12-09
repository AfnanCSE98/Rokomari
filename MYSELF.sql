/*
 Navicat Premium Data Transfer

 Source Server         : ORCLPDB
 Source Server Type    : Oracle
 Source Server Version : 190000
 Source Host           : localhost:1521
 Source Schema         : MYSELF

 Target Server Type    : Oracle
 Target Server Version : 190000
 File Encoding         : 65001

 Date: 10/12/2020 05:47:06
*/


-- ----------------------------
-- Table structure for AUTHOR
-- ----------------------------
DROP TABLE "MYSELF"."AUTHOR";
CREATE TABLE "MYSELF"."AUTHOR" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "NAME" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "PROFILE" VARCHAR2(1000 BYTE) VISIBLE
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of AUTHOR
-- ----------------------------
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000001', 'আতিউর রহমান', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000002', 'রবীন্দ্রনাথ ঠাকুর', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000003', 'জিল্লুর রহমান সিদ্দিকী', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000004', 'শাহরিয়ার কবির', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000005', 'মুনতাসীর মামুন', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000006', 'ড. হারুণ অর রশিদ', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000007', 'ফজলুল আলম', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000008', 'ড. ফজলুল করীম', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000009', 'মুস্তাফা জামান আব্বাসী', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000010', 'নাসির আলী মামুন', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000011', 'আসিফ নজরুল', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000012', 'আমীরুল ইসলাম', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000013', 'মেজর জেনারেল (অব:) সৈয়দ মুহাম্মদ ইবরাহিম,বীরপ্রতীক', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000014', 'অরুণ চৌধুরী', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000015', 'আসমা আব্বাসী', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000016', 'হুমায়ূন আহমেদ', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000017', 'ধীরাজ কুমার নাথ', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000018', 'সাকিল চৌধুরী', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000019', 'নাশিদ কামাল', NULL);
INSERT INTO "MYSELF"."AUTHOR" VALUES ('1000020', 'হাসানআল আব্দুল্লাহ', NULL);

-- ----------------------------
-- Table structure for BOOK
-- ----------------------------
DROP TABLE "MYSELF"."BOOK";
CREATE TABLE "MYSELF"."BOOK" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "ISBN" VARCHAR2(15 BYTE) VISIBLE,
  "TITLE" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "EDITION" VARCHAR2(15 BYTE) VISIBLE,
  "NO OF PAGES" VARCHAR2(15 BYTE) VISIBLE,
  "COUNTRY" VARCHAR2(255 BYTE) VISIBLE,
  "LANGUAGE" VARCHAR2(255 BYTE) VISIBLE,
  "PRICE" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "IMAGE_SRC" VARCHAR2(1000 BYTE) VISIBLE,
  "SUMMARY" VARCHAR2(1000 BYTE) VISIBLE,
  "AUTHOR ID" VARCHAR2(15 BYTE) VISIBLE,
  "CATEGORY ID" VARCHAR2(15 BYTE) VISIBLE,
  "PUBLISHER ID" VARCHAR2(15 BYTE) VISIBLE,
  "STOCK" VARCHAR2(15 BYTE) VISIBLE DEFAULT '10',
  "SALES COUNT" VARCHAR2(15 BYTE) VISIBLE DEFAULT '0'
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of BOOK
-- ----------------------------
INSERT INTO "MYSELF"."BOOK" VALUES ('1', '98257732', 'সুশাসনের সন্ধানে', '1', '215', NULL, 'Bangla', '325', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/71d819b94_1.jpg', NULL, '1000001', '1', '100001', '9', '1');
INSERT INTO "MYSELF"."BOOK" VALUES ('2', '0', 'নির্বাচিত প্রবন্ধ', '1', '0', NULL, 'Bangla', '420', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/90c0529fd_30755.jpg', NULL, '1000001', '2', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('3', '0', 'উন্নয়ন কার জন্য', '1', '0', NULL, 'Bangla', '225', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/cee5331eb_30758.jpg', NULL, '1000001', '3', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('4', '0', 'অধিকারভিত্তিক উন্নয়ন', '2', '0', NULL, 'Bangla', '275', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/c8bdb50ef_30761.jpg', NULL, '1000001', '4', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('5', '0', 'মানবিক ব্যাংকিং', '2', '0', NULL, 'Bangla', '450', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/ae2739468_78184.jpg', NULL, '1000001', '5', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('6', '95800000', 'তব ভুবনে তব ভবনে', '1', '360', NULL, 'Bangla', '600', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/06002d85a_93467.jpg', NULL, '1000001', '6', '100001', '7', '3');
INSERT INTO "MYSELF"."BOOK" VALUES ('7', '59000000', 'বুনে গেলাম আশার স্বপন-গভর্নরের দিনলিপি (মে ২০০৯-মার্চ ২০১৬)', '1', '832', NULL, 'Bangla', '1500', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/9b845dd7e0b4_133603.jpg', NULL, '1000001', '7', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('8', '0', 'নির্বাচিত প্রবন্ধ', '1', '0', NULL, 'Bangla', '200', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/f22316e5b_30720.jpg', NULL, '1000003', '2', '100001', '9', '1');
INSERT INTO "MYSELF"."BOOK" VALUES ('9', '0', 'নির্বাচিত প্রবন্ধ', '1', '0', NULL, 'Bangla', '275', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/eb379125e_30752.jpg', NULL, '1000005', '2', '100001', '7', '3');
INSERT INTO "MYSELF"."BOOK" VALUES ('10', '0', 'ক্রান্তিকালে প্রতারক', '2', '0', NULL, 'Bangla', '85', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/59fd79d19_31219.jpg', NULL, '1000007', '8', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('11', '0', 'অস্বচ্ছ দূরবীন', '2', '0', NULL, 'Bangla', '70', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/15563edaf_31221.jpg', NULL, '1000007', '8', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('12', '3430000', 'পুড়িব একাকী', '2', '320', NULL, 'Bangla', '500', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/856164051_53890.jpg', NULL, '1000009', '8', '100001', '7', '3');
INSERT INTO "MYSELF"."BOOK" VALUES ('13', '2340000', 'হুমায়ূন আহমেদ : অনন্ত জীবন যদি', '1', '96', NULL, 'Bangla', '800', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/456d526022a4_113105.gif', NULL, '1000010', '9', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('14', '0', 'যুদ্ধাপরাধীর বিচার : জাহানারা ইমামের চিঠি', '2', '0', NULL, 'Bangla', '120', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/img_30709.gif', NULL, '1000011', '10', '100001', '9', '1');
INSERT INTO "MYSELF"."BOOK" VALUES ('15', '49000000', 'নির্বাচিত ১০০ ছড়া', '3', '160', NULL, 'Bangla', '300', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/imgrok_39007.GIF', NULL, '1000012', '11', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('16', '4530', 'মুক্তিযুদ্ধের ১০০ ছড়া', '3', '120', NULL, 'Bangla', '250', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/94b9913238a4_129341.jpg', NULL, '1000012', '11', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('17', '24325433', 'রূপার পালঙ্ক', '2', '88', NULL, 'Bangla', '200', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/imgrok_20141214_898.gif', NULL, '1000016', '8', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('18', '5433452', 'অদ্ভুত সব উপন্যাস', '2', '368', NULL, 'Bangla', '600', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/63bfb202d_900.jpg', NULL, '1000016', '11', '100001', '10', '0');
INSERT INTO "MYSELF"."BOOK" VALUES ('19', '53300000', 'কানী ডাইনী', '2', '16', NULL, 'Bangla', '150', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/img141201_906.gif', NULL, '1000016', '12', '100001', '8', '2');
INSERT INTO "MYSELF"."BOOK" VALUES ('20', '3334245232', 'বৃষ্টি বিলাস', '1', '104', NULL, 'Bangla', '200', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/260X372/7b32142666f4_908.gif', NULL, '1000016', '8', '100001', '9', '1');
INSERT INTO "MYSELF"."BOOK" VALUES ('21', '9784120802', 'ইস্টিশন', '10', '92', 'বাংলাদেশ', 'বাংলা', '141', 'https://ds.rokomari.store/rokomari110/ProductNew20190903/130X186/img141201_879.gif', 'রাতের বেলা ট্রেনের শব্দ শুনলে আমি বিছানায় উঠে বসি ঠিকই কিন্তু স্টেশনে যাই না। ধলা সামছু যায়। হাতে হারিকেন ঝুলিয়ে ছুটে যায়। প্রতিটি কামরা লণ্ঠন উঁচিয়ে দেখে ।', '1000016', '12', '100004', '2', '8');

-- ----------------------------
-- Table structure for BOOK CART
-- ----------------------------
DROP TABLE "MYSELF"."BOOK CART";
CREATE TABLE "MYSELF"."BOOK CART" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "USER ID" VARCHAR2(15 BYTE) VISIBLE,
  "BOOK ID" VARCHAR2(15 BYTE) VISIBLE,
  "ORDER ID" VARCHAR2(15 BYTE) VISIBLE,
  "BOOK QUANTITY" VARCHAR2(15 BYTE) VISIBLE DEFAULT '0'
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of BOOK CART
-- ----------------------------
INSERT INTO "MYSELF"."BOOK CART" VALUES ('1', '1', '7', '3', '1');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('13', '3', '9', '11', '3');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('4', '3', '8', '5', '5');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('14', '3', '19', '11', '2');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('15', '2', '1', '14', '1');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('22', '3', '12', '15', '3');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('17', '4', '1', '1', '1');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('18', '3', '8', '13', '1');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('19', '3', '14', '13', '1');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('24', '5', '21', '22', '3');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('2', '3', '5', '4', '1');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('12', '2', '19', '9', '3');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('23', '3', '21', '20', '5');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('5', '3', '3', '6', '4');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('3', '1', '1', '3', '1');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('6', '3', '15', '7', '2');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('7', '3', '19', '7', '4');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('8', '3', '12', '8', '10');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('9', '3', '13', '8', '10');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('10', '3', '16', '8', '10');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('11', '3', '15', '8', '10');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('25', '5', '6', '23', '3');
INSERT INTO "MYSELF"."BOOK CART" VALUES ('21', '2', '20', '14', '1');

-- ----------------------------
-- Table structure for BOOK CATEGORY
-- ----------------------------
DROP TABLE "MYSELF"."BOOK CATEGORY";
CREATE TABLE "MYSELF"."BOOK CATEGORY" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "NAME" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "DESCRIPTION" VARCHAR2(1000 BYTE) VISIBLE
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of BOOK CATEGORY
-- ----------------------------
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('1', 'প্রসঙ্গ বাংলাদেশ', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('2', 'প্রবন্ধ ও গবেষণা সমগ্র', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('3', 'অর্থনীতিঃ প্রসঙ্গ বাংলাদেশ', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('4', 'বিবিধ প্রবন্ধ', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('5', 'ব্যাংকিং ও ফিনান্স', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('6', 'রবীন্দ্রনাথ', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('7', 'পেশাগত স্মৃতিচারণ ও অভিজ্ঞতা', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('8', 'সমকালীন উপন্যাস', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('9', 'ছবির অ্যালবাম', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('10', 'ডায়েরি ও চিঠিপত্র সংকলন', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('11', 'ছড়া', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('12', 'উপন্যাস সমগ্র/সংকলন', NULL);
INSERT INTO "MYSELF"."BOOK CATEGORY" VALUES ('13', 'শিশু-কিশোর উপন্যাস', NULL);

-- ----------------------------
-- Table structure for BOOK WISHLIST
-- ----------------------------
DROP TABLE "MYSELF"."BOOK WISHLIST";
CREATE TABLE "MYSELF"."BOOK WISHLIST" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "USER ID" VARCHAR2(15 BYTE) VISIBLE,
  "BOOK ID" VARCHAR2(15 BYTE) VISIBLE
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of BOOK WISHLIST
-- ----------------------------
INSERT INTO "MYSELF"."BOOK WISHLIST" VALUES ('2', '2', '20');

-- ----------------------------
-- Table structure for BRAND
-- ----------------------------
DROP TABLE "MYSELF"."BRAND";
CREATE TABLE "MYSELF"."BRAND" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "NAME" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "PHONE_NUMBER" VARCHAR2(11 BYTE) VISIBLE,
  "WEB_URL" VARCHAR2(255 BYTE) VISIBLE,
  "EMAIL" VARCHAR2(255 BYTE) VISIBLE,
  "ADDRESS" VARCHAR2(1000 BYTE) VISIBLE,
  "IMAGE_SRC" VARCHAR2(1000 BYTE) VISIBLE
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of BRAND
-- ----------------------------
INSERT INTO "MYSELF"."BRAND" VALUES ('13', 'Gigabyte', NULL, NULL, NULL, NULL, 'https://m.media-amazon.com/images/S/abs-image-upload-na/8/AmazonStores/ATVPDKIKX0DER/5602db0bb9250e19d48ead276a95fc24.w400.h400._CR0%2C0%2C400%2C400_SX100_.png');
INSERT INTO "MYSELF"."BRAND" VALUES ('14', 'Logitech', NULL, NULL, NULL, NULL, 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/company/c654ffb16_5848.png');
INSERT INTO "MYSELF"."BRAND" VALUES ('15', 'Panda', NULL, NULL, NULL, NULL, 'amazon.com/images/I/61is3OsVooL.png');
INSERT INTO "MYSELF"."BRAND" VALUES ('1', 'Onnorokom Electronics', NULL, NULL, NULL, NULL, 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/company/6976f5c9db74_4207.jpg');
INSERT INTO "MYSELF"."BRAND" VALUES ('2', 'Kaspersky', NULL, NULL, NULL, NULL, 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/company/fbd786c39_4559.png');
INSERT INTO "MYSELF"."BRAND" VALUES ('3', 'Asus', NULL, NULL, NULL, NULL, 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/company/746b729e19d4_4193.png');
INSERT INTO "MYSELF"."BRAND" VALUES ('4', 'Adata', NULL, NULL, NULL, NULL, 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/company/1b15bc414b54_4194.jpg');
INSERT INTO "MYSELF"."BRAND" VALUES ('5', 'Toshiba', NULL, NULL, NULL, NULL, 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/company/803a91fd2_4297.jpg');
INSERT INTO "MYSELF"."BRAND" VALUES ('6', 'Pny', NULL, NULL, NULL, NULL, 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/company/997f53eeb_4298.png');
INSERT INTO "MYSELF"."BRAND" VALUES ('7', 'Rapoo', NULL, NULL, NULL, NULL, 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/company/237e3ef27294_4200.png');
INSERT INTO "MYSELF"."BRAND" VALUES ('8', 'Delux', NULL, NULL, NULL, NULL, 'http://www.deluxworld.com/templets/qyskin/images/logo.png');
INSERT INTO "MYSELF"."BRAND" VALUES ('9', 'A4Tech', NULL, NULL, NULL, NULL, 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/company/7764805444d4_4195.jpg');
INSERT INTO "MYSELF"."BRAND" VALUES ('10', 'Golden Field', NULL, NULL, NULL, NULL, 'http://amcomputerbd.com/image/cache/catalog/AM%20Computer/menufector/d6fe617f968bbcf81764c4e0721a56b8.w661.h661-380x430h.jpg');
INSERT INTO "MYSELF"."BRAND" VALUES ('11', 'Twinmos', NULL, NULL, NULL, NULL, 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/company/367808497_4290.jpg');
INSERT INTO "MYSELF"."BRAND" VALUES ('12', 'Samsung', NULL, NULL, NULL, NULL, 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/company/b663b41dd764_4198.jpg');
INSERT INTO "MYSELF"."BRAND" VALUES ('16', 'Intel', '01710000000', 'https://www.intel.co.uk/content/www/uk/en/homepage.html', 'intel@gmail.com', 'USA', 'https://www.startech.com.bd/image/cache/catalog/component/processor/core-i3/coffee-lake/8100-1-500x500.jpg');

-- ----------------------------
-- Table structure for COMMENT
-- ----------------------------
DROP TABLE "MYSELF"."COMMENT";
CREATE TABLE "MYSELF"."COMMENT" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "USER ID" VARCHAR2(15 BYTE) VISIBLE,
  "BOOK ID" VARCHAR2(15 BYTE) VISIBLE,
  "ELECTRONICS ID" VARCHAR2(15 BYTE) VISIBLE,
  "DESCRIPTION" VARCHAR2(1000 BYTE) VISIBLE,
  "COMMENT TIME" DATE VISIBLE DEFAULT SYSDATE
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of COMMENT
-- ----------------------------
INSERT INTO "MYSELF"."COMMENT" VALUES ('3', '1', '1', NULL, 'hello', TO_DATE('2020-11-17 03:10:22', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('4', '1', '7', NULL, 'nice book', TO_DATE('2020-11-17 03:11:52', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('1', '1', '1', NULL, 'good book', TO_DATE('2020-11-17 03:00:42', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('2', '1', '8', NULL, 'good book', TO_DATE('2020-11-17 03:09:27', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('5', '1', '5', NULL, 'best book', TO_DATE('2020-11-17 03:13:10', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('10', '3', NULL, '1000012', 'good product ', TO_DATE('2020-11-23 00:31:22', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('11', '2', '2', NULL, 'Good book', TO_DATE('2020-11-27 07:51:02', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('12', '3', NULL, '1000008', 'Good product', TO_DATE('2020-11-27 09:22:05', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('13', '3', '1', NULL, 'Nice book', TO_DATE('2020-11-27 10:20:28', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('14', '3', '4', NULL, 'Good book', TO_DATE('2020-11-27 10:49:39', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('15', '3', NULL, '1000015', 'Good product', TO_DATE('2020-11-28 05:44:09', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('16', '3', '2', NULL, 'Nice book', TO_DATE('2020-11-28 05:48:53', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('17', '2', NULL, '1000008', 'Nice product', TO_DATE('2020-11-28 05:52:09', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('18', '2', NULL, '1000023', 'good webcam', TO_DATE('2020-11-28 05:52:37', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('19', '2', '20', NULL, 'good book', TO_DATE('2020-11-28 06:06:09', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('20', '3', '1', NULL, 'nice boi', TO_DATE('2020-11-28 07:25:30', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('21', '3', '12', NULL, 'noise boi', TO_DATE('2020-11-28 07:27:36', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('22', '3', '3', NULL, 'Nice book', TO_DATE('2020-11-28 11:35:29', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('23', '3', '7', NULL, 'valo boi', TO_DATE('2020-12-06 13:07:04', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('24', '5', '21', NULL, 'good book', TO_DATE('2020-12-10 05:15:34', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('6', '3', '3', NULL, 'Good book ', TO_DATE('2020-11-22 13:22:25', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('7', '3', '15', NULL, 'nice book', TO_DATE('2020-11-22 13:23:11', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('8', '3', '19', NULL, 'Recomended to read it', TO_DATE('2020-11-22 13:23:48', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('9', '3', '13', NULL, 'Good biography by the author', TO_DATE('2020-11-22 13:26:20', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."COMMENT" VALUES ('25', '5', '6', NULL, 'good book', TO_DATE('2020-12-10 05:38:07', 'SYYYY-MM-DD HH24:MI:SS'));

-- ----------------------------
-- Table structure for ELECTRONICS
-- ----------------------------
DROP TABLE "MYSELF"."ELECTRONICS";
CREATE TABLE "MYSELF"."ELECTRONICS" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "TITLE" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "MODEL" VARCHAR2(255 BYTE) VISIBLE,
  "PRICE" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "IMAGE_SRC" VARCHAR2(1000 BYTE) VISIBLE,
  "DESCRIPTION" VARCHAR2(1000 BYTE) VISIBLE,
  "WARRANTY" VARCHAR2(15 BYTE) VISIBLE,
  "CATEGORY ID" VARCHAR2(15 BYTE) VISIBLE,
  "BRAND ID" VARCHAR2(15 BYTE) VISIBLE,
  "STOCK" VARCHAR2(15 BYTE) VISIBLE DEFAULT '10',
  "SALES COUNT" VARCHAR2(15 BYTE) VISIBLE DEFAULT '0'
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of ELECTRONICS
-- ----------------------------
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000000', 'Kaspersky Antivirus 2019 -1 User (1 Year)', 'Kaspersky Anti-Virus', '589', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/2fd70b32a_111412.jpg', 'Secures your devices – in any combination', '1', '1000000', '2', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000001', 'Kaspersky Antivirus 2019 - 3 User (1 Year)', 'Kaspersky Anti-Virus', '1219', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/e175b55d1_111411.jpg', 'Secures your devices – in any combination', '1', '1000000', '2', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000002', 'Kaspersky Internet Security 2019 -1 Device (1 Year)', '	Kaspersky Internet Security', '869', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/20b2214c3_111410.jpg', 'Secures your devices – in any combination', '1', '1000000', '2', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000003', 'Panda Internet Security 1 User 1 Year ', 'Panda Internet Security', '1000', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/rokimg_20151030_106244.gif', 'Secures your devices – in any combination', '1', '1000000', '15', '13', '3');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000004', 'Delux Optical Mouse- DLM-363BU', '	DLM-363BU300', '300', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/6381663b6ef4_111961.jpg', '3D Wired Optical', '1', '1000001', '8', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000005', 'Wireless Mouse M10 (White)', 'M10 ', '600', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/rokimg_20150606_99924.gif', '2.4G Wireless Entry Level 3 Key Mouse Blue', '2', '1000001', '7', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000006', 'A4 Tech Bloody 4000cpi gaming Mouse A91', 'Bloody V3M', '1650', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/7dba49f09_100789.jpg', 'High precision optical engine; Intelligent 3 Cores', '1', '1000001', '9', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000007', 'A4 Tech Wireless Desktop Keyboard (9300F)', 'A4Tech 9300F', '1850', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/rokimg_20150331_98742.gif', 'Wireless; USB', '1', '1000002', '9', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000008', 'Logitech MK345 Combo Wireless Mouse and Keyboard', 'MK345', '3100', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/63e4d5b14_136761.png', 'Keyboard and Mouse ; 10 meters', '1', '1000002', '14', '6', '4');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000009', 'Rapoo White Wireless Keyboard and Mouse Combo - X1800S', 'Rapoo X1800S', '1400', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/3ea7a3404_192462.jpg', '12M battery life ; Spill-resistant design', '2', '1000002', '7', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000010', 'TWINMOS X3 PREMIUM-16GB USB 3.0', 'Twinmos X3 PREMIUM', '480', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/ff6b58d76a04_112553.jpg', 'USB-3.0 ; 16 GB', '1', '1000003', '11', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000011', 'ADATA UV 131 USB 3.2 PEN DRIVE 16GB GRAY COLOR', 'UV 131', '675', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/94f6d534f_123386.jpg', 'USB-3.2 ; 16 GB', '1', '1000003', '4', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000012', 'Gigabyte GA-H61M-DS2 Motherboard', 'GA-H61M-DS2', '5700', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/9f9bc7072_152880.jpg', 'Dual Channel ; 27.9 x 25.4 x 7.6 cm', '3', '1000004', '13', '5', '5');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000013', 'TOSHIBA INTERNAL HARD DRIVE 2TB 3.5', 'DT01ACA200', '5700', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/c8a09b302af4_112622.jpg', 'SATA 6.0 Gb per Second ; 2 TB', '2', '1000005', '5', '9', '1');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000014', 'ADATA ULTIMATE SU 800S SSD', 'SU 800S', '9500', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/b3d05765f_161069.jpg', '256GB SSD ; 6Gb Per Second', '3', '1000005', '4', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000015', 'Asus Graphics Card nVIDIA Chipset MATRIX-GTX980-P-4GD5 ', 'NVIDIA GeForce GTX 980', '67000', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/rokimg_20150610_100840.gif', ' PCI Express 3.0 ;11.7 "" x 6 "" x 1.6 "" Inch 29.72 x 15.2 x4.06 Centimeter ; GPU Boost Clock : 1342 MHz GPU Base Clock : 1241 MHz', '3', '1000006', '3', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000016', 'Asus Graphics Card AMD Chipset R9290X-4GD5', 'AMD Radeon R9 290X', '46000', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/rokimg_20150412_98715.gif', 'PCI Express 3.0 ; 10.9 " x 4.3 " x 1.4 " Inch ;1000 MHz', '2', '1000006', '3', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000017', 'অন্যরকম বিজ্ঞানবাক্স (রকমারি কালেকশন)', NULL, '5536', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/5c6ff209e_110775.jpg', 'Odvot Mapjokh ; Rashayon Rohosho ; Torith Tandob etc', '0', '1000007', '1', '8', '2');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000018', 'শব্দকল্প', NULL, '1490', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/58f833cb0_155446.jpg', 'নিজে নিজে এক্সপেরিমেন্টগুলি করার ফলে তার মধ্যে এক ধরণের আত্মবিশ্বাস তৈরি হবে এবং সে বিজ্ঞানের সৌন্দর্য উপলব্ধি করতে সক্ষম হবে।', '0', '1000007', '1', '8', '2');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000019', 'Golden Field Speaker LA-121D (4:1)', 'LA 121D', '3100', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/rokimg_20151030_106150.gif', 'USB or SD or FM with Remote', '1', '1000008', '10', '7', '3');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000020', 'A4 Tech LAPTOP SPEAKER (P-200)', 'P-200', '1200', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/rokimg_20150331_98768.gif', 'System Requirements: Windows 2000 / XP / 2003 / Vista / Windows 7', '1', '1000008', '9', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000021', 'Rapoo Bluetooth Headset (S500)', 'S500', '2500', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/a3e40cb0e_187663.jpg', 'Aluminium alloy trimming ; COM-Ti Membrane Vibrating Technology', '1', '1000009', '7', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000022', 'Logitech USB Headset H390', 'H390', '3960', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/c4e1541fd_136790.png', '20Hz to 20kHz ; Pure digital USB', '2', '1000009', '14', '7', '3');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000023', 'Logitech Webcam C922 Pro', 'C922 Pro', '10100', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/6183b3655_136806.png', 'Full HD 1080p at 30fps / 720p at 60fps streaming', '2', '10000010', '14', '8', '2');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000024', 'ASUS Router RT-AC3200 (3G/4G Supported)', 'RT-AC3200', '27000', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/rokimg_20151014_104746.gif', 'Ultra-fast 802.11ac Wi-Fi router with a combined tri-band data rate of 3200 Mbps for smooth up to 4K/UHD video playback; ultra-fast file-sharing for large files and low-latency online gaming and intelligent gigabit router.', '1', '10000011', '3', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000025', 'ASUS Wi-Fi ROUTER 2.4 GHz and 5 GHz Concurrent Dual-Band Transmissions for Strong Signal Strength and Ultra-Fast Connection Rates up to 900Mbps (RT-N66W [3G/4G Supported])', 'RT-N66W', '11500', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/rokimg_20150412_98788.gif', 'IEEE 802.11a; IEEE 802.11b; IEEE 802.11g; IEEE 802.11n; IPv4; IPv6; N900 ultimate performance; 450 450Mbps', '1', '10000011', '3', '8', '2');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000026', 'Samsung In-Ear Basic Mass Earphone (EO-IG935B)-Black', 'Samsung In-Ear Basic Mass Earphone', '970', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/cec7b143f_190978.jpg', '3.5mm headphone connector; 1.2 m; 20Hz~20KHz', '1', '1000009', '12', '10', '0');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000027', 'PNY HOOK ATTACHE 128GB USB 3.0', 'PNY HOOK ATTACHE', '1725', 'https://s3-ap-southeast-1.amazonaws.com/rokomari110/ProductNew20190903/260X372/28aac2fc0_191768.jpg', 'USB-3.0; 128 GB', '1', '1000003', '6', '10', '3');
INSERT INTO "MYSELF"."ELECTRONICS" VALUES ('1000028', 'Asus ROG Rapture GT AX11000 Tri-band WiFi Gaming Router', 'Asus ROG Rapture GT AX11000', '42400', 'https://www.startech.com.bd/image/cache/catalog/router/asus/rog-rapture-ax11000/asus-rog-rapture-ax11000-500x500.jpg', 'Triple-level Game Acceleration, Battle-ready-hardware , Front-line Network Security', '2', '10000011', '3', '99', '1');

-- ----------------------------
-- Table structure for ELECTRONICS CART
-- ----------------------------
DROP TABLE "MYSELF"."ELECTRONICS CART";
CREATE TABLE "MYSELF"."ELECTRONICS CART" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "USER ID" VARCHAR2(15 BYTE) VISIBLE,
  "ELECTRONICS ID" VARCHAR2(15 BYTE) VISIBLE,
  "ORDER ID" VARCHAR2(15 BYTE) VISIBLE,
  "ELECTRONICS QUANTITY" VARCHAR2(15 BYTE) VISIBLE DEFAULT '0'
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of ELECTRONICS CART
-- ----------------------------
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('1', '3', '1000012', '10', '3');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('2', '3', '1000008', '11', '4');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('3', '3', '1000003', '12', '3');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('4', '3', '1000012', '13', '1');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('5', '3', '1000017', '13', '2');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('11', '3', '1000012', '15', '1');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('7', '2', '1000025', '14', '2');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('8', '2', '1000013', '14', '1');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('9', '2', '1000023', '14', '2');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('10', '3', '1000019', '15', '1');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('12', '3', '1000012', '16', '2');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('15', '3', '1000028', '19', '1');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('19', '5', '1000019', '22', '2');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('13', '3', '1000027', '17', '3');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('14', '3', '1000012', '18', '1');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('21', '5', '1000018', '23', '2');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('16', '3', '1000022', '21', '3');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('17', '3', '1000018', '1', '1');
INSERT INTO "MYSELF"."ELECTRONICS CART" VALUES ('18', '3', '1000008', '1', '1');

-- ----------------------------
-- Table structure for ELECTRONICS CATEGORY
-- ----------------------------
DROP TABLE "MYSELF"."ELECTRONICS CATEGORY";
CREATE TABLE "MYSELF"."ELECTRONICS CATEGORY" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "NAME" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "DESCRIPTION" VARCHAR2(1000 BYTE) VISIBLE,
  "IMAGE_SRC" VARCHAR2(1000 BYTE) VISIBLE
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of ELECTRONICS CATEGORY
-- ----------------------------
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('1000000', 'Antivirus', NULL, 'https://www.rokomari.com/static/new/img/electronics/computer.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('1000001', 'Mouse', NULL, 'https://www.rokomari.com/static/new/img/electronics/mouse.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('1000002', 'Keyboard', NULL, 'https://www.rokomari.com/static/new/img/electronics/keyboard.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('1000003', 'Pen Drive', NULL, 'https://www.rokomari.com/static/new/img/electronics/pendrive.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('1000004', 'Motherboard', NULL, 'https://www.rokomari.com/static/new/img/electronics/motherboard.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('1000005', 'Hard Disk Drive', NULL, 'https://www.rokomari.com/static/new/img/electronics/harddiskdrive.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('1000006', 'Graphics Card', NULL, 'https://www.rokomari.com/static/new/img/electronics/graphiccard.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('1000007', 'Science Kit', NULL, 'https://www.rokomari.com/static/new/img/electronics/upsstabilizer.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('1000008', 'Speaker', NULL, 'https://www.rokomari.com/static/new/img/electronics/speaker.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('1000009', 'Headphone', NULL, 'https://www.rokomari.com/static/new/img/electronics/speaker.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('10000010', 'WebCam', NULL, 'https://www.rokomari.com/static/new/img/electronics/webcam.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('10000011', 'Router', NULL, 'https://www.rokomari.com/static/new/img/electronics/router.png');
INSERT INTO "MYSELF"."ELECTRONICS CATEGORY" VALUES ('10000012', 'Ram', 'Random-access memory (RAM /ræm/) is a form of computer memory that can be read and changed in any order, typically used to store working data and machine code', '//upload.wikimedia.org/wikipedia/commons/thumb/d/db/Swissbit_2GB_PC2-5300U-555.jpg/220px-Swissbit_2GB_PC2-5300U-555.jpg');

-- ----------------------------
-- Table structure for ELECTRONICS WISHLIST
-- ----------------------------
DROP TABLE "MYSELF"."ELECTRONICS WISHLIST";
CREATE TABLE "MYSELF"."ELECTRONICS WISHLIST" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "USER ID" VARCHAR2(15 BYTE) VISIBLE,
  "ELECTRONICS ID" VARCHAR2(15 BYTE) VISIBLE
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of ELECTRONICS WISHLIST
-- ----------------------------
INSERT INTO "MYSELF"."ELECTRONICS WISHLIST" VALUES ('2', '2', '1000022');
INSERT INTO "MYSELF"."ELECTRONICS WISHLIST" VALUES ('3', '2', '1000008');
INSERT INTO "MYSELF"."ELECTRONICS WISHLIST" VALUES ('4', '2', '1000023');
INSERT INTO "MYSELF"."ELECTRONICS WISHLIST" VALUES ('6', '3', '1000008');

-- ----------------------------
-- Table structure for ORDER HISTORY
-- ----------------------------
DROP TABLE "MYSELF"."ORDER HISTORY";
CREATE TABLE "MYSELF"."ORDER HISTORY" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "USER ID" VARCHAR2(15 BYTE) VISIBLE,
  "STATUS" VARCHAR2(50 BYTE) VISIBLE,
  "ORDER TIME" DATE VISIBLE DEFAULT SYSDATE
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of ORDER HISTORY
-- ----------------------------
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('3', '1', 'Pending', TO_DATE('2020-11-22 13:01:04', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('4', '3', 'Pending', TO_DATE('2020-11-22 13:10:26', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('5', '3', 'Pending', TO_DATE('2020-11-22 13:11:02', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('10', '3', 'Pending', TO_DATE('2020-11-23 00:28:55', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('11', '3', 'Pending', TO_DATE('2020-11-27 23:33:14', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('12', '3', 'Pending', TO_DATE('2020-11-28 01:22:32', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('13', '3', 'Pending', TO_DATE('2020-11-28 02:02:13', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('14', '2', 'Delivered', TO_DATE('2020-11-28 06:20:29', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('15', '3', 'Pending', TO_DATE('2020-11-28 07:28:05', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('16', '3', 'Pending', TO_DATE('2020-11-28 07:52:07', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('18', '3', 'Pending', TO_DATE('2020-12-06 13:13:53', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('19', '3', 'Delivered', TO_DATE('2020-12-06 13:16:54', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('22', '5', 'Pending', TO_DATE('2020-12-09 14:29:25', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('23', '5', 'Pending', TO_DATE('2020-12-10 05:40:02', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('1', '1', 'undetermined', TO_DATE('2020-11-21 21:32:15', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('9', '2', 'Pending', TO_DATE('2020-11-22 20:22:37', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('17', '3', 'Delivered', TO_DATE('2020-11-28 09:45:34', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('20', '3', 'Pending', TO_DATE('2020-12-08 14:23:39', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('21', '3', 'Pending', TO_DATE('2020-12-08 15:11:26', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('6', '3', 'Pending', TO_DATE('2020-11-22 13:22:41', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('7', '3', 'Pending', TO_DATE('2020-11-22 13:24:12', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."ORDER HISTORY" VALUES ('8', '3', 'Delivered', TO_DATE('2020-11-22 13:27:03', 'SYYYY-MM-DD HH24:MI:SS'));

-- ----------------------------
-- Table structure for PUBLISHER
-- ----------------------------
DROP TABLE "MYSELF"."PUBLISHER";
CREATE TABLE "MYSELF"."PUBLISHER" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "NAME" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "PHONE_NUMBER" VARCHAR2(11 BYTE) VISIBLE,
  "WEB_URL" VARCHAR2(255 BYTE) VISIBLE,
  "EMAIL" VARCHAR2(255 BYTE) VISIBLE,
  "ADDRESS" VARCHAR2(1000 BYTE) VISIBLE
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of PUBLISHER
-- ----------------------------
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100021', 'জ্ঞানকোষ প্রকাশনী', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100022', 'পার্ল পাবলিকেশন্স', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100023', 'প্রতীক প্রকাশনা সংস্থা', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100001', 'অন্যপ্রকাশ', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100002', 'বিশ্বসাহিত্য ভবন', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100003', 'রাফাত পাবলিকেশন্স', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100004', 'অনন্যা', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100005', 'কমন', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100006', 'মুক্তচিন্তা', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100007', 'অনার্য', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100008', 'উৎস প্রকাশন', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100009', 'কথাপ্রকাশ', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100010', 'ভাষাপ্রকাশ', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100011', 'সুবর্ণ', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100012', 'ইত্যাদি গ্রন্থ প্রকাশ', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100013', 'ঘাসফুল নদী', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100014', 'শ্রাবণ প্রকাশনী', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100015', 'বর্ণায়ন', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100016', 'আফসার ব্রাদার্স', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100017', 'অনুপম প্রকাশনী', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100018', 'অন্বেষা প্রকাশন', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100019', 'অবসর প্রকাশনা সংস্থা', NULL, NULL, NULL, NULL);
INSERT INTO "MYSELF"."PUBLISHER" VALUES ('100020', 'কাকলী প্রকাশনী', NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for RATING
-- ----------------------------
DROP TABLE "MYSELF"."RATING";
CREATE TABLE "MYSELF"."RATING" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "USER ID" VARCHAR2(15 BYTE) VISIBLE,
  "BOOK ID" VARCHAR2(15 BYTE) VISIBLE,
  "ELECTRONICS ID" VARCHAR2(15 BYTE) VISIBLE,
  "STARS" VARCHAR2(2 BYTE) VISIBLE,
  "RATING TIME" DATE VISIBLE DEFAULT SYSDATE
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of RATING
-- ----------------------------
INSERT INTO "MYSELF"."RATING" VALUES ('3', '1', '8', NULL, '2', TO_DATE('2020-11-17 03:09:18', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('1', '1', '1', NULL, '3', TO_DATE('2020-11-17 03:00:31', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('7', '1', '7', NULL, '1', TO_DATE('2020-11-21 22:18:52', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('5', '1', '5', NULL, '5', TO_DATE('2020-11-17 03:13:14', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('8', '3', '9', NULL, '3', TO_DATE('2020-11-21 22:42:52', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('16', '3', NULL, '1000023', '4', TO_DATE('2020-11-23 00:38:17', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('46', '2', NULL, '1000023', '4', TO_DATE('2020-11-28 05:52:42', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('49', '2', '20', NULL, '3', TO_DATE('2020-11-28 06:05:58', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('40', '3', NULL, '1000015', '3', TO_DATE('2020-11-28 05:44:28', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('42', '3', NULL, '1000017', '3', TO_DATE('2020-11-28 05:47:29', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('32', '3', '19', NULL, '2', TO_DATE('2020-11-27 11:04:42', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('45', '2', NULL, '1000008', '2', TO_DATE('2020-11-28 05:52:01', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('43', '3', '2', NULL, '3', TO_DATE('2020-11-28 05:49:02', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('44', '2', NULL, '1000022', '4', TO_DATE('2020-11-28 05:51:22', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('47', '2', NULL, '1000025', '3', TO_DATE('2020-11-28 05:55:27', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('48', '2', NULL, '1000003', '3', TO_DATE('2020-11-28 06:01:24', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('50', '2', '14', NULL, '3', TO_DATE('2020-11-28 06:11:42', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('51', '2', '7', NULL, '4', TO_DATE('2020-11-28 06:24:14', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('52', '3', NULL, '1000026', '3', TO_DATE('2020-11-28 07:15:41', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('57', '3', '8', NULL, '3', TO_DATE('2020-11-28 07:47:33', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('54', '3', '1', NULL, '2', TO_DATE('2020-11-28 07:25:12', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('55', '3', '12', NULL, '4', TO_DATE('2020-11-28 07:27:28', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('56', '3', NULL, '1000000', '4', TO_DATE('2020-11-28 07:29:51', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('59', '3', NULL, '1000024', '3', TO_DATE('2020-11-28 07:51:07', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('60', '3', NULL, '1000003', '3', TO_DATE('2020-11-28 07:54:53', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('72', '5', NULL, '1000028', '3', TO_DATE('2020-12-10 05:38:57', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('19', '3', '14', NULL, '5', TO_DATE('2020-11-23 07:19:18', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('61', '3', '3', NULL, '3', TO_DATE('2020-11-28 11:35:12', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('69', '3', NULL, '1000022', '1', TO_DATE('2020-12-08 14:35:20', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('70', '5', '21', NULL, '3', TO_DATE('2020-12-10 05:15:21', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('9', '3', '11', NULL, '3', TO_DATE('2020-11-21 23:07:34', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('12', '3', '15', NULL, '3', TO_DATE('2020-11-22 13:23:04', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('14', '3', '13', NULL, '3', TO_DATE('2020-11-22 13:26:01', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('71', '5', '6', NULL, '3', TO_DATE('2020-12-10 05:37:58', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('23', '2', '5', NULL, '5', TO_DATE('2020-11-26 22:38:04', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('63', '3', '4', NULL, '3', TO_DATE('2020-12-06 13:37:10', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('64', '3', '5', NULL, '1', TO_DATE('2020-12-06 13:37:22', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('65', '3', '7', NULL, '5', TO_DATE('2020-12-06 13:39:36', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('66', '3', NULL, '1000012', '5', TO_DATE('2020-12-06 13:44:08', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('67', '3', NULL, '1000008', '5', TO_DATE('2020-12-06 13:44:42', 'SYYYY-MM-DD HH24:MI:SS'));
INSERT INTO "MYSELF"."RATING" VALUES ('68', '3', NULL, '1000014', '3', TO_DATE('2020-12-06 13:46:48', 'SYYYY-MM-DD HH24:MI:SS'));

-- ----------------------------
-- Table structure for USER
-- ----------------------------
DROP TABLE "MYSELF"."USER";
CREATE TABLE "MYSELF"."USER" (
  "ID" VARCHAR2(15 BYTE) VISIBLE NOT NULL,
  "NAME" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "PHONE NUMBER" VARCHAR2(15 BYTE) VISIBLE,
  "EMAIL" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "SALT" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "KEY" VARCHAR2(255 BYTE) VISIBLE NOT NULL,
  "ADDRESS" VARCHAR2(1000 BYTE) VISIBLE,
  "TYPES" VARCHAR2(1 BYTE) VISIBLE,
  "IS ACTIVE" VARCHAR2(2 BYTE) VISIBLE DEFAULT 'Y'
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;

-- ----------------------------
-- Records of USER
-- ----------------------------
INSERT INTO "MYSELF"."USER" VALUES ('2', 'Mahi', '01771300000', 'mahi@gmail.com', '30643330333066313463303761303832356564643238316337633535393130343066316135393863303930386332326337666333623763396337356661396335', '63653066396364326162393534356535333032626431346632383061376136663234386634353632653836303366376366616236313734303635393863326261', 'Cumilla', 'C', 'Y');
INSERT INTO "MYSELF"."USER" VALUES ('3', 'Hamim', '01762344574', 'hamim@gmail.com', '38383530363865323162613633313563343032393738646634623131356666303230616535396134313239646437303561316361333433396238363536623433', '30313633386139323838326662313338393761326636386132396361373236643533643832313536343437303235376239396264343932646436333437306136', 'Cumilla', 'C', 'Y');
INSERT INTO "MYSELF"."USER" VALUES ('5', 'Tabbi', '123', 'a@gmail.com', '36633732626237323033376663336632623437333161373938626532393733616363376537663861636637396461393033613238353631623265346333383266', '33396162373030363366383539363339626338373262633862363961356663333861316333323932316331346361343639663134353161386336663832323535', 'Dhaka', 'C', 'Y');
INSERT INTO "MYSELF"."USER" VALUES ('6', 'Deepto', '92929292929', 'dep@gmail.com', '31393934303963393432316237613731666261353435306434323938656566616130653838373065356336663265646438303036613564623437616130653264', '62393036373030623933643931613730336137396665626631663239383838303837616537623864653362636565666362653134323963663333333430356263', 'Cumilla', 'C', 'Y');
INSERT INTO "MYSELF"."USER" VALUES ('4', 'Rabbi', '11111111111', 'rabbi@gmail.com', '36323038323236613232633361616137393435373337666363623534393532366338363533313066653030306336366365376530356138666537363532333963', '31396331653262373531353962663131366566343462666338623434613835666137386331663262663961353632393666656265646164306334643631306465', 'Cumilla', 'C', 'Y');
INSERT INTO "MYSELF"."USER" VALUES ('1', 'Afnan', '01710680500', 'sihatafnan15.9.1997@gmail.com', '32316263633834643733353031613865363131323463393230643033363737643932383930393036636230626238393737623266333262356565306436373936', '63396461386561666361616565336235626232613637653030646662346165346162393134663435666464366239653264316430386131353830346133306665', 'Dhaka', 'A', 'Y');

-- ----------------------------
-- Function structure for ADD_TO_BOOK_CART
-- ----------------------------
CREATE OR REPLACE
PROCEDURE "MYSELF"."ADD_TO_BOOK_CART" AS
BEGIN
	SELECT NVL(COUNT(*), 0) INTO CNT
	FROM "BOOK CART"
	WHERE "BOOK ID" = book_id
	AND "USER ID" = user_id
	AND "ORDER ID" = order_id;
	DBMS_OUTPUT.PUT_LINE(CNT);
	IF CNT <= 0 THEN
		 INSERT INTO "BOOK CART"
     VALUES( id, user_id, book_id, order_id, book_quantity);
		 COMMIT;
	END IF;
END;
/

-- ----------------------------
-- Function structure for ADD_TO_ELECTRONICS_CART
-- ----------------------------
CREATE OR REPLACE
PROCEDURE "MYSELF"."ADD_TO_ELECTRONICS_CART" AS
BEGIN
	SELECT NVL(COUNT(*), 0) INTO CNT
	FROM "ELECTRONICS CART"
	WHERE "ELECTRONICS ID" = electronics_id
	AND "USER ID" = user_id
	AND "ORDER ID" = order_id;
	IF CNT <= 0 THEN
		 INSERT INTO "ELECTRONICS CART"
     VALUES( id, user_id, electronics_id, order_id, electronics_quantity);
		 COMMIT;
	END IF;
END;
/

-- ----------------------------
-- Function structure for GET_AVERAGE_BOOK_RATING
-- ----------------------------
CREATE OR REPLACE
FUNCTION "MYSELF"."GET_AVERAGE_BOOK_RATING" AS
BEGIN
	SELECT  TO_CHAR(ROUND(AVG(TO_NUMBER(STARS))))
	INTO AVERAGE 
	FROM RATING
	WHERE "BOOK ID" = BID;
	RETURN AVERAGE;
EXCEPTION
	WHEN NO_DATA_FOUND THEN
		RETURN NULL;
END;
/

-- ----------------------------
-- Function structure for GET_AVERAGE_ELECTRONICS_RATING
-- ----------------------------
CREATE OR REPLACE
FUNCTION "MYSELF"."GET_AVERAGE_ELECTRONICS_RATING" AS
BEGIN
	SELECT  TO_CHAR(ROUND(AVG(TO_NUMBER(STARS))))
	INTO AVERAGE 
	FROM RATING
	WHERE "ELECTRONICS ID" = EID;
	RETURN AVERAGE;
EXCEPTION
	WHEN NO_DATA_FOUND THEN
		RETURN NULL;
END;
/

-- ----------------------------
-- Primary Key structure for table AUTHOR
-- ----------------------------
ALTER TABLE "MYSELF"."AUTHOR" ADD CONSTRAINT "AUTHOR_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Checks structure for table AUTHOR
-- ----------------------------
ALTER TABLE "MYSELF"."AUTHOR" ADD CONSTRAINT "SYS_C008068" CHECK ("NAME" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Primary Key structure for table BOOK
-- ----------------------------
ALTER TABLE "MYSELF"."BOOK" ADD CONSTRAINT "BOOK_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Checks structure for table BOOK
-- ----------------------------
ALTER TABLE "MYSELF"."BOOK" ADD CONSTRAINT "SYS_C008074" CHECK ("TITLE" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."BOOK" ADD CONSTRAINT "SYS_C008075" CHECK ("PRICE" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Primary Key structure for table BOOK CART
-- ----------------------------
ALTER TABLE "MYSELF"."BOOK CART" ADD CONSTRAINT "BOOK_CART_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Primary Key structure for table BOOK CATEGORY
-- ----------------------------
ALTER TABLE "MYSELF"."BOOK CATEGORY" ADD CONSTRAINT "BOOK_CATEGORY_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Checks structure for table BOOK CATEGORY
-- ----------------------------
ALTER TABLE "MYSELF"."BOOK CATEGORY" ADD CONSTRAINT "SYS_C008070" CHECK ("NAME" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Primary Key structure for table BOOK WISHLIST
-- ----------------------------
ALTER TABLE "MYSELF"."BOOK WISHLIST" ADD CONSTRAINT "BOOK_WISHLIST_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Primary Key structure for table BRAND
-- ----------------------------
ALTER TABLE "MYSELF"."BRAND" ADD CONSTRAINT "BRAND_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Checks structure for table BRAND
-- ----------------------------
ALTER TABLE "MYSELF"."BRAND" ADD CONSTRAINT "SYS_C008116" CHECK ("NAME" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Primary Key structure for table COMMENT
-- ----------------------------
ALTER TABLE "MYSELF"."COMMENT" ADD CONSTRAINT "COMMENT_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Triggers structure for table COMMENT
-- ----------------------------
CREATE TRIGGER "MYSELF"."COMMENT_INSERT" BEFORE INSERT ON "MYSELF"."COMMENT" REFERENCING OLD AS "OLD" NEW AS "NEW" FOR EACH ROW 
DECLARE
	T_ID NUMBER;
BEGIN
	SELECT NVL(MAX(TO_NUMBER(ID)), 0) INTO T_ID
	FROM "COMMENT";
	:NEW.ID := TO_CHAR(T_ID + 1) ;
END;
/

-- ----------------------------
-- Primary Key structure for table ELECTRONICS
-- ----------------------------
ALTER TABLE "MYSELF"."ELECTRONICS" ADD CONSTRAINT "ELECTRONICS_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Checks structure for table ELECTRONICS
-- ----------------------------
ALTER TABLE "MYSELF"."ELECTRONICS" ADD CONSTRAINT "SYS_C008150" CHECK ("TITLE" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."ELECTRONICS" ADD CONSTRAINT "SYS_C008151" CHECK ("PRICE" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Primary Key structure for table ELECTRONICS CART
-- ----------------------------
ALTER TABLE "MYSELF"."ELECTRONICS CART" ADD CONSTRAINT "ELECTRONICS_CART_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Primary Key structure for table ELECTRONICS CATEGORY
-- ----------------------------
ALTER TABLE "MYSELF"."ELECTRONICS CATEGORY" ADD CONSTRAINT "ELECTRONICS_CATEGORY_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Checks structure for table ELECTRONICS CATEGORY
-- ----------------------------
ALTER TABLE "MYSELF"."ELECTRONICS CATEGORY" ADD CONSTRAINT "SYS_C008148" CHECK ("NAME" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Primary Key structure for table ELECTRONICS WISHLIST
-- ----------------------------
ALTER TABLE "MYSELF"."ELECTRONICS WISHLIST" ADD CONSTRAINT "ELECTRONICS_WISHLIST_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Primary Key structure for table ORDER HISTORY
-- ----------------------------
ALTER TABLE "MYSELF"."ORDER HISTORY" ADD CONSTRAINT "ORDER_HISTORY_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Triggers structure for table ORDER HISTORY
-- ----------------------------
CREATE TRIGGER "MYSELF"."ORDER_INSERT" BEFORE INSERT ON "MYSELF"."ORDER HISTORY" REFERENCING OLD AS "OLD" NEW AS "NEW" FOR EACH ROW 
DECLARE
	T_ID NUMBER;
BEGIN
	SELECT NVL(MAX(TO_NUMBER(ID)), 0) INTO T_ID
	FROM "ORDER HISTORY";
	:NEW.ID := TO_CHAR(T_ID + 1) ;
END;
/

-- ----------------------------
-- Primary Key structure for table PUBLISHER
-- ----------------------------
ALTER TABLE "MYSELF"."PUBLISHER" ADD CONSTRAINT "PUBLISHER_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Checks structure for table PUBLISHER
-- ----------------------------
ALTER TABLE "MYSELF"."PUBLISHER" ADD CONSTRAINT "SYS_C008072" CHECK ("NAME" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Primary Key structure for table RATING
-- ----------------------------
ALTER TABLE "MYSELF"."RATING" ADD CONSTRAINT "RATING_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Triggers structure for table RATING
-- ----------------------------
CREATE TRIGGER "MYSELF"."RATING_INSERT" BEFORE INSERT ON "MYSELF"."RATING" REFERENCING OLD AS "OLD" NEW AS "NEW" FOR EACH ROW 
DECLARE
	T_ID NUMBER;
BEGIN
	SELECT NVL(MAX(TO_NUMBER(ID)), 0) INTO T_ID
	FROM "RATING";
	:NEW.ID := TO_CHAR(T_ID + 1) ;
END;
/

-- ----------------------------
-- Primary Key structure for table USER
-- ----------------------------
ALTER TABLE "MYSELF"."USER" ADD CONSTRAINT "USER_PK" PRIMARY KEY ("ID");

-- ----------------------------
-- Uniques structure for table USER
-- ----------------------------
ALTER TABLE "MYSELF"."USER" ADD CONSTRAINT "SYS_C008185" UNIQUE ("PHONE NUMBER") NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."USER" ADD CONSTRAINT "SYS_C008186" UNIQUE ("EMAIL") NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Checks structure for table USER
-- ----------------------------
ALTER TABLE "MYSELF"."USER" ADD CONSTRAINT "SYS_C008180" CHECK ("NAME" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."USER" ADD CONSTRAINT "SYS_C008181" CHECK ("EMAIL" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."USER" ADD CONSTRAINT "SYS_C008182" CHECK ("SALT" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."USER" ADD CONSTRAINT "SYS_C008183" CHECK ("KEY" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Foreign Keys structure for table BOOK
-- ----------------------------
ALTER TABLE "MYSELF"."BOOK" ADD CONSTRAINT "BOOK_FK1" FOREIGN KEY ("AUTHOR ID") REFERENCES "MYSELF"."AUTHOR" ("ID") ON DELETE SET NULL NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."BOOK" ADD CONSTRAINT "BOOK_FK2" FOREIGN KEY ("CATEGORY ID") REFERENCES "MYSELF"."BOOK CATEGORY" ("ID") ON DELETE SET NULL NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."BOOK" ADD CONSTRAINT "BOOK_FK3" FOREIGN KEY ("PUBLISHER ID") REFERENCES "MYSELF"."PUBLISHER" ("ID") ON DELETE SET NULL NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Foreign Keys structure for table BOOK CART
-- ----------------------------
ALTER TABLE "MYSELF"."BOOK CART" ADD CONSTRAINT "BOOK_CART_FK1" FOREIGN KEY ("USER ID") REFERENCES "MYSELF"."USER" ("ID") ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."BOOK CART" ADD CONSTRAINT "BOOK_CART_FK2" FOREIGN KEY ("ORDER ID") REFERENCES "MYSELF"."ORDER HISTORY" ("ID") ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."BOOK CART" ADD CONSTRAINT "BOOK_CART_FK3" FOREIGN KEY ("BOOK ID") REFERENCES "MYSELF"."BOOK" ("ID") ON DELETE SET NULL NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Foreign Keys structure for table BOOK WISHLIST
-- ----------------------------
ALTER TABLE "MYSELF"."BOOK WISHLIST" ADD CONSTRAINT "BOOK_WISHLIST_FK1" FOREIGN KEY ("USER ID") REFERENCES "MYSELF"."USER" ("ID") ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."BOOK WISHLIST" ADD CONSTRAINT "BOOK_WISHLIST_FK2" FOREIGN KEY ("BOOK ID") REFERENCES "MYSELF"."BOOK" ("ID") ON DELETE SET NULL NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Foreign Keys structure for table COMMENT
-- ----------------------------
ALTER TABLE "MYSELF"."COMMENT" ADD CONSTRAINT "COMMENT_FK1" FOREIGN KEY ("USER ID") REFERENCES "MYSELF"."USER" ("ID") ON DELETE SET NULL NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."COMMENT" ADD CONSTRAINT "COMMENT_FK2" FOREIGN KEY ("BOOK ID") REFERENCES "MYSELF"."BOOK" ("ID") ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."COMMENT" ADD CONSTRAINT "COMMENT_FK3" FOREIGN KEY ("ELECTRONICS ID") REFERENCES "MYSELF"."ELECTRONICS" ("ID") ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Foreign Keys structure for table ELECTRONICS
-- ----------------------------
ALTER TABLE "MYSELF"."ELECTRONICS" ADD CONSTRAINT "ELECTRONICS_FK1" FOREIGN KEY ("CATEGORY ID") REFERENCES "MYSELF"."ELECTRONICS CATEGORY" ("ID") ON DELETE SET NULL NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."ELECTRONICS" ADD CONSTRAINT "ELECTRONICS_FK2" FOREIGN KEY ("BRAND ID") REFERENCES "MYSELF"."BRAND" ("ID") ON DELETE SET NULL NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Foreign Keys structure for table ELECTRONICS CART
-- ----------------------------
ALTER TABLE "MYSELF"."ELECTRONICS CART" ADD CONSTRAINT "ELECTRONICS_CART_FK1" FOREIGN KEY ("USER ID") REFERENCES "MYSELF"."USER" ("ID") ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."ELECTRONICS CART" ADD CONSTRAINT "ELECTRONICS_CART_FK2" FOREIGN KEY ("ORDER ID") REFERENCES "MYSELF"."ORDER HISTORY" ("ID") ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."ELECTRONICS CART" ADD CONSTRAINT "ELECTRONICS_CART_FK3" FOREIGN KEY ("ELECTRONICS ID") REFERENCES "MYSELF"."ELECTRONICS" ("ID") ON DELETE SET NULL NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Foreign Keys structure for table ELECTRONICS WISHLIST
-- ----------------------------
ALTER TABLE "MYSELF"."ELECTRONICS WISHLIST" ADD CONSTRAINT "ELECTRONICS_WISHLIST_FK1" FOREIGN KEY ("USER ID") REFERENCES "MYSELF"."USER" ("ID") ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."ELECTRONICS WISHLIST" ADD CONSTRAINT "ELECTRONICS_WISHLIST_FK2" FOREIGN KEY ("ELECTRONICS ID") REFERENCES "MYSELF"."ELECTRONICS" ("ID") ON DELETE SET NULL NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Foreign Keys structure for table ORDER HISTORY
-- ----------------------------
ALTER TABLE "MYSELF"."ORDER HISTORY" ADD CONSTRAINT "ORDER_HISTORY_FK" FOREIGN KEY ("USER ID") REFERENCES "MYSELF"."USER" ("ID") ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Foreign Keys structure for table RATING
-- ----------------------------
ALTER TABLE "MYSELF"."RATING" ADD CONSTRAINT "RATING_FK1" FOREIGN KEY ("USER ID") REFERENCES "MYSELF"."USER" ("ID") ON DELETE SET NULL NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."RATING" ADD CONSTRAINT "RATING_FK2" FOREIGN KEY ("BOOK ID") REFERENCES "MYSELF"."BOOK" ("ID") ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "MYSELF"."RATING" ADD CONSTRAINT "RATING_FK3" FOREIGN KEY ("ELECTRONICS ID") REFERENCES "MYSELF"."ELECTRONICS" ("ID") ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
