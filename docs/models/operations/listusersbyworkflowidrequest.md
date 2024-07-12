# ListUsersByWorkflowidRequest


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `workflow_id`                                                   | *str*                                                           | :heavy_check_mark:                                              | The Id of the parent workflow you would like to list users for. |
| `user_id`                                                       | *Optional[str]*                                                 | :heavy_minus_sign:                                              | The Id of the user you would like to query.                     |