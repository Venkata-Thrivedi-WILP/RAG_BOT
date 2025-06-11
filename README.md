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
**Question-2**: How to delete an app?

**Answer**:
I don't know. The provided context only describes the API endpoints and metadata for deleting a policy block, a tag, an authentication profile, creating a tag with no apps, but does not mention anything about deleting an app.

![image](https://github.com/user-attachments/assets/931ded98-9f0b-4f1e-a209-c5276dc941c9)
-------------------------------------------------------------------------------------------------------------------------------------------
