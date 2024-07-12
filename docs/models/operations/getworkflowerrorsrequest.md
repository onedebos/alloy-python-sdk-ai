# GetWorkflowErrorsRequest


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `workflow_id`                                                                       | *str*                                                                               | :heavy_check_mark:                                                                  | The Id of the workflow you want to find errors for                                  |
| `user_id`                                                                           | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The Id of the user you want delete logs for. Returned from the Create User endpoint |