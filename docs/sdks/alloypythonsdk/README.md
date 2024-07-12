# AlloyPythonSDK


## Overview

### Available Operations

* [update_a_user](#update_a_user) - Update a user
* [get_a_user](#get_a_user) - Retrieve a single user
* [delete_a_user](#delete_a_user) - Delete a user
* [create_a_user](#create_a_user) - Create a user
* [list_all_users](#list_all_users) - Retrieve a list of all users
* [create_a_credential](#create_a_credential) - Create Credential
* [get_credential_metadata](#get_credential_metadata) - Retrieve all credential structures
* [generate_jwt_token](#generate_jwt_token) - Generate a new JWT for a user
* [list_user_credentials](#list_user_credentials) - Retrieve all credentials for a user
* [list_workflows](#list_workflows) - Retrieve a list of workflows
* [deactivate_a_workflow](#deactivate_a_workflow) - Deactivate a workflow
* [activate_a_workflow](#activate_a_workflow) - Activate a workflow
* [get_workflow_analytics](#get_workflow_analytics) - Retrieve usage metrics for a workflow
* [disable_all_workflows_for_a_user](#disable_all_workflows_for_a_user) - Deactivate workflows for a user
* [get_workflow_logs](#get_workflow_logs) - Retrieve all execution logs for a workflow
* [get_workflow_errors](#get_workflow_errors) - Retrieve all error logs for a workflow
* [delete_logs_for_a_user](#delete_logs_for_a_user) - Delete all logs for a user
* [delete_a_credential](#delete_a_credential) - Delete a Credential for a user
* [run_event](#run_event) - Trigger an event for a user
* [rerun_workfow](#rerun_workfow) - Rerun a single workflow execution
* [run_workflow](#run_workflow) - Run Workflow
* [list_apps](#list_apps) - Retrieve all supported apps
* [list_integrations](#list_integrations) - Retrieve a list of all integrations
* [batch_create_users](#batch_create_users) - Create a batch of users
* [list_events](#list_events) - Retrieve a list of custom events
* [generate_alloy_link](#generate_alloy_link) - Create an Embedded link for an integration
* [generate_oauth_link](#generate_oauth_link) - Create OAuth Link
* [delete_workflow](#delete_workflow) - Delete a workflow
* [find_a_workflow](#find_a_workflow) - Retrieve a single workflow
* [get_an_integration](#get_an_integration) - Retrieve a single integration
* [list_users_by_workflowid](#list_users_by_workflowid) - List Users by workflowId
* [upgrade_workflow](#upgrade_workflow) - Upgrade a workflow
* [list_versions](#list_versions) - Retrieve a list of workflow versions
* [credential_medata_by_app](#credential_medata_by_app) - Retrieve credential structure for an app
* [start_installation](#start_installation) - Start Installation
* [complete_installation](#complete_installation) - Complete Installation

## update_a_user

Updates a user given a specified userId. This endpoint allows you to update a username or fullName and returns the updated user object.

### Example Usage

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

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                           | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The Id of the user you want to lookup. Returned from the Create User endpoint. Note: you can also use the Embedded user's `username` in this field. |
| `request_body`                                                                                                                                      | [Optional[operations.UpdateAUserRequestBody]](../../models/operations/updateauserrequestbody.md)                                                    | :heavy_minus_sign:                                                                                                                                  | N/A                                                                                                                                                 |


### Response

**[operations.UpdateAUserResponse](../../models/operations/updateauserresponse.md)**
### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.UpdateAUserResponseBody | 401                            | application/json               |
| errors.SDKError                | 4xx-5xx                        | */*                            |

## get_a_user

Returns a specific user given a userId and any active workflows associated with the user.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.get_a_user(user_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                           | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The Id of the user you want to lookup. Returned from the Create User endpoint. Note: you can also use the Embedded user's `username` in this field. |


### Response

**[operations.GetAUserResponse](../../models/operations/getauserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_a_user

This endpoint deletes a user account. It is most commonly used when a user stops being a customer of your platform or in conjunction with a GDPR compliance request. Note that this endpoint only deletes the user's account – not any corresponding workflow logs or other data. To remove that data as part of a compliance request, see our 'Delete User Logs' endpoint

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.delete_a_user(user_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                           | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The Id of the user you want to lookup. Returned from the Create User endpoint. Note: you can also use the Embedded user's `username` in this field. |


### Response

**[operations.DeleteAUserResponse](../../models/operations/deleteauserresponse.md)**
### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.DeleteAUserResponseBody | 401                            | application/json               |
| errors.SDKError                | 4xx-5xx                        | */*                            |

## create_a_user

Creates a new user in your Embedded account. The user record acts like a "container" to store all the integrations, workflows, and credentials for any given user. Returns a user identifier.

### Example Usage

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.create_a_user(request=operations.CreateAUserRequestBody(
    username='Cornelius.Pfannerstill79',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateAUserRequestBody](../../models/operations/createauserrequestbody.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateAUserResponse](../../models/operations/createauserresponse.md)**
### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.CreateAUserResponseBody | 401                            | application/json               |
| errors.SDKError                | 4xx-5xx                        | */*                            |

## list_all_users

Returns a list of all users created in your Embedded account.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.list_all_users(parent_workflow_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `parent_workflow_id`                                                               | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | You can pass a parentWorkflowId if you wish to list users for a specific workflow. |


### Response

**[operations.ListAllUsersResponse](../../models/operations/listallusersresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ListAllUsersResponseBody | 401                             | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |

## create_a_credential

Use this endpoint to add a credential programmatically via the API. This endpoint should be used primarily for non-OAuth blocks. If you are using Secrets Manager with an OAuth block and you have the OAuth tokens already, you can add them to Alloy with this endpoint. Please reference [this](https://docs.runalloy.com/docs/headless) section of our docs for a complete tutorial on when and how to use this endpoint.

### Example Usage

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.create_a_credential(request=operations.CreateACredentialRequestBody(
    credential='{"type":"netsuite","data":{"realm":"XXX","consumerKey":"XXX","tokenId":"XXX","tokenSecret":"XXX"}}',
    user_id='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateACredentialRequestBody](../../models/operations/createacredentialrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.CreateACredentialResponse](../../models/operations/createacredentialresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_credential_metadata

This endpoint returns a basic structure of what data must be inputted when adding a credential manually. This should be used when creating a credential using the POST credential endpoint.

This endpoint returns the structure of every supported block on Alloy Embedded. It returns a boolean flag called `isOauth` which indicates if the credential uses OAuth or an API key.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.get_credential_metadata()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetCredentialMetadataResponse](../../models/operations/getcredentialmetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## generate_jwt_token

This endpoint is used to generate a new user token in the form of a JSON Web Token (JWT) which is required to securely render the Embedded Modal in your application. Once retrieved, you'll want to pass this token to your frontend.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.generate_jwt_token(user_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                           | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The Id of the user you want to lookup. Returned from the Create User endpoint. Note: you can also use the Embedded user's `username` in this field. |


### Response

**[operations.GenerateJwtTokenResponse](../../models/operations/generatejwttokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_user_credentials

Returns a list of all credentials created for a specified user.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.list_user_credentials(user_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                              | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `user_id`                              | *str*                                  | :heavy_check_mark:                     | The id of the currently logged in user |


### Response

**[operations.ListUserCredentialsResponse](../../models/operations/listusercredentialsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_workflows

Returns a list of all active **parent** workflows associated with your Alloy Embedded account. Note this endpoint does _not_ return a list of workflows that the user has installed, but rather a list of all _available_ workflows. The `installed` flag indicates if the user has installed a copy of the workflow but does not  indicate if the user has a given workflow "active".

For each workflow, this endpoint returns the individual apps that are required as part of the workflow. Commonly used to populate data on an integrations page.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.list_workflows(user_id='<value>', integration='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                                                          | *str*                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                 | The Id of the user you want to lookup. Returned from the Create User endpoint. Note: you can also use the Embedded user's `username` in this field.                                |
| `integration`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                 | This parameter allows you to filter workflows based on the name of the integration you're looking for. For example, if you were looking for a Shopify integration, specify shopify |


### Response

**[operations.ListWorkflowsResponse](../../models/operations/listworkflowsresponse.md)**
### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ListWorkflowsResponseBody | 400                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |

## deactivate_a_workflow

Disables all future invocations and runs for a given workflow. 

By deactivating a workflow, this endpoint will turn off any events or webhooks a workflow is subscribed to. May be reactivated by the Reactivate workflow endpoint.

### Example Usage

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.deactivate_a_workflow(request=operations.DeactivateAWorkflowRequestBody(
    user_id='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.DeactivateAWorkflowRequestBody](../../models/operations/deactivateaworkflowrequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.DeactivateAWorkflowResponse](../../models/operations/deactivateaworkflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## activate_a_workflow

Reactivates a workflow that was previously disabled by the Disable Workflow endpoint. This endpoint requires a specified WorkflowId and returns a success/failure.

### Example Usage

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.activate_a_workflow(request=operations.ActivateAWorkflowRequestBody(
    user_id='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ActivateAWorkflowRequestBody](../../models/operations/activateaworkflowrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.ActivateAWorkflowResponse](../../models/operations/activateaworkflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_workflow_analytics

This endpoint returns the `totalAppActions` (the number of times each block inside the workflow has been executed over the course of the workflow's lifetime), the `totalWorkflowRuns` (which represents the number of times the workflow has been invoked) and the `totalErrors` (the number of times the workflow has had an error).

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.get_workflow_analytics(workflow_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `workflow_id`                                      | *str*                                              | :heavy_check_mark:                                 | The Id of the workflow you want to find errors for |


### Response

**[operations.GetWorkflowAnalyticsResponse](../../models/operations/getworkflowanalyticsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## disable_all_workflows_for_a_user

Deactivates all active workflows for a user in bulk. 

This endpoint may be used to perform a bulk operation such as temporarily disabling a user's account in lieu of deleting the user account if the user wants to "pause" their account.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.disable_all_workflows_for_a_user(user_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `user_id`                                                                     | *str*                                                                         | :heavy_check_mark:                                                            | The Id of the user you want to lookup. Returned from the Create User endpoint |


### Response

**[operations.DisableAllWorkflowsForAUserResponse](../../models/operations/disableallworkflowsforauserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_workflow_logs

Retrieves log data for a given workflow over time. Logs are stored for a maximum of 60 days before being purged.

Each log includes the `executionId` (which can be used to rerun an execution), the `startedAt` and `stoppedAt` date stamps, and the JSON output of the execution.

### Example Usage

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.get_workflow_logs(request=operations.GetWorkflowLogsRequest(
    workflow_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetWorkflowLogsRequest](../../models/operations/getworkflowlogsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetWorkflowLogsResponse](../../models/operations/getworkflowlogsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_workflow_errors

This endpoint fetches an array of errors for a specific workflow.

It returns the error message, and the date stamp when the error was thrown, the block that caused the error, and the `workflowId` . Commonly used to debug workflows when they error and identify historical errors; this endpoint may be used in conjunction with the route error messages feature.

If there are no errors for the specified workflow, this endpoint will return an empty array.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.get_workflow_errors(workflow_id='<value>', user_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `workflow_id`                                                                       | *str*                                                                               | :heavy_check_mark:                                                                  | The Id of the workflow you want to find errors for                                  |
| `user_id`                                                                           | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The Id of the user you want delete logs for. Returned from the Create User endpoint |


### Response

**[operations.GetWorkflowErrorsResponse](../../models/operations/getworkflowerrorsresponse.md)**
### Errors

| Error Object                         | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetWorkflowErrorsResponseBody | 400                                  | application/json                     |
| errors.SDKError                      | 4xx-5xx                              | */*                                  |

## delete_logs_for_a_user

This endpoint deletes all historical logs associated with a user and is most commonly used in conjunction with a compliance request such as GDPR. This endpoint requires a userId. 

Note that this action cannot be undone.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.delete_logs_for_a_user(user_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `user_id`                                                                           | *str*                                                                               | :heavy_check_mark:                                                                  | The Id of the user you want delete logs for. Returned from the Create User endpoint |


### Response

**[operations.DeleteLogsForAUserResponse](../../models/operations/deletelogsforauserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_a_credential

To delete a credential via the API, you need to invoke the below endpoint.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.delete_a_credential(credential_id='<value>', user_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `credential_id`                                    | *str*                                              | :heavy_check_mark:                                 | The credential you're looking to delete            |
| `user_id`                                          | *str*                                              | :heavy_check_mark:                                 | The Id of the user associated with this credential |


### Response

**[operations.DeleteACredentialResponse](../../models/operations/deleteacredentialresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## run_event

This endpoint runs a workflow that uses a **Custom Event **. Note that this endpoint cannot be used to invoke a workflow that has a Custom Webhook Trigger.

If you have defined a custom JSON body for the Custom Event, it should be passed into the `data` body parameter.

### Example Usage

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.run_event(request=operations.RunEventRequestBody(
    event='<value>',
    user_id='<value>',
    data='{key: 61661, key1: null, key2: "<value>"}',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.RunEventRequestBody](../../models/operations/runeventrequestbody.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.RunEventResponse](../../models/operations/runeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## rerun_workfow

Retrieves log data for a given workflow over time. Logs are stored for a maximum of 60 days before being purged.

Each log includes the `executionId` (which can be used to rerun an execution), the `startedAt` and `stoppedAt` date stamps, and the JSON output of the execution.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.rerun_workfow(workflow_id='<value>', execution_id='<value>', user_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `workflow_id`                                                                               | *str*                                                                                       | :heavy_check_mark:                                                                          | The Id of the workflow you want to find logs for                                            |
| `execution_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | The Id of the execution to rerun. This can be retrieved from the GET Workflow Logs endpoint |
| `user_id`                                                                                   | *str*                                                                                       | :heavy_check_mark:                                                                          | The Id of the user you want delete logs for. Returned from the Create User endpoint         |


### Response

**[operations.RerunWorkfowResponse](../../models/operations/rerunworkfowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## run_workflow

This endpoint runs a workflow that uses a **Webhook Trigger.** Note that this endpoint should not be used to invoke a workflow that has a Custom Event. If you have defined a custom JSON body for the webhook trigger, it should be passed into the `data` body parameter.

### Example Usage

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.run_workflow(request=operations.RunWorkflowRequestBody(
    user_id='<value>',
    data='{key: 25693, key1: null, key2: "<value>"}',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RunWorkflowRequestBody](../../models/operations/runworkflowrequestbody.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.RunWorkflowResponse](../../models/operations/runworkflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_apps

Returns all the available apps currently supported by Alloy Embedded

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.list_apps()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.ListAppsResponse](../../models/operations/listappsresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ListAppsResponseBody | 400                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## list_integrations

Returns all the available integrations in your Alloy Embedded Account. Includes integrations/apps you've created an "integration" for, their workflows and statuses. If `installed` equals `true`, the `installedVersion` key will show the currently installed version.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.list_integrations(user_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `user_id`                                                                                              | *str*                                                                                                  | :heavy_check_mark:                                                                                     | The Id used to identify the user. Note: you can also use the Embedded user's `username` in this field. |


### Response

**[operations.ListIntegrationsResponse](../../models/operations/listintegrationsresponse.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.ListIntegrationsResponseBody | 400                                 | application/json                    |
| errors.SDKError                     | 4xx-5xx                             | */*                                 |

## batch_create_users

Creates a new user in your Embedded account. The user record acts like a "container" to store all the integrations, workflows, and credentials for any given user. Returns a user identifier.

### Example Usage

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.batch_create_users(request=operations.BatchCreateUsersRequestBody())

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.BatchCreateUsersRequestBody](../../models/operations/batchcreateusersrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.BatchCreateUsersResponse](../../models/operations/batchcreateusersresponse.md)**
### Errors

| Error Object                                | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| errors.BatchCreateUsersResponseBody         | 400                                         | application/json                            |
| errors.BatchCreateUsersResponseResponseBody | 401                                         | application/json                            |
| errors.SDKError                             | 4xx-5xx                                     | */*                                         |

## list_events

Returns a list of all Custom Events you have enabled in Alloy Embedded.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.list_events()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.ListEventsResponse](../../models/operations/listeventsresponse.md)**
### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.ListEventsResponseBody | 400                           | application/json              |
| errors.SDKError               | 4xx-5xx                       | */*                           |

## generate_alloy_link

This endpoint generates an alloy Link. For more details on Embedded Link, please [read](https://docs.runalloy.com/docs/alloy-link) this tutorial.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.generate_alloy_link(user_id='<value>', integration_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `user_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | The user to generate the Embedded Link for                           |
| `integration_id`                                                     | *str*                                                                | :heavy_check_mark:                                                   | The Id of the integration you want to generate the Embedded Link for |


### Response

**[operations.GenerateAlloyLinkResponse](../../models/operations/generatealloylinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## generate_oauth_link

This endpoint can be used to generate an OAuth link if you want to completely white label your authentication experience. You can use this endpoint to generate a link which your users can click to redirect to the specified application without rendering the Alloy Embedded Modal.

Note: this endpoint **only** works with OAuth enabled integrations. To add a credential manually, please use the [POST Create Credential API](https://docs.runalloy.com/v2.1/reference/create-a-credential).

This endpoint takes a `userId`, `integrationId`, and `credentialName` as inputs. It should be used in conjunction with the [GET Credential Metadata API](https://docs.runalloy.com/v2.1/reference/get-credential-metadata). `credentialName` represents the name of the integration you want to call.

If the credential metadata endpoint returns any `properties,` you must pass them as query string parameters at the end of this call.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.generate_oauth_link(user_id='<value>', app='<value>', credential_name='the credentialName')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `user_id`                                                    | *str*                                                        | :heavy_check_mark:                                           | The id of the user to generate this link for                 |
| `app`                                                        | *Optional[str]*                                              | :heavy_minus_sign:                                           | The name of the app you want the user to authorize access to |
| `credential_name`                                            | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |


### Response

**[operations.GenerateOauthLinkResponse](../../models/operations/generateoauthlinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_workflow

Deletes a workflow for a specific user. This endpoint does not delete a workflow for all users.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.delete_workflow(user_id='<value>', workflow_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                           | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The Id of the user you want to lookup. Returned from the Create User endpoint. Note: you can also use the Embedded user's `username` in this field. |
| `workflow_id`                                                                                                                                       | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The Id of the workflow to delete                                                                                                                    |


### Response

**[operations.DeleteWorkflowResponse](../../models/operations/deleteworkflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## find_a_workflow

Find a workflow given a workflowId

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.find_a_workflow(user_id='<value>', workflow_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                           | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The Id of the user you want to lookup. Returned from the Create User endpoint. Note: you can also use the Embedded user's `username` in this field. |
| `workflow_id`                                                                                                                                       | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The Id of the workflow to find                                                                                                                      |


### Response

**[operations.FindAWorkflowResponse](../../models/operations/findaworkflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_an_integration

Finds a specific integration for a user

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.get_an_integration(integration_id='<value>', user_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `integration_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | This API parameter allows you to filter results based on the integrationId or the integrationName (also referred to as 'app'). The integration name (app) is a custom name that you have set for your integration. When using the integration name (app), provide the name of the integration you want to filter for (e.g. 'shopify order sync' or 'magento product creation'). You can obtain the integration name (app) from the List Integrations endpoint under the 'app' parameter, or by checking your UI. Either integrationId or integrationName must be provided but it cannot be both. |
| `user_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The Id used to identify the user. Note: you can also use the Embedded user's `username` in this field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |


### Response

**[operations.GetAnIntegrationResponse](../../models/operations/getanintegrationresponse.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GetAnIntegrationResponseBody | 400                                 | application/json                    |
| errors.SDKError                     | 4xx-5xx                             | */*                                 |

## list_users_by_workflowid

List Users by workflowId

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.list_users_by_workflowid(workflow_id='<value>', user_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `workflow_id`                                                   | *str*                                                           | :heavy_check_mark:                                              | The Id of the parent workflow you would like to list users for. |
| `user_id`                                                       | *Optional[str]*                                                 | :heavy_minus_sign:                                              | The Id of the user you would like to query.                     |


### Response

**[operations.ListUsersByWorkflowidResponse](../../models/operations/listusersbyworkflowidresponse.md)**
### Errors

| Error Object                             | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.ListUsersByWorkflowidResponseBody | 400                                      | application/json                         |
| errors.SDKError                          | 4xx-5xx                                  | */*                                      |

## upgrade_workflow

This endpoint allows you as the ISV to upgrade the workflow for a specified end user.  <br /> <br />In order to upgrade a workflow via this endpoint, the new workflow must have the same configurable fields as the original. If any new configurable fields were added, you will not be able to upgrade the workflow programmatically and instead would need to reinstall the workflow for the end user.

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.upgrade_workflow(workflow_id='<value>', user_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `workflow_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | Id of the parent workflow in which you are upgrading for the end user |
| `user_id`                                                             | *str*                                                                 | :heavy_check_mark:                                                    | Id of the end user you wish to upgrade the workflow for               |


### Response

**[operations.UpgradeWorkflowResponse](../../models/operations/upgradeworkflowresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UpgradeWorkflowResponseBody | 400                                | application/json                   |
| errors.SDKError                    | 4xx-5xx                            | */*                                |

## list_versions

Returns a list of all versions available for a given workflow

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.list_versions(user_id='<value>', workflow_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                           | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The Id of the user you want to lookup. Returned from the Create User endpoint. Note: you can also use the Embedded user's `username` in this field. |
| `workflow_id`                                                                                                                                       | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | The Id of the workflow you want to retrieve versions for                                                                                            |


### Response

**[operations.ListVersionsResponse](../../models/operations/listversionsresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ListVersionsResponseBody | 400                             | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |

## credential_medata_by_app

Retrieve credential structure for an app

### Example Usage

```python
import alloypythonsdk

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.credential_medata_by_app(app='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `app`                                                           | *str*                                                           | :heavy_check_mark:                                              | Name of App (camelCased, can be found in App Metadata response) |


### Response

**[operations.CredentialMedataByAppResponse](../../models/operations/credentialmedatabyappresponse.md)**
### Errors

| Error Object                             | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.CredentialMedataByAppResponseBody | 400                                      | application/json                         |
| errors.SDKError                          | 4xx-5xx                                  | */*                                      |

## start_installation

This endpoint will create an installation record and return the information required to create a form for your user to fill out.

### Example Usage

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.start_installation(request=operations.StartInstallationRequestBody(
    user_id='<value>',
    integration_id='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.StartInstallationRequestBody](../../models/operations/startinstallationrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.StartInstallationResponse](../../models/operations/startinstallationresponse.md)**
### Errors

| Error Object                         | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.StartInstallationResponseBody | 400                                  | application/json                     |
| errors.SDKError                      | 4xx-5xx                              | */*                                  |

## complete_installation

Complete Installation

### Example Usage

```python
import alloypythonsdk
from alloypythonsdk.models import operations

s = alloypythonsdk.AlloyPythonSDK(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.complete_installation(request=operations.CompleteInstallationRequestBody(
    installation_id='<value>',
    data=[
        operations.Data(
            workflow_id='<value>',
            block_id='<value>',
        ),
    ],
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CompleteInstallationRequestBody](../../models/operations/completeinstallationrequestbody.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.CompleteInstallationResponse](../../models/operations/completeinstallationresponse.md)**
### Errors

| Error Object                            | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.CompleteInstallationResponseBody | 400                                     | application/json                        |
| errors.SDKError                         | 4xx-5xx                                 | */*                                     |
