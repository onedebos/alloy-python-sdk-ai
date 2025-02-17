"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from alloypythonsdk import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeactivateAWorkflowRequestBody:
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId') }})
    r"""The Id of the user you want to lookup. Returned from the Create User endpoint. Note: you can also use the Embedded user's `username` in this field."""
    workflow_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflowId'), 'exclude': lambda f: f is None }})
    r"""The Id of the workflow to activate. If you pass this parameter, then `workflowName` is not required."""
    workflow_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflowName'), 'exclude': lambda f: f is None }})
    r"""The name of the workflow to activate.  If you pass this parameter, then `workflowId` is not required."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeactivateAWorkflowResponseBody:
    r"""200"""
    activated: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('activated'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeactivateAWorkflowResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[DeactivateAWorkflowResponseBody] = dataclasses.field(default=None)
    r"""200"""
    

