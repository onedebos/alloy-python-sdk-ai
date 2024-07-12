<!-- Start SDK Example Usage [usage] -->
```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.update_a_user(user_id='<value>', request_body=operations.UpdateAUserRequestBody())

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->