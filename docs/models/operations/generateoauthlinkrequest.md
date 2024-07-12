# GenerateOauthLinkRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `user_id`                                                    | *str*                                                        | :heavy_check_mark:                                           | The id of the user to generate this link for                 |
| `app`                                                        | *Optional[str]*                                              | :heavy_minus_sign:                                           | The name of the app you want the user to authorize access to |
| `credential_name`                                            | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |