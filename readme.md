###Auto poster for ketangpai.com

**Useage:** autopost.bat  filename  *course_index*  

if course_index is not given, it will be posted to the first class.  

---
**If file uploading issues keeps appearing, check file read permission.**  
**If in Windows, try "Run as  Administrator" .**

---
Because python lib *requests* foreces ecoding file name into UTF-8, Chinese file name is not supported.  
To avoid unnecessary confusion, all files will be renamed as current time.  
The origional file name is kept in the post text.  