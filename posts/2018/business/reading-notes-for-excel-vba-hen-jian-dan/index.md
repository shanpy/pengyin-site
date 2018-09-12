.. title: (In Process)Reading Notes for "别怕, Excel+VBA其实很简单" Written by Excel Home
.. date: 2018-08-23
.. category: Business
.. tags: draft, Reading Notes, Excel
.. slug: reading-notes-for-excel-vba-hen-jian-dan
.. authors: Pengyin Shan
.. description: A review of Excel VBA before new school year: The study notes for the Chinese book "别怕, Excel+VBA其实很简单", produced by Excel Home

[TOC]

##Basics

###Data Type

- Byte

####Numbers

- Integer: 2 bytes
- Long: 4 bytes
- Single: 4 bytes
- Double: 8 bytes
- Decimal: 14 bytes

####Other

- String
- Object
- Date
- Curreny
- Boolean
- Variant: any data

###Variables

####Declare

`Dim name As type` or use declartion character: `Dim name$`

#####Table of Declaration

![excel_vba_1](/images/2018/business/excel_vba_1.png)

#####Multiple Declaration

`Dim A,B As type`

>If no type is used, the variable will be Variant type