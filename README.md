# FileSorting
sorting files by extensions in folders


1. edit ```config.json```\
example: 
```json
{
  "ignored": ["config.json", "main.py"],

  "sort" : {
    "pictures" : ["jpg", "png", "webp"],
    "pictures/icons" : ["ico"],
    "C:/Users/krystofex/Documents" : ["doc", "docx", "txt"]
  }
}
```
2. ```python3 main.py```
