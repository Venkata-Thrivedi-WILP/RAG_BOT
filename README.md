-------------------------------------------------------------------------------------------------------------------------------------------
**Question-1**: How to set a policy?

**Answer**:
To set a policy, you should use the POST method to the /Policy/SavePolicyBlock3 endpoint. The request body must be a JSON object containing the policy details and plinks, with the following schema:

```json
{
  "policy": {
    "Newpolicy": boolean,
    "Version": integer,
    "Path": string,
    "RevStamp": string,
    "Description": string
  },
  "plinks": [
    {}
  ]
}
```

You must also include the x-codegen-request-body-name: payload in the metadata.

![image](https://github.com/user-attachments/assets/0df99386-9141-46e5-9757-f953de12431c)
-------------------------------------------------------------------------------------------------------------------------------------------
