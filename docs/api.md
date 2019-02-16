### /v2/identify/plate
---
##### ***GET***
**Summary:** Recognize plates from query parameter `image_url`.

**Responses**

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Result | [Result](#Result) |
| 400 | Error  | [Error](#error) |

##### ***POST***
**Summary:** Recognize plates from uploaded `image`.

**Responses**

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Result | [Result](#Result) |
| 400 | Error  | [Error](#error) |

### Models
---

### Error

| Name  | Type    | Description        |
| ----- | ------- | ------------------ |
| text  | string  | Error status code. |
| error | integer | Error massage.     |

### Result

Returns response received from [OpenALPR library](http://doc.openalpr.com/cloud_api.html#results).